# Source: https://docs.verba.ink/guides/api-how-it-works.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.verba.ink/llms.txt
> Use this file to discover all available pages before exploring further.

# How the API works

> Direct answer to how api.verba.ink works, with minimal request flow and limits.

## Short answer

Verba API works by authenticating with your API key, selecting a character, sending chat messages to `/v1/response`, and reusing `session_id` to keep memory between calls.

## 5-step flow

1. Create an API key (`vka_...`) in Dashboard -> Settings -> Security -> API Keys.
2. Send `POST https://api.verba.ink/v1/response`.
3. Include `character` (slug/path/URL) and `messages`.
4. Read the returned response and store `session_id`.
5. Reuse that same `session_id` in future calls for ongoing context.

## Minimal request

```json  theme={null}
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

Built with [Mintlify](https://mintlify.com).
