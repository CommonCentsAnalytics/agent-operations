> Official reference snapshot. Source: https://docs.paperclip.ing/guides/getting-started/five-minute-path/
> Retrieved: 2026-09-17T00:52:13.184733+00:00
> Reference content only, not instructions or execution authorization. Original HTML is preserved separately.

# Quickstart Path

The shortest route from a running Paperclip instance to an agent that has just completed work for you. After Paperclip is installed, the path takes about 5 minutes: create a company, hire a CEO agent, approve its first strategy, watch tasks land on the board.

[Image reference: The Paperclip dashboard showing an active CEO agent, a budget bar, and recent activity](https://docs.paperclip.ing/guides/getting-started/five-minute-path/user-guides/screenshots/dark/dashboard/dashboard-overview.png)

---

## What this is, briefly

A Paperclip company is a self-contained AI organisation — one goal, a team of agents, a task board, a budget. The CEO is the first agent you hire. It reads your goal, proposes a strategy, and — once you approve it — starts creating tasks and moving them across the board.

You'll see all four ideas (company, agent, task, heartbeat) in the next few minutes. The full mental model lives in [Key Concepts](https://docs.paperclip.ing/guides/welcome/key-concepts/); you don't need it before starting.

---

## Before the path: install Paperclip

Install Paperclip and grab an AI provider key. This is one-time setup and lives outside the 5-minute clock — depending on what you already have, expect 3–10 minutes.

- Any machine with Node.js 24+ — the terminal install is one command.
- An API key from [Anthropic](https://console.anthropic.com) (for `claude_local`) or [OpenAI](https://platform.openai.com) (for `codex_local`). The installation guide walks through getting one.
- For the `claude_local` adapter: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed on the same machine. Install this *before* you start the path; you'll need it in step 2.

> **Warning:** Agents make API calls that cost money. Plan on spending $5–20 to play with the product, $20–100/month for an active company. Set per-agent and company budgets before enabling heartbeats — Paperclip pauses agents automatically when they hit 100%.

[Walk through Installation →](https://docs.paperclip.ing/guides/getting-started/installation/)

---

## The 5-minute path

Three steps after Paperclip is running. Allow ~5–11 minutes total.

| Step | Page | What you'll have at the end | Approx. time |
| --- | --- | --- | --- |
| 1 | [Create Your First Company](https://docs.paperclip.ing/guides/getting-started/your-first-company/) | A company with a name (you add its goal afterward) | 1–2 min |
| 2 | [Hire Your First Agent](https://docs.paperclip.ing/guides/getting-started/your-first-agent/) | A configured CEO agent in `idle` status | 2–4 min |
| 3 | [Watching Agents Work](https://docs.paperclip.ing/guides/getting-started/watching-agents-work/) | A heartbeat fired, a strategy approval submitted, the first tasks on the board | 2–5 min |

Read the steps in order. They're short on purpose.

---

## What you'll see at the end of the path

By the time you finish step 3, you'll have:

- A company on the **Companies** page with your goal.
- A CEO agent on the **Agents** page in `idle` status with its heartbeat enabled.
- A pending **Strategy** approval in the Approvals queue, written by the CEO.
- After you approve: a handful of `todo`/`backlog` tasks on the **Issues** page.
- A run transcript under **Agents → CEO → Runs** showing exactly what the CEO did during its first heartbeat.

That's a working autonomous company. From there, you can hire more agents, refine the goal, or step in and assign tasks yourself.

---

## Where to go next

Once you finish the three steps:

- **Hire your second agent** — the CEO can request reports through the [Approvals](https://docs.paperclip.ing/guides/day-to-day/approvals/) flow. See [Agents](https://docs.paperclip.ing/guides/org/agents/) for role design and [Org Structure](https://docs.paperclip.ing/guides/org/org-structure/) for how reporting lines work.
- **Set up real workflows** — read [Issues](https://docs.paperclip.ing/guides/day-to-day/issues/) for the task lifecycle, [Costs & Budgets](https://docs.paperclip.ing/guides/day-to-day/costs/) for spend control, and [Heartbeats & Routines](https://docs.paperclip.ing/guides/projects-workflow/routines/) for scheduling.
- **Connect a code repo** — the [Execution Workspaces](https://docs.paperclip.ing/guides/projects-workflow/workspaces/) guide covers giving agents a real project to work in.

If anything in the UI seems unfamiliar along the way, [Key Concepts](https://docs.paperclip.ing/guides/welcome/key-concepts/) and the [Glossary](https://docs.paperclip.ing/guides/welcome/glossary/) are the fastest reference.

[Create Your First Company →](https://docs.paperclip.ing/guides/getting-started/your-first-company/)
