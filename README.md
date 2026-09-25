# Agent Operations

Private, cross-business reference material for Sebastian Cwik's agent operations.

Start with [the Paperclip knowledge base](knowledge/paperclip/README.md).

This folder is separate from SourceCorrect's product and program repositories. It does not grant execution authority or contain a running Paperclip installation.

> **Status change, 2026-09-25.** The original text of this file, authored by Codex on 2026-09-16, ended with the sentence: *"No remote repository or offsite backup has been configured for this folder."* That was true when written and is no longer true — this folder is now backed up to a private GitHub repository, verified by restore. The verbatim original is preserved in this repository's history at commit `54577fc` (416 bytes, SHA-256 `e373729c…`). Everything above this note is Codex's original wording, unchanged.

---

## Backup

Offsite backup of `C:\ClaudeProject\AgentOperations\`, which before 2026-09-25 existed only on Sebastian's desktop with no copy anywhere.

**Private repository. Not for distribution.**

| Folder | Contents |
|---|---|
| `knowledge/paperclip/` | Captured reference snapshot of the Paperclip documentation (193 pages, markdown and original HTML), the capture tooling, and the capability, findings and hosting analyses written from it |
| `reports/hostinger-paperclip-v1-test-2026-09-21/` | Hostinger / Paperclip v1.0 test report, 12 evidence files, evidence manifest, verification record, and the Chief Advisor review |
| `reports/paperclip-approval-control-test-2026-09-25/` | Human-only approval-control test (task SOU-4) and its findings |

### Sensitivity

Screened before upload: no credentials, API keys, private keys, customer data or financial data. The test evidence does contain **private hostnames, internal identifiers and screenshots of our own Paperclip instance**, which is why this repository is private and stays private.

Storing raw screenshots in version control is a deliberate exception to the program's standing evidence rule, authorized by Sebastian on 2026-09-25, on the grounds that this is our own test tooling rather than customer or financial evidence, and that leaving it unbacked on a single machine was the larger risk.

### Restoring — read this first

**On Windows, use this command, not a plain `git clone`:**

```
git -c core.longpaths=true clone https://github.com/CommonCentsAnalytics/agent-operations.git
```

**Clone into a short path** such as `C:\AgentOperations`, not a deeply nested folder.

**Why this matters.** Two files inside the Paperclip snapshot have paths long enough that a plain clone into a nested folder exceeds Windows' 260-character path limit. Git prints a single easily-missed warning and carries on, leaving those two files absent while everything looks successful:

```
knowledge/paperclip/snapshots/.../prepare-mcp-integration.html
knowledge/paperclip/snapshots/.../prepare-mcp-integration.md
```

This was found during restore verification, not in production. With the command above, all 445 files restore and `git status` reports clean.

### Verification performed on creation

All 444 original files were hashed before any change was made. The backup was then downloaded fresh from GitHub and every restored file compared against those hashes:

- **443 byte-identical** after the round trip
- **0 original files missing**
- 1 differed — this README, which had been overwritten and has since been restored above
- 1 added — `.gitattributes`, which disables line-ending conversion so clones stay byte-exact
