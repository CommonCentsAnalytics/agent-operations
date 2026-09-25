# Hosting readiness — next decision, not a purchase plan

**Status:** the [hosting comparison](HOSTING_COMPARISON.md) is now available, with current source checks and a recommendation awaiting review. No provider selected, server created, API key requested, or spending authorized. This page preserves the requirements used for that comparison.

Sebastian is leaning toward self-hosted Paperclip and wants the most efficient, cost-effective arrangement. His priorities are speed, visible multi-business coordination, limited maintenance burden, safe approvals, and room to expand. The cheapest advertised server is not necessarily the cheapest working system.

## What the next comparison must price

1. **The management application:** Paperclip and its database, with authenticated access from the devices Sebastian actually uses.
2. **The workers:** where agents execute, how many can run at once, and whether their files and credentials are isolated appropriately.
3. **Model usage:** the permitted account/authentication method for each chosen runtime, actual consumption, and enforceable spending controls. Paperclip documentation is not the final authority on a model provider's subscription terms.
4. **Recovery:** protected offsite backups, retained decision history, and a tested restore. Company exports alone omit important historical records.
5. **Ongoing care:** upgrades, security fixes, monitoring, incident recovery, and the time needed to keep the system healthy.

Compare a small self-managed virtual server against hosting with more managed operations, where a current supported Paperclip deployment path exists. Do not assume a specific provider or price before checking current offerings. Separate a low-cost pilot from the capacity required for parallel workers across multiple businesses.

## Questions to answer before selecting a host

- What Paperclip release and deployment method will we pin and support?
- Which two agent runtimes are first, and can they run unattended under the selected provider terms?
- What baseline CPU, memory, storage, and concurrency do the application **and workers** need in a representative pilot?
- Is access private-network only or authenticated over the public internet, and how does Sebastian reach it from his phone?
- How are business files, management records, contractor access, and credentials separated?
- Who receives an alert when a worker stops, the budget is reached, or a backup fails?
- What does it cost per month at idle, at pilot usage, and at a plausible multi-project workload? Include maintenance effort, not just infrastructure.
- Can we restore the full instance and move to another host without losing approvals or history?

## Sources already on hand

- [Deployment overview](snapshots/2026-09-17T005212Z/pages/reference/deploy/overview.md)
- [Deployment modes](snapshots/2026-09-17T005212Z/pages/reference/deploy/deployment-modes.md)
- [Database](snapshots/2026-09-17T005212Z/pages/reference/deploy/database.md)
- [Storage](snapshots/2026-09-17T005212Z/pages/reference/deploy/storage.md)
- [Secrets](snapshots/2026-09-17T005212Z/pages/reference/deploy/secrets.md)
- [Docker](snapshots/2026-09-17T005212Z/pages/reference/deploy/docker.md)
- [Private access with Tailscale](snapshots/2026-09-17T005212Z/pages/reference/deploy/tailscale-private-access.md)
- [Agent adapters](snapshots/2026-09-17T005212Z/pages/reference/adapters/overview.md)
- [Company backup/export limitations](snapshots/2026-09-17T005212Z/pages/how-to/back-up-and-restore-a-company.md)

These are reading links, not a claim that every deployment page has already been reviewed or tested. Use current hosting prices and verify the chosen release against the live documentation when the hosting comparison is undertaken.

**Deliverable available:** [sourced hosting comparison](HOSTING_COMPARISON.md), including the recommended self-hosted starting arrangement, a managed alternative, cost assumptions, retained responsibilities, and a small proof-of-workflow test. No need to read every reference page before making that bounded decision.
