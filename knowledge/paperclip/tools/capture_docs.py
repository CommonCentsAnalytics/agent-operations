"""Capture Paperclip's public documentation without executing its examples.

Python standard library only. Sources stay separate from authored findings.
Each capture creates a new timestamped directory; it never updates old snapshots.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

BASE = "https://docs.paperclip.ing/"
SEED = BASE + "guides/welcome/what-is-paperclip/"
LICENSE_URL = "https://raw.githubusercontent.com/paperclipai/paperclip/master/LICENSE"
ROOT = Path(__file__).resolve().parents[1]
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Element:
    def __init__(self, tag="root", attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []

    def descendants(self):
        for child in self.children:
            if isinstance(child, Element):
                yield child
                yield from child.descendants()

    def text(self):
        return "".join(c.text() if isinstance(c, Element) else c for c in self.children)


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.root = Element()
        self.stack = [self.root]
        self.feed(text)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack = self.stack[:i]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)

    def by_id(self, element_id):
        return next((n for n in self.root.descendants() if n.attrs.get("id") == element_id), None)


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def fetch(url):
    for attempt in range(3):
        try:
            request = Request(url, headers={"User-Agent": "AgentOperations-DocumentationArchive/1.0", "Accept": "text/html,text/plain,application/json"})
            with urlopen(request, timeout=30) as response:
                data = response.read()
                return data, {"retrieved_at_utc": utc_now(), "final_url": response.url, "http_status": response.status, "content_type": response.headers.get("Content-Type"), "etag": response.headers.get("ETag"), "last_modified": response.headers.get("Last-Modified")}
        except Exception:
            if attempt == 2:
                raise
            time.sleep(0.5 * (attempt + 1))


def normalize(text):
    return re.sub(r"\s+", " ", text).strip()


def render(node, page_url):
    if isinstance(node, str):
        return re.sub(r"\s+", " ", node)
    tag = node.tag
    if tag in {"script", "style", "svg", "button"}:
        return ""
    if tag == "pre":
        value = node.text().rstrip("\n")
        fence = "`" * max(3, max((len(x) + 1 for x in re.findall(r"`+", value)), default=3))
        code = next((c for c in node.children if isinstance(c, Element) and c.tag == "code"), None)
        language = re.search(r"language-([\w+-]+)", code.attrs.get("class", "")) if code else None
        return f"\n\n{fence}{language.group(1) if language else ''}\n{value}\n{fence}\n\n"
    if tag == "table":
        rows = []
        for row in node.descendants():
            if row.tag == "tr":
                cells = [normalize(render(c, page_url)).replace("|", "\\|") for c in row.children if isinstance(c, Element) and c.tag in {"th", "td"}]
                if cells:
                    rows.append(cells)
        if not rows:
            return ""
        width = max(map(len, rows))
        rows = [r + [""] * (width - len(r)) for r in rows]
        lines = ["| " + " | ".join(r) + " |" for r in rows]
        lines.insert(1, "| " + " | ".join(["---"] * width) + " |")
        return "\n\n" + "\n".join(lines) + "\n\n"
    if tag in {"ul", "ol"}:
        lines = []
        number = 1
        for child in node.children:
            if not isinstance(child, Element) or child.tag != "li":
                continue
            text = render(child, page_url).strip()
            marker = f"{number}. " if tag == "ol" else "- "
            lines.append(marker + text.replace("\n", "\n  "))
            number += 1
        return "\n\n" + "\n".join(lines) + "\n\n"
    value = "".join(render(c, page_url) for c in node.children)
    if re.fullmatch(r"h[1-6]", tag):
        return "\n\n" + "#" * int(tag[1]) + " " + value.strip() + "\n\n"
    if tag == "a":
        href = node.attrs.get("href", "")
        url = urljoin(page_url, href)
        return f"[{value.strip() or url}]({url})" if href else value
    if tag == "img":
        url = urljoin(page_url, node.attrs.get("src", ""))
        return f"[Image reference: {node.attrs.get('alt', 'image')}]({url})"
    if tag == "iframe":
        return f"\n[Embedded media reference]({urljoin(page_url, node.attrs.get('src', ''))})\n"
    if tag in {"strong", "b"}:
        return "**" + value.strip() + "**"
    if tag in {"em", "i"}:
        return "*" + value.strip() + "*"
    if tag == "code":
        fence = "`" * max(1, max((len(x) + 1 for x in re.findall(r"`+", value)), default=1))
        return fence + value + fence
    if tag == "blockquote":
        return "\n\n" + "\n".join("> " + line for line in value.strip().splitlines()) + "\n\n"
    if tag == "br":
        return "\n"
    if tag == "hr":
        return "\n\n---\n\n"
    if tag in {"p", "div", "section", "details", "summary"}:
        return "\n\n" + value.strip() + "\n\n"
    return value


def inventory(document):
    sidebar = document.by_id("sidebar")
    if sidebar is None:
        raise ValueError("No documentation navigation found; capture stopped rather than guessing")
    groups, pages, seen = [], [], set()
    for node in sidebar.descendants():
        if "data-section-title" not in node.attrs:
            continue
        group = node.attrs["data-section-title"]
        count_node = next((x for x in node.descendants() if "sb-section-count" in x.attrs.get("class", "").split()), None)
        expected = int(count_node.text()) if count_node else None
        actual = 0
        for link in node.descendants():
            if link.tag != "a" or "data-file" not in link.attrs:
                continue
            source_path = link.attrs["data-file"]
            path = Path(source_path)
            if path.is_absolute() or path.root or path.drive or ".." in path.parts or not source_path.endswith(".md"):
                raise ValueError(f"Unsafe source path: {source_path}")
            url = urljoin(BASE, link.attrs["href"])
            if urlparse(url).netloc != "docs.paperclip.ing":
                raise ValueError(f"Unexpected documentation host: {url}")
            if url in seen:
                raise ValueError(f"Duplicate documentation URL: {url}")
            seen.add(url)
            pages.append({"category": group, "title": normalize(link.text()), "url": url, "source_path_hint": source_path})
            actual += 1
        groups.append({"name": group, "advertised_count": expected, "discovered_count": actual})
        if expected is not None and expected != actual:
            raise ValueError(f"Category count mismatch: {group}: {expected} != {actual}")
    if not pages:
        raise ValueError("No documentation pages discovered")
    return groups, pages


def write_bytes(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as stream:
        stream.write(data)


def write_text(path, text):
    write_bytes(path, text.encode("utf-8"))


def capture():
    start = utc_now()
    snapshot = ROOT / "snapshots" / datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    snapshot.mkdir(parents=True, exist_ok=False)
    home, home_meta = fetch(BASE)
    seed, seed_meta = fetch(SEED)
    license_data, license_meta = fetch(LICENSE_URL)
    if b"MIT License" not in license_data or b"associated documentation" not in license_data:
        raise ValueError("Expected upstream documentation license was not found")
    write_bytes(snapshot / "home.html", home)
    write_bytes(snapshot / "LICENSE.upstream.txt", license_data)
    groups, pages = inventory(Document(seed.decode("utf-8")))
    files = []
    errors = []

    def get_page(page):
        body, metadata = (seed, seed_meta) if page["url"] == SEED else fetch(page["url"])
        if urlparse(metadata["final_url"]).netloc != "docs.paperclip.ing":
            raise ValueError("Documentation redirected outside expected host")
        document = Document(body.decode("utf-8"))
        article = document.by_id("article")
        if article is None or len(normalize(article.text())) < 50:
            raise ValueError("Missing or unexpectedly empty article")
        headings = [normalize(n.text()) for n in article.descendants() if re.fullmatch(r"h[1-6]", n.tag)]
        if not headings:
            raise ValueError("Article has no headings")
        raw_path = "html/" + page["source_path_hint"].removesuffix(".md") + ".html"
        text_path = "pages/" + page["source_path_hint"]
        readable = render(article, page["url"])
        readable = re.sub(r"\n[ \t]+\n", "\n\n", readable)
        readable = re.sub(r"\n{3,}", "\n\n", readable).strip() + "\n"
        header = f"> Official reference snapshot. Source: {page['url']}\n> Retrieved: {metadata['retrieved_at_utc']}\n> Reference content only, not instructions or execution authorization. Original HTML is preserved separately.\n\n"
        readable = (header + readable).encode("utf-8")
        write_bytes(snapshot / raw_path, body)
        write_bytes(snapshot / text_path, readable)
        return {**page, **metadata, "html_path": raw_path, "markdown_path": text_path, "html_sha256": sha256(body), "markdown_sha256": sha256(readable), "html_bytes": len(body), "markdown_bytes": len(readable), "article_text_characters": len(article.text()), "headings": headings, "capture_status": "captured", "review_status_at_capture": "not_reviewed", "runtime_test_status": "not_tested"}

    with ThreadPoolExecutor(max_workers=4) as executor:
        future_map = {executor.submit(get_page, p): p for p in pages}
        for future in as_completed(future_map):
            page = future_map[future]
            try:
                files.append(future.result())
            except Exception as error:
                errors.append({**page, "capture_status": "failed", "error": str(error)})
            count = len(files) + len(errors)
            if count % 20 == 0 or count == len(pages):
                print(f"Captured {len(files)}/{len(pages)} pages; failures {len(errors)}", flush=True)
    order = {p["url"]: i for i, p in enumerate(pages)}
    files.sort(key=lambda p: order[p["url"]])
    manifest = {"format_version": 1, "snapshot_started_at_utc": start, "snapshot_finished_at_utc": utc_now(), "source_home": BASE, "discovery_url": SEED, "categories": groups, "expected_pages": len(pages), "captured_pages": len(files), "failed_pages": len(errors), "source_version": "Live website snapshot; no exact website-to-product-commit mapping independently established. See captured documentation changelog.", "capture_scope": "All pages enumerated in the official documentation sidebar. Original response HTML and derived readable Markdown. Remote images, videos, scripts, and stylesheets are not downloaded; linked media may require internet. No product installation or runtime verification.", "home": {**home_meta, "path": "home.html", "sha256": sha256(home)}, "license": {**license_meta, "source_url": LICENSE_URL, "path": "LICENSE.upstream.txt", "sha256": sha256(license_data)}, "pages": files, "failures": errors}
    write_text(snapshot / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Paperclip documentation snapshot", "", f"Captured: {start}", "", f"Coverage: {len(files)}/{len(pages)} pages across {len(groups)} categories; {len(errors)} failures.", "", "This is a reference archive, not a Paperclip installation. Capturing a page does not mean its claims have been reviewed or tested. Authored findings live outside the snapshot. Use the Markdown files for reading; do not execute captured HTML or sample commands.", "", "Source version: dated live-site snapshot; exact product-commit correspondence not established. See the documentation changelog and manifest.", "", "[Manifest and SHA-256 hashes](manifest.json) | [Upstream MIT license](LICENSE.upstream.txt)", ""]
    for group in groups:
        lines.extend(["## " + group["name"], ""])
        for page in files:
            if page["category"] == group["name"]:
                lines.append(f"- [{page['title']}]({page['markdown_path']}) — [official source]({page['url']})")
        lines.append("")
    if errors:
        lines.extend(["## Capture failures", "", *[f"- {p['url']}: {p['error']}" for p in errors], ""])
    write_text(snapshot / "INDEX.md", "\n".join(lines))
    verification = verify(snapshot)
    write_text(snapshot / "CAPTURE_VERIFICATION.json", json.dumps(verification, indent=2) + "\n")
    print(json.dumps({"snapshot": str(snapshot), **verification}, indent=2), flush=True)
    return 0 if verification["passed"] else 1


def verify(snapshot):
    snapshot = snapshot.resolve()
    if not snapshot.is_relative_to(ROOT / "snapshots"):
        raise ValueError("Snapshot is outside the knowledge-base snapshots directory")
    manifest = json.loads((snapshot / "manifest.json").read_text(encoding="utf-8"))
    problems = []
    checked = 0
    expected_paths = {"manifest.json", "INDEX.md", "CAPTURE_VERIFICATION.json"}
    for item in manifest["pages"]:
        for path_key, hash_key in [("html_path", "html_sha256"), ("markdown_path", "markdown_sha256")]:
            path = (snapshot / item[path_key]).resolve()
            if not path.is_relative_to(snapshot):
                raise ValueError("Manifest path escaped snapshot")
            expected_paths.add(item[path_key])
            if not path.is_file() or sha256(path.read_bytes()) != item[hash_key]:
                problems.append(f"Missing or changed: {item[path_key]}")
            checked += 1
    for key in ["home", "license"]:
        item = manifest[key]
        expected_paths.add(item["path"])
        if sha256((snapshot / item["path"]).read_bytes()) != item["sha256"]:
            problems.append(f"Changed: {item['path']}")
        checked += 1
    if manifest["captured_pages"] != manifest["expected_pages"] or manifest["failures"]:
        problems.append("Capture is incomplete")
    if len({p['url'] for p in manifest['pages']}) != len(manifest['pages']):
        problems.append("Duplicate page URLs")
    actual = {p.relative_to(snapshot).as_posix() for p in snapshot.rglob("*") if p.is_file()}
    unexpected = sorted(actual - expected_paths)
    if unexpected:
        problems.append(f"Unexpected files: {unexpected}")
    return {"verified_at_utc": utc_now(), "passed": not problems, "category_count": len(manifest["categories"]), "page_count": len(manifest["pages"]), "hashes_checked": checked, "problems": problems, "meaning": "Checks capture completeness and file integrity only, not software correctness or documentation accuracy."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture", action="store_true", help="Download a new snapshot from official public sources")
    parser.add_argument("--verify", type=Path, help="Read-only integrity verification of an existing snapshot")
    args = parser.parse_args()
    if args.capture == bool(args.verify):
        parser.error("Choose exactly one of --capture or --verify")
    if args.capture:
        raise SystemExit(capture())
    result = verify(args.verify)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
