# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/core/trace.md

# trace

Decorator for automatic function tracing with input/output capture.

Uses the global FiddlerClient when client= is not passed. Supports async functions with proper trace isolation per task.

## Parameters

| Parameter        | Type                                             | Required | Default | Description                                        |
| ---------------- | ------------------------------------------------ | -------- | ------- | -------------------------------------------------- |
| `func`           | \`Callable                                       | None\`   | ✗       | `None`                                             |
| `name`           | \`str                                            | None\`   | ✗       | `function name`                                    |
| `as_type`        | `Literal['span', 'generation', 'chain', 'tool']` | ✗        | `span`  | Span type ('span', 'generation', 'chain', 'tool'). |
| `capture_input`  | `bool`                                           | ✗        | `True`  | Capture function arguments as input.               |
| `capture_output` | `bool`                                           | ✗        | `True`  | Capture return value as output.                    |
| `client`         | \`FiddlerClient                                  | None\`   | ✗       | `get_client()`                                     |
| `model`          | \`str                                            | None\`   | ✗       | `None`                                             |
| `user_id`        | \`str                                            | None\`   | ✗       | `None`                                             |
| `version`        | \`str                                            | None\`   | ✗       | `None`                                             |
| `system`         | \`str                                            | None\`   | ✗       | `None`                                             |

## Returns

Decorated function.

**Return type:** *Callable*
