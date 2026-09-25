# Findings and verification

Prepared by Codex, September 16, 2026 (New York). No independent reviewer has checked these authored notes. No Paperclip installation was run.

## Capture evidence

| Check | Result | Evidence |
| --- | --- | --- |
| Documentation navigation | 15 categories, 193 page links | [Manifest](snapshots/2026-09-17T005212Z/manifest.json), including each category's advertised and discovered count |
| Page retrieval | 193 captured; zero failed | Same manifest: URL, retrieval time, response metadata, and output paths for each page |
| File integrity | 388 source/derived file fingerprints checked; passed | [Capture verification](snapshots/2026-09-17T005212Z/CAPTURE_VERIFICATION.json) |
| Original content retention | Downloaded HTML retained alongside readable Markdown | Snapshot `html/` and `pages/` folders |
| Redistribution notice | Upstream MIT license retained | [License](snapshots/2026-09-17T005212Z/LICENSE.upstream.txt) |
| Offline extraction and navigation tests | **11 tests passed**: discovery guards, rendering, all-page headings, code-line content, hashes, and guide/index links | [Reusable test suite](tools/test_capture_docs.py); run after the authored guides were created |
| Product behavior | **Not tested** | No installation, agent run, permission test, or restoration performed |

Fingerprints detect a later mismatch against this locally generated manifest. They do not prove that the documentation is correct, certify the vendor, or independently authenticate an archive if both files and manifest are changed together. The capture covers sidebar-listed pages, not every URL, image, script, or external reference on the internet.

The Markdown conversion changes presentation, including blank-line spacing and indentation inside lists or quotations. The automated code-content check compares non-empty lines while allowing those presentation differences; it is not a byte-for-byte check of executable examples. Exact downloaded HTML remains available. No documentation commands were executed. The snapshot occupies about 24.3 MB before any filesystem compression.

## Review coverage

The initial map uses selected passages on delegation, organization structure, execution policies, dashboards, company boundaries, membership/access, adapters, costs, deployment modes, and backup/export exclusions. It is **not** a full audit of those pages or of all 193 documents. Projects, goals, routines, and artifacts are linked as next-reading material where their exact fit has not yet been established.

The snapshot manifest's `not_reviewed` fields describe the state **at capture time**. This separate file records subsequent review; do not rewrite historical capture metadata to imply the entire library was reviewed.

## Material findings worth keeping

### 1. Handoffs and review stages are documented product capabilities

**Source:** [Delegation](snapshots/2026-09-17T005212Z/pages/guides/org/delegation.md), [Execution policies](snapshots/2026-09-17T005212Z/pages/guides/power/execution-policy.md).

**Documented:** task assignment can wake an agent; review and approval stages can intercept completion and route work to a reviewer or human. The execution-policy page describes executor exclusion from its own review and a review-round escalation mechanism.

**Our interpretation:** these are promising building blocks for reducing Sebastian's relay work. They are not proof that our preferred models, permissions, and exact Chief of Staff workflow already work together. A responsible human must be configured for the documented loop-escalation behavior.

**Verification:** relevant documentation read by Codex; not reproduced; independently unchecked.

### 2. Workflow approval and permission to act are different controls

**Source:** [Execution policies](snapshots/2026-09-17T005212Z/pages/guides/power/execution-policy.md).

**Documented:** the described gate controls issue transitions and who can advance review/approval stages.

**Our interpretation:** do not infer that this blocks every external side effect. Before a worker can deploy, push to a protected repository, spend money, or change AWS, its tools and credentials also need the appropriate restrictions. This library does not grant those rights.

**Verification:** distinction derived from the documented scope; no external-action bypass test performed.

### 3. Multiple companies do not automatically create one cross-business Chief of Staff

**Source:** [Companies API](snapshots/2026-09-17T005212Z/pages/reference/api/companies.md), [Members and access](snapshots/2026-09-17T005212Z/pages/guides/org/members-and-access.md).

**Documented:** records and agent access are company-scoped; board/administrator access follows different rules.

**Open question:** how should a single management agent assemble only the approved cross-business summaries while workers remain isolated? We have not established the answer. Application tenancy is also not a verified worker sandbox.

**Verification:** relevant documentation read by Codex; not reproduced; independently unchecked.

### 4. A company export is not a complete operational backup

**Source:** [Back up and restore a company](snapshots/2026-09-17T005212Z/pages/how-to/back-up-and-restore-a-company.md), sections “What a package contains” and “Check what the bundle won't carry.”

**Documented:** company packages omit approvals, cost events, activity logs, and secret values. Projects, skills, and issues also require the relevant inclusion settings rather than assuming everything is exported by default.

**Our interpretation:** portability is useful, but preserving decision evidence and recovering a whole instance requires a separate backup-and-restore design. We must test recovery before calling the future installation backed up.

**Verification:** relevant documentation read by Codex; no export or restore performed.

### 5. Documentation capture is not long-term memory or full understanding

**Evidence:** the local capture manifest and the scope of this task.

**Finding:** future agents can retrieve the same saved sources rather than reconstructing them from chat. They still need access, must read the relevant passages, and must check for version changes. No model has permanently absorbed this entire library simply because it exists.

## How to add a useful finding

Keep it short: claim; exact source and date/version; collected by; checked by **and what was actually checked**; remaining uncertainty; consequence for our decision. Say “not tested” when appropriate. Sebastian's approval selects a direction; it does not turn an untested technical claim into a verified result.

Do not turn minor wording notes into a new governance workstream. Prioritize gaps that affect confidentiality, approval authority, recovery, cost, or whether the required workflow can operate.
