# Source: https://docs.qodo.ai/qodo-documentation/qodo-command/features/qodo-webhook-server.md

# Qodo Webhook Server

Serve any agent command defined in your agent configuration over HTTP, with optional real‑time streaming via Server‑Sent Events (SSE).

This guide explains what the server does, how to run it, the available endpoints, request/response formats, streaming, sessions, timeouts, and common usage patterns.

### Overview <a href="#overview" id="overview"></a>

* Purpose: Turn your agent commands into HTTP endpoints. Each command becomes a POST /webhook/{commandName}.
* Modes of use:
  * One‑shot request: POST and wait for the final JSON response
  * Two‑step streaming: POST to start, then connect to an SSE stream to receive incremental updates until completion
* Typical use cases: Integrations with your CI/CD, backend workflows, or any external systems that want to trigger agents programmatically.

### Prerequisites <a href="#prerequisites" id="prerequisites"></a>

* QODO\_API\_KEY must be set and valid for your environment.
* A valid agent configuration file (agent.toml/agent.yaml/agent.yml) must be available in the current working directory or parent directories.

### Start the Server <a href="#start-the-server" id="start-the-server"></a>

* Command:
  * `qodo --webhook`
  * Optional port override: `qodo --webhook -p 6666`
* Default port: 6666. The server will search for the first available port at or above the requested port.
* Exposed commands:
  * By default, every command in your agent config is exposed at `/webhook/{commandName}`.
  * If you start Qodo targeting a specific command or use a single‑command agent file, only that command is exposed.
* Shutdown:
  * Press ESC or Ctrl+C to exit.

### Endpoints <a href="#endpoints" id="endpoints"></a>

#### 1) POST /webhook/{commandName} <a href="#id-1-post-webhookcommandname" id="id-1-post-webhookcommandname"></a>

Trigger an agent command. Choose between a one‑shot (no streaming) or a two‑step streaming workflow.

* Query parameters:
  * `sse` (boolean): If present and truthy, the server returns `{ sessionId }` immediately, and you then connect to SSE (see below).
  * `stream` (boolean): Optional; streaming is effectively enabled whenever `sse` is provided.
  * `sessionId` (string): Optional; reuse an existing session (also supported as an `X-Session-ID` header). If omitted, the server generates a new sessionId.
* Headers:
  * `X-Session-ID` (optional on request): Reuse an existing session.
  * `X-Session-ID` (always on response): The sessionId used for this request.
* Request body (JSON):
  * Fields must match your command’s `arguments` definition in the agent config. Invalid payloads return a 400 status code with validation errors.
* Responses:
  * 200 (non‑SSE): Final JSON result. If your agent emits structured output, that JSON is returned; otherwise `{ "result": "<final text>" }`.
  * 200 (SSE mode): `{ "sessionId": "<id>" }` so you can open an SSE stream.
  * 400: Invalid payload → `{ error: string, details?: any[] }`
  * 500: Internal error (includes a readable message when possible)

#### 2) GET /webhook/{commandName}?sessionId=... <a href="#id-2-get-webhookcommandnamesessionid" id="id-2-get-webhookcommandnamesessionid"></a>

Server‑Sent Events (SSE) stream for a session started via POST with `sse=true`.

* Query parameters:
  * `sessionId` (required): The sessionId returned by the POST call.
* SSE events:
  * `event: message` `data: { "content": string }` – incremental agent messages
  * `event: error` `data: { "error": string }` – error messages
  * `event: loading` `data: { "isLoading": boolean }` – task activity flag
  * `event: done` `data: {}` – sent right before the stream closes (completion)
* Errors:
  * 400: missing/invalid `sessionId`
  * 404: unknown `commandName` or `sessionId`

### Request Validation <a href="#request-validation" id="request-validation"></a>

Incoming JSON is validated against your command’s `arguments` schema:

* Supported types: `string`, `number`, `boolean`, `array`, `object`
* Required by default unless a field has `required: false`
* Defaults and enums (if provided) are applied/validated
* On validation error: HTTP 400 with details

### Sessions and Lifecycle <a href="#sessions-and-lifecycle" id="sessions-and-lifecycle"></a>

* Session assignment:
  * Provide `X-Session-ID` header or `?sessionId=` to reuse an existing session.
  * If omitted, the server obtains a fresh sessionId from the backend and returns it.
* Session storage:
  * Each session is backed by an internal message manager that tracks AI messages, error state, and loading state.
* Cleanup & TTL:
  * Non‑SSE: the session is cleaned up after the response is sent.
  * SSE: the session is cleaned up when `loading=false` (you’ll receive a final `done` event) or if the client disconnects.
  * Periodic cleanup removes sessions older than 90 minutes. Cleanup runs every 5 minutes.
* Timeout (non‑SSE only):
  * The synchronous POST request has a 90-minute timeout and returns a 500 error if exceeded.

#### Continue an existing session <a href="#continue-an-existing-session" id="continue-an-existing-session"></a>

To keep working within the same session context:

* Include `X-Session-ID: <SESSION_ID>` on the POST `/webhook/{commandName}` request. The server will reuse that session and its context/history.
* For streaming:
  1. Start the task with `POST /webhook/{commandName}?sse=true` and the same `X-Session-ID` header (or pass `sessionId=<SESSION_ID>` in the query).
  2. Connect to `GET /webhook/{commandName}?sessionId=<SESSION_ID>` to receive events.

