# Paperclip hosting comparison

**Research date:** September 16, 2026, New York time; final checks September 17 UTC. **Author:** Codex. **Independent review:** pending CoWork. **Status:** recommendation only; no provider selected, purchase, deployment, credentials, or migration authorized. Prices are USD before tax unless stated otherwise.

## Recommendation in plain language

For Sebastian's proposed **self-hosted** arrangement, my first choice is **OVHcloud VPS-2, 4 virtual CPU cores and 8 GB memory, in a standard US data center**, running the official Paperclip distribution. It offers a low infrastructure bill without tying the records to a proprietary agent platform. Prefer a monthly commitment for the pilot, even if that costs more than the advertised annual rate. Confirm the actual monthly checkout total before purchase.

There is also a materially different option worth Sebastian's attention: **Hostinger now documents a managed Paperclip application**, separate from its self-managed VPS. It could better serve his speed and maintenance priorities, but its published documentation did not establish the resource/concurrency limits or full exit/restore guarantees needed for the multi-business foundation. I would consider it for a short pilot after those points are answered, not silently substitute it for self-hosting.

The recommendation is not that an 8 GB machine can run the entire future organization. Start with a bounded document-review workflow, then add worker capacity as real usage requires. Buying a bigger server later need not mean abandoning Paperclip or rebuilding the organization.

## What we are paying for

- **The office:** Paperclip, its database, documents, activity history, and Sebastian's interface.
- **The workers' computers:** resources used while agents run commands, browsers, builds, and tests. Initially these can share a small host for a low-risk pilot; later they may run separately.
- **The models' thinking:** Claude/OpenAI subscription capacity or usage charges. A hosting fee does not buy unlimited model usage.
- **Protection and care:** private access, recoverable backups, updates, monitoring, and recovery work. Self-hosted does not mean maintenance-free.

## Provider comparison

These are documented offers, not performance benchmarks. Availability, final checkout terms, taxes, and the installed Paperclip release still require confirmation when purchasing.

