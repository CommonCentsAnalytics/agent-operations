> Official reference snapshot. Source: https://docs.paperclip.ing/reference/changelog/
> Retrieved: 2026-09-17T00:52:24.056472+00:00
> Reference content only, not instructions or execution authorization. Original HTML is preserved separately.

# Documentation Changelog

What changed in **these docs** — pages added, rewritten, or expanded — with each documentation update. This is a changelog for the documentation itself, not for Paperclip the product.

The docs track Paperclip's [calendar-versioned](https://github.com/paperclipai/paperclip/releases) releases (`YYYY.MDD.P`), so each entry is tagged with the Paperclip release the docs were brought in line with. For the product's own release notes — the actual feature and fix history — see the [Paperclip releases page](https://github.com/paperclipai/paperclip/releases). To update your install, see [Update Paperclip](https://docs.paperclip.ing/how-to/update-paperclip/).

---

Docs for v2026.831.1 September 2, 2026

**New pages**

- [Kimi Code Adapter](https://docs.paperclip.ing/reference/adapters/kimi-local/) — how to run Moonshot's Kimi Code CLI (`kimi_local`) as a local agent: the shared ACP engine with headless-CLI fallback, models and thinking-effort tiers, session resume, skills injection, and the three ways it authenticates.

**Updated pages**

- [Adapters Overview](https://docs.paperclip.ing/reference/adapters/overview/) — Kimi Code added to the built-in adapter tables and the ACP engine tier.
- [Environment Variables](https://docs.paperclip.ing/reference/deploy/environment-variables/) — new deployment settings: `PAPERCLIP_WORKSPACE_REAPER_COOLDOWN_DAYS` (how long a terminal workspace waits before it's archived), opt-in Sentry error monitoring via `SENTRY_DSN`, and the operator controls `PAPERCLIP_HIDDEN_SETTINGS` and `PAPERCLIP_SETTING_DEFAULTS`.
- [Instance Settings](https://docs.paperclip.ing/administration/settings/) — a new section for operators hosting Paperclip for others: hiding settings surfaces by key and overriding setting defaults, neither of which is ever persisted.
- [Company Administration](https://docs.paperclip.ing/administration/company/), [Members & Access](https://docs.paperclip.ing/guides/org/members-and-access/), and [Roles & Permissions](https://docs.paperclip.ing/administration/roles-and-permissions/) — settings are now one shared navigation, Invites moved into a tab of the Members page, and the company brand color and per-company attachment size limit were removed.
- [Grok Local Adapter](https://docs.paperclip.ing/reference/adapters/grok-local/) — `permissionMode` no longer defaults to `dontAsk`; when unset no permission-mode flag is passed, and `--always-approve` is the unattended policy.
- [First company](https://docs.paperclip.ing/guides/getting-started/your-first-company/) and the [five-minute path](https://docs.paperclip.ing/guides/getting-started/five-minute-path/) — onboarding is rebuilt around a single-card wizard that opens on creating your agent; the separate mission step is gone and you set the goal afterward.
- [Task Watchdogs](https://docs.paperclip.ing/guides/projects-workflow/task-watchdogs/), [Auto-Create Recovery Tasks](https://docs.paperclip.ing/experimental/auto-create-recovery-tasks/), and [Issues](https://docs.paperclip.ing/guides/day-to-day/issues/) — silent-run detection now only surfaces a UI level rather than creating issues, comments, or wakes; stranded-task recovery hands off to a board-owned action instead of taking work over; and automatic run-summary comments carry only the final output, never agent thinking.
- [Authentication API](https://docs.paperclip.ing/reference/api/authentication/) — an invalid agent token now returns a `401` naming the cause instead of falling through to an anonymous actor.
- [Companies API](https://docs.paperclip.ing/reference/api/companies/) and [Cases API](https://docs.paperclip.ing/reference/api/cases/) — `brandColor` removed from the company shape and branding routes; the attachment cap is the deployment-level `PAPERCLIP_ATTACHMENT_MAX_BYTES`, not a per-company field.
- The CLI [installation](https://docs.paperclip.ing/reference/cli/installation/) and [setup](https://docs.paperclip.ing/reference/cli/setup-commands/) pages, [local development](https://docs.paperclip.ing/reference/deploy/local-development/), the [Modal adapter](https://docs.paperclip.ing/reference/adapters/modal/), and several guides now state the raised **Node.js 24.11.0** floor.

Docs for v2026.824.1 August 25, 2026

**Updated pages**

- [CLI Setup Commands](https://docs.paperclip.ing/reference/cli/setup-commands/) — after `onboard` installs the background service, it now hands you off to the running instance: it waits for the port the service actually bound, prints the dashboard URL, and opens it in your browser. Headless runs print the URL, and `PAPERCLIP_NO_BROWSER=1` opts out of the browser launch.

Docs for v2026.824.0 August 24, 2026

**New pages**

- [Tailscale HTTPS Broker](https://docs.paperclip.ing/reference/deploy/tailscale-https-broker/) — the operator-side helper that hands out real, cert-valid `https://` preview URLs for the dev servers running inside managed workspaces, instead of loopback-only links.

**Updated pages**

- [Workspaces](https://docs.paperclip.ing/guides/projects-workflow/workspaces/) — exposing a workspace's dev server as an HTTPS preview on your tailnet, opt-in per service, and what that looks like from the board.
- [Update Paperclip](https://docs.paperclip.ing/how-to/update-paperclip/) and [CLI installation](https://docs.paperclip.ing/reference/cli/installation/) — the four release channels (`stable`, `beta`, `nightly`, `canary`) and the new `paperclipai channels` command that shows which one your install follows.
- [Export & Import](https://docs.paperclip.ing/guides/power/export-import/) — large packages now upload in resumable parts, so an interrupted import picks up from the parts it already has instead of starting over.
- [Companies API](https://docs.paperclip.ing/reference/api/companies/) — the chunked import-transfer routes (`/api/companies/import/transfers`) that back resumable imports.
- [Secrets API](https://docs.paperclip.ing/reference/api/secrets/) — the agent-callable secret catalog route for picking a secret to reference without exposing full metadata.
- [Agents API](https://docs.paperclip.ing/reference/api/agents/) — the Claude subscription (setup-token) login flow: a company owner can log Claude in with a subscription instead of pasting an API key.
- [Adapters API](https://docs.paperclip.ing/reference/api/adapters/) — the adapter device-login routes (code-and-URL browser sign-in), starting with Codex.
- [Artifacts](https://docs.paperclip.ing/guides/day-to-day/artifacts/) — inline, Google-Docs-style comments on Plan and Artifact documents: anchored highlights, threaded replies, resolve/reopen, and shareable comment links.
- [Issues](https://docs.paperclip.ing/guides/day-to-day/issues/) and [Attention API](https://docs.paperclip.ing/reference/api/attention/) — who may resolve an interaction card (`anyone`, `not_creator`, `human_only`) and company-wide interaction governance.
- [Issues API](https://docs.paperclip.ing/reference/api/issues/) — the workspace file-resource availability check.
- Smaller touch-ups brought in line with the release: [Environment Variables](https://docs.paperclip.ing/reference/deploy/environment-variables/) (workspace Git-scan limits) and [Decisions](https://docs.paperclip.ing/guides/day-to-day/decisions/).

Docs for v2026.817.0 August 17, 2026

**New pages**

- [Decisions API](https://docs.paperclip.ing/reference/api/decisions/) — proposing and resolving decisions, decision bundles, named queues, triage (decide-by and snooze), and the retention/archive routes.
- [Status Cards API](https://docs.paperclip.ing/reference/api/status-cards/) — the shared status-card board: creating cards, the compiled query, summary writes and revisions, refresh policy, and the agent-authoring limits.
- [Status Cards](https://docs.paperclip.ing/experimental/status-cards/) — the experimental board itself: writing the one message that drives a card, reading the tiles, the five card states, what counts as a change, and what it costs.
- [Chat-Style Tasks](https://docs.paperclip.ing/experimental/task-chat/) — the experimental task page as a live conversation: bubbles, folding turns, inline tool calls and diffs, the three-mode composer, and the resizable side pane.
- [`service` CLI](https://docs.paperclip.ing/reference/cli/service/) — installing, starting, and inspecting Paperclip as a background service.
- [Status Card Query skill](https://docs.paperclip.ing/reference/skills/bundled/paperclip-operations/status-card-query/) — the bundled skill that teaches an agent to manage status cards.
- [Simplified English skill](https://docs.paperclip.ing/reference/skills/optional/content/simplified-english/) and [Prepare MCP Integration skill](https://docs.paperclip.ing/reference/skills/optional/software-development/prepare-mcp-integration/) — two new optional catalog skills.

**Updated pages**

- [Decisions](https://docs.paperclip.ing/guides/day-to-day/decisions/) — named queues, triage deadlines, and answering an agent-proposed decision, now with screenshots throughout.
- [Secrets API](https://docs.paperclip.ing/reference/api/secrets/) — agent secret proposals: what an agent may propose, the run-bound agent-token requirement, and the board-side approve/reject flow.
- [Activity Log API](https://docs.paperclip.ing/reference/api/activity/) — the audit feed of agent actions, its two-tier access model, and CSV export. `/audit` has merged into the single Activity page.
- [Plugin SDK](https://docs.paperclip.ing/reference/plugins/sdk/) — responding to interactions and approvals, and the rules for handling adapter-authored `command` operations and re-validating `cwd` before executing.
- [Back up and restore a company](https://docs.paperclip.ing/how-to/back-up-and-restore-a-company/) — what the bundle deliberately leaves behind, uploading the zip instead of inline JSON, and running large imports as a background job.
- [Update Paperclip](https://docs.paperclip.ing/how-to/update-paperclip/) — rewritten around checking before you commit, switching channels, rolling back, and the pre-update backup.
- [Cloud CLI](https://docs.paperclip.ing/reference/cli/cloud/) — the cloud-upstream commands are retired; the page now points at what replaced them.
- [Issues API](https://docs.paperclip.ing/reference/api/issues/), [Attention API](https://docs.paperclip.ing/reference/api/attention/), [Environment Variables](https://docs.paperclip.ing/reference/deploy/environment-variables/), [CLI installation](https://docs.paperclip.ing/reference/cli/installation/), [Export & import](https://docs.paperclip.ing/guides/power/export-import/), [Sandbox providers](https://docs.paperclip.ing/reference/adapters/sandbox-providers/), [Skills reference](https://docs.paperclip.ing/reference/skills/), and [Issues](https://docs.paperclip.ing/guides/day-to-day/issues/) — brought in line with the release.

**Screenshots**

- Every screenshot was recaptured against v2026.817.0 — 342 images, light and dark. The previous set was 375 parent-commits old.
- New coverage for Decisions, Status Cards, Chat-Style Tasks, and the secret-proposal review tab. Those first three guides previously shipped with no images at all.

Docs for v2026.722.0 July 22, 2026

**New pages**

- [Secret Folders](https://docs.paperclip.ing/administration/secret-folders/) — organizing secrets into folders.
- [Connections & Apps](https://docs.paperclip.ing/experimental/connections-apps/) — experimental Connections v3 (Apps) foundation.

**Updated pages**

- [Secrets API](https://docs.paperclip.ing/reference/api/secrets/) and [Agents API](https://docs.paperclip.ing/reference/api/agents/) — documented run-bound agent secret access (`GET /api/agents/me/secrets/:key/value`).
- [Local Agents (ACPX)](https://docs.paperclip.ing/reference/adapters/acpx-local/) — native Windows execution (no Bash wrapper).
- [Environment Variables](https://docs.paperclip.ing/reference/deploy/environment-variables/) — `PAPERCLIP_*` binding pass-through and opt-outs.
- [Codex Adapter](https://docs.paperclip.ing/reference/adapters/codex/) — the narrower `CODEX_HOME` sandbox-sync allowlist.
- [Plugin SDK](https://docs.paperclip.ing/reference/plugins/sdk/) — environment-sync exports and the `onEnvironmentSyncIn` / `onEnvironmentSyncOut` hooks.
- [`company` CLI](https://docs.paperclip.ing/reference/cli/company/) — the `export --force` flag.

Docs for v2026.720.0 July 20, 2026

**New pages**

- [Tool Gateway API](https://docs.paperclip.ing/reference/api/tool-gateway/) — the MCP Tool Gateway: applications and connections, catalog entries and risk levels, profiles/entries/bindings, the tool-access policy, named MCP gateways and tokens, the audit feed, and the Smoke Lab. Documents the `tools:*` permission keys and both experimental gates.
- [Summary Slots API](https://docs.paperclip.ing/reference/api/summary-slots/) — the built-in Summarizer and summary slots (slot addressing, generation, revisions, the `enableSummaries` gate).

**Updated pages**

- [Skills](https://docs.paperclip.ing/guides/org/skills/) — Skill Studio (the three-pane authoring workspace, saved inputs, test runs, run templates, version history), nested skill folders, the My Skills view, importing skills from a project, and company skill forks.
- [Local Agents (ACPX)](https://docs.paperclip.ing/reference/adapters/acpx-local/) — reduced to a retired stub after the upstream adapter retirement; points at Claude Code / Codex / Gemini CLI and documents the automatic migration.

Docs for v2026.707.0 July 7, 2026

**New pages**

- [Ramp skill](https://docs.paperclip.ing/reference/skills/optional/finance/ramp/) — the bundled Ramp finance skill.
- Custom sandbox images — documented on [Sandbox Providers](https://docs.paperclip.ing/reference/adapters/sandbox-providers/).

**Updated pages**

- [Work Timeline](https://docs.paperclip.ing/guides/day-to-day/work-timeline/) — the work-timeline view.
- [Secret Scopes](https://docs.paperclip.ing/administration/secret-scopes/) — secret-scope content.

Docs for v2026.626.0 June 26, 2026

**Updated pages**

- [Hermes Adapter](https://docs.paperclip.ing/reference/adapters/hermes/) and [Hermes Gateway](https://docs.paperclip.ing/reference/adapters/hermes-gateway/) — the two built-in Hermes adapters.
- [Work Modes](https://docs.paperclip.ing/guides/day-to-day/work-modes/) — the new "ask" work mode.
- [Routines](https://docs.paperclip.ing/guides/projects-workflow/routines/) — routine date variables.
- [Plugin SDK](https://docs.paperclip.ing/reference/plugins/sdk/) — the plugin target command; also task watchdogs and workspace file downloads.

Docs for v2026.618.0 June 18, 2026

**New pages**

- Novita Agent Sandbox provider (driver `novita`) — added to [Sandbox Providers](https://docs.paperclip.ing/reference/adapters/sandbox-providers/).
- The `paperclip-board` bundled skill — added to [Skills](https://docs.paperclip.ing/guides/org/skills/).

**Updated pages**

- Adapters — [Codex](https://docs.paperclip.ing/reference/adapters/codex/), [Gemini CLI](https://docs.paperclip.ing/reference/adapters/gemini-cli/), [OpenCode](https://docs.paperclip.ing/reference/adapters/opencode/), [Pi](https://docs.paperclip.ing/reference/adapters/pi/), [OpenClaw Gateway](https://docs.paperclip.ing/reference/adapters/openclaw-gateway/), plus Kubernetes on [Sandbox Providers](https://docs.paperclip.ing/reference/adapters/sandbox-providers/).
- [Agents API](https://docs.paperclip.ing/reference/api/agents/), [Plugin SDK](https://docs.paperclip.ing/reference/plugins/sdk/), and [Environment Variables](https://docs.paperclip.ing/reference/deploy/environment-variables/) (`TRUST_PROXY` / OTEL).
- Day-to-day guides — [Artifacts](https://docs.paperclip.ing/guides/day-to-day/artifacts/), [Issues](https://docs.paperclip.ing/guides/day-to-day/issues/), [Routines](https://docs.paperclip.ing/guides/projects-workflow/routines/).

Docs for v2026.609.0 June 9, 2026

**New pages**

- [`token` CLI](https://docs.paperclip.ing/reference/cli/token/) — the `token agent` / `token board` API-key commands.
- [`connect` CLI](https://docs.paperclip.ing/reference/cli/connect/) — the interactive `connect` setup wizard.
- [Teams Catalog API](https://docs.paperclip.ing/reference/api/teams-catalog/) — the teams catalog REST API.

**Updated pages**

- Release-stamped 49 pages to `v2026.609.0` and registered the three new pages in the nav.

Docs for v2026.529.0 May 29, 2026

**Updated pages**

- [Claude Code Adapter](https://docs.paperclip.ing/reference/adapters/claude-code/) — UI-driven live model discovery (`/v1/models` lookup via `ANTHROPIC_API_KEY`, 60s cache, built-in fallback, Bedrock IDs, refresh control).
- [Workspaces](https://docs.paperclip.ing/guides/projects-workflow/workspaces/) — reused-workspace environment consistency and finalize-gated dependent wakes.
- Inherited nightly drafts: [Resource Memberships API](https://docs.paperclip.ing/reference/api/resource-memberships/), document annotations, bundled plugins in the plugin manager, the skills CLI + catalog, and first-admin claim.

Docs for v2026.525.0 May 25, 2026

**New pages**

- Modal sandbox provider — added to [Sandbox Providers](https://docs.paperclip.ing/reference/adapters/sandbox-providers/).
- [Workspace Diff Viewer plugin](https://docs.paperclip.ing/reference/plugins/workspace-diff/) — split/unified and working-tree/against-ref toggles, base-ref input, sticky toolbar.

**Updated pages**

- [Plugin SDK](https://docs.paperclip.ing/reference/plugins/sdk/) — SDK surface audit plus the managed-resources concept.
- [Routines](https://docs.paperclip.ing/guides/projects-workflow/routines/) — the routine env runtime contract and secret-ref binding picker.
- Added a troubleshooting note for a 401 after creating a new secret.

Docs for v2026.517.0 May 17, 2026

**New pages**

- [Grok Local Adapter](https://docs.paperclip.ing/reference/adapters/grok-local/) — the `grok_local` adapter, wired into the Adapters overview and nav.

**Updated pages**

- [Issues](https://docs.paperclip.ing/guides/day-to-day/issues/) and [Issues API](https://docs.paperclip.ing/reference/api/issues/) — the locking workflow (lock/unlock, derived-document redirect) and Board-view scaling controls.
- [Sandbox Providers](https://docs.paperclip.ing/reference/adapters/sandbox-providers/) — Cloudflare reliability tuning notes.

Docs for v2026.513.0 May 13, 2026

**New pages**

- [Develop a plugin locally](https://docs.paperclip.ing/how-to/develop-a-plugin-locally/) — a walkthrough of `paperclipai plugin init`, local-path install, the dev watcher, and reload.
- [Blocked Inbox](https://docs.paperclip.ing/guides/day-to-day/blocked-inbox/) — the Blocked Inbox tab, chip variants, filters, sort, and triage.

**Updated pages**

- [Issues](https://docs.paperclip.ing/guides/day-to-day/issues/) and [Issues API](https://docs.paperclip.ing/reference/api/issues/) — recovery actions and walking through sub-issues.
- [Claude Code Adapter](https://docs.paperclip.ing/reference/adapters/claude-code/) — resuming a session's workspace.
- [Plugin SDK](https://docs.paperclip.ing/reference/plugins/sdk/) — worker entrypoint validation.
- [Plugins (administration)](https://docs.paperclip.ing/administration/plugins/) — developing plugins locally.

---

*This changelog begins at v2026.513.0, the first release tracked in this repo. For the product's full feature and fix history, see the [Paperclip releases page](https://github.com/paperclipai/paperclip/releases).*