Notes:

* You can take the session ID from the `X-Session-ID` response header of a prior request, or from the `{ "sessionId": "..." }` returned when using `sse=true`.
* If the session was already cleaned up (completion/timeout/TTL), reusing its ID returns 404. Start a new task (optionally with `sse=true`) to create a fresh session.

### Example <a href="#example" id="example"></a>

`review` command that analyzes code changes (diffs/PRs) and returns structured findings.

* Arguments:
  * `pr` (string, optional): URL of the pull request to analyze (recommended when using webhook mode).
* Output (structured):
  * An object with `summary` and `findings[]`.
  * Each finding includes: `finding_title`, `severity_level` ("breaking-issue" | "concern"), `repo_name`, `file_path`, `reason`, `diff_pointer`, `recommended_fix`, and `evidence`.
  * `diff_pointer` shape (as defined in the command’s schema) includes: `start_line`, `end_line`, and `hunk_header`.

Tip: In webhook mode, there is no free‑text prompt. For the review agent, prefer passing a `pr` URL so the agent can fetch and analyze the changes. (For scenarios that rely on providing a unified diff directly in a prompt, use the interactive CLI or web UI modes.)

#### A) One‑shot (no streaming) <a href="#a-oneshot-no-streaming" id="a-oneshot-no-streaming"></a>

```bash
curl -X POST "http://localhost:6666/webhook/review" \
  -H "Content-Type: application/json" \
  -d '{ "pr": "https://github.com/org/repo/pull/123" }'
```

Response (example):

```json
{
  "summary": "Analyzed PR #123 – identified 2 issues likely to break runtime behavior.",
  "findings": [
    {
      "finding_title": "Null check removed in foo()",
      "severity_level": "breaking-issue",
      "repo_name": "org/repo",
      "file_path": "src/foo.ts",
      "reason": "Removal of null guard introduces potential null dereference at runtime.",
      "diff_pointer": {
        "start_line": 120,
        "end_line": 130,
        "hunk_header": "@@ -118,6 +120,12 @@"
      },
      "recommended_fix": "Restore the null check before accessing the value; add a unit test to cover null inputs.",
      "evidence": "Before: value was checked for null; After: direct access without guard. This path is reachable when config is missing."
    }
  ]
}
```

If your command specifies a structured output (like `review`), the response will be the structured JSON. Otherwise, it falls back to `{ "result": "<final text>" }`.

#### B) Two‑step with SSE <a href="#b-twostep-with-sse" id="b-twostep-with-sse"></a>

1. Start the task and get a sessionId:

```bash
curl -s -X POST "http://localhost:6666/webhook/review?sse=true" \
  -H "Content-Type: application/json" \
  -d '{ "pr": "https://github.com/org/repo/pull/123" }'
# => { "sessionId": "<SESSION_ID>" }
```

2. Connect to the SSE stream:

```bash
curl -N "http://localhost:6666/webhook/review?sessionId=<SESSION_ID>"
```

You will receive events like:

```
event: loading
data: {"isLoading":true}

event: message
data: {"content":"Analyzing PR #123..."}

event: message
data: {"content":"Found 2 potential issues"}

event: loading
data: {"isLoading":false}

event: done
data: {}
```

The connection closes after `done`, and the session is cleaned up.

#### C) Reusing a session <a href="#c-reusing-a-session" id="c-reusing-a-session"></a>

```bash
curl -X POST "http://localhost:6666/webhook/review" \
  -H "X-Session-ID: <EXISTING_SESSION>" \
  -H "Content-Type: application/json" \
  -d '{ "pr": "https://github.com/org/repo/pull/456" }'
```

### Options and Flags That Influence Behavior <a href="#options-and-flags-that-influence-behavior" id="options-and-flags-that-influence-behavior"></a>

* `--webhook` – start the webhook server
* `-p, --port` – set the starting port (default: 6666)
* Tool selection:
  * `--tool <name>` (repeatable) or `--tools=name1,name2`
  * `--no-tool <server.tool>` (repeatable) or `--no-tools=server.tool1,server.tool2`
* Permissions:
  * `--permissions <r|rw|rwx|->` to override command permissions

These flags affect the agent’s tool access and permissions at startup; they do not change the HTTP contract.

### Security Considerations <a href="#security-considerations" id="security-considerations"></a>

* The server does not enforce HTTP authentication. Treat it as a development/local service or place it behind your API gateway/reverse proxy that handles auth and TLS.
* Ensure QODO\_API\_KEY is set appropriately and that you don’t expose this server publicly without protections.

### Troubleshooting <a href="#troubleshooting" id="troubleshooting"></a>

* 400 Invalid Payload:
  * Ensure your request body matches the command’s `arguments` definition (for `review`, the optional `pr` string).
* 404 Not Found:
  * Check the `commandName` path, and ensure `sessionId` is valid for SSE.
* 500 Internal Error / Timeout:
  * Non‑SSE POST requests time out after 90 minutes. Use SSE for long‑running tasks.
* No output / empty result:
  * If the agent produced no messages, the non‑SSE response falls back to `{ "result": "No response" }`.

### Notes <a href="#notes" id="notes"></a>

* Requests are executed in a non‑interactive, webhook‑friendly manner. Do not expect to receive user prompts or approvals through this interface.
* For long-running operations and real-time visibility into progress, prefer the two-step SSE pattern.
