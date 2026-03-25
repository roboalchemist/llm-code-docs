# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/is-fiddler-span.md

# is\_fiddler\_span

Check if a span belongs to Fiddler's tracer.

Verifies span ownership by checking for Fiddler's APPLICATION\_ID in resource attributes. This ensures isolation from other OpenTelemetry tracers that may be active.

## Parameters

| Parameter | Type   | Required | Default | Description |
| --------- | ------ | -------- | ------- | ----------- |
| `span`    | \`Span | None\`   | ✗       | `None`      |

## Returns

True if span is a Fiddler span, False otherwise.

**Return type:** bool
