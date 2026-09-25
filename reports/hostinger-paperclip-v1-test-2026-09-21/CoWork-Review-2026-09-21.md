# Chief Advisor review — Hostinger / Paperclip v1.0 test report

**Reviewer:** CoWork, Chief Advisor · **Report reviewed:** Revision 1, prepared by Codex, dated 2026-09-21 (runtime evidence 2026-09-18)
**Review date:** 2026-09-21 · **Outcome: the verdict is supported. Accept the report as written.**
**Status of this file:** a separate dated review, as the package README directs. No original evidence was altered. This review authorizes nothing.

---

## What I checked myself

Not a re-reading of Codex's summary. I verified:

- **All 12 evidence files hash-match the manifest.** 12 matched, 0 mismatched, 0 missing.
- **The PDF matches the hash recorded in verification.json** (`561344e1…`).
- **E03**, the approval card, reads verbatim: "Anyone — Anyone in the organization can respond — the board or any agent, including the one that asked." Characterised accurately.
- **E02**, the reviewer run, reads verbatim: "[paperclip] Adapter execution timeout: none (no adapter wall-clock timeout for this target; set adapterConfig.timeoutSec to add one)." Characterised accurately. Also shows claude_local, anthropic/unknown, succeeded, 2m 4s, SOU-3 done, Cost shown as a dash.
- **E06**, the Claude environment test, reads: "ANTHROPIC_API_KEY is not set; subscription-based auth can be used if Claude is logged in," result Passed, Node v24.20.0, ACP engine.

**On the report's discipline.** It refuses to claim timebox compliance it cannot evidence, refuses to treat "both paused" as a verified state, refuses to carry deleted-instance facts forward, records renewal as NOT VERIFIED rather than estimating it, and separates NOT ASSESSED from ABSENT so an untested view is never scored as a failure. That restraint is what makes the rest of it trustworthy.

**A correction to my own record.** On 2026-09-17 I advised that Claude agents could not be tested within the boundaries, because Hostinger exposes Anthropic only as an API-key field. Sebastian challenged that and was right. E06 and E02 together settle it: a Claude Code agent ran to success on the managed instance with no Anthropic API key set, on subscription authentication. My advice was wrong and the test disproved it.

---

## Question 1 — Is the partial-success classification supported?

**Yes, and I would sharpen both halves.**

**What was demonstrated matters more than "partial" conveys.** An OpenAI-backed Chief of Staff and an Anthropic-backed reviewer passed work between them, and the reviewer produced five substantive findings against the draft, with no human relaying messages between engines. That is the central question of the last three weeks and it is now answered yes, on evidence.

**What was not demonstrated is more serious than a missing checkbox.** The approval gate is the control the entire governance case rests on. Without it, Paperclip is a workflow tracker rather than a governance layer.

**On separate agents versus audited isolation, the report's distinction is correct and should stay.** Two agent identities on two adapters were observed. Nothing tested whether their filesystems, secrets or credentials are actually separated. Independence of *assignment* was shown; independence of *access* was not. Those are different claims and the report is right not to blur them.

---

## Question 2 — Are those three the right prerequisites?

Yes, with a reordering and two additions.

### G1, approval audience — the blocking one, and worse than "not met"

The setting is not merely permissive, it is inverted against our own rule. The card was proposed by the Chief of Staff and allows "any agent, including the one that asked" to answer it. Our operating model states in two places that nobody reviews or approves their own work. This configuration permits exactly that.

**Two things the report notes but does not elevate.** The earlier plan card *was* human-only and the final card was not, so either the setting does not persist across cards, is not inherited, or was reset. That is a behaviour question rather than a one-off operator slip, and it should be isolated before anything else. Second, no agent actually self-approved, so this is a demonstrated capability and not a demonstrated incident. Correct as stated.

**Acceptance criterion for any retest:** not "a human can approve" but "an agent is refused." The gate must be proven by rejection, not by the absence of misuse.

### G2, reviewer timeout — narrower than it looks, and therefore more diagnosable

The log line is explicit and is stronger evidence than elapsed time, as the report says. The useful detail is the asymmetry: the Codex run reported a 300-second timeout and the Claude run reported none. The mechanism works on one adapter and not the other in this configuration. That points at something specific to the Claude adapter, or to how its configuration was saved, which is a narrow question worth one check rather than a broad concern.

