# Source: https://braintrust.dev/docs/reference/streaming.md

# Streaming

Braintrust supports executing prompts, functions, and evaluations through the API and within the UI through the [playground](/core/playground).
Like popular LLM services, Braintrust supports streaming results using [Server-Sent Events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events).

The Braintrust SDK and UI automatically parse the SSE stream, and we have adapters for common libraries like the [Vercel AI SDK](https://sdk.vercel.ai/docs),
so you can quickly integrate with the rich and growing ecosystem of LLM tools. However, the SSE format itself is also purposefully simple, so if you need to
parse it yourself, you can!

To see more about how to use streaming data, see the [prompts documentation](/core/functions/prompts#streaming).

## Why does this exist

Streaming is a very powerful way to consume LLM outputs, but the predominant "chat" data structure produced by modern LLMs is more complex than most applications
need. In fact, the most common use cases are to (a) convert the text of the first message into a string or (b) parse the arguments of the first tool call
into a JSON object. The Braintrust SSE format is really optimized to make these use cases easy to parse, while also supporting more advanced scenarios like parallel
tools calls.

## Formal spec

SSE events consist of three fields: `id` (optional), `event` (optional), and `data`. The Braintrust SSE format always sets `event` and `data`, and never sets `id`.

The SSE events in Braintrust follow this structure:

```cpp  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
<BraintrustSSEEvent> ::= <TextDeltaEvent> | <JSONDeltaEvent> | <DoneEvent>

<TextDeltaEvent> ::=
    event: "text_delta"
    data: <JSON-encoded-string>

<JSONDeltaEvent> ::=
    event: "json_delta"
    data: <JSON-snippet>

<ErrorEvent> ::=
    event: "error"
    data: <JSON-encoded-string>

<ProgressEvent> ::=
    event: "progress"
    data: <JSON-encoded-object>

<DoneEvent> ::=
    event: "done"
    data: ""
```

### Text

A `text_delta` is a snippet of text, which is JSON-encoded. For example, you might receive:

```ansi  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
event: text_delta
data: "this is a line\nbreak"

event: text_delta
data: "with some \"nested quotes\"."

event: done
data:
```

As you process a `text_delta`, you can JSON-decode the string and display it directly.

### JSON

A `json_delta` is a snippet of JSON-encoded data, which cannot necessarily be parsed on its own.
For example:

```ansi  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
event: json_delta
data: {"name": "Cecil",

event: json_delta
data: "age": 30}

event: done
data:
```

As you process a `json_delta` events, concatenate the strings together and then parse them
as JSON at the end of the stream.

### Error

An `error` event is a JSON-encoded string that contains the error message. For example:

```ansi  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
event: error
data: "Something went wrong."

event: done
data:
```

### Progress

A `progress` event is a JSON-encoded object that contains intermediate events produced by functions
while they are executing. Each json object contains the following fields:

```json  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
{
    "id": "A span id for this event",
    "object_type": "prompt" | "tool" | "scorer" | "task",
    "format": "llm" | "code" | "global",
    "output_type": "completion" | "score" | "any",
    "name": "The name of the function or prompt",
    "event": "text_delta" | "json_delta" | "error" | "start" | "done",
    "data": "The delta or error message"
}
```

The `event` field is the type of event produced by the intermediate function call, and the
`data` field is the same as the data field in the `text_delta` and `json_delta` events.

### Start

A `start` event is a progress event with `event: "start"` and an empty string for `data`. Start is not guaranteed
to be sent and is for display purposes only.

### Done

A `done` event is a progress event with `event: "done"` and an empty string for `data`. Once a `done` event is received,
you can safely assume that the function has completed and will send no more events.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt