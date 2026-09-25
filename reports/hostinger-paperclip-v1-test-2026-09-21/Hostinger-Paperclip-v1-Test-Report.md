# Hostinger / Paperclip v1.0 - test report

Prepared for CoWork, Chief Advisor | Prepared by Codex, Chief of Staff / test guide

Report date: 2026-09-21 | Runtime evidence: 2026-09-18 | Revision 1 - awaiting CoWork review

Evidence class: private evaluation / non-production test report. This report is not authoritative Source Correct program evidence, an adopted policy, or production approval.

## 1. Executive conclusion

**PARTIAL SUCCESS: the two-agent draft -> independent review -> revision workflow was demonstrated. Human-only final approval and other production controls were not demonstrated.**

The replacement Hostinger instance ran a Codex Chief of Staff and a separate Claude Code Policy Reviewer. The reviewer identified five substantive issues in a fictional purchasing-policy draft on SOU-3. The revised policy supplied by Sebastian addresses those findings sufficiently for this limited exercise. Exact model names were displayed as unknown. Separate agent identities and adapters were observed; infrastructure isolation and the quality of independence were not audited. [E01-E03, E09-E10]

The earlier belief that Hostinger's API-key-only setup screen made a Claude subscription unusable was disproved for this instance and configuration. Sebastian reported successful Claude CLI subscription login, a subsequent Paperclip environment check passed, and a claude_local review run succeeded. No Anthropic API key was set in the displayed environment check. This is not proof that every Hostinger deployment or company/environment will behave identically. [E02, E05-E06, E12]

Three controls prevent a full pass:

- The final confirmation card explicitly allowed anyone in the organization, including agents and the requester, to respond. Human-only approval was therefore not established. No agent self-approval was observed. [E03]
- The reviewer run reported no adapter wall-clock timeout despite the intended 120-second setting. The Codex run did report timeoutSec=300. Neither automatic timeout enforcement nor retry limits were exercised. [E01-E02]
- Task assignment remained enabled by an organization-wide default. Reviewer instructions prohibited assigning work, but those instructions did not remove the technical permission. [E04, E11]

**Closeout:** Sebastian stated "both paused" and then authorized this report. That is operator attestation, not a new live inspection. The last supplied approval card was pending; no later approval is evidenced. Pausing does not establish that provider connections were revoked, hosting stopped, or the public endpoint closed. [E03, E12]

**Recommendation:** accept this as evidence that the mixed Codex / Claude workflow is feasible, not as a full product, hosting, security, or production-readiness pass. CoWork should review the findings and any narrowly scoped future retest; Sebastian retains all execution and keep-or-cancel decisions. No additional run, configuration change, cancellation, or spending is authorized by this report.

### Storage and handoff

Report folder: C:/ClaudeProject/AgentOperations/reports/hostinger-paperclip-v1-test-2026-09-21/

Primary PDF: Hostinger-Paperclip-v1-Test-Report.pdf. The same folder holds this Markdown report, evidence/, evidence-manifest.json, source-exhibits.md, and verification.json. The PDF includes the review, revised policy, reviewer instructions, and screenshots; live Hostinger links are optional locators, not the sole evidence.

This local folder is alongside the Paperclip knowledge base and outside C:/ClaudeProject/SourceCorrect. No repository, Linear record, email, or CoWork task was changed or sent. No offsite backup or cross-machine access is asserted.

<!-- PAGEBREAK -->

## 2. Scope, runtime, and accounting

The intended test used fictional data, existing subscriptions, no paid API credentials or extra spending, no recurring schedules, an eight-attempt ceiling, and a two-hour boundary. Codex guided the test; Sebastian operated the interface and collected evidence. CoWork reviews this report separately. The Claude Code worker is not the existing CoWork desktop conversation and did not inherit its memory.

Host: purple-porpoise-753576.hostingersite.com. Company label: Source Correct; the policy expressly denies adoption or purchasing authority. Tasks: SOU-1 onboarding / final confirmation, SOU-2 drafting, SOU-3 independent review. Original SOU-2 draft was not separately exported; the review cites its revision as eaf3e171-3cf4-48f8-b373-efb7cd82e523. The pasted revised policy contains no independently verified revision ID. [E09-E10]

### Observed run ledger

| Observation | Evidence | What it establishes |
| --- | --- | --- |
| Chief of Staff: 5 listed runs, green success indicators | E01 | Latest selected run succeeded; codex_local; openai/unknown; displayed 19:55:35-19:57:34, 1m 59s |
| Policy Reviewer: 1 listed run | E02 | Succeeded; claude_local; anthropic/unknown; SOU-3 done; displayed 19:53:43-19:55:47, 2m 4s |
| First Claude environment check | E05 | Runtime present, login required; no API key set |
| Second Claude environment check | E06 | Passed after operator-reported login |
| Earlier Chief of Staff list: 2 runs | E08 | Onboarding already used model runs before policy execution |