Note also that even the working case proves only that the value reached the invocation. Nothing was terminated by a timeout. No run limit and no retry limit was exercised at all.

### G3, permissions — consistent with an independent finding, which strengthens it

Task assignment remained enabled by an organisation-wide default while the instructions forbade assigning. Instructions narrow requested behaviour, not access. This matches what my capability assessment found from the documentation: **Paperclip governs workflow, not capability.** Two independent routes reaching the same conclusion is worth recording as a settled property of the product rather than a finding about this instance.

### Two prerequisites I would add

**G4 — identity attribution.** E02 shows the run executed "On behalf of Admin." If every agent run is attributed to the administrator rather than to a distinct agent identity, the audit trail is weaker than it appears and the per-user secrets model is unlikely to deliver per-business separation. One check, high consequence for the four-business design.

**G5 — cost reporting.** Both runs show Cost as a dash, not zero. The report states this correctly but leaves it in the usage section. Its consequence belongs with the controls: **if runs are recorded unpriced, a budget policy that meters dollars never fires.** I flagged this as a documented risk on 2026-09-16; it is now an observed one. Any future test must establish whether a budget cap can actually stop work on this platform.

---

## Question 3 — The smallest useful follow-up scope

**The next test should not be another workflow test.** The workflow works. The open questions are about controls and about plain facts, and most of them need no agent runs at all.

### Phase A — zero agent runs, mostly clicks

Do this first, because several answers could close the question before anything is spent.

1. **Renewal date and price**, from the billing page. Currently NOT VERIFIED, and it governs a decision with a deadline attached to it.
2. **Paperclip version, and processor, memory and disk allocation** on the replacement instance. Unknown capacity against software with an unresolved memory defect is the single largest reason this platform may be unsuitable.
3. **Upgrade controls** — whether any pin, defer or rollback exists.
4. **Create a second company.** Does one plan hold more than one? Do views separate? This decides whether four businesses means one bill or four, and it was never tested.
5. **The backup page**: what exists, what retention, and what a download actually contains.
6. **Whether the approval audience can be set to human-only at all**, in configuration, without running anything.

### Phase B — minimum runs, only if Phase A does not disqualify

7. **Prove the gate refuses an agent.** Set human-only, have an agent attempt to answer, record the refusal. Two runs at most.
8. **Prove a timeout terminates a run** on the Claude adapter. One deliberately overlong run.
9. **Prove a budget cap stops work**, given costs report as a dash. One run against a cap set near zero.

Three runs. The stop conditions and the honest-gap rule from the first test carry over unchanged.

**Out of scope for a follow-up:** production data, real credentials, repository connections, migration, and any further five-view assessment. The views can be judged once the platform's suitability is settled, not before.

---

## One item needing attention regardless of what is decided next

**The instance is publicly addressable, is not confirmed disconnected, and now has a working Claude subscription login attached to it.**

The report is properly careful that "both paused" is operator attestation, and that pausing is not credential revocation, endpoint closure or shutdown. That care is right, and the consequence deserves stating plainly: Sebastian's Claude subscription and his ChatGPT subscription are currently connected to a publicly reachable application, protected by a password, with no second factor documented, running software with unresolved security history.

Nothing suggests anything has gone wrong. But this is standing exposure for no current benefit, because the test is over.

**Recommended, and needing Sebastian's instruction rather than mine:** disconnect both provider connections at the application, confirm the agents are paused with a screenshot taken after the fact, and decide whether the application stays running at all while the keep-or-cancel decision is open.

Separately, the Google dangerous-site warning on the deleted first instance is correctly recorded as historical and unexplained. It should stay on the open list. An unexplained safe-browsing flag on a platform being considered to hold four businesses' management records is worth understanding, even though the instance that carried it is gone.

---

## Disposition

**Accept Revision 1 as written.** The verdict is supported, the evidence is intact and internally consistent, the limitations are stated more rigorously than I would have required, and the errors it corrects — mine about Claude authentication, its own about the deliverable link and the B4 finding — are recorded rather than quietly fixed.

Sebastian retains every decision: whether to disconnect and pause, whether to run Phase A, and whether to keep or cancel the subscription. This review requests none of them.
