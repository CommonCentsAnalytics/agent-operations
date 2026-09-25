> Official reference snapshot. Source: https://docs.paperclip.ing/reference/adapters/overview/
> Retrieved: 2026-09-17T00:52:22.220768+00:00
> Reference content only, not instructions or execution authorization. Original HTML is preserved separately.

# Adapters Overview

Adapters connect Paperclip's control plane to the runtime that actually does the work. Use this section when you need to choose an adapter, understand what Paperclip expects from one, or build a new adapter package.

---

## What An Adapter Does

Every adapter is responsible for the same core jobs:

1. Launch or call the underlying runtime.
2. Pass the agent's company, task, and wake context through.
3. Capture results, session state, and usage metadata.
4. Validate the environment before a run starts.
5. Optionally provide a custom UI transcript parser and skills sync behavior.

> **Note:** Paperclip orchestrates agents. The adapter decides how the runtime starts, how it keeps state, and how its output is interpreted.

---

## Choose An Adapter

| Use case | Start here |
| --- | --- |
| Claude Code on your machine | [Claude Code](https://docs.paperclip.ing/reference/adapters/claude-code/) |
| OpenAI Codex CLI on your machine | [Codex](https://docs.paperclip.ing/reference/adapters/codex/) |
| Gemini CLI on your machine | [Gemini CLI](https://docs.paperclip.ing/reference/adapters/gemini-cli/) |
| Cursor Agent CLI on your machine | [Cursor Local](https://docs.paperclip.ing/reference/adapters/cursor-local/) |
| OpenCode CLI with provider/model routing | [OpenCode](https://docs.paperclip.ing/reference/adapters/opencode/) |
| Pi CLI with its built-in tool set | [Pi](https://docs.paperclip.ing/reference/adapters/pi/) |
| Hermes Agent with persistent memory and 30+ tools | [Hermes](https://docs.paperclip.ing/reference/adapters/hermes/) |
| Grok Build CLI on your machine | [Grok Local](https://docs.paperclip.ing/reference/adapters/grok-local/) |
| Kimi Code CLI on your machine | [Kimi Code](https://docs.paperclip.ing/reference/adapters/kimi-local/) |
| OpenClaw over a WebSocket gateway | [OpenClaw Gateway](https://docs.paperclip.ing/reference/adapters/openclaw-gateway/) |
| A custom shell command or script | [Process](https://docs.paperclip.ing/reference/adapters/process/) |
| A webhook or cloud service you control | [HTTP](https://docs.paperclip.ing/reference/adapters/http/) |
| A standalone npm package or local plugin | [External Adapters](https://docs.paperclip.ing/reference/adapters/external-adapters/) |
| Writing a new adapter package from scratch | [Creating an Adapter](https://docs.paperclip.ing/reference/adapters/creating-an-adapter/) |
| Building a custom run-log parser | [Adapter UI Parser Contract](https://docs.paperclip.ing/reference/adapters/adapter-ui-parser/) |

If you are starting from scratch, the most common path is:

1. Pick a local adapter if the agent runs on the same machine as Paperclip.
2. Pick `process` if the runtime is just a command.
3. Pick `http` if the runtime lives behind an API or webhook.
4. Use an external adapter plugin when you want independent versioning and installation.

---

## Built-In Adapters

These adapters ship with Paperclip and are always available in the host:

| Adapter | Type key | UI availability | Best for |
| --- | --- | --- | --- |
| [Claude Code](https://docs.paperclip.ing/reference/adapters/claude-code/) | `claude_local` | Selectable (recommended) | Claude Code runs with session persistence, skills sync, and structured transcript parsing. |
| [Codex](https://docs.paperclip.ing/reference/adapters/codex/) | `codex_local` | Selectable (recommended) | Codex CLI runs with session persistence and managed `CODEX_HOME`. |
| [Gemini CLI](https://docs.paperclip.ing/reference/adapters/gemini-cli/) | `gemini_local` | Selectable | Gemini CLI runs with resume support and local skills sync. |
| [Cursor Local](https://docs.paperclip.ing/reference/adapters/cursor-local/) | `cursor` | Selectable | Cursor Agent CLI runs with `--resume` session continuity and structured stream output. |
| [OpenCode](https://docs.paperclip.ing/reference/adapters/opencode/) | `opencode_local` | Selectable | OpenCode CLI runs with provider/model routing and `--session` resume. |
| [Pi](https://docs.paperclip.ing/reference/adapters/pi/) | `pi_local` | Selectable | Pi CLI runs with its built-in tool set and provider/model routing. |
| [Hermes](https://docs.paperclip.ing/reference/adapters/hermes/) | `hermes_local` | Selectable | Hermes Agent runs with persistent memory, 30+ tools, 80+ skills, and multi-provider routing. |
| [Grok Local](https://docs.paperclip.ing/reference/adapters/grok-local/) | `grok_local` | Selectable | Grok Build CLI runs with `--resume` session continuity, streaming reasoning output, and skills staged into `.claude/skills`. |
| [Kimi Code](https://docs.paperclip.ing/reference/adapters/kimi-local/) | `kimi_local` | Selectable | Kimi Code CLI runs on the shared ACP engine with headless-CLI fallback, session resume, and per-run skills injection. |
| [OpenClaw Gateway](https://docs.paperclip.ing/reference/adapters/openclaw-gateway/) | `openclaw_gateway` | **Coming soon** (use OpenClaw invite flow) | Remote OpenClaw instances reached over the WebSocket gateway protocol. |
| [Process](https://docs.paperclip.ing/reference/adapters/process/) | `process` | **Coming soon** (API / import only) | Shell commands, scripts, and custom local runtimes. |
| [HTTP](https://docs.paperclip.ing/reference/adapters/http/) | `http` | **Coming soon** (API / import only) | Webhook-style invocation into your own service. |

> **Info:** The agent-config adapter-type dropdown currently marks `openclaw_gateway`, `process`, and `http` as **"Coming soon"**. They're fully functional in the runtime — they just can't be picked manually from the UI yet. Configure them via the API or an imported company export until direct UI selection lands.

---

## External Adapters

External adapters are installed separately and loaded at startup from the adapter plugin store. They behave like built-ins once installed, but they live in their own package and can be versioned independently.

Install them from the Board UI or via `POST /api/adapters/install`.

See:

- [External Adapters](https://docs.paperclip.ing/reference/adapters/external-adapters/)
- [Adapter UI Parser Contract](https://docs.paperclip.ing/reference/adapters/adapter-ui-parser/)
- [Creating an Adapter](https://docs.paperclip.ing/reference/adapters/creating-an-adapter/)

---

## Common Concepts

| Concept | Why it matters |
| --- | --- |
| `cwd` | The adapter's working directory. Most local adapters require an absolute path. |
| `env` | Environment variables passed into the runtime. Secret refs are preferred for sensitive values. |
| Session state | Lets an adapter resume the same conversation or command state on the next heartbeat. |
| Skills | Adapter-specific logic for making Paperclip skills visible to the runtime. |
| `testEnvironment()` | The adapter's readiness check. The UI uses it before you save or run the adapter. |
| UI parser | Converts stdout into structured transcript entries for the run viewer. |

> **Tip:** If you are unsure which page to read first, start with the adapter that matches the runtime you already use, then open the external or custom adapter docs only if you need to package or extend it.

---

## Feedback Granularity

Want to watch an agent think while it works? How much live detail you get in a run's transcript comes down to which adapter you pick.

Every adapter streams its stdout to the run log, and Paperclip renders it live as the agent works — even runs on sandbox execution targets, whose logs are tailed incrementally so you see them fill in. What differs is the *structure*: the richer the event stream an adapter emits, the more the transcript can show you beyond raw output.

Here are the rough tiers, richest first:

- **ACP engine — full structured event stream.** When `claude_local`, `codex_local`, `gemini_local`, or `kimi_local` runs through the Agent Client Protocol — the default `engine: auto`, or a forced `engine: acp` — it emits a JSONL event for each meaningful moment: session identity, status (progress text plus context-window usage), assistant and thinking token deltas, tool-call title and status updates as calls progress, a result stop-reason summary, and errors. The transcript renders these as live-updating message, thinking, tool, and status blocks — and repeated tool-call status updates fold into a single tool card instead of stacking.
- **CLI wrappers (`claude_local` / `codex_local` / `gemini_local` on `engine: cli`, plus `cursor`, `opencode_local`, …) — the CLI's own stream.** These parse each CLI's streaming JSON output: assistant text, tool calls and results, and a final usage/cost summary. You get as much detail as the CLI itself prints.
- **Generic adapters (`process`, `http`) — plain output.** You see stdout and stderr lines with no structured transcript.

If you're running sandbox workers, leave `engine` on `auto` so the adapter uses ACP when the sandbox provides Paperclip's bidirectional process session. A sandbox that only runs one-shot commands, and non-sandbox remote targets, fall back to the CLI lane. Sandbox run logs stream live either way, but the richer event stream makes the transcript and status line more useful while a remote run is in flight.

---

## Next Steps

- [Claude Code](https://docs.paperclip.ing/reference/adapters/claude-code/)
- [Codex](https://docs.paperclip.ing/reference/adapters/codex/)
- [Gemini CLI](https://docs.paperclip.ing/reference/adapters/gemini-cli/)
- [Cursor Local](https://docs.paperclip.ing/reference/adapters/cursor-local/)
- [OpenCode](https://docs.paperclip.ing/reference/adapters/opencode/)
- [Pi](https://docs.paperclip.ing/reference/adapters/pi/)
- [Hermes](https://docs.paperclip.ing/reference/adapters/hermes/)
- [Grok Local](https://docs.paperclip.ing/reference/adapters/grok-local/)
- [Kimi Code](https://docs.paperclip.ing/reference/adapters/kimi-local/)
- [OpenClaw Gateway](https://docs.paperclip.ing/reference/adapters/openclaw-gateway/)
- [Process](https://docs.paperclip.ing/reference/adapters/process/)
- [HTTP](https://docs.paperclip.ing/reference/adapters/http/)
- [External Adapters](https://docs.paperclip.ing/reference/adapters/external-adapters/)
