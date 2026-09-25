> Official reference snapshot. Source: https://docs.paperclip.ing/guides/getting-started/your-first-agent/
> Retrieved: 2026-09-17T00:52:13.406879+00:00
> Reference content only, not instructions or execution authorization. Original HTML is preserved separately.

# Hire Your First Agent

An agent isn't just "an AI". It's a configuration — a specific role, with a specific AI system powering it, operating under a specific budget, with defined rules for when and how it wakes up and works.

When you hire an agent, you're telling Paperclip: which AI system should run this agent, what role does it play in the company, and what constraints does it operate within. The AI itself (Claude, Codex, etc.) lives outside Paperclip. Paperclip is the management layer above it.

The CEO is always the first agent you create. It has a special role: reading the company goal, proposing a strategy, creating tasks, and delegating work to its reports. Nothing in your company moves until the CEO is running.

---

## Before you start

You'll need:

- A company already created (see [Create Your First Company](https://docs.paperclip.ing/guides/getting-started/your-first-company/))
- An API key from Anthropic (for the `claude_local` adapter) or OpenAI (for `codex_local`) — see the [Installation guide](https://docs.paperclip.ing/guides/getting-started/installation/) for how to get one
- **For `claude_local`:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed on your Mac

---

1. **Open the Agents page and click "New Agent"**

   

  In the sidebar, click **Agents**. If this is your first agent, you'll see an empty list with a prompt to create one. Click **New Agent**.

   

  [Image reference: The empty agents list with a New Agent button](https://docs.paperclip.ing/guides/getting-started/your-first-agent/user-guides/screenshots/dark/agents/agents-list-empty.png)
2. **Set the agent's name**

   

  Give the agent a name (e.g. "CEO"). If this is your first agent, Paperclip automatically makes it the **CEO**.

   

  [Image reference: The new agent form showing the Name and Role fields filled in for a CEO agent](https://docs.paperclip.ing/guides/getting-started/your-first-agent/user-guides/screenshots/dark/agents/new-agent-name-role.png)

   

  The **CEO role** is special: it has no "Reports To" field, because the CEO reports directly to the board — to you. Every other agent you hire later will have a "Reports To" field where you (or the CEO) assigns a manager.
3. **Choose an adapter**

   

  An adapter tells Paperclip how to run your agent. Click the **Adapter Type** dropdown to see your options.

   

  [Image reference: The adapter type dropdown showing available adapter options](https://docs.paperclip.ing/guides/getting-started/your-first-agent/user-guides/screenshots/dark/agents/adapter-type-dropdown.png)

   

  **Claude Code** runs a Claude Code agent directly on your Mac. The agent has full access to your filesystem in its working directory, can run terminal commands, write and edit files, and call the Claude API on your behalf.

This is the most capable and most commonly used adapter for Paperclip agents.

**Prerequisites:** Claude Code must be installed on your Mac. If you haven't installed it, follow the [Claude Code installation guide](https://docs.anthropic.com/en/docs/claude-code) — it's a separate Anthropic product. Come back here once it's installed.

**Configuration fields:**

[Image reference: The Claude Code adapter configuration form with all fields filled in](https://docs.paperclip.ing/guides/getting-started/your-first-agent/user-guides/screenshots/dark/agents/claude-local-config-filled.png)

- **Working directory** — The folder on your Mac where the agent will do its work. This is where files get created, edited, and read. If you're not sure what to use, create a folder called `paperclip-workspace` on your Desktop and paste that path here (e.g. `/Users/yourname/Desktop/paperclip-workspace`).
- **Model** — Which Claude model powers this agent. `claude-opus-4-6` is the most capable and best for strategic roles like the CEO. `claude-sonnet-4-6` is faster and cheaper, and works well for more routine tasks.
- **Environment variables** — Add `ANTHROPIC_API_KEY` and either paste the key as a plain value or store it as a Paperclip secret. This is how the adapter gets access to Claude.
- **Test environment** — Use this button to confirm Paperclip can see Claude Code and that your `ANTHROPIC_API_KEY` binding works before you create the agent.

> **Tip:** If you're unsure about the working directory, create a new folder called `paperclip-workspace` on your Desktop. Use that path until you decide on a better home for your agents' work.