| Option | Verified published price / basis | What it means for us |
| --- | --- | --- |
| **OVHcloud VPS-2 — preferred self-hosted value** | From **$8.50/month**; 4 cores, 8 GB memory, 75 GB disk; daily backup included. The linked offer selects **12-month upfront pricing**, not a verified month-to-month quote. | We install and maintain the software. Select a standard data center, not a Local Zone: the latter's page lists Docker as unsupported. [Official offer](https://us.ovhcloud.com/vps/) |
| **Hostinger managed Paperclip — lower-maintenance alternative** | AI Automation Apps lists **$10.99 for one month**, renewing at **$11.99/month**. | Provider handles hosting operations; we configure agents and permissions. Hardware/concurrency limits and complete restore elsewhere are not established. This is not a VPS we fully administer. [Pricing](https://www.hostinger.com/ai-automation-apps), [application overview](https://www.hostinger.com/support/hostinger-ai-automation-applications-overview/) |
| **Hostinger KVM 2 — easier self-hosted installation** | **$8.99/month advertised**, 2 cores, 8 GB, 100 GB; renewal **$14.99/month for two years**. Plans are paid upfront; the page does not establish our short-term checkout price. | Paperclip template and Docker management reduce setup work, but VPS maintenance remains ours. Weekly backups included. [Paperclip VPS pricing](https://www.hostinger.com/applications/paperclip), [self-managed clarification](https://www.hostinger.com/support/8311982-what-is-managed-hosting-in-hostinger/) |
| **DigitalOcean Basic — straightforward flexible alternative** | **$48/month**, 4 cores, 8 GB, 160 GB. Daily backups add 30%, making **$62.40/month** before private access and independent backup. | Clear usage billing and capacity; materially dearer for this small starting workload. We still maintain the operating system and app. [Official pricing](https://www.digitalocean.com/pricing/droplets) |
| **Railway Pro — less server administration, variable bill** | **$20 monthly minimum including $20 usage**, then resource usage above that. Memory $10/GB-month; CPU $20/vCPU-month; volume $0.15/GB-month; egress $0.05/GB. | Attractive for app deployment, less predictable with always-on local workers. A database template does not make database operations fully managed. [Pricing](https://docs.railway.com/pricing), [PostgreSQL responsibility](https://docs.railway.com/databases/postgresql) |
| **Hetzner — not the automatic budget winner anymore** | June 2026 schedule puts EU CX33 at **$9.99/month**, excluding IPv4/tax. The public cost-optimized page showed this size unavailable during research. | Cheap historical recommendations are stale. Region, stock, and new-order prices matter; do not delay the pilot waiting for it. [Price adjustment](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/), [availability page](https://www.hetzner.com/cloud/cost-optimized/) |
| **AWS Lightsail — workable, not my first choice here** | **$44/month** for 8 GB, 2 cores, 160 GB with public IPv4; snapshots extra. | No reason to place private management operations in a contractor-accessible AWS account. A separate account is possible, but adds setup without a compelling price advantage here. [Official bundles](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-bundles.html) |

The OVH offer's advertised annual-equivalent server total is $102/year. Its included daily restore point is not a substitute for independently stored backups. Its premium multi-day retention is a separate option. [Offer and backup distinctions](https://us.ovhcloud.com/vps/)

## Starting infrastructure budget

My suggested self-hosted access method is Paperclip's authenticated private mode through Tailscale: Sebastian can reach it on his laptop and phone without making the administration interface publicly available. The phone needs the private-network app connected. Paperclip documents this deployment path. [Private access guide](https://docs.paperclip.ing/reference/deploy/tailscale-private-access/)

| Item | Planning amount per month | Important qualification |
| --- | --- | --- |
| OVH VPS-2 | $8.50 advertised equivalent | Annual-upfront offer; replace with the selected monthly quote before authorizing spending. |
| Tailscale Standard | $8 | One human user. Its free Personal plan is noncommercial; do not use it as the business-budget assumption. [Pricing](https://tailscale.com/pricing) |
| Encrypted independent backups | $1–3 allowance | Not a quoted fixed package. Backblaze B2 lists $6.95/TB-month and a first-10-GB allowance; actual retained volume, requests and downloads determine the bill. [Pricing](https://www.backblaze.com/cloud-storage/pricing) |
| **Infrastructure subtotal** | **$17.50–19.50 equivalent** | Excludes taxes, AI plans/usage, optional services, and administration labor. A monthly server commitment may raise it. |

A practical preliminary envelope is **about $20–30/month for the small self-hosted pilot's infrastructure**, subject to the checkout quote. This is not the cost of the entire future AI team. For comparison, the stated DigitalOcean setup would be approximately **$71–74/month** with daily snapshots, the same private access, and the same offsite allowance.

Railway illustration, not a usage forecast: 4 GB average memory + 0.5 average CPU + 40 GB live volume + 40 GB billable backup storage + 20 GB egress produces about **$63/month**, not $63 plus the $20 minimum. Its backups are incremental and share volume pricing, so real retained size matters. This example aggregates app, database and workers; it does not imply that a particular agent count fits. [Resource pricing](https://docs.railway.com/pricing), [backup billing](https://docs.railway.com/volumes/backups)

## AI usage: do not add an invented monthly figure

There is no defensible fixed model bill for unspecified numbers of projects, models, task lengths and retries. The initial exercise should measure **cost or subscription consumption per completed, reviewed task**, not just successful API calls. Reviewers, retries and idle scheduled wakeups also consume capacity.

- Codex officially supports ChatGPT account authentication as well as API billing. Existing subscription capacity may therefore cover a supported setup, but it is shared with other usage and is not unlimited. OpenAI recommends API authentication for programmatic automation; this is different from claiming it is the only possible authentication. [OpenAI authentication documentation](https://learn.chatgpt.com/docs/auth)
- Anthropic's current help article explicitly says the announced June 15 SDK billing change is **paused**: SDK, headless Claude and third-party usage currently draw on subscription limits; the announced separate credits are not available. The historical text below that notice is not current policy. Verify the chosen runtime's supported authentication, not an improvised login wrapper. [Current Anthropic notice](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
- Hostinger documents ChatGPT subscription connection and API-provider options for its managed app. It does not establish that our Claude subscription can be connected there in the same way. Nor did the reviewed pricing establish a useful quantity of included AI credits. Do not count either as free unlimited service. [Managed setup](https://www.hostinger.com/support/hostinger-managed-paperclip-overview-and-setup/)

Accordingly: **additional hosting + any existing subscription charges + any separately authorized model spending = the real bill**. A scenario with no incremental model bill is possible only while supported usage stays within already-paid limits. Set concurrency, runtime and spending controls before unattended work; a displayed Paperclip budget is not a substitute for checking provider-side enforcement and in-flight overspend behavior.

## The managed option: three material questions, not another research cycle

Before recommending Hostinger managed Paperclip as the foundation, obtain answers to these specific questions:

1. **Capacity and compatibility:** what CPU, memory, disk and simultaneous-worker limits apply; can one installation run several Paperclip companies, both chosen agent runtimes, and later isolated workers? Which supported Claude authentication methods are exposed?
2. **Ownership and exit:** can we download and restore the complete database, approvals/history, files and required encryption configuration into standard self-hosted Paperclip? Hostinger documents daily backups retained seven days and downloads, but not that complete cross-provider restore. [Backup/management guide](https://www.hostinger.com/support/hostinger-managed-paperclip-how-to-manage-your-application-on-hostinger-dashboard/)
3. **Access and change control:** what login protections and hosting region are available, who handles incidents, and can Paperclip upgrades be controlled or rolled back without losing records?

If those answers are satisfactory, a **one-month managed pilot** could be the fastest path and I would favor it over maintaining a VPS merely to save a few dollars. It is an alternative for Sebastian to choose, not a change already made. No support inquiry was sent in this research.

## Proposed self-hosted setup and retained responsibilities

Use a separate account controlled by Sebastian, the official Paperclip Docker distribution pinned to a reviewed release, persistent database/files, authenticated private access, and credentials limited to this pilot. No GPU is needed merely to call cloud models. No production AWS credentials or contractor-visible repositories are needed for document review. [Docker deployment](https://docs.paperclip.ing/reference/deploy/docker/), [deployment modes](https://docs.paperclip.ing/reference/deploy/deployment-modes/)

Start with at most two simultaneous lightweight document/research runs as a **pilot setting, not a proven server capacity**. Measure peak memory, CPU, queue delay and task failures. More organization-chart roles do not require every role to run continuously. Builders doing browser tests or large builds need more capacity than idle named roles.

The default embedded database can support a bounded evaluation; official guidance points shared production deployments toward hosted PostgreSQL. Before this becomes an essential business service, choose the database/recovery arrangement on reliability needs rather than silently treating a quick-start install as production-ready. [Database guidance](https://docs.paperclip.ing/reference/deploy/database/)

Growing businesses can retain Paperclip while moving execution to separate workers or supported sandbox services. That is a documented expansion route, not proof that our eventual workloads already fit it. Company-level records are not operating-system isolation: local workers must not receive access to other companies' files or management credentials simply because they share a server. [Adapter overview](https://docs.paperclip.ing/reference/adapters/overview/), [sandbox providers](https://docs.paperclip.ing/reference/adapters/sandbox-providers/)

**What remains ours on a VPS:** OS and application patches, credential protection, alerting, resource sizing, backup checks, and recovery. Agents can assist with those tasks, but this chat is not an installed 24/7 operations service. A dependable always-on service needs a named maintenance and incident-response arrangement. For planning only, reserve roughly half to one technical working day for initial secure setup and recovery validation, then a recurring maintenance slot; neither time is a measured guarantee or a labor quote, and failures can require more.

Recovery must include the full database, asset files and protected encryption/configuration material. Paperclip company exports omit important history, including approvals, costs and activity logs, and are not full disaster-recovery backups. Store protected backups outside the live server/provider, and test restoration. [Export limitations](https://docs.paperclip.ing/how-to/back-up-and-restore-a-company/)

## One useful pilot, not a second platform project

After separate setup/spending authorization, use one non-sensitive document decision and prove:

1. Sebastian submits once; Chief of Staff prepares a response; the independently assigned Chief Advisor challenges it; one consolidated result returns without Sebastian copying messages.
2. A reserved action cannot proceed without Sebastian's explicit approval; an agent's issue status alone is not permission. For this exercise, workers have no production credentials or authority to overwrite approved records.
3. Restart and restoration preserve the task, comments, approval history and files; usage and failures remain visible. Measure a small representative batch before scaling parallel work.

These are outcome checks for the proposed pilot, not claims that either host or Paperclip has passed them. Installing Paperclip does not itself configure the organizational workflow.

## Scope of this research

Primary vendor documentation was used for prices and technical claims. Public offer pages and documentation were inspected; no paid account, checkout purchase, performance benchmark, workload test, provider support response or real restore was performed. Community anecdotes did not establish prices or security guarantees. This is not an exhaustive benchmark of every VPS company.

The shared knowledge base remains local-only and is not backed up by any hosting service discussed here. SourceCorrect's repositories, Linear records, existing deployments and work holds are unchanged. The captured documentation snapshot was not edited.