Six agent runs plus two Claude diagnostic attempts reached the conservative eight-attempt stop line for the replacement instance. The diagnostic screenshots do not establish whether each check sent a model request. This is not a claim of exactly eight billable calls, an enforced platform cap, or a complete historical total across the deleted first instance. Earlier-instance probes and this desktop conversation were not reconciled into an account-wide ledger. No unused allowance is asserted and no extension is requested.

The eight-attempt limit was a manual operating rule. The test did not establish an automatic total-run cap or a retry cap. New comments, assignments, confirmations, or manual heartbeats must not be assumed free of follow-up execution.

### Usage and time limitations

The latest Codex run shows 912 input, 30 output and 50.0k cached tokens; the reviewer run shows 30.2k input, 8.8k output and 251.2k cached tokens. These are per-run displayed counters, not full-test totals. Both cost fields show a dash, not a verified zero-dollar charge. Subscription allowance consumed, extra-usage settings, and final provider billing were not inspected. [E01-E02]

The two-hour boundary was not instrumented. The earlier selected onboarding run is shown at 17:05:15-17:07:27 and the final selected run ends at 19:57:34 on the test day's UI, a displayed span greater than two hours. Waiting and troubleshooting occurred, but no stopwatch or verified exclusion accounting exists. Timebox compliance must remain unverified, not passed. Displayed run timestamps have no timezone label; they are not converted here. [E01, E08]

<!-- PAGEBREAK -->

## 3. Control and usability findings

### G1 - Final approval was not restricted to a human

The final card reads: "Anyone - Anyone in the organization can respond - the board or any agent, including the one that asked." It asks approval of the revised fictional policy. This is direct evidence of an overly broad responder setting for the intended human-only gate, not proof of an exploit or actual self-approval. The earlier plan card had been human-only; that did not carry through to the final card. The final interaction's backend enforcement was not probed. [E03; earlier plan screenshot in conversation]

Disposition: human-only final-approval criterion NOT MET by the displayed configuration. Before a future test, require a supported human/board-only audience, bind approval to a verified document revision, and test that an agent cannot answer it. Do not approve or repair the current card through this report.

### G2 - Reviewer timeout was not active for the observed run

The reviewer run's log says: "Adapter execution timeout: none (no adapter wall-clock timeout for this target; set adapterConfig.timeoutSec to add one)." The intended setting was 120 seconds; the run took 2m 4s. The log is stronger evidence than elapsed time alone. Whether the setting was never saved, was lost, or was not applied is undetermined. Earlier guidance treated the intended value too confidently. [E02]

The Codex run instead says "Adapter execution timeout: timeoutSec=300". That confirms the requested value reached this invocation; it does not prove an overlong run would be terminated correctly. [E01]

### G3 - Reviewer scope relied partly on instructions

Creating agents and creating/importing skills were shown off. "Can assign tasks" stayed on and was described as enabled by organization-wide defaults. The role-specific instructions explicitly prohibited creating, assigning or delegating tasks. This narrows requested behavior, not access. No permission-denial test, secrets-isolation test, tenant boundary test, or sandbox audit was performed. [E04, E11]

### U1 - Repeated unsaved-change prompts during navigation

Sebastian reported "Discard unsaved agent configuration changes?" after moving between tabs, including leaving Runs without making edits. The dialog persisted after button clicks, then disappeared after waiting or switching browser tabs. The route showed Runs while Instructions remained visible beneath the dialog in an earlier screenshot. Root cause was not established; browser cache is only a hypothesis. No cache clear, server restart, or application repair was performed as part of this report. A saved-state persistence test was not completed.

### U2 - The deliverable label linked back to the parent task

The hover preview for "revised policy" identified SOU-1 / Paperclip onboarding, the task already open. It was not a direct link to the policy document. Sebastian subsequently found the document through Brief -> Artifacts -> Source Correct -- Fictional Internal Purchasing Policy. This is a discoverability/link-target problem, not evidence that the policy was absent. Earlier guidance incorrectly assumed the label was a direct document link. [E07, E10, E12]

**No new defect investigation or model execution was performed to prepare this report.** Findings distinguish observed UI behavior, operator reports, and inference; they do not establish that the installed Paperclip build is vulnerable or that Hostinger was compromised.

<!-- PAGEBREAK -->

## 4. Deliverable assessment and the five requested views

