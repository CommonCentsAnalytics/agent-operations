# Paperclip capability map for Sebastian's businesses

Initial documentation review, September 16, 2026 (New York). **This is a fit assessment, not an implementation plan or a guarantee.** Source links below point to the preserved snapshot; each page also carries its original website URL.

## Our aim

One visible management environment in which Sebastian can see work across businesses, communicate with a Chief of Staff, obtain independent Chief Advisor review, and authorize consequential actions. Project Leads and Specialist Workers should handle parallel work without Sebastian carrying messages between them.

Paperclip is a candidate coordination layer. The agent runtimes that do the work, their model access, and the machines running them still need configuration and funding. Saving its documentation has not created that team.

## Fit and what remains to prove

| Need | What the documentation supports | What we still need to establish |
| --- | --- | --- |
| A visible organization with managers and workers | [Org structure](snapshots/2026-09-17T005212Z/pages/guides/org/org-structure.md) describes a reporting tree and agent roles. | Map Chief of Staff, Chief Advisor, and Project Leads without confusing a reporting line with review independence. Multiple project assignments do not imply multiple managers. |
| Different models for different agents | [Adapter overview](snapshots/2026-09-17T005212Z/pages/reference/adapters/overview.md) documents several agent-runtime connections, including Claude Code and Codex. | Verify the exact runtime, authentication, availability, and provider terms we will use. This does not connect existing desktop conversations or establish a CoWork desktop trigger. |
| Handoffs without copy-paste | [Delegation](snapshots/2026-09-17T005212Z/pages/guides/org/delegation.md) describes assignments waking workers, progress comments, and manager escalation. | Exercise one complete proposal → independent review → consolidated answer → Sebastian decision loop. Check failures and paused agents, not only the successful route. |
| Independent review with a human decision | [Execution policies](snapshots/2026-09-17T005212Z/pages/guides/power/execution-policy.md) documents review and approval stages, reassignment, recorded decisions, and exclusion of the executor from its own review. | Configure a responsible human and verify our selected release enforces the intended route. An issue-completion gate alone is not proof that an agent cannot push code or change AWS before approval. |
| Stop unproductive agent-to-agent loops | The same [execution-policy page](snapshots/2026-09-17T005212Z/pages/guides/power/execution-policy.md) describes a configurable review-round limit and escalation to the responsible human. | Confirm a responsible human is actually set; the documented fallback without one can continue the loop. Also bound retries and spend outside review rounds. |
| See what is happening without asking | [Dashboard](snapshots/2026-09-17T005212Z/pages/guides/day-to-day/dashboard.md) describes agent status, work counts, spending, approvals, and activity. | Inspect the interface with real tasks. Check freshness, failure visibility, and whether it answers Sebastian's questions clearly. Documentation is not a visual acceptance test. |
| Separate business entities | [Companies API](snapshots/2026-09-17T005212Z/pages/reference/api/companies.md) describes company-scoped agents, projects, work, and access. | Prove company permissions and worker filesystem/network isolation. A company boundary in the application is not automatically a separate machine or credential boundary. |
| A Chief of Staff across those entities | Company-scoped records and [member access](snapshots/2026-09-17T005212Z/pages/guides/org/members-and-access.md) provide relevant building blocks. | **Not established:** one agent's safe, authorized access to summaries across companies. Do not assume an all-business Chief of Staff exists automatically, or solve it by giving every worker administrator access. |
| Parallel projects and an intelligible roadmap | Relevant pages are captured: [Projects](snapshots/2026-09-17T005212Z/pages/guides/projects-workflow/projects.md), [Goals](snapshots/2026-09-17T005212Z/pages/guides/projects-workflow/goals.md), and [Routines](snapshots/2026-09-17T005212Z/pages/guides/projects-workflow/routines.md). | Detailed fit review and a small multi-project demonstration remain. Coverage in the index is not evidence that every desired portfolio view exists. |
| A discoverable document library | Relevant pages are captured: [Artifacts](snapshots/2026-09-17T005212Z/pages/guides/day-to-day/artifacts.md) and [Issues](snapshots/2026-09-17T005212Z/pages/guides/day-to-day/issues.md). | Verify document navigation, search, and links to authoritative records. Passage-level annotation is not a mandatory acceptance requirement. |
| Understand and limit expenditure | [Costs](snapshots/2026-09-17T005212Z/pages/guides/day-to-day/costs.md) documents budget controls and spend reporting. | Measure real task costs, usage coverage, in-flight overrun behavior, and provider bills. Agent budgets do not include every hosting or maintenance cost. No monthly estimate is approved. |
| Keep records portable and recoverable | [Backup/restore guide](snapshots/2026-09-17T005212Z/pages/how-to/back-up-and-restore-a-company.md) documents exports and imports. It explicitly excludes approvals, cost events, and activity logs from company bundles. | Design and test complete instance recovery, not just a company export. Include database, files, configuration, and necessary secrets under appropriate protection. |
| Operate while Sebastian's laptop is closed | [Deployment overview](snapshots/2026-09-17T005212Z/pages/reference/deploy/overview.md) describes local and authenticated deployments. | Compare an always-on host and worker arrangement, security, backups, updates, capacity, and total cost. Self-hosting is not maintenance-free. |

## Smallest useful future proof

After hosting and access are separately authorized, use non-sensitive sample records to test a Chief of Staff, an independent Chief Advisor, and Sebastian's approval step. Then add a second project/company to expose cross-project visibility and isolation gaps. This is a **proposed test**, not permission to deploy or resume paused SourceCorrect work.

The goal is to test the management process before trusting it with production actions, not to reproduce every feature in 193 pages.
