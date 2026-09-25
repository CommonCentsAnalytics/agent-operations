# AgentOperations — backup

Offsite backup of the agent-orchestration research folder that previously existed
only on Sebastian's desktop at `C:\ClaudeProject\AgentOperations\`.

**Private repository. Not for distribution.**

## What is here

| Folder | Contents |
|---|---|
| `knowledge/paperclip/` | Captured reference snapshot of the Paperclip documentation (193 pages, markdown + original HTML), plus the capture tooling and the capability, findings and hosting analyses written from it |
| `reports/hostinger-paperclip-v1-test-2026-09-21/` | The Hostinger / Paperclip v1.0 test report, its 12 evidence files, the evidence manifest, verification record, and the Chief Advisor review |

## Sensitivity

Screened before upload: no credentials, API keys, private keys, customer data or
financial data. The test evidence does contain **private hostnames, internal
identifiers and screenshots of our own Paperclip instance**, which is why this
repository is private and stays private.

Storing raw screenshots in version control is a deliberate exception to the
program's standing evidence rule, authorized by Sebastian on 2026-09-25, on the
grounds that this is our own test tooling rather than customer or financial
evidence, and that leaving it unbacked on a single machine was the larger risk.

## Restoring

```
git clone https://github.com/CommonCentsAnalytics/agent-operations.git
```

`.gitattributes` disables line-ending conversion, so a clone is byte-identical to
what was committed. The backup was verified on creation by cloning it fresh and
comparing the SHA-256 of all 444 files against the originals.
