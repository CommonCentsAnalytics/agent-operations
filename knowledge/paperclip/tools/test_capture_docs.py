"""Offline checks for capture extraction and the actual documentation snapshot.

Run with Python -B to avoid generating bytecode files in the library.
These checks validate the archive, not Paperclip's software behavior.
"""
import json
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlparse

from capture_docs import Document, ROOT, inventory, normalize, render, verify

SNAPSHOT = ROOT / "snapshots" / "2026-09-17T005212Z"


def sidebar(path="guides/example.md", count=1, href="/guides/example/"):
    return Document(
        '<nav id="sidebar"><section data-section-title="Example">'
        f'<span class="sb-section-count">{count}</span>'
        f'<a href="{href}" data-file="{path}">Example page</a>'
        '</section></nav>'
    )


class ExtractionTests(unittest.TestCase):
    def test_inventory(self):
        categories, pages = inventory(sidebar())
        self.assertEqual(categories[0]["discovered_count"], 1)
        self.assertEqual(pages[0]["url"], "https://docs.paperclip.ing/guides/example/")

    def test_count_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, "count mismatch"):
            inventory(sidebar(count=2))

    def test_unsafe_paths_rejected(self):
        for path in ("../escape.md", "C:/escape.md", "/escape.md", "file.exe"):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "Unsafe"):
                inventory(sidebar(path=path))

    def test_external_host_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unexpected documentation host"):
            inventory(sidebar(href="https://example.net/file/"))

    def test_missing_navigation_rejected(self):
        with self.assertRaisesRegex(ValueError, "No documentation navigation"):
            inventory(Document("<p>not a docs page</p>"))

    def test_readable_content_and_no_script_body(self):
        doc = Document('<article id="article"><h1>Title</h1>'
                       '<p>A <a href="../source/">source</a>.</p>'
                       '<script>DO_NOT_EXECUTE_THIS</script>'
                       '<table><tr><th>Field</th><th>Value</th></tr>'
                       '<tr><td>A</td><td>B</td></tr></table></article>')
        value = render(doc.by_id("article"), "https://docs.paperclip.ing/test/page/")
        self.assertIn("# Title", value)
        self.assertIn("[source](https://docs.paperclip.ing/test/source/)", value)
        self.assertIn("| A | B |", value)
        self.assertNotIn("DO_NOT_EXECUTE_THIS", value)

    def test_code_unicode_and_whitespace(self):
        source = 'tree: \u251c\u2500\u2500 child \u2192 next\n  indented & value\n\n\nend'
        doc = Document('<pre><code class="language-text">' + source.replace('&', '&amp;') + '</code></pre>')
        self.assertIn(source, render(doc.root, "https://docs.paperclip.ing/"))


class SnapshotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((SNAPSHOT / "manifest.json").read_text(encoding="utf-8"))

    def test_completeness_and_integrity(self):
        result = verify(SNAPSHOT)
        self.assertTrue(result["passed"], result["problems"])
        self.assertEqual(result["category_count"], 15)
        self.assertEqual(result["page_count"], 193)
        self.assertEqual(result["hashes_checked"], 388)

    def test_every_page_has_source_body_and_original_headings(self):
        for page in self.manifest["pages"]:
            with self.subTest(page=page["source_path_hint"]):
                original = Document((SNAPSHOT / page["html_path"]).read_text(encoding="utf-8"))
                article = original.by_id("article")
                readable = (SNAPSHOT / page["markdown_path"]).read_text(encoding="utf-8")
                self.assertIn(page["url"], readable[:500])
                self.assertGreater(len(readable), 100)
                for heading in (n for n in article.descendants() if re.fullmatch(r"h[1-6]", n.tag)):
                    self.assertIn(render(heading, page["url"]).strip(), readable)

    def test_code_content_preserved_ignoring_blank_spacing(self):
        # Derived Markdown may normalize blank lines or indent list items.
        # Compare non-empty code lines; raw HTML remains the exact source.
        for page in self.manifest["pages"]:
            with self.subTest(page=page["source_path_hint"]):
                article = Document((SNAPSHOT / page["html_path"]).read_text(encoding="utf-8")).by_id("article")
                readable = (SNAPSHOT / page["markdown_path"]).read_text(encoding="utf-8")
                # Markdown blockquotes prefix every line, including code.
                # Remove only that presentation prefix for this comparison.
                lines = {line.strip() for line in readable.splitlines()}
                lines |= {re.sub(r"^(?:> ?)+", "", line).strip() for line in lines}
                for block in (n for n in article.descendants() if n.tag == "pre"):
                    for line in block.text().splitlines():
                        if line.strip():
                            self.assertTrue(line.strip() in lines, "Missing code line: " + ascii(line.strip()))

    def test_authored_and_index_file_links_resolve(self):
        files = list(ROOT.glob("*.md")) + [ROOT.parent.parent / "README.md", SNAPSHOT / "INDEX.md"]
        for file in files:
            for target in re.findall(r'\]\(([^)]+)\)', file.read_text(encoding="utf-8")):
                if urlparse(target).scheme or target.startswith("#"):
                    continue
                path = (file.parent / unquote(target.split("#", 1)[0])).resolve()
                with self.subTest(file=file.name, target=target):
                    self.assertTrue(path.is_file(), f"Missing local link: {path}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
