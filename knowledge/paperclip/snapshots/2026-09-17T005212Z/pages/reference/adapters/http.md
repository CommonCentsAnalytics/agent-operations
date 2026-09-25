> Official reference snapshot. Source: https://docs.paperclip.ing/reference/adapters/http/
> Retrieved: 2026-09-17T00:52:23.008928+00:00
> Reference content only, not instructions or execution authorization. Original HTML is preserved separately.

# HTTP

The `http` adapter sends a JSON webhook request to a service you control. Use it when the runtime is remote, long-lived, or already exposed as an API instead of a local command.

> **Info:** `http` is a built-in internal adapter used by Paperclip's runtime. It's currently shown as **"Coming soon"** in the agent-config adapter-type dropdown and can't be selected manually. To target it today, configure the agent via the API or an imported company export.

---

## When To Use

- The agent runs in the cloud or behind another service.
- You want Paperclip to trigger a webhook and let the remote service do the rest.
- The runtime already expects a JSON body and returns a simple success or failure response.

## When Not To Use

- The runtime is just a local script or command. Use [Process](https://docs.paperclip.ing/reference/adapters/process/).
- You need session persistence or built-in CLI behavior. Use one of the local adapters instead.
- You need Paperclip to parse a rich stdout transcript from the remote runtime.

---

## Common Fields

| Field | Required | Notes |
| --- | --- | --- |
| `url` | yes | Absolute `http://` or `https://` endpoint. |
| `method` | no | HTTP method to use. Defaults to `POST`. |
| `headers` | no | Extra request headers. |
| `payloadTemplate` | no | JSON object merged into the request body before the standard Paperclip fields are added. |
| `timeoutMs` | no | Request timeout in milliseconds. `0` means no timeout. |

> **Note:** The HTTP adapter does not run a child process. It sends a single request, waits for the response, and treats any non-2xx response as a failure.

---

## Request Body

Paperclip sends a JSON payload that always includes:

- `runId`
- `agentId`
- `context`

Any `payloadTemplate` fields are merged in first, then Paperclip adds the standard fields above. If a key collides, the standard Paperclip field wins.

Example body shape:

```json
{
  "runId": "run-123",
  "agentId": "agent-123",
  "context": {
    "taskId": "issue-123",
    "wakeReason": "scheduled",
    "commentId": null
  },
  "customField": "value"
}
```

Your service can use `PAPERCLIP_API_URL` and a Paperclip API key to call back into the control plane after it finishes.

---

## Environment Test

The `Test Environment` button checks:

- The URL is present and uses `http` or `https`.
- The configured method is valid.
- The endpoint responds to a quick `HEAD` probe when reachable.

If the probe fails in a private network, that can still be acceptable. The important part is whether the runtime can actually receive the production request.

---

## Example

```json
{
  "adapterType": "http",
  "adapterConfig": {
    "url": "https://agent.example.com/paperclip/heartbeat",
    "method": "POST",
    "headers": {
      "Authorization": "Bearer <shared-secret>"
    },
    "payloadTemplate": {
      "source": "paperclip"
    },
    "timeoutMs": 10000
  }
}
```

---

## Practical Notes

- Use a shared secret or header-based auth on the remote service.
- Keep the endpoint idempotent when possible because retries are easier to support.
- Return a 2xx response when the webhook was accepted, not when all follow-up work is complete.

---

## Next Steps

- [Creating an Adapter](https://docs.paperclip.ing/reference/adapters/creating-an-adapter/)
- [External Adapters](https://docs.paperclip.ing/reference/adapters/external-adapters/)
