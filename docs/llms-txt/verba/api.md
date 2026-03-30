# Source: https://docs.verba.ink/guides/api.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# Public API v1

> Use API keys to talk to characters outside Discord.

## Base URL

`https://api.verba.ink`

## How the API works (short answer)

1. Create an API key in Dashboard -> Settings -> Security -> API Keys.
2. Call `POST /v1/response` with `character` + `messages`.
3. Save the returned `session_id` and reuse it for follow-up requests.
4. Use `stream: true` for SSE streaming on Plus/Pro/Ultra plans.
5. Use `POST /v1/image` when you need image generation.

Minimal text request:

```json  theme={null}
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

```json  theme={null}
{
  "character": "mycharacter_abc",
  "messages": [
    { "role": "user", "content": "My name is Sam. Remember that." }
  ]
}
```

Response includes `session_id`:

```json  theme={null}
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

```json  theme={null}
{
  "character": "mycharacter_abc",
  "session_id": "sess_abc123",
  "messages": [
    { "role": "user", "content": "What's my name?" }
  ]
}
```

### Vision input example

```json  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

```text  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

```json  theme={null}
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

Built with [Mintlify](https://mintlify.com).