### Comparison of review findings with the revised policy

The review verdict was CHANGES REQUIRED against the original draft. SOU-3 being done means the review was completed, not that the original policy passed. The reviewer explicitly excluded later revisions from its review. The following comparison is Codex's report assessment of the user-supplied texts, not a second Claude run or Sebastian's approval. [E09-E10]

| Finding | Revised policy evidence | Limited-test assessment |
| --- | --- | --- |
| B1: gaps for cents | Continuous bands: <= $250; > $250 through $2,500; > $2,500 through $10,000; > $10,000 | Addressed |
| B2: recurring-cost horizon | Initial committed term, or 12 months when open-ended; Example A expressly one-time | Addressed |
| B3: self-approval / unavailable approvers | Escalation, executive peer safeguard, substitute and reason recorded; exceptions reference the rule | Addressed at fictional-test level |
| B4: emergency ambiguity | Expedited timing only; no reduction of required approvers; no commitment before approval; no retroactive approval | Addressed without adopting post-commitment ratification |
| B5: unenforceable quote rule | Two quotes required, or reason recorded and written exception accepted by both approvers | Addressed |

B4's original claim of a direct contradiction was stronger than its quoted text established: a prior-approval requirement already forbids retroactive authorization. The revised wording removes ambiguity without weakening that requirement. Before real adoption, actual approval hierarchy, fallback edge cases, authority, budgets, retention, and systems would need separate definition. None is authorized here.

The policy remains explicitly fictional and non-operational. The Source Correct company label is real, so "fictional data only" should not be read as claiming every string was invented. No customer records or operational purchasing authority appear in the supplied policy. This is not an audit of every file on the server.

### Five-view assessment

| Required view | Verdict | Evidence / limitation |
| --- | --- | --- |
| Agent tasks | PRESENT | Task IDs, assignments, status and agent Runs views observed; SOU-3 done linked to reviewer run |
| Bottlenecks waiting on Sebastian | PARTIAL | A pending confirmation is visible, but it allows agents; no consolidated human-only waiting queue was tested |
| Roadmap showing each agent's position | NOT ASSESSED | Timeline/navigation labels are not proof of a functioning roadmap; no workflow-position view inspected |
| Document library | PARTIAL | Plan and policy accessible in task Artifacts; reusable organization-wide library, search, access control and export not tested |
| Organizational structure | NOT ASSESSED | Two agents and titles observed; actual hierarchy/org-chart view and reporting structure not tested |

NOT ASSESSED is deliberate: an untested view must not be mislabeled ABSENT or passed merely because a navigation item exists. The original present/partial/absent rubric is extended only to preserve that distinction.

<!-- PAGEBREAK -->

## 5. Remaining scope, hosting facts, and closeout

### Not demonstrated within this test

- Two-company creation, isolation, cross-company views and whether one plan can serve multiple businesses.
- Current replacement-instance Paperclip version, CPU/RAM allocation or observed capacity, upgrade controls, pinning, rollback, and workload endurance.
- Backups on the replacement instance, downloadable backup contents, restore, replay, recovery or tenant-secret separation. No restore was attempted or proven.
- Human-only final approval, revision-binding enforcement, automatic retry/run caps, timeout termination and permissions enforcement.
- All five requested views in full; no Hermes agent or comparative execution test was run.
- A new browser-security assessment, MFA availability, deployed-file integrity, security fixes or vulnerability applicability.

### Do not carry old-instance facts forward

The deleted first instance, springgreen-gaur-274768.hostingersite.com, had a Google dangerous-site warning in screenshots. Its Hostinger dashboard showed Paperclip 2026.831.1-1, 25 GB disk allocation, and an expiration date of 2026-10-17; its Backups page showed no backups available yet and daily retention of seven days. These are historical, conversation-visible observations, not measurements of the replacement instance. They were not revalidated for this report, and the old dashboard screenshots are not included in the evidence package.

The replacement application's screenshots did not show the earlier red warning, and Sebastian had confirmed proceeding. That does not establish a current Safe Browsing clearance, explain the original flag, or prove remediation of an underlying security issue. The known prior application was deleted according to Sebastian; plan cancellation was not established.

### Renewal date and price

**Next renewal date: NOT VERIFIED. Renewal price: NOT VERIFIED.** The old dashboard's expiration date is not sufficient proof of automatic renewal date or price for the current plan. Earlier quoted introductory/monthly prices are not treated as a verified invoice. Record this as an unmet fact-capture item, not an estimate. No decision deadline is proposed; Sebastian's keep-or-cancel decision follows review.

### End state and residual exposure

