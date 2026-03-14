# Verba Documentation

Source: https://docs.verba.ink/llms-full.txt

---

# Account and security

Source: https://docs.verba.ink/guides/account-and-security

Magic-link login, 2FA, API keys, connected services, and account safety.

## Questions this guide answers

* How does passwordless magic-link login work?
* How do I enable and verify 2FA?
* How many API keys can I create?
* What happens when I revoke a key?
* Can I disconnect Patreon anytime?

## Passwordless login (magic link)

Verba supports passwordless email auth.

Flow:

1. Request a magic link with your email.
2. Open the email and click the link.
3. Verba verifies the token and signs you in.

Important behavior:

* Magic links expire after `20 minutes`.
* You can request a resend.
* Invalid/expired links must be requested again.

## Two-factor authentication (2FA)

### Setup

* Open settings security section.
* Generate QR/secret.
* Confirm with a valid authenticator code.
* Save backup codes.

### Login verification

During protected login flows, Verba may require:

* 6-digit authenticator token
* Or 8-character backup code

Backup codes are one-time use and removed after successful verification.

### Disable 2FA

* Requires valid 2FA verification to disable.

## API keys

### Key format and limits

* Keys use prefix: `vka_`
* Active key limit: up to `3` keys

### Key lifecycle

* Create from Settings -> Security -> API Keys.
* Full key value is shown once on creation.
* Revoke any key instantly from dashboard.
* Revoked keys stop authenticating immediately.

### Authentication headers

Use one of:

* `Authorization: Bearer vka_...`
* `x-api-key: vka_...`

## Connected services

### Patreon linking

* Patreon can be linked from settings.
* Tier/benefits sync with account profile.

### Patreon disconnect guard

Disconnect may be blocked while an active Patreon subscription is still attached.

## Profile asset uploads

From settings:

* Avatar/banner image uploads are validated and moderated.
* Keep files under dashboard limits (commonly `10MB` for profile uploads).

## Deleting your account

Account deletion removes your account data and associated records.

Behavior includes cleanup for:

* Verbs and related references
* Group/DM associations
* Messages and conversation records tied to deleted entities

Group ownership handling:

* If other members exist, ownership can transfer.
* If no replacement exists, owned groups may be removed.

<Warning>
  Account deletion is destructive. Export or copy anything you need before
  confirming deletion.
</Warning>

<CardGroup>
  <Card title="Public API v1" icon="code" href="/guides/api">
    Full endpoint docs for authentication, requests, streaming, and errors.
  </Card>

  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Fix login, 2FA, and API key issues quickly.
  </Card>
</CardGroup>

# AI engine settings

Source: https://docs.verba.ink/guides/ai-engine

Tune model behavior, response length, context, and search.

## Questions this guide answers

* Which settings affect creativity vs consistency?
* Why are responses short or long?
* How much context and max tokens can my plan use?
* What does web search actually do?

## Core controls

| Setting       | Range          | What it changes                    |
| ------------- | -------------- | ---------------------------------- |
| Temperature   | `0..2`         | Randomness and creativity          |
| Top-p         | `0..1`         | Diversity of token selection       |
| Model Context | plan-limited   | Number of recent messages included |
| Reply Style   | preset         | Voice/format tendency              |
| Multi-message | on/off + delay | Sends split follow-up replies      |
| Web search    | on/off         | Allows live web-grounded replies   |

## System instructions (behavior prompt)

System instructions are your verb's persistent behavior rules.

Where to set:

* Dashboard -> Bot -> AI Engine -> Behavior
* Field name: `systemInstructions`

Limit:

* Up to `8000` characters

How they interact with other layers:

* `systemInstructions`: behavior/rules/tone constraints
* Training examples: style shaping and response pattern hints
* Long-term memory: durable facts/preferences
* Knowledge entries: factual/reference content
* Conversation context: recent turns in current chat/thread/session

Practical rule:

* Put "how to behave" in system instructions.
* Put "facts to remember" in knowledge/memory.
* Put "how to phrase outputs" in training examples.

## Plan-based limits

Current default limits:

| Plan  | Max model context | Max response tokens |
| ----- | ----------------- | ------------------- |
| Free  | `50`              | `4096`              |
| Plus  | `75`              | `8192`              |
| Pro   | `100`             | `16384`             |
| Ultra | `150`             | `32768`             |

<Note>
  If you request settings above your tier limits, they are clamped or rejected
  depending on the endpoint.
</Note>

## Recommended presets

<CardGroup>
  <Card title="Reliable support" icon="shield">
    Temperature `0.4-0.7`, top-p `0.7-0.9`, moderate context.
  </Card>

  <Card title="Creative roleplay" icon="sparkles">
    Temperature `0.8-1.1`, top-p `0.9-1.0`, higher context.
  </Card>

  <Card title="Cost-aware" icon="wallet">
    Lower context, web search off, shorter reply style.
  </Card>

  <Card title="Fast troubleshooting" icon="bolt">
    Lower context + deterministic settings to reduce latency variance.
  </Card>
</CardGroup>

## Multi-message behavior

When enabled:

* Verba can split a response into multiple shorter messages.
* Delay between parts is configurable (`0..10000ms`).

Use this for natural chat pacing; disable if you want one compact answer.

## Web search behavior

When enabled, Verba may perform model-driven search planning before the final answer.
This improves freshness, but can increase:

* Latency
* Token usage
* Cost

Use web search for:

* News
* Live pricing
* Fast-changing product details

Keep it off for:

* Roleplay
* Stable canon/lore
* Deterministic support flows

## System instructions best practices

* Keep instructions concrete and scoped.
* Avoid contradictory rules.
* Prefer short imperative bullets over long prose.
* Include failure policy (what to do when unknown).
* Specify output format explicitly (headings, bullets, steps, code blocks).

## Quick diagnostics

<AccordionGroup>
  <Accordion title="Replies are too generic">
    Lower temperature, tighten system instructions, and add targeted training examples.
  </Accordion>

  <Accordion title="Bot forgets recent details">
    Increase model context (within your plan limit).
  </Accordion>

  <Accordion title="Replies are too short">
    Increase max tokens and use a fuller reply style.
  </Accordion>

  <Accordion title="Replies are too slow">
    Reduce context and disable web search unless needed.
  </Accordion>
</AccordionGroup>

<Card title="Bot Settings Reference" icon="book" href="/guides/bot-settings-reference">
  See all AI-related fields and limits in one place.
</Card>

# Public API v1

Source: https://docs.verba.ink/guides/api

Use API keys to talk to characters outside Discord.

## Base URL

`https://api.verba.ink`

## How the API works (short answer)

1. Create an API key in Dashboard -> Settings -> Security -> API Keys.
2. Call `POST /v1/response` with `character` + `messages`.
3. Save the returned `session_id` and reuse it for follow-up requests.
4. Use `stream: true` for SSE streaming on Plus/Pro/Ultra plans.
5. Use `POST /v1/image` when you need image generation.

Minimal text request:

```json theme={null}
{
  "character": "mycharacter_abc",
  "messages": [
    { "role": "user", "content": "How does the API work?" }
  ]
}
```

## Fast answers

* Base URL: `https://api.verba.ink`
* Text endpoint: `POST /v1/response`
* Image endpoint: `POST /v1/image`
* Auth: `Authorization: Bearer vka_...` or `x-api-key: vka_...`
* Session memory: reuse `session_id` on later calls to continue context
* Streaming: `stream: true` on `/v1/response` (Plus/Pro/Ultra)
* Message count limit: up to `60` items in `messages`
* Message size limits: each message text up to `4000` chars, total up to `20000` chars
* Session ID format: optional, max `128` chars, allowed chars `A-Z a-z 0-9 : _ -`
* Image URL limit: up to `4` combined URLs
* Tool limits: up to `8` tool definitions, up to `2` executed tool calls per request

## Request limits (fast reference)

| Field                        | Limit                     |
| ---------------------------- | ------------------------- |
| `messages` length            | `60` max                  |
| Per-message text             | `4000` chars max          |
| Total text across `messages` | `20000` chars max         |
| `session_id`                 | optional, `128` chars max |
| `image_urls` (combined)      | `4` max                   |
| `tools` definitions          | `8` max                   |
| Executed tool calls          | `2` max per request       |
| `/v1/image` prompt           | `1500` chars max          |
| `/v1/image` size             | only `1024x1024`          |

## Quick start

<Steps>
  <Step title="Create an API key">
    Go to Verba <strong>Settings -> Security -> API Keys</strong> and create a key.
  </Step>

  <Step title="Pick a character">
    Use your character vanity slug or vanity URL (for example `mycharacter_abc` or `https://verba.ink/v/mycharacter_abc`).
  </Step>

  <Step title="Call an endpoint">
    Use `POST /v1/response` for text replies, or `POST /v1/image` for image generation.
  </Step>
</Steps>

## Authentication

Send your API key in either header:

* `Authorization: Bearer vka_...`
* `x-api-key: vka_...`

If no key is provided, or the key is invalid/revoked, the API returns `401`.

## API key quick facts

* API key prefix is `vka_`.
* Maximum active keys per account: `3`.
* Key revocation is immediate.

## Character identifier

Both endpoints use `character` (not `verb_id`).

Accepted formats:

* Vanity slug: `mycharacter_abc`
* Vanity path: `/v/mycharacter_abc`
* Full vanity URL: `https://verba.ink/v/mycharacter_abc`

## Endpoints

* `POST /v1/response` for text chat completions
* `POST /v1/image` for image generation

## POST `/v1/response`

Text completion endpoint. You can optionally attach image URLs for vision-enabled prompting.

<Note>
  Supports both standard JSON and streaming. Set `stream: true` to receive Server-Sent Events (SSE) chunks.
</Note>

<Note>
  Streaming on `/v1/response` is available for Plus, Pro, and Ultra plans.
</Note>

Required:

* `character` string (vanity URL or vanity slug)
* `messages` array (`role` + `content`)

Optional:

* `session_id` string
* `temperature` number (`0..2`)
* `top_p` number (`0..1`)
* `max_tokens` number
* `stream` boolean (`true` for SSE stream, default `false`)
* `image_urls` array of image URLs (`http/https`, max 4)
* `tools` array (OpenAI-style function tools, max 8)
* `tool_choice` (`"auto"` or `"none"`)
* `debug` object (`{ "tools": true }` to include tool traces)

### Session memory on `/v1/response`

How it works:

1. Send your first request with or without `session_id`.
2. If omitted, the API generates one and returns it in the response.
3. Reuse that same `session_id` in later requests to keep context for that caller + character.

If you use a new `session_id`, you start a new conversation state.

`messages[].content` supports:

* String text content
* Array parts with:
  * `{ "type": "text", "text": "..." }`
  * `{ "type": "image_url", "image_url": { "url": "https://..." } }`

You can pass image URLs either in `messages[].content` or top-level `image_urls` (both are merged, max 4 total).
You cannot pass custom `system` messages on `/v1/response`; character personality + system instructions are applied automatically.
Tool configuration is request-scoped only (not stored on your character/dashboard).

