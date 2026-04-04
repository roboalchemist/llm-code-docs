# Source: https://docs.fiddler.ai/api/fiddler-strands-agents-sdk/fiddler-span-processor.md

# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/fiddler-span-processor.md

# FiddlerSpanProcessor

Span processor that automatically propagates attributes from parent to child spans.

## DENORMALIZED\_ATTRIBUTES

**Type:** `ClassVar[list[str]]`

**Values:**

* `'gen_ai.agent.name'`
* `'gen_ai.agent.id'`
* `'gen_ai.conversation.id'`
* `'session.id'`
* `'user.id'`

## on\_start()

Called when a span starts. Automatically propagates attributes from parent.

## Parameters

| Parameter        | Type      | Required | Default | Description            |
| ---------------- | --------- | -------- | ------- | ---------------------- |
| `span`           | `Span`    | ✗        | `None`  | The span being started |
| `parent_context` | \`Context | None\`   | ✗       | `None`                 |
