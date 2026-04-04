# Source: https://docs.fiddler.ai/api/fiddler-langgraph-sdk/tracing/add-session-attributes.md

# add\_session\_attributes

Adds custom session-level attributes that persist across all spans in the current context.

Session attributes are key-value pairs that apply to all operations within the current execution context (thread or async coroutine). Use this to add metadata that describes the session environment, such as user information, deployment environment, or feature flags.

These attributes are stored in context variables and automatically included in all spans created during the session. They persist until the context ends or the attribute is updated with a new value.

Note: Context variables are shallow copied - modifications to mutable values (lists, dicts) are shared between contexts.

## Parameters

| Parameter | Type  | Required | Default | Description                                                                                                      |
| --------- | ----- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| `key`     | `str` | ✓        | `-`     | The attribute key to add or update. Will be formatted as 'fiddler.session.user.{key}' in the OpenTelemetry span. |
| `value`   | `str` | ✓        | `-`     | The attribute value to set.                                                                                      |

## Returns

None

**Return type:** None

## Examples

```python
from fiddler_langgraph.tracing.instrumentation import add_session_attributes

# Add user information to all spans in this session
add_session_attributes("user_id", "user_12345")
add_session_attributes("tier", "premium")

# Add deployment environment context
add_session_attributes("environment", "production")
add_session_attributes("region", "us-west-2")

# Update an existing attribute
add_session_attributes("user_id", "user_67890")  # Overwrites previous value
```