### Request examples

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.verba.ink/v1/response \
    -X POST \
    -H "Authorization: Bearer $VERBA_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "character": "mycharacter_abc",
      "messages": [
        { "role": "user", "content": "Tell me a short story about space pirates." }
      ],
      "stream": false
    }'
  ```

  ```javascript Node.js theme={null}
  const response = await fetch("https://api.verba.ink/v1/response", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.VERBA_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      character: "mycharacter_abc",
      messages: [
        { role: "user", content: "Tell me a short story about space pirates." }
      ],
      stream: false
    })
  });

  const data = await response.json();
  console.log(data);
  ```

  ```python Python theme={null}
  import os
  import requests

  response = requests.post(
      "https://api.verba.ink/v1/response",
      headers={
          "Authorization": f"Bearer {os.environ['VERBA_API_KEY']}",
          "Content-Type": "application/json",
      },
      json={
          "character": "mycharacter_abc",
          "messages": [
              {"role": "user", "content": "Tell me a short story about space pirates."}
          ],
          "stream": False,
      },
      timeout=60,
  )

  print(response.status_code)
  print(response.json())
  ```

  ```powershell PowerShell theme={null}
  $headers = @{
    Authorization = "Bearer $env:VERBA_API_KEY"
    "Content-Type" = "application/json"
  }

  $body = @{
    character = "mycharacter_abc"
    messages = @(
      @{
        role = "user"
        content = "Tell me a short story about space pirates."
      }
    )
    stream = $false
  } | ConvertTo-Json -Depth 10

  Invoke-RestMethod `
    -Method Post `
    -Uri "https://api.verba.ink/v1/response" `
    -Headers $headers `
    -Body $body
  ```

</CodeGroup>

### Session memory example

First call:

```json theme={null}
{
  "character": "mycharacter_abc",
  "messages": [
    { "role": "user", "content": "My name is Sam. Remember that." }
  ]
}
```

Response includes `session_id`:

```json theme={null}
{
  "session_id": "sess_abc123",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "Got it, Sam."
      }
    }
  ]
}
```

Follow-up call (same session):

```json theme={null}
{
  "character": "mycharacter_abc",
  "session_id": "sess_abc123",
  "messages": [
    { "role": "user", "content": "What's my name?" }
  ]
}
```

### Vision input example

```json theme={null}
{
  "character": "mycharacter_abc",
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "Describe what is happening here." },
        { "type": "image_url", "image_url": { "url": "https://example.com/city.jpg" } }
      ]
    }
  ],
  "stream": false
}
```

### Request-scoped tool calling

`/v1/response` supports server-executed HTTP function tools passed in the request.

* Tools are not persisted.
* Allowed methods: `GET`, `POST`.
* Tool URLs support only `http/https` on ports `80` or `443`.
* Local/private network targets are blocked.
* Tool responses must be `application/json` (or `+json`) or `text/plain`.
* Max executed tool calls per request: `2`.
* Built-in character `webSearch` remains separate and unchanged.

Tool object shape:

```json theme={null}
{
  "type": "function",
  "function": {
    "name": "search_web",
    "description": "Search latest web results",
    "parameters": {
      "type": "object",
      "properties": {
        "query": { "type": "string" }
      },
      "required": ["query"]
    },
    "x_verba_http": {
      "url": "https://example.com/search",
      "method": "GET",
      "query_param": "q",
      "headers": {
        "Authorization": "Bearer sk_live_..."
      },
      "timeout_ms": 8000
    }
  }
}
```

`tool_choice` supports:

* `"auto"` (default model decides)
* `"none"` (disable tool calls for this request)

How `auto` works:

* Verba first lets the model decide natively (provider `tool_calls` if supported).
* If the provider does not emit native `tool_calls`, Verba runs an internal model planner step to decide whether one tool should be used.
* This preserves model-driven behavior while improving compatibility across providers.

When `debug.tools=true`:

* Non-stream response includes `debug.tool_runs[]`.
* Stream response emits extra SSE frames with `object: "chat.completion.tool_trace"`.

### Tool example (`GET` web search)

```json theme={null}
{
  "character": "mycharacter_abc",
  "messages": [
    { "role": "user", "content": "What happened in AI this week?" }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "search_web",
        "description": "Search web headlines",
        "parameters": {
          "type": "object",
          "properties": {
            "query": { "type": "string" }
          },
          "required": ["query"]
        },
        "x_verba_http": {
          "url": "https://example-search-api.com/search",
          "method": "GET",
          "query_param": "q",
          "headers": {
            "Authorization": "Bearer sk_live_..."
          }
        }
      }
    }
  ],
  "tool_choice": "auto",
  "debug": { "tools": true }
}
```

### Tool example (`POST` JSON)

```json theme={null}
{
  "character": "mycharacter_abc",
  "messages": [
    { "role": "user", "content": "Fetch weather for Paris and summarize it." }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "weather_lookup",
        "description": "Return weather by city",
        "parameters": {
          "type": "object",
          "properties": {
            "city": { "type": "string" }
          },
          "required": ["city"]
        },
        "x_verba_http": {
          "url": "https://example.com/weather",
          "method": "POST",
          "headers": {
            "Authorization": "Bearer sk_live_..."
          },
          "body_mode": "json"
        }
      }
    }
  ]
}
```

### Example response

```json theme={null}
{
  "id": "chatcmpl_...",
  "object": "chat.completion",
  "created": 1739730000,
  "model": "m_free_a",
  "character": "mycharacter_abc",
  "session_id": "sess_...",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0
  }
}
```

Example response addition when `debug.tools=true`:

```json theme={null}
{
  "debug": {
    "tool_runs": [
      {
        "tool_name": "search_web",
        "method": "GET",
        "url": "https://example-search-api.com/search?q=ai",
        "status": "success",
        "http_status": 200,
        "duration_ms": 412,
        "request_preview": { "query": { "q": "ai" } },
        "response_preview": { "results": [{ "title": "..." }] }
      }
    ]
  }
}
```

### Streaming (`stream: true`)

With `stream: true`, `/v1/response` returns `text/event-stream` and emits `data:` events.

* Each event is an OpenAI-style `chat.completion.chunk` payload.
* If `debug.tools=true` and tools run, extra events use `object: "chat.completion.tool_trace"`.
* The final event is `data: [DONE]`.
* You should concatenate `choices[0].delta.content` chunks to build the assistant message.
* Free plans return `403 stream_plan_upgrade_required` when `stream: true` is used.

Example chunk:

```json theme={null}
{
  "id": "chatcmpl_...",
  "object": "chat.completion.chunk",
  "created": 1739730000,
  "model": "m_free_a",
  "character": "mycharacter_abc",
  "session_id": "sess_...",
  "choices": [
    {
      "index": 0,
      "delta": { "content": "Hello" },
      "finish_reason": null
    }
  ]
}
```

Final chunk:

```json theme={null}
{
  "id": "chatcmpl_...",
  "object": "chat.completion.chunk",
  "created": 1739730000,
  "model": "m_free_a",
  "character": "mycharacter_abc",
  "session_id": "sess_...",
  "choices": [
    {
      "index": 0,
      "delta": {},
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 0,
    "completion_tokens": 0,
    "total_tokens": 0
  }
}
```

Then:

```text theme={null}
data: [DONE]
```

### Streaming request examples

<CodeGroup>
  ```bash cURL theme={null}
  curl -N https://api.verba.ink/v1/response \
    -X POST \
    -H "Authorization: Bearer $VERBA_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "character": "mycharacter_abc",
      "messages": [
        { "role": "user", "content": "Give me a short greeting." }
      ],
      "stream": true
    }'
  ```

  ```javascript Node.js theme={null}
  const response = await fetch("https://api.verba.ink/v1/response", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.VERBA_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      character: "mycharacter_abc",
      messages: [{ role: "user", content: "Give me a short greeting." }],
      stream: true
    })
  });

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = "";

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;

    buffer += decoder.decode(value, { stream: true });
    const events = buffer.split("\\n\\n");
    buffer = events.pop() || "";

    for (const event of events) {
      if (!event.startsWith("data:")) continue;
      const data = event.slice(5).trim();
      if (data === "[DONE]") {
        process.stdout.write("\\n");
        continue;
      }
      const chunk = JSON.parse(data);
      const delta = chunk.choices?.[0]?.delta?.content;
      if (delta) process.stdout.write(delta);
    }
  }
  ```

  ```python Python theme={null}
  import json
  import os
  import requests

  response = requests.post(
      "https://api.verba.ink/v1/response",
      headers={
          "Authorization": f"Bearer {os.environ['VERBA_API_KEY']}",
          "Content-Type": "application/json",
      },
      json={
          "character": "mycharacter_abc",
          "messages": [{"role": "user", "content": "Give me a short greeting."}],
          "stream": True,
      },
      stream=True,
      timeout=120,
  )

  for line in response.iter_lines(decode_unicode=True):
      if not line or not line.startswith("data:"):
          continue
      data = line[5:].strip()
      if data == "[DONE]":
          print()
          break
      chunk = json.loads(data)
      delta = (((chunk.get("choices") or [{}])[0].get("delta") or {}).get("content"))
      if delta:
          print(delta, end="", flush=True)
  ```

  ```powershell PowerShell theme={null}
  $json = @{
    character = "mycharacter_abc"
    messages = @(
      @{
        role = "user"
        content = "Give me a short greeting."
      }
    )
    stream = $true
  } | ConvertTo-Json -Depth 10

  $http = [System.Net.Http.HttpClient]::new()
  $request = New-Object System.Net.Http.HttpRequestMessage([System.Net.Http.HttpMethod]::Post, "https://api.verba.ink/v1/response")
  $request.Headers.Authorization = [System.Net.Http.Headers.AuthenticationHeaderValue]::new("Bearer", $env:VERBA_API_KEY)
  $request.Content = New-Object System.Net.Http.StringContent($json, [System.Text.Encoding]::UTF8, "application/json")

  $response = $http.SendAsync($request, [System.Net.Http.HttpCompletionOption]::ResponseHeadersRead).Result
  $stream = $response.Content.ReadAsStreamAsync().Result
  $reader = New-Object System.IO.StreamReader($stream)

  while (-not $reader.EndOfStream) {
    $line = $reader.ReadLine()
    if (-not $line -or -not $line.StartsWith("data:")) { continue }
    $data = $line.Substring(5).Trim()
    if ($data -eq "[DONE]") { break }
    $chunk = $data | ConvertFrom-Json
    $delta = $chunk.choices[0].delta.content
    if ($delta) { Write-Host -NoNewline $delta }
  }
  Write-Host ""
  ```

</CodeGroup>

Streaming with tools works the same way: the API executes tool calls server-side first, then streams final assistant text chunks.

```json theme={null}
{
  "character": "mycharacter_abc",
  "messages": [{ "role": "user", "content": "Find and summarize today's top AI headline." }],
  "stream": true,
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "search_web",
        "parameters": {
          "type": "object",
          "properties": { "query": { "type": "string" } },
          "required": ["query"]
        },
        "x_verba_http": {
          "url": "https://example-search-api.com/search",
          "method": "GET",
          "query_param": "q"
        }
      }
    }
  ],
  "debug": { "tools": true }
}
```

## POST `/v1/image`

Generates one image URL.

Required:

* `character` string (vanity URL or vanity slug)
* `prompt` string

Optional:

* `session_id` string
* `image_urls` string array (reference images)
* `size` (`1024x1024` only)
* `response_format` (`url` only)

### Request examples

<CodeGroup>
  ```bash cURL theme={null}
  curl https://api.verba.ink/v1/image \
    -X POST \
    -H "Authorization: Bearer $VERBA_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "character": "mycharacter_abc",
      "prompt": "A cinematic portrait of a cyberpunk fox detective",
      "size": "1024x1024",
      "response_format": "url"
    }'
  ```

  ```javascript Node.js theme={null}
  const response = await fetch("https://api.verba.ink/v1/image", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${process.env.VERBA_API_KEY}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      character: "mycharacter_abc",
      prompt: "A cinematic portrait of a cyberpunk fox detective",
      size: "1024x1024",
      response_format: "url"
    })
  });

  const data = await response.json();
  console.log(data);
  ```

  ```python Python theme={null}
  import os
  import requests

  response = requests.post(
      "https://api.verba.ink/v1/image",
      headers={
          "Authorization": f"Bearer {os.environ['VERBA_API_KEY']}",
          "Content-Type": "application/json",
      },
      json={
          "character": "mycharacter_abc",
          "prompt": "A cinematic portrait of a cyberpunk fox detective",
          "size": "1024x1024",
          "response_format": "url",
      },
      timeout=120,
  )

  print(response.status_code)
  print(response.json())
  ```

  ```powershell PowerShell theme={null}
  $headers = @{
    Authorization = "Bearer $env:VERBA_API_KEY"
    "Content-Type" = "application/json"
  }

  $body = @{
    character = "mycharacter_abc"
    prompt = "A cinematic portrait of a cyberpunk fox detective"
    size = "1024x1024"
    response_format = "url"
  } | ConvertTo-Json -Depth 10

  Invoke-RestMethod `
    -Method Post `
    -Uri "https://api.verba.ink/v1/image" `
    -Headers $headers `
    -Body $body
  ```

</CodeGroup>

### Example response

```json theme={null}
{
  "created": 1739730000,
  "character": "mycharacter_abc",
  "session_id": "sess_...",
  "model": "m_free_a",
  "revised_prompt": "A cinematic portrait of a cyberpunk fox detective",
  "data": [
    {
      "url": "https://api.verba.ink/uploads/generated-images/img_...png"
    }
  ]
}
```

## Sessions and memory

* `session_id` is optional.
* If omitted, Verba generates one and returns it.
* Reusing the same `session_id` preserves API conversation context for that caller + verb pair.
* API memory is stored in conversation history only (not DM or message logs).

## Access, billing, and limits

* API access is available to all users.
* Verb privacy still applies:
  * Private characters: owner only
  * Public characters: any API caller
* Billing and tier/model enforcement are applied to the **character owner account**.
* `/v1/*` uses account rate limits via the same per-user limiter model.

## Message format (`/v1/response`)

* `messages` must be an array.
* Include at least one `user` message.
* Allowed roles: `user`, `assistant` (`assistant` maps internally to model role).
* `system` role is blocked on `/v1/response` to prevent overriding character instructions.
* `messages[].content` supports text and `image_url` parts.
* Top-level `image_urls` is also supported.
* Combined image URL limit is 4.
* `tools` is optional and request-scoped (max 8 per request).
* `tool_choice` is optional (`auto` or `none`).

## Error model

Errors return JSON with a top-level `message` and an `error` object.

```json theme={null}
{
  "message": "stream must be a boolean",
  "error": {
    "message": "stream must be a boolean",
    "type": "invalid_stream",
    "code": 400
  }
}
```

* `error.type`: stable machine-readable error type (for program logic)
* `error.code`: HTTP status code

Common error cases:

* `401 invalid_api_key` for missing/invalid/revoked API key
* `403 verb_access_denied` for private character access by non-owner
* `403 stream_plan_upgrade_required` when free plans request `stream: true`
* `403 insufficient_credits` when the character owner has no credits for the selected model
* `400 invalid_message_role` when `system` role is provided in `messages`
* `400 invalid_stream` when `stream` is not a boolean
* `400 invalid_tools` for malformed tool schema/config
* `400 invalid_tool_choice` for invalid `tool_choice`
* `400 blocked_tool_url` when tool URL targets local/private hosts
* `400 tool_call_limit_exceeded` when model attempts more than 2 tool calls
* `400 invalid_image_urls` when image URL payload format is invalid
* `400 blocked_image_url` when image URL targets local/private network hosts
* `400 too_many_image_urls` when more than 4 image URLs are provided
* `502 tool_execution_failed` when upstream tool execution fails
* `400 invalid_size` when `/v1/image` size is not `1024x1024`

# How the API works

Source: https://docs.verba.ink/guides/api-how-it-works

Direct answer to how api.verba.ink works, with minimal request flow and limits.

## Short answer

Verba API works by authenticating with your API key, selecting a character, sending chat messages to `/v1/response`, and reusing `session_id` to keep memory between calls.

## 5-step flow

1. Create an API key (`vka_...`) in Dashboard -> Settings -> Security -> API Keys.
2. Send `POST https://api.verba.ink/v1/response`.
3. Include `character` (slug/path/URL) and `messages`.
4. Read the returned response and store `session_id`.
5. Reuse that same `session_id` in future calls for ongoing context.

## Minimal request

```json theme={null}
{
  "character": "mycharacter_abc",
  "messages": [
    { "role": "user", "content": "How does the API work?" }
  ]
}
```

## Required headers

* `Authorization: Bearer vka_...`
* or `x-api-key: vka_...`

## Important limits

* `messages`: max `60`
* message text: `4000` chars each
* total text across messages: `20000` chars
* `session_id`: optional, max `128` chars
* combined image URLs: max `4`
* `/v1/image` prompt: max `1500` chars

## Streaming

Set `stream: true` on `/v1/response` to receive SSE chunks.
Streaming is available on Plus/Pro/Ultra plans.

## Related

* [Public API v1](/guides/api)
* [Plans and limits](/guides/plans-and-limits)
* [Question bank](/guides/question-bank)

# Best practices

Source: https://docs.verba.ink/guides/best-practices

Small habits that make verbs feel great.

## Build in layers

* Start with a short personality.
* Test in chat.
* Add depth only after the voice feels right.

## Keep prompts clean

* Use clear, direct language.
* Avoid conflicting instructions.
* Remove redundant details.

## Tune with intention

* Lower temperature for consistency.
* Increase context when you need continuity.
* Turn off web search unless it is required.

## Ask for feedback

Share your verb with friends or the community. Fresh eyes spot drift fast.

<Card title="Community" icon="users" href="/guides/community">
  Get quick feedback from other creators.
</Card>

# Billing and refunds

Source: https://docs.verba.ink/guides/billing-and-refunds

Purchases, invoices, and what to do if something looks off.

## Buying credits

Credits power text, image, and voice features. Buy a pack when you need more
headroom, and keep an eye on usage for big tests.

## Refunds and issues

If a purchase looks wrong:

1. Check your billing history.
2. Grab the transaction ID.
3. Contact support with the details.

<Note>
  Refunds are handled through support. Keep receipts handy to speed things up.
</Note>

<CardGroup>
  <Card title="Billing page" icon="credit-card" href="https://verba.ink/billing">
    See purchases and current balance.
  </Card>

  <Card title="Support" icon="envelope" href="https://verba.ink/contact">
    Reach the team with billing questions.
  </Card>
</CardGroup>

# Bot settings reference

Source: https://docs.verba.ink/guides/bot-settings-reference

Field-by-field guide to AI, memory, knowledge, training, voice, and Discord settings.

## Why this page exists

This is a practical reference for all major bot configuration panels in the dashboard.
Use it when you need exact ranges, limits, and behavior implications.

## AI engine settings

| Field                 | Range / Limit | Notes                                            |
| --------------------- | ------------- | ------------------------------------------------ |
| `temperature`         | `0..2`        | Creativity/randomness                            |
| `top_p`               | `0..1`        | Diversity control                                |
| `modelContext`        | plan-capped   | Number of history messages considered            |
| `replyStyle`          | preset enum   | `default`, `short`, `creative`, `crazy`, `human` |
| `webSearch`           | boolean       | Enables web-grounded answers                     |
| `multiMessageEnabled` | boolean       | Split response into multiple messages            |
| `multiMessageDelayMs` | `0..10000` ms | Delay between split parts                        |

### Plan caps

| Plan  | maxModelContext | maxTokens |
| ----- | --------------- | --------- |
| Free  | 50              | 4096      |
| Plus  | 75              | 8192      |
| Pro   | 100             | 16384     |
| Ultra | 150             | 32768     |

## Behavior settings

| Field                | Limit        | Notes                                             |
| -------------------- | ------------ | ------------------------------------------------- |
| `systemInstructions` | `8000` chars | Extra behavior control                            |
| `autonomousMode`     | boolean      | Enables autonomous behavior paths where supported |

## Training settings

Per example:

* `input`: max `500` chars
* `expected`: max `2000` chars
* `importance`: `1..10`
* `keywords[]`: optional relevance hints

Keyword matches can prioritize specific examples during generation.

## Memory settings

Per memory entry:

* `content`: max `2000` chars
* `context`: max `500` chars
* `importance`: `1..10`

Global memory toggles:

* `autoMemoryEnabled`: boolean
* `autoMemoryInstructions`: max `2000` chars

## Knowledge settings

Per knowledge entry:

* `title`: max `100` chars
* `content`: max `8000` chars
* `category`: max `50` chars
* `importance`: `1..10`

Per verb:

* max `50` knowledge entries

URL scrape helper:

* Can auto-draft title/content/category from a provided URL.

## Voice engine settings

Common fields:

* `voiceEnabled`
* `voiceResponseFrequency` (`0..100`)
* `selectedVoice`
* `voiceLanguage`
* `voiceModel`
* `voiceReferenceText`

Voice cloning:

* Up to `3` clones per verb

## Image engine settings

* `imageGeneration` toggle controls whether image commands/flows are active.
* `imageModel` selection is tier-aware.
* Non-eligible model selections can be automatically downgraded to allowed tiers.

## Discord module settings

Main controls:

* Connect/disconnect bot token
* Status/presence profile
* Slash command toggles
* AI channel management
* Server list/leave server tools

Core profile defaults include:

* Presence values: `online`, `idle`, `dnd`, `offline`
* Default status text behavior if unset

## Custom messages settings

Customizable response strings include:

* Rate limit
* Reset success/empty messages (DM + server)
* AI/processing/image errors
* Channel management messages
* Permission and server-only errors
* Voice join/leave messages

Per custom message field:

* Max length: `500` chars at schema level

<Note>
  UI may show stricter editing caps for some textareas to keep messages concise.
</Note>

## Validation and save failures

Common save rejection reasons:

* Out-of-range numeric values
* Context/model limit above plan cap
* Oversized memory/knowledge/training content
* Invalid types for structured fields

If a save fails, check browser console + response payload first, then compare against limits on this page.

<CardGroup>
  <Card title="AI Engine Settings" icon="sliders" href="/guides/ai-engine">
    Practical tuning guidance for model behavior.
  </Card>

  <Card title="Memory and Knowledge" icon="database" href="/guides/memory-and-knowledge">
    How persistence layers interact in real usage.
  </Card>
</CardGroup>

# Chat and groups

Source: https://docs.verba.ink/guides/chat-and-groups

How conversations, groups, DMs, and live updates work in Verba.

## Questions this guide answers

* When does a verb auto-reply in chats?
* What is the difference between a Group chat and a DM?
* Why did a message get blocked?
* What are the message and upload limits?
* How do invites, members, and permissions work?
* How does real-time syncing work across tabs/devices?

## Chat modes at a glance

| Mode  | Who can participate            | Typical use                                    |
| ----- | ------------------------------ | ---------------------------------------------- |
| Group | Multiple users + verbs         | Community rooms, roleplay, collaborative chats |
| DM    | 1:1 user + user or user + verb | Focused private conversations                  |

<Note>
  Group and DM conversations keep their own history, so context stays scoped to
  the current conversation.
</Note>

## Group basics

* Group owners can create up to `15` groups.
* New groups start with a `general` text channel.
* Invite links are generated per group and can be refreshed.
* Group roles are intentionally simple: `owner` and `member`.

### Ownership rules

* Only the owner can rename/update/delete the group.
* Only the owner can add/remove members directly.
* Only the owner can add/remove verbs in the group.
* Owners cannot leave their own group without transferring ownership first.

## Members and verbs

### Adding members

* Members added through invite codes join with member permissions.
* Inviting/joining triggers system events visible to the group.

### Adding verbs

You can add:

* Your own verbs.
* Public verbs from other users.

You cannot add:

* Private verbs you do not own.

## DMs

You can start DMs with:

* Another user.
* A verb.

For verb DMs:

* Public verbs are available to everyone.
* Private verbs are only available to the owner.

## Message flow and limits

### History pagination

When loading messages:

* Default fetch size: `50`
* Max fetch size: `200`

### Message requirements

A message must include at least one of:

* Text content
* A valid URL-style content body
* At least one attachment

### Anti-spam protection

Messages can be blocked when they look abusive, including:

* Mention flood
* Excessive zero-width character usage

<Warning>
  If users report random send failures, check for copied invisible characters
  and heavy mention payloads first.
</Warning>

### Upload limits

* Message image uploads: up to `5MB`
* Supported upload type: images only

## Reactions, edits, and deletes

* Users can edit/delete their own messages.
* Group owners (or users with manage message permissions) can moderate group messages.
* Reactions are supported for both group and DM messages.

## Real-time behavior (WebSocket)

Verba live chat uses WebSocket channels for:

* New message events
* Message edits/deletes
* Typing indicators
* Group/DM subscription updates

This is why messages appear instantly across open sessions when everything is healthy.

## Why a verb did not reply

Common causes:

* The verb was not configured to auto-respond in that context.
* The message was blocked by anti-spam rules.
* The sender does not have permission to post in the group.
* The verb or channel settings limit responses.

See [Troubleshooting](/guides/troubleshooting) for quick fixes.

<CardGroup>
  <Card title="Discord Deployment" icon="message" href="/guides/discord">
    Connect your verb to Discord with command controls and server settings.
  </Card>

  <Card title="Memory and Knowledge" icon="database" href="/guides/memory-and-knowledge">
    Understand how context and long-term memory affect response quality.
  </Card>
</CardGroup>

# Community

Source: https://docs.verba.ink/guides/community

Find help, share verbs, and get feedback.

## Join the Discord

The fastest way to get help is the community Discord.

* Invite link: [https://discord.gg/verba](https://discord.gg/verba)
* Ask questions in help channels
* Share your verbs in showcase

## Share and learn

* Post screenshots and chat logs
* Ask for feedback on personality
* Swap tips for prompts and settings

<Info>
  Be kind, be clear, and include screenshots when you report bugs.
</Info>

<Card title="Contact" icon="envelope" href="https://verba.ink/contact">
  Reach support if you need a private channel.
</Card>

# Credits and billing

Source: https://docs.verba.ink/guides/credits

Understand how credits work and plan usage.

## Credits in plain language

Credits are used for text, image, and voice generation. Bigger models, longer
outputs, and search-enabled workflows typically consume more.

## Plan-aware limits that affect credit usage

| Plan  | Monthly included allowance | Max context | Max tokens |
| ----- | -------------------------- | ----------- | ---------- |
| Free  | `0`                        | `50`        | `4096`     |
| Plus  | `2.5`                      | `75`        | `8192`     |
| Pro   | `5`                        | `100`       | `16384`    |
| Ultra | `10`                       | `150`       | `32768`    |

<Note>
  Included monthly allowance comes from your active tier. You can still top up
  credits separately.
</Note>

## Usage strategy

* Keep web search off for stable topics.
* Use smaller context for routine support replies.
* Reserve larger token limits for long-form answers.
* Use deterministic settings for troubleshooting to reduce retries.

## Common billing questions

<AccordionGroup>
  <Accordion title="Why did usage spike?">
    Typical causes are higher context, longer max tokens, web search, or a more expensive model selection.
  </Accordion>

  <Accordion title="Why does a model disappear?">
    Model access is tier-based. If tier or mapping changed, unavailable models are removed or remapped.
  </Accordion>

  <Accordion title="Do I lose access if Patreon is disconnected?">
    Active premium subscriptions can block Patreon disconnect until status is consistent.
  </Accordion>
</AccordionGroup>

<CardGroup>
  <Card title="Billing" icon="credit-card" href="https://verba.ink/billing">
    Buy credits and review purchase history.
  </Card>

  <Card title="Pricing" icon="tag" href="https://verba.ink/pricing">
    Compare plans and pricing.
  </Card>
</CardGroup>

<Info>
  If a model is unavailable, your current tier may not include it.
</Info>

<Card title="Billing and refunds" icon="receipt" href="/guides/billing-and-refunds">
  What to do if something looks off.
</Card>

<Card title="Plans and limits" icon="gauge" href="/guides/plans-and-limits">
  Full premium matrix: verbs, limits, streaming, and allowances.
</Card>

# Discord deployment

Source: https://docs.verba.ink/guides/discord

Connect a verb to Discord and configure how, where, and when it responds.

## Questions this guide answers

* Why does my bot show "connection failed"?
* Why does the bot ignore messages in some channels?
* How do mention mode and AI-channel mode differ?
* Why does `/reset` work in DMs but fail in servers?
* Why does the bot say "application did not respond"?

## Before you connect

You need:

* A Discord application + bot user
* A valid bot token
* Privileged intents enabled in Discord Developer Portal

<Warning>
  Missing privileged intents is the most common cause of a bot that connects in
  dashboard UI but does not respond in Discord.
</Warning>

## Connect flow

<Steps>
  <Step title="Create bot in Discord">
    Use the Discord Developer Portal and create an app/bot.
  </Step>

  <Step title="Enable required intents">
    Enable Message Content and other required privileged intents in the bot settings.
  </Step>

  <Step title="Paste token in Verba">
    Open your verb's Discord module and connect with your token.
  </Step>

  <Step title="Invite the bot">
    Use the generated OAuth link to add it to your server.
  </Step>
</Steps>

## How response routing works

In server channels, a connected verb responds when at least one condition is true:

* The verb is directly mentioned
* The channel is marked as an AI channel
* A training keyword match is detected

It does not respond when:

* Another bot is speaking (bot messages are ignored)
* Message includes `@everyone`/`@here`
* Message role-pings the bot's role directly
* User is on ignore/ban controls

## Mention mode vs AI-channel mode

### Mention mode

* Best for shared channels where bot noise should stay low
* Users ping the bot to trigger responses

### AI-channel mode (`/activate-channel`)

* Bot can respond without mentions in that channel
* Best for support/help channels or dedicated AI rooms

Use `/remove-channel` to disable AI-channel behavior.

## Slash commands available

Default command set:

* `/activate-channel`
* `/remove-channel`
* `/reset`
* `/generate`
* `/dashboard`
* `/vc-join`
* `/vc-leave`
* `/ping`

You can enable/disable each command in Discord module settings.

## Permissions behavior

* `/activate-channel` and `/remove-channel` require Administrator permission.
* `/reset` in server requires Administrator, server owner, or bot owner.
* `/reset` in DM is user-scoped and available without server permissions.
* Voice commands require Voice Engine enabled for the verb.

## Profile and presence settings

You can configure:

* Activity type (playing/listening/watching/custom)
* Activity text
* Presence (`online`, `idle`, `dnd`, `offline`)
* Slash command toggles

<Note>
  Activity text over dashboard limits is rejected or clamped. Keep status text short.
</Note>

## Server management tools

In the Discord module you can:

* View current server count
* Refresh profile/server data
* Leave specific servers
* Copy invite link quickly

## Typical failure patterns

<AccordionGroup>
  <Accordion title="Connection failed during token setup">
    Usually invalid token format, token already linked to another verb, or Discord rate limiting. Retry with a fresh token and verify it is not already attached elsewhere.
  </Accordion>

  <Accordion title="The application did not respond">
    Most often command timeout or missing Discord permissions in that channel. Check command toggle, channel permissions, and voice/image settings for the invoked command.
  </Accordion>

  <Accordion title="Bot is online but does not answer messages">
    Check whether the message was a mention, in an AI channel, or matched training keywords. Also verify intents and that the sender is not ignored/banned.
  </Accordion>

  <Accordion title="/reset fails in server">
    Server reset requires elevated permissions (admin/server owner/bot owner). DM reset does not.
  </Accordion>
</AccordionGroup>

<CardGroup>
  <Card title="Discord Command Reference" icon="terminal" href="/guides/discord-command-reference">
    Exact behavior and permission rules for each slash command.
  </Card>

  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Fast fix checklist for connection failures, timeouts, and no-response bugs.
  </Card>
</CardGroup>

# Discord command reference

Source: https://docs.verba.ink/guides/discord-command-reference

Exact slash command behavior, permissions, and expected responses.

## Command availability

Verba can register these slash commands:

* `/activate-channel`
* `/remove-channel`
* `/reset`
* `/generate`
* `/dashboard`
* `/vc-join`
* `/vc-leave`
* `/ping`

Each command can be toggled on/off in your Discord module settings.

## Permission matrix

| Command             | Where     | Permission requirement                      |
| ------------------- | --------- | ------------------------------------------- |
| `/activate-channel` | Server    | Administrator                               |
| `/remove-channel`   | Server    | Administrator                               |
| `/reset`            | DM        | None (user-scoped DM reset)                 |
| `/reset`            | Server    | Administrator, server owner, or bot owner   |
| `/generate`         | Server/DM | Command enabled + image generation enabled  |
| `/dashboard`        | Server/DM | Command enabled                             |
| `/vc-join`          | Server    | Voice engine enabled + voice channel access |
| `/vc-leave`         | Server    | Voice engine enabled                        |
| `/ping`             | Server/DM | Command enabled                             |

## Command behavior details

### `/activate-channel`

* Marks the current channel as AI-enabled.
* In AI-enabled channels, bot can reply without mentions.

### `/remove-channel`

* Removes the current channel from AI-enabled list.

### `/reset`

* In DM: clears DM conversation memory for that user context.
* In server: clears server conversation memory for that bot/server context.

### `/generate`

* Generates an image from prompt.
* Optional reference image is supported.
* If image generation is disabled on the bot, command returns a disabled message.

### `/dashboard`

* Returns the dashboard URL.

### `/vc-join`

* Joins the requester's voice channel (or selected voice channel parameter).
* Fails if bot lacks voice permissions or voice runtime dependencies.

### `/vc-leave`

* Leaves current voice channel if connected.

### `/ping`

* Health/status check command with latency output.

## Command toggle behavior

When a command is disabled in dashboard:

* Invocation returns a disabled-command response.
* Command registration may take a short delay to reflect in Discord command picker.

## Common command errors

<AccordionGroup>
  <Accordion title="This command is disabled for this bot">
    Re-enable the command in Discord module -> Slash Command Toggles.
  </Accordion>

  <Accordion title="You need Administrator permission">
    Server-only administrative commands require admin privileges in that guild.
  </Accordion>

  <Accordion title="This command can only be used in a server channel">
    Channel-management commands are server scoped and not available in DMs.
  </Accordion>

  <Accordion title="Image provider unavailable">
    Temporary upstream issue. Retry shortly or simplify prompt/reference image.
  </Accordion>

  <Accordion title="Voice runtime unavailable">
    Worker/runtime dependency issue. Restart worker and verify voice deps.
  </Accordion>
</AccordionGroup>

## Custom message templates

You can customize command/error text in the **Custom Messages** page.

Frequently used template variables:

* `{messagesPerMinute}`
* `{contextLabel}`
* `{channelMention}`
* `{verb}`
* `{user}`

<Card title="Discord Deployment" icon="message" href="/guides/discord">
  Setup guide for connection, intents, profiles, and server routing.
</Card>

# FAQ

Source: https://docs.verba.ink/guides/faq

High-frequency questions across API, Discord, memory, billing, and account settings.

## Top support answers

* How does the API work: create API key -> call `POST /v1/response` with `character` + `messages` -> reuse `session_id`.
* Where to set system instructions: Dashboard -> Bot -> AI Engine -> Behavior (`systemInstructions`, max `8000` chars).
* Plan limits: Free `50/4096`, Plus `75/8192`, Pro `100/16384`, Ultra `150/32768` (context/max tokens).
* Full tier matrix (`verbs/msg-min/context/max-tokens`): Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768`.

## Product basics

<AccordionGroup>
  <Accordion title="Can I keep a verb private?">
    Yes. Private verbs are only accessible by the owner. Public verbs can be discovered and used by others.
  </Accordion>

  <Accordion title="Why do replies consume credits?">
    Credits cover model inference and processing. Longer context and larger outputs consume more.
  </Accordion>

  <Accordion title="Can I use Verba outside Discord?">
    Yes. Use the public API at `api.verba.ink` with your API key.
  </Accordion>

  <Accordion title="Do I need a paid plan to use the API?">
    API access is available on all plans. Limits and model availability vary by tier.
  </Accordion>
</AccordionGroup>

## Discord FAQ

<AccordionGroup>
  <Accordion title="Why does the bot not answer unless pinged?">
    In server channels, the bot replies when mentioned, when channel is marked AI-enabled, or when a training keyword rule triggers.
  </Accordion>

  <Accordion title="How do I make it answer without mention in one channel?">
    Use `/activate-channel` in that channel.
  </Accordion>

  <Accordion title="How do I stop auto replies in a channel?">
    Use `/remove-channel`.
  </Accordion>

  <Accordion title="Why does /reset fail in server?">
    Server reset requires admin/server-owner/bot-owner permission.
  </Accordion>
</AccordionGroup>

## Memory and knowledge FAQ

<AccordionGroup>
  <Accordion title="What is the difference between memory and knowledge?">
    Memory is compact persistent facts; knowledge entries are richer structured references/lore.
  </Accordion>

  <Accordion title="How many knowledge entries can one verb store?">
    Up to `50` entries.
  </Accordion>

  <Accordion title="Can Verba auto-save memory from chats?">
    Yes, with Auto Memory enabled and instructions configured.
  </Accordion>

  <Accordion title="Why is it not using my docs correctly?">
    Improve knowledge entry quality (clear title/category/content), reduce ambiguity, and add training examples for recurring question patterns.
  </Accordion>
</AccordionGroup>

## API FAQ

<AccordionGroup>
  <Accordion title="How does the API work?">
    Create an API key, call `POST /v1/response` for text (or `POST /v1/image` for images), and reuse `session_id` for follow-up context.
  </Accordion>

  <Accordion title="How do I authenticate API requests?">
    Use `Authorization: Bearer vka_...` or `x-api-key`.
  </Accordion>

  <Accordion title="How does session memory work in API calls?">
    Reuse `session_id` to preserve context for the same caller + character.
  </Accordion>

  <Accordion title="Can I stream responses?">
    Yes with `stream: true` on `/v1/response` (tier restrictions apply).
  </Accordion>

  <Accordion title="Can I pass system messages directly in /v1/response?">
    No. Character system/personality is applied automatically.
  </Accordion>

  <Accordion title="What are the main /v1/response limits?">
    Max `60` messages, max `4000` chars per message, max `20000` total chars, max `4` image URLs, and max `128` chars for `session_id`.
  </Accordion>

  <Accordion title="How many API keys can I keep active?">
    Up to `3` active API keys per account.
  </Accordion>
</AccordionGroup>

## Plans and premium FAQ

<AccordionGroup>
  <Accordion title="Which plans support streaming on /v1/response?">
    Streaming is available on Plus, Pro, and Ultra. Free plan streaming requests are rejected.
  </Accordion>

  <Accordion title="How many verbs can I create per plan?">
    Free: 5, Plus: 10, Pro: 20, Ultra: 40.
  </Accordion>

  <Accordion title="Do plans affect context and token limits?">
    Yes. Plan tier sets max model context and max response tokens.
  </Accordion>

  <Accordion title="Where can I see the full plan matrix?">
    See the Plans and limits guide for complete tier-by-tier details.
  </Accordion>
</AccordionGroup>

## Account and security FAQ

<AccordionGroup>
  <Accordion title="How many API keys can I keep active?">
    Up to `3` active keys per account by default.
  </Accordion>

  <Accordion title="How long is a magic-link login valid?">
    Magic links expire after `20` minutes.
  </Accordion>

  <Accordion title="Can I disable 2FA later?">
    Yes. You can disable it from settings after verification.
  </Accordion>

  <Accordion title="Can I disconnect Patreon anytime?">
    Not while an active paid Patreon subscription is still linked.
  </Accordion>
</AccordionGroup>

<CardGroup>
  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Fix connection, timeout, and no-response issues.
  </Card>

  <Card title="Question Bank" icon="book-open" href="/guides/question-bank">
    Larger question-driven reference generated from backend/frontend behavior.
  </Card>
</CardGroup>

<Card title="Plans and limits" icon="gauge" href="/guides/plans-and-limits">
  Premium tiers, usage limits, streaming, and allowances.
</Card>

# Create your first verb

Source: https://docs.verba.ink/guides/first-verb

Design personality, visuals, and behavior in one flow.

## 1. Define the essentials

Start with the basics: name, description, age, and language. These fields shape
how your verb is introduced and how it speaks.

<Info>
  Keep the description short and concrete. Focus on tone, role, and what the
  verb helps with.
</Info>

## 2. Build a visual identity

Upload an avatar and banner that match the personality you want users to feel.

<Columns>
  <div>
    **Avatar**

    * Clear, centered subject
    * Works at small sizes
    * Consistent style with your banner
  </div>

  <div>
    **Banner**

    * Wider framing, more context
    * Reinforce the theme or mood
    * Optional but impactful
  </div>
</Columns>

## 3. Write the personality

Fill in core personality, backstory, beliefs, likes, and dislikes. This is the
primary source of behavior.

<CardGroup>
  <Card title="Core personality" icon="star">
    The non-negotiable traits and quirks.
  </Card>

  <Card title="Backstory" icon="book">
    Motivations that explain the personality.
  </Card>

  <Card title="Beliefs" icon="compass">
    Opinions and values that guide responses.
  </Card>

  <Card title="Likes and dislikes" icon="heart">
    Quick hooks for natural conversation.
  </Card>
</CardGroup>

## 4. Tune behavior

Set your AI engine controls to balance creativity and consistency. Start with
defaults, then iterate while chatting.

<Tip>
  If responses feel too generic, raise temperature slightly. If they drift off
  topic, lower it and reduce top-p.
</Tip>

## 5. Test and iterate

Run live chats, adjust prompts, and refine until the personality holds under
real usage.

<Card title="AI engine guide" icon="sliders" href="/guides/ai-engine">
  Learn how each control changes behavior.
</Card>

# Getting around

Source: https://docs.verba.ink/guides/getting-around

A quick tour of where things live in Verba.

## The basics

Think of Verba like a studio. You have a dashboard, a creation space, and a
chat room. Most of what you need is two clicks away.

<CardGroup>
  <Card title="Dashboard" icon="house">
    Your home base for verbs, stats, and quick actions.
  </Card>

  <Card title="Create" icon="plus">
    The guided flow for building a new verb.
  </Card>

  <Card title="Chat" icon="comments">
    Test your verb and tweak it fast.
  </Card>

  <Card title="Settings" icon="gear">
    Profile, billing, and account preferences.
  </Card>
</CardGroup>

## Useful shortcuts

* Use search to jump to a verb fast.
* Pin the verbs you use the most.
* Keep a test chat open while editing personality.

<Tip>
  If you feel lost, open Quickstart again. It mirrors the creation flow.
</Tip>

## What to click first

1. Create a verb.
2. Open chat and test a few prompts.
3. Adjust personality and AI engine settings.
4. Add visuals when the voice feels right.

<Card title="Quickstart" icon="rocket" href="/quickstart">
  Run the full setup in a few minutes.
</Card>

# Image generation

Source: https://docs.verba.ink/guides/image-generation

Let your verb create visuals on demand.

## Turn it on

Enable image generation when you want your verb to respond with visuals. This
is great for inspiration, mood boards, or quick mockups.

## Prompt tips

* Describe subject, style, and mood.
* Add a few details, then stop.
* If results drift, simplify the prompt.

<AccordionGroup>
  <Accordion title="Example prompts">
    - "Moody neon alley, rain, cyberpunk, cinematic"
    - "Soft watercolor landscape, sunrise, warm tones"
    - "Minimal logo concept, flat, modern"
  </Accordion>

  <Accordion title="Common mistakes">
    * Overly long prompts
    * Too many styles at once
    * Unclear subject
  </Accordion>
</AccordionGroup>

<Note>
  Image generation uses credits. Keep it off if you do not need it.
</Note>

# Memory and knowledge

Source: https://docs.verba.ink/guides/memory-and-knowledge

How context, long-term memory, training examples, and knowledge entries work together.

## Questions this guide answers

* Why does my verb forget details between messages?
* What is short-term context vs long-term memory?
* What should go into knowledge entries vs memory entries?
* How does URL scraping fill knowledge automatically?
* How do training examples and keywords influence replies?

## The four memory layers

### 1. Conversation context (short-term)

* Uses recent messages from the active conversation.
* Controlled by your `Model Context` setting.
* Higher context improves continuity but costs more tokens.

### 2. Long-term memory

* Manual memory items your verb can keep using over time.
* Best for durable facts and preferences.

### 3. Knowledge entries

* Structured lore/reference entries (title, category, content, importance).
* Best for world facts, policies, product facts, and evergreen docs.

### 4. Training examples

* Input/output examples for style and behavior shaping.
* Keyword matching can prioritize specific examples when relevant.

## Where system instructions fit

System instructions are not a memory entry type. They are the persistent
behavior policy prompt for the verb.

Where to configure:

* Dashboard -> Bot -> AI Engine -> Behavior
* Field: `systemInstructions`

Limit:

* `systemInstructions`: up to `8000` chars

Recommended split of responsibilities:

* System instructions: behavior rules, format constraints, refusal/uncertainty policy
* Knowledge entries: factual source material and documentation
* Long-term memory: durable user/world facts
* Training examples: preferred phrasing and style patterns

## Long-term memory limits

Per memory entry:

* `content`: up to `2000` chars
* `context`: up to `500` chars
* `importance`: `1..10`

Auto-memory settings:

* `autoMemoryEnabled`: on/off
* `autoMemoryInstructions`: up to `2000` chars

<Note>
  Auto-memory is selective, not guaranteed on every turn. The system saves when
  it detects durable information worth retaining.
</Note>

## Knowledge entry limits

Per entry:

* `title`: up to `100` chars
* `content`: up to `8000` chars
* `category`: up to `50` chars
* `importance`: `1..10`

Per verb:

* Maximum knowledge entries: `50`

## Training data limits

Per example:

* `input`: up to `500` chars
* `expected`: up to `2000` chars
* Optional keywords: used for relevance matching

When a user message matches example keywords, those examples are prioritized in
prompt construction.

## URL scraping into knowledge

The knowledge page can scrape a URL and generate a draft entry.

Expected result:

* `title`
* `content`
* `category`

If AI structuring fails, Verba still attempts a basic extraction fallback so you
can edit and save manually.

## Session memory by surface

| Surface           | Memory keying behavior                   |
| ----------------- | ---------------------------------------- |
| Public API v1     | Uses `session_id` per caller + character |
| Discord DM        | Scoped to user-DM context                |
| Discord server    | Scoped to server context                 |
| App group/DM chat | Scoped to group/DM conversation          |

## What to store where

### Put this in long-term memory

* Stable personal preferences
* Ongoing commitments
* Persistent roleplay relationships

### Put this in knowledge entries

* Product facts and policies
* Rulebooks
* Canon lore
* Documentation snippets you want the bot to cite reliably

### Put this in training examples

* Desired phrasing style
* Tone and boundary examples
* Repeated Q/A patterns

## Common mistakes

<AccordionGroup>
  <Accordion title="Dumping full chats into memory">
    Store compact facts, not raw transcripts. Long noisy entries reduce retrieval quality.
  </Accordion>

  <Accordion title="Using knowledge for temporary plans">
    Time-sensitive details belong in conversation context, not permanent knowledge.
  </Accordion>

  <Accordion title="No keywords in training examples">
    Add targeted keywords so examples are picked when users ask matching questions.
  </Accordion>

  <Accordion title="Oversized auto-memory instructions">
    Keep instructions strict and concise. Long broad prompts increase noisy memory writes.
  </Accordion>
</AccordionGroup>

<CardGroup>
  <Card title="AI Engine Settings" icon="sliders" href="/guides/ai-engine">
    Tune model context, creativity, and response behavior.
  </Card>

  <Card title="Bot Settings Reference" icon="book" href="/guides/bot-settings-reference">
    Field-by-field guide for all dashboard settings and limits.
  </Card>
</CardGroup>

# Content moderation

Source: https://docs.verba.ink/guides/moderation

Keep your community safe with automated checks.

## Why this exists

Moderation helps keep communities safe. It blocks harmful content while staying
permissive for normal creative use.

## What gets checked

<CardGroup>
  <Card title="Profile images" icon="image">
    Avatars and banners are scanned before they go live.
  </Card>

  <Card title="Character content" icon="file">
    Personality text is checked for unsafe themes.
  </Card>
</CardGroup>

## If something gets blocked

* Read the error message.
* Tweak the content.
* Try again with a simpler version.

<Note>
  We would rather let safe content through than block good work by mistake.
</Note>

# Notifications and privacy

Source: https://docs.verba.ink/guides/notifications-and-privacy

Control what is public and what stays private.

## Visibility settings

* **Public**: others can discover your verb.
* **Private**: only you can access it.

## Notifications

Stay in the loop without getting spammed.

* Enable alerts for mentions and replies.
* Use browser notifications only if you want real time pings.
* Mute a chat when you are focused on creation.

<Info>
  If you run into unexpected alerts, check notification settings first.
</Info>

<Card title="Community" icon="users" href="/guides/community">
  See where people share and support each other.
</Card>

# Personality playbook

Source: https://docs.verba.ink/guides/personality-playbook

Make your verb sound consistent and alive.

## Start with a simple core

Pick 3 to 5 traits and write them like bullet points. Keep it short and clear.
Then expand with examples. You can always add depth later.

<Info>
  Great personalities are specific. "Helpful" is fine. "Helpful with dry
  humor" is better.
</Info>

## Write with examples

Give the model samples of how the verb should respond. Short examples are
perfect.

```txt theme={null}
User: Can you explain this like I am five?
Verb: Sure. Think of it like building with blocks...
```

## Balance tone and boundaries

* If the verb is playful, say where it should still be serious.
* If the verb is sarcastic, say when to avoid it.
* If the verb is formal, say when it can relax.

<AccordionGroup>
  <Accordion title="Do this">
    - Use concrete behaviors.
    - Add phrases the verb loves to use.
    - Describe how it reacts when confused.
  </Accordion>

  <Accordion title="Avoid this">
    * Contradicting traits.
    * Huge walls of text with no examples.
    * Instructions that fight the system prompt.
  </Accordion>
</AccordionGroup>

## Keep it consistent

If the voice feels off, reduce complexity before adding more. A tight core
beats a giant block of lore every time.

<Card title="AI engine" icon="sliders" href="/guides/ai-engine">
  Tune creativity after the personality feels stable.
</Card>

# Plans and limits

Source: https://docs.verba.ink/guides/plans-and-limits

Complete plan matrix for premium features, usage limits, and API behavior.

## Premium quick answers

* API access is available on all plans (`/v1/response`, `/v1/image`).
* Full matrix (`verbs/msg-min/context/max-tokens`): Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768`.
* Free: `5` verbs, `20` msg/min, `50` context, `4096` max tokens.
* Plus: `10` verbs, `40` msg/min, `75` context, `8192` max tokens.
* Pro: `20` verbs, `100` msg/min, `100` context, `16384` max tokens.
* Ultra: `40` verbs, unlimited msg/min, `150` context, `32768` max tokens.
* Streaming (`stream: true`) is available on Plus/Pro/Ultra.

## Plan tiers

Verba currently supports four tiers:

* `free`
* `plus`
* `pro`
* `ultra`

Quick reference (context/tokens):

* Free: `50` / `4096`
* Plus: `75` / `8192`
* Pro: `100` / `16384`
* Ultra: `150` / `32768`

## Feature matrix

| Feature                                            | Free      | Plus        | Pro               | Ultra                     |
| -------------------------------------------------- | --------- | ----------- | ----------------- | ------------------------- |
| Monthly credit allowance                           | `0`       | `2.5`       | `5`               | `10`                      |
| Max verbs                                          | `5`       | `10`        | `20`              | `40`                      |
| Message rate limit (per minute)                    | `20`      | `40`        | `100`             | `Unlimited`               |
| Max model context                                  | `50`      | `75`        | `100`             | `150`                     |
| Max response tokens                                | `4096`    | `8192`      | `16384`           | `32768`                   |
| API access (`/v1/response`, `/v1/image`)           | Yes       | Yes         | Yes               | Yes                       |
| API streaming (`/v1/response` with `stream: true`) | No        | Yes         | Yes               | Yes                       |
| Default model tier access                          | Free      | Free + Plus | Free + Plus + Pro | Free + Plus + Pro + Ultra |
| Watermark removal                                  | No        | Yes         | Yes               | Yes                       |
| Advanced AI flag                                   | No        | No          | Yes               | Yes                       |
| Early feature access                               | No        | Yes         | Yes               | Yes                       |
| VIP support                                        | No        | No          | No                | Yes                       |
| Image generations per month                        | Unlimited | Unlimited   | Unlimited         | Unlimited                 |

<Note>
  These values are enforced by backend tier feature controls and can be updated
  over time.
</Note>

## What each limit changes

* `Max verbs`: how many verbs you can create on your account.
* `Message rate limit`: per-user server-side throttle window.
* `Max model context`: max recent-message window your verb can use.
* `Max response tokens`: cap for generated response length.
* `Monthly credit allowance`: recurring included credit amount tied to tier.

## Behavior when you exceed limits

* Verb creation over your tier cap is rejected.
* Model context above your cap is clamped or rejected depending on endpoint.
* Free tier streaming requests return a plan-upgrade error.
* Message bursts above tier limits return rate-limit responses.

## Model access and tiering

Model availability is tier-controlled. If a selected model is not available for
your current tier, the system may remap/fallback to an allowed model.

## Patreon and plan sync

Premium tier is synced from Patreon membership data. On tier changes:

* Your account tier is updated.
* Model access can be adjusted.
* Monthly allowance logic follows tier/cycle rules.

If you unlink Patreon while a premium subscription is active, disconnection may
be blocked for account safety/billing consistency.

## Related guides

* [Credits and billing](/guides/credits)
* [Billing and refunds](/guides/billing-and-refunds)
* [AI engine settings](/guides/ai-engine)
* [Troubleshooting](/guides/troubleshooting)

# Plans quick reference

Source: https://docs.verba.ink/guides/plans-quick-reference

One-line tier matrix for verbs, message rate, context, and max tokens.

## One-line matrix

Format: `verbs/msg-min/context/max-tokens`

* Free: `5/20/50/4096`
* Plus: `10/40/75/8192`
* Pro: `20/100/100/16384`
* Ultra: `40/unlimited/150/32768`

## Expanded matrix

| Plan  | Verbs | Message rate  | Context | Max tokens |
| ----- | ----- | ------------- | ------- | ---------- |
| Free  | `5`   | `20 msg/min`  | `50`    | `4096`     |
| Plus  | `10`  | `40 msg/min`  | `75`    | `8192`     |
| Pro   | `20`  | `100 msg/min` | `100`   | `16384`    |
| Ultra | `40`  | `Unlimited`   | `150`   | `32768`    |

## Notes

* API access is available on all plans.
* Streaming (`stream: true`) is available on Plus/Pro/Ultra.

## Related

* [Plans and limits](/guides/plans-and-limits)
* [Credits and billing](/guides/credits)

# Question bank

Source: https://docs.verba.ink/guides/question-bank

Large question-driven reference generated from backend routes and frontend settings flows.

## About this page

This page is a high-volume Q\&A index built from real product behavior in the
backend and frontend codepaths.

Use it when users ask operational questions and you need fast, practical
answers.

## Quick high-signal answers

* API flow: create API key -> call `POST /v1/response` -> reuse returned `session_id` for follow-ups.
* System instructions: set in Dashboard -> Bot -> AI Engine -> Behavior (`systemInstructions`, max `8000` chars).
* `/v1/response` auth: `Authorization: Bearer vka_...` or `x-api-key: vka_...`.
* Session memory: reuse `session_id` for follow-up calls.
* Plan limits (context/tokens): Free `50/4096`, Plus `75/8192`, Pro `100/16384`, Ultra `150/32768`.
* Plan full matrix (`verbs/msg-min/context/max-tokens`): Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768`.

## API questions

<AccordionGroup>
  <Accordion title="How does the API work?">
    Create an API key, call `POST /v1/response` with `character` + `messages`, then reuse the returned `session_id` to keep conversation memory. Use `stream: true` for SSE on Plus/Pro/Ultra.
  </Accordion>

  <Accordion title="How do I authenticate requests to api.verba.ink?">
    Send `Authorization: Bearer vka_...` or `x-api-key: vka_...`.
  </Accordion>

  <Accordion title="How do I call the text endpoint?">
    Use `POST /v1/response` with `character` and `messages`.
  </Accordion>

  <Accordion title="How do I call /v1/response with API key auth and session memory?">
    Use `Authorization: Bearer vka_...` (or `x-api-key`), send `character` + `messages`, and reuse `session_id` across calls. If omitted on first call, API returns a generated `session_id` you can keep using.
  </Accordion>

  <Accordion title="How do I generate images through API?">
    Use `POST /v1/image` with `character` and `prompt`.
  </Accordion>

  <Accordion title="What value goes in character?">
    A vanity slug/path/URL (for example `/v/my_slug`).
  </Accordion>

  <Accordion title="Does API support streaming?">
    Yes, `/v1/response` supports SSE when `stream: true`.
  </Accordion>

  <Accordion title="Why does streaming return forbidden?">
    Streaming is plan-gated; free tier requests can return upgrade-required errors.
  </Accordion>

  <Accordion title="Does API keep session memory?">
    Yes, reuse `session_id` to continue context.
  </Accordion>

  <Accordion title="Can I pass system role messages?">
    No, system role is blocked on `/v1/response`.
  </Accordion>

  <Accordion title="Can I send images in /v1/response?">
    Yes, via `messages[].content` image parts or top-level `image_urls`.
  </Accordion>

  <Accordion title="How many image URLs can I attach?">
    Up to 4 combined per request.
  </Accordion>

  <Accordion title="Can I use tools/function calls?">
    Yes, request-scoped HTTP tools are supported with validation and limits.
  </Accordion>

  <Accordion title="What are /v1/response hard payload limits?">
    `messages`: max `60`; each message text max `4000` chars; total text max `20000` chars; combined `image_urls` max `4`; `session_id` max `128` chars; tools max `8` definitions and `2` executed calls per request.
  </Accordion>

  <Accordion title="How many API keys can I keep active?">
    Up to `3` active API keys per account.
  </Accordion>

  <Accordion title="Why do I get payload too large errors?">
    Request bodies have size guards; oversized JSON payloads are rejected.
  </Accordion>
</AccordionGroup>

## Plans and limits questions

<AccordionGroup>
  <Accordion title="What are Free/Plus/Pro/Ultra limits for context, max tokens, verbs, and message rate?">
    Free `5/20/50/4096`, Plus `10/40/75/8192`, Pro `20/100/100/16384`, Ultra `40/unlimited/150/32768` (format: verbs/msg-min/context/max-tokens).
  </Accordion>

  <Accordion title="What are max model context and max response tokens by plan?">
    Free: `50` context, `4096` max tokens. Plus: `75`, `8192`. Pro: `100`, `16384`. Ultra: `150`, `32768`.
  </Accordion>

  <Accordion title="Which plans support streaming on /v1/response?">
    Plus, Pro, and Ultra support `stream: true`. Free does not.
  </Accordion>

  <Accordion title="How many verbs can I create per plan?">
    Free `5`, Plus `10`, Pro `20`, Ultra `40`.
  </Accordion>
</AccordionGroup>

## Discord questions

<AccordionGroup>
  <Accordion title="Why does my bot connect but not respond?">
    Most often missing intents, wrong routing mode, or command/channel permission issues.
  </Accordion>

  <Accordion title="How do I make it respond without pinging in one channel?">
    Use `/activate-channel` there.
  </Accordion>

  <Accordion title="How do I stop auto-replies in that channel?">
    Use `/remove-channel`.
  </Accordion>

  <Accordion title="Can the bot reply to other bots?">
    Default behavior ignores bot-authored messages.
  </Accordion>

  <Accordion title="Why does /reset fail for regular members in a server?">
    Server reset requires elevated permissions.
  </Accordion>

  <Accordion title="Does /reset work in DMs?">
    Yes, DM reset is user-scoped.
  </Accordion>

  <Accordion title="Why does /generate fail?">
    Image generation may be disabled, prompt invalid, or provider temporarily unavailable.
  </Accordion>

  <Accordion title="Why does 'The application did not respond' appear?">
    Usually command timeout or permission/runtime failure.
  </Accordion>

  <Accordion title="Can I hide/disable specific slash commands?">
    Yes, via command toggles in Discord module settings.
  </Accordion>

  <Accordion title="Can I update bot status/presence from dashboard?">
    Yes, status type/text/presence are configurable.
  </Accordion>

  <Accordion title="How do I remove bot from a specific server?">
    Use the server list in Discord module and leave server action.
  </Accordion>

  <Accordion title="Why do only some pings get a reply when many bots are tagged?">
    Multi-bot mention handling intentionally limits responding bots for stability.
  </Accordion>
</AccordionGroup>

## Memory, knowledge, and training questions

<AccordionGroup>
  <Accordion title="How do system instructions work?">
    System instructions are persistent behavior rules for the verb. They define response policy and format, while knowledge/memory provide facts and training examples shape style.
  </Accordion>

  <Accordion title="Where do I set system instructions and what is the limit?">
    Set them in Dashboard -> Bot -> AI Engine -> Behavior (`systemInstructions`). Max length is `8000` characters.
  </Accordion>

  <Accordion title="How many knowledge entries can I store?">
    Up to 50 per verb.
  </Accordion>

  <Accordion title="How do I add docs quickly from a URL?">
    Use knowledge URL scrape to draft title/content/category.
  </Accordion>

  <Accordion title="What if URL scrape gives poor output?">
    Manually edit the draft entry and tighten structure before saving.
  </Accordion>

  <Accordion title="What is auto memory?">
    Optional automatic saving of durable facts from conversation history.
  </Accordion>

  <Accordion title="What should auto-memory instructions include?">
    Durable facts to keep; explicit exclusions for temporary/noisy details.
  </Accordion>

  <Accordion title="Why does my bot ignore training examples?">
    Add keywords and ensure examples match real user phrasing.
  </Accordion>

  <Accordion title="Can knowledge and memory conflict?">
    Yes. Keep one canonical source and remove outdated entries.
  </Accordion>

  <Accordion title="How does context size affect memory quality?">
    Larger context keeps recent flow better but costs more and can add noise.
  </Accordion>

  <Accordion title="Do memory entries have importance levels?">
    Yes, entries use importance scoring.
  </Accordion>

  <Accordion title="Should I store full transcripts in memory?">
    No. Store compact facts and reusable rules.
  </Accordion>
</AccordionGroup>

## Chat, groups, and realtime questions

<AccordionGroup>
  <Accordion title="How many groups can one user own?">
    Up to 15 owned groups.
  </Accordion>

  <Accordion title="Why did my message get blocked in group chat?">
    Anti-spam filters can block mention floods and invisible-character abuse.
  </Accordion>

  <Accordion title="What is the message history page size?">
    Default 50, capped at 200 per request.
  </Accordion>

  <Accordion title="Can I DM a private verb I do not own?">
    No, private verbs are owner-only.
  </Accordion>

  <Accordion title="Why are updates instant across tabs?">
    WebSocket subscriptions broadcast message/typing/update events in real time.
  </Accordion>

  <Accordion title="Can owner leave their own group?">
    No, owner must transfer ownership or delete the group.
  </Accordion>

  <Accordion title="Who can add/remove verbs in groups?">
    Group owner only.
  </Accordion>

  <Accordion title="Are message image uploads limited?">
    Yes, chat message image upload path is capped to small file sizes (5MB class limits).
  </Accordion>
</AccordionGroup>

## Account, billing, and security questions

<AccordionGroup>
  <Accordion title="How many active API keys can I keep?">
    Up to 3 active keys.
  </Accordion>

  <Accordion title="Do revoked API keys keep working?">
    No, revocation is immediate.
  </Accordion>

  <Accordion title="How long does a magic link stay valid?">
    20 minutes.
  </Accordion>

  <Accordion title="Can I sign in with backup code for 2FA?">
    Yes. Backup codes are one-time use.
  </Accordion>

  <Accordion title="Can I disconnect Patreon anytime?">
    Active paid subscription linkage can block disconnect.
  </Accordion>

  <Accordion title="Why is a model missing in settings?">
    Tier gating: available model set depends on plan.
  </Accordion>

  <Accordion title="Why do requests fail with insufficient credits?">
    Credits are exhausted for the account/owner being billed for that request.
  </Accordion>

  <Accordion title="What happens when I delete my account?">
    Related entities and associations are cleaned up; some owned resources may transfer or be removed.
  </Accordion>
</AccordionGroup>

<CardGroup>
  <Card title="Bot Settings Reference" icon="book" href="/guides/bot-settings-reference">
    Full limits and field behavior for dashboard configuration.
  </Card>

  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Operational fix guide for the most common failures.
  </Card>
</CardGroup>

# System instructions

Source: https://docs.verba.ink/guides/system-instructions

How system instructions work, where to set them, limits, and how they interact with memory/knowledge/training.

## What system instructions are

System instructions are the verb's persistent behavior rules.

Quick facts:

* Set in Dashboard -> Bot -> AI Engine -> Behavior
* Field name: `systemInstructions`
* Limit: `8000` characters

They should define:

* how the verb should behave
* response format and tone constraints
* uncertainty policy (what to do when information is missing)
* boundaries and refusal style

They should not be used as a dump for raw documentation or long transcripts.

## Interaction with other configuration layers

| Layer                | What it should contain                            |
| -------------------- | ------------------------------------------------- |
| `systemInstructions` | Behavior rules and output formatting policy       |
| Training examples    | Input/output style patterns and phrasing examples |
| Long-term memory     | Durable facts/preferences from conversation       |
| Knowledge entries    | Structured factual/reference information          |
| Conversation context | Recent turns from active chat/thread/session      |

## Practical precedence model

Use this order for authoring:

1. Put behavior policy in system instructions.
2. Put canonical facts in knowledge entries.
3. Put durable user/world facts in long-term memory.
4. Use training examples for style and recurring patterns.

If these layers conflict, clean up older memory/knowledge entries and keep one
canonical source of truth.

## Best-practice template

```text theme={null}
Role:
- You are Verba Documentation Assistant.

Behavior:
- Be factual and concise.
- Do not speculate.

Output format:
- Start with a direct answer.
- Then provide short sections with bullets.
- Include numbered steps for procedures.

Uncertainty:
- If docs context is insufficient, say what is missing and ask for the exact page/topic.
```

## Common mistakes

<AccordionGroup>
  <Accordion title="Putting factual docs only in system instructions">
    Put facts in knowledge entries; keep system instructions focused on behavior policy.
  </Accordion>

  <Accordion title="Conflicting rules">
    Avoid mixing contradictory rules like "be very short" and "be extremely detailed" in the same instruction set.
  </Accordion>

  <Accordion title="No uncertainty policy">
    Include explicit fallback behavior for missing info to reduce hallucinations.
  </Accordion>

  <Accordion title="Overlong and vague instructions">
    Keep instructions concrete and testable; split long policy into clear bullets.
  </Accordion>
</AccordionGroup>

## Related guides

* [AI engine settings](/guides/ai-engine)
* [Memory and knowledge](/guides/memory-and-knowledge)
* [Bot settings reference](/guides/bot-settings-reference)

# Troubleshooting

Source: https://docs.verba.ink/guides/troubleshooting

Fix common Verba issues fast with concrete checks and recovery steps.

## Fast triage checklist

1. Confirm you are logged into the correct account/workspace.
2. Hard refresh the page and retry once.
3. Check plan limits (context, tokens, credits, model availability).
4. Confirm your verb settings were actually saved.
5. Test with a minimal prompt in a clean chat/thread.

## Discord issues

<AccordionGroup>
  <Accordion title="Connection failed while linking Discord token">
    Verify token format, ensure the token is not already linked to another verb, and retry after a short delay if Discord is rate limiting requests.
  </Accordion>

  <Accordion title="The application did not respond">
    This usually means command timeout, missing channel permission, or a disabled slash command. Check command toggles and bot permissions in that server/channel.
  </Accordion>

  <Accordion title="Bot only responds sometimes">
    In servers, bot response depends on routing: mention, AI channel, or keyword match. If none of those apply, no response is expected.
  </Accordion>

  <Accordion title="Bot replies in wrong places or too often">
    Remove AI channels with `/remove-channel` and keep mention-only behavior in shared channels.
  </Accordion>

  <Accordion title="/reset fails in server but works in DM">
    Server reset requires admin/server-owner/bot-owner level permission. DM reset is user scoped.
  </Accordion>
</AccordionGroup>

## Response quality issues

<AccordionGroup>
  <Accordion title="Replies are too short">
    Increase max tokens and use a fuller reply style. Also check whether your current plan caps output lower than expected.
  </Accordion>

  <Accordion title="Replies are too generic">
    Tighten system instructions, add focused training examples, and lower temperature.
  </Accordion>

  <Accordion title="Bot forgets earlier messages">
    Increase model context (within plan cap) and avoid splitting related topics across many disconnected chats.
  </Accordion>

  <Accordion title="Bot misses known docs/knowledge">
    Add or refine knowledge entries, improve titles/categories, and verify entries are active. For URL imports, scrape again and clean the generated draft.
  </Accordion>

  <Accordion title="Web search feels noisy or irrelevant">
    Disable web search for stable topics. Keep it for fresh/live data only.
  </Accordion>
</AccordionGroup>

## Performance and timeout issues

<AccordionGroup>
  <Accordion title="Responses are slow">
    Reduce context, disable web search, and test a lighter model. Long prompts + web search + high max tokens significantly increase latency.
  </Accordion>

  <Accordion title="Intermittent provider failures">
    Retries/backoff are built into the call path, but upstream outages still happen. Retry shortly and keep fallback models available in your plan tier.
  </Accordion>

  <Accordion title="Image generation fails randomly">
    Provider capacity spikes can cause temporary errors. Retry with a shorter prompt and no reference image first.
  </Accordion>
</AccordionGroup>

## Account and billing issues

<AccordionGroup>
  <Accordion title="Insufficient credits error">
    Top up credits or switch to a lower-cost model. Credits are charged to the account tied to the request/verb owner depending on surface.
  </Accordion>

  <Accordion title="Model not selectable">
    Your plan may not include that model tier. Choose an available model or upgrade.
  </Accordion>

  <Accordion title="API key works in dashboard but fails in API calls">
    Check header format (`Authorization: Bearer vka_...` or `x-api-key`), key revocation status, and whether you exceeded active key limits.
  </Accordion>
</AccordionGroup>

## Chat and group issues

<AccordionGroup>
  <Accordion title="Message send blocked">
    Anti-spam protections can block mention floods and invisible-character abuse. Remove unusual hidden characters and retry.
  </Accordion>

  <Accordion title="Uploads fail">
    Ensure the file is an image and under limit for that surface (for chat message uploads, 5MB max).
  </Accordion>

  <Accordion title="Group invite problems">
    Verify invite code freshness and that owner has not regenerated it recently.
  </Accordion>
</AccordionGroup>

## When to contact support

Contact support with:

* Exact timestamp (with timezone)
* Verb ID/vanity URL
* Surface (`Discord`, `chat`, `API`)
* Error text + screenshot
* Repro steps from clean session

<CardGroup>
  <Card title="Contact Support" icon="envelope" href="https://verba.ink/contact">
    Share reproducible steps and timestamps for fastest resolution.
  </Card>

  <Card title="Community" icon="users" href="https://discord.gg/verba">
    Ask in community channels for quick operational help.
  </Card>
</CardGroup>

# Visual identity

Source: https://docs.verba.ink/guides/visual-identity

Avatars, banners, and a look that sticks.

## Choose a clear avatar

Your avatar shows up everywhere, so it needs to read at a tiny size. Keep it
simple, centered, and high contrast.

* Use a single subject.
* Avoid busy backgrounds.
* Keep faces or icons near the center.

## Make the banner support the avatar

Banners are wide, so use them for mood. Think background texture, environment,
or a simple pattern that matches the character.

<Info>
  If the avatar is bright, keep the banner calm. If the avatar is subtle, make
  the banner pop.
</Info>

## Tips for a clean look

* Stick to one color palette.
* Avoid text inside the image.
* Test on mobile and desktop.

<Card title="Content moderation" icon="shield" href="/guides/moderation">
  Learn what gets flagged before upload.
</Card>

# Voice and audio

Source: https://docs.verba.ink/guides/voice-and-audio

Give your verb a voice that fits the vibe.

## Voice replies

Voice is optional and can be enabled per verb. Start with text only, then add
voice once the personality feels right.

## Voice cloning

Upload a short, clean sample to create a custom voice. The best results come
from 6 to 12 seconds of clear speech with minimal background noise.

Reference text is optional. If you can, paste the exact transcript of the
sample. It improves similarity and keeps the voice more stable across replies.

## Supported languages

The voice engine supports a focused language set:

* Auto (recommended default)
* English
* Chinese
* Japanese
* Korean
* German
* French
* Russian
* Portuguese
* Spanish
* Italian

If you pick a language outside this list, the engine falls back to Auto.

## Keep it natural

* Short replies sound better.
* Avoid long paragraphs in voice mode.
* Set a frequency that feels human.

<Tip>
  If the voice feels off, lower reply length and reduce random creativity.
</Tip>

## Safety and permissions

Only upload audio you own or have permission to use.

<Card title="AI engine" icon="sliders" href="/guides/ai-engine">
  Lower temperature for clearer voice output.
</Card>

# Web search

Source: https://docs.verba.ink/guides/web-search

When to turn it on and when to keep it off.

## What web search does

Web search lets your verb pull in fresh info when it is needed. It is great for
news, live data, and things that change fast.

## When to use it

* Current events
* Policies or pricing that change often
* Fresh releases or updates

## When to skip it

* Roleplay or storytelling
* Static lore and worldbuilding
* Anything that should stay consistent

<Note>
  Web search can cost more and slow replies. Use it only when freshness matters.
</Note>

## Troubleshooting

If results feel noisy, turn web search off and reduce temperature.

<Card title="AI engine" icon="sliders" href="/guides/ai-engine">
  Get the tuning knobs right first.
</Card>

# Welcome to Verba

Source: https://docs.verba.ink/index

Create, deploy, and manage AI verbs with a guided workflow.

## Start here

New to Verba? These pages get you moving fast.

<CardGroup>
  <Card title="Quickstart" icon="rocket" href="/quickstart">
    From signup to a working verb in minutes.
  </Card>

  <Card title="Getting around" icon="map" href="/guides/getting-around">
    A quick tour of the dashboard and tools.
  </Card>

  <Card title="Your first verb" icon="user" href="/guides/first-verb">
    Build a personality, add visuals, and test the voice.
  </Card>

  <Card title="Personality playbook" icon="star" href="/guides/personality-playbook">
    Make your verb feel consistent and real.
  </Card>
</CardGroup>

## Make it yours

These settings shape how your verb looks and behaves.

<CardGroup>
  <Card title="Visual identity" icon="image" href="/guides/visual-identity">
    Avatars, banners, and a clean style.
  </Card>

  <Card title="AI engine" icon="sliders" href="/guides/ai-engine">
    Tune creativity, context, and cost.
  </Card>

  <Card title="Memory and knowledge" icon="book" href="/guides/memory-and-knowledge">
    Keep your verb consistent over time.
  </Card>

  <Card title="Web search" icon="globe" href="/guides/web-search">
    Use fresh info only when it matters.
  </Card>
</CardGroup>

## Chat and community

Test fast and learn from other creators.

<CardGroup>
  <Card title="Chat and groups" icon="comments" href="/guides/chat-and-groups">
    Run conversations and group rooms.
  </Card>

  <Card title="Community" icon="users" href="/guides/community">
    Join the Discord and share your work.
  </Card>

  <Card title="Image generation" icon="image" href="/guides/image-generation">
    Let your verb create visuals on demand.
  </Card>

  <Card title="Voice and audio" icon="microphone" href="/guides/voice-and-audio">
    Add voice once the personality feels right.
  </Card>
</CardGroup>

## Safety, billing, and help

When something feels off, this is where you go.

<CardGroup>
  <Card title="Moderation" icon="shield" href="/guides/moderation">
    Learn how content checks work.
  </Card>

  <Card title="Billing and refunds" icon="credit-card" href="/guides/billing-and-refunds">
    Credits, purchases, and what to do if something looks wrong.
  </Card>

  <Card title="Best practices" icon="check" href="/guides/best-practices">
    Small habits that improve quality fast.
  </Card>

  <Card title="Troubleshooting" icon="life-ring" href="/guides/troubleshooting">
    Quick fixes for common issues.
  </Card>
</CardGroup>

# Quickstart

Source: https://docs.verba.ink/quickstart

Launch a working verb in minutes.

## Get set in three steps

<Steps>
  <Step title="Create your account">
    Sign up at verba.ink, then open the dashboard. That is where all your verbs
    live.
  </Step>

  <Step title="Build the basics">
    Give your verb a name, a short description, and a few tags. Add an avatar
    if you have one, but do not overthink it yet.
  </Step>

  <Step title="Test in chat">
    Open a chat, send a few prompts, and see how it sounds. Adjust personality
    or AI engine settings until it feels right.
  </Step>
</Steps>

<Tip>
  Keep your first test prompts short. You will learn more in three tiny chats
  than in one giant paragraph.
</Tip>

## What to do next

<CardGroup>
  <Card title="Getting around" icon="map" href="/guides/getting-around">
    Learn where everything lives in the app.
  </Card>

  <Card title="Your first verb" icon="user" href="/guides/first-verb">
    Go deeper on personality and settings.
  </Card>

  <Card title="AI engine" icon="sliders" href="/guides/ai-engine">
    Tune creativity and cost.
  </Card>

  <Card title="Visual identity" icon="image" href="/guides/visual-identity">
    Add an avatar and banner that match the vibe.
  </Card>
</CardGroup>
