> Official reference snapshot. Source: https://docs.paperclip.ing/reference/deploy/overview/
> Retrieved: 2026-09-17T00:52:23.448298+00:00
> Reference content only, not instructions or execution authorization. Original HTML is preserved separately.

# Deployment Overview

Paperclip supports three deployment configurations, from zero-friction local use to login-protected private and public deployments.

Use this section when you need to choose a mode, understand the storage and secrets defaults, or move from local development into a more durable setup.

---

## Deployment Modes

| Mode | Auth | Best For |
| --- | --- | --- |
| `local_trusted` | No login required | Single-operator local machine |
| `authenticated` + `private` | Login required | Private network (Tailscale, VPN, LAN) |
| `authenticated` + `public` | Login required | Internet-facing cloud deployment |

## Quick Comparison

### Local Trusted

- Loopback-only host binding (`localhost`)
- No human login flow
- Fastest local startup
- Best for solo development and experimentation

### Authenticated + Private

- Login required via Better Auth
- Binds to all interfaces for network access
- Auto base URL mode for lower-friction private access
- Best for team access over Tailscale or a local network

### Authenticated + Public

- Login required
- Explicit public URL required
- Stricter security checks
- Best for cloud hosting and internet-facing deployment

---

## Choosing A Mode

- Just trying Paperclip: use `local_trusted` first.
- Sharing with a team on a private network: use `authenticated` + `private`.
- Deploying to the cloud: use `authenticated` + `public`.

Start from onboarding:

```sh
pnpm paperclipai onboard
```

Or change the mode later:

```sh
pnpm paperclipai configure --section server
```

---

## Start Here

If you want the shortest path to a working instance, read [Local Development](https://docs.paperclip.ing/reference/deploy/local-development/) first.

If you are deciding how to expose the instance, read [Deployment Modes](https://docs.paperclip.ing/reference/deploy/deployment-modes/) next.

If you already know the shape and only need the operational details, jump to:

- [Database](https://docs.paperclip.ing/reference/deploy/database/)
- [Storage](https://docs.paperclip.ing/reference/deploy/storage/)
- [Secrets](https://docs.paperclip.ing/reference/deploy/secrets/)
- [Environment Variables](https://docs.paperclip.ing/reference/deploy/environment-variables/)
- [Docker](https://docs.paperclip.ing/reference/deploy/docker/)
- [Tailscale Private Access](https://docs.paperclip.ing/reference/deploy/tailscale-private-access/)

> **Tip:** Keep the deployment pages grouped together in the docs nav. They are easiest to understand when read as one flow.