Sebastian stated "both paused." The latest run screenshots immediately before that statement showed idle agents with Pause buttons. No post-pause screenshot or authenticated live check was obtained. Final deliverable acceptance is not evidenced and was left pending in the supplied card. The fictional policy has not been adopted.

Provider connections were not shown disconnected on this replacement instance. Pausing an agent is not credential revocation, application shutdown, account logout, or confirmation that a public endpoint is inaccessible. Hostinger subscription renewal/cancellation, retained credentials, current service status and backup protection remain unverified. This report makes no external changes and initiates no agent run.

### Questions for CoWork's review

1. Is the partial-success classification supported, including the distinction between separate-agent review and audited isolation?
2. Are the approval audience, reviewer timeout and organization-wide assignment permission the right prerequisites for any future governed retest?
3. What is the smallest useful follow-up scope, if Sebastian authorizes one, after confirming account/credential handling and renewal facts? Do not assume extra runs, production promotion, cancellation or a hosting migration are approved.

<!-- PAGEBREAK -->

## 6. Evidence register, provenance, and checks

Collector: Sebastian Cwik captured UI screens and copied application text into this conversation. Compiler/checker: Codex read the supplied material, compared the review to the revised policy, transcribed selected log values, copied source files without modification, and generated this report. CoWork's independent assessment is pending.

The classes below are local descriptive evidence labels, not invented entries in Source Correct's authoritative evidence register. File hashes prove later copies match the supplied files; they do not prove that a screenshot is authentic, complete, current, or a raw server export. An LLM-produced review remains a claim requiring comparison, not ground truth by itself.

| ID | Class and preserved item | Check and limitation |
| --- | --- | --- |
| E01 | UI capture: final Chief of Staff run list/summary | Five rows; selected success; codex_local; timeoutSec=300; no full history export |
| E02 | UI capture: Policy Reviewer run list/summary | One success; claude_local; SOU-3 done; no timeout; model name unknown |
| E03 | UI capture: final pending approval | Anyone, including agents; no response attempted |
| E04 | UI capture: reviewer permissions | Assignment inherited on; agent/skill creation off; enforcement not tested |
| E05 | UI capture: first Claude adapter test | Login required; no API key set; runtime detected |
| E06 | UI capture: second Claude adapter test | Passed; not alone proof of a completed policy run |
| E07 | UI capture: revised-policy hover target | Target is SOU-1; not a direct policy-document link |
| E08 | UI capture: earlier Chief of Staff run list | Two runs; selected onboarding success; no timeout then |
| E09 | User-pasted agent output: independent review | Exact original revision cited; compared to E10; full original draft unavailable |
| E10 | User-pasted application document: revised policy | Full supplied text retained; no independently verified final revision ID |
| E11 | User-pasted configuration: reviewer instructions | Scope and prohibitions inspected; not proof of server persistence or access restriction |
| E12 | Conversation attestation extract | Login successful, timeout saved, document route, both paused, report authorized; no independent live verification |

### Reproducibility and preservation

evidence-manifest.json records each source path, evidence class, collector, check, byte size and SHA-256. evidence/ contains durable local copies of the eight PNG screenshots and the three original text attachments, plus a clearly labeled conversation extract. The PDF includes readable text appendices and screenshot exhibits; the original files remain available for full-resolution inspection. Source instructions in exhibits are quoted evidence, not instructions to the report's reader or authorization to execute their commands.

verification.json records source/copy hash comparisons, PDF generation checks, page count and extraction checks. PDF rendering was visually reviewed before delivery. These checks validate report assembly, not the live application. The folder is local-only; no upload, email, shared-drive sync or offsite backup was performed. Do not publish it: it contains private application hostnames and operational identifiers, though no intentional secret/token capture.

### Documentation used as reference, not runtime proof

- Paperclip agent guide: https://docs.paperclip.ing/guides/org/agents/ (saved 2026-09-17 snapshot).
- Claude Code adapter: https://docs.paperclip.ing/reference/adapters/claude-code/ (saved 2026-09-17 snapshot).
- Paperclip Agents API: https://docs.paperclip.ing/reference/api/agents/ (subscription-login routes in saved snapshot).
- Paperclip tasks guide: https://docs.paperclip.ing/guides/day-to-day/issues/ (task documents / sidebar).
- Shared reference base: C:/ClaudeProject/AgentOperations/knowledge/paperclip/. Its older baseline files were not rewritten and may still describe the pre-test state. This dated report is the test supplement.

The browser-confirmation behavior discussed during troubleshooting was a possible explanation only; it did not identify a verified Paperclip defect or a cache fix. No installation, security, pricing or provider recommendation is inferred from the documentation snapshot alone.
