# ComponentState

The base interface for defining a Streamlit custom component's state shape.

```typescript
import { ComponentState } from '@streamlit/component-v2-lib';
```

Component state is a persistent key-value store of state and trigger values. You can extend this type or define your own interface to add type-safe state and trigger key-value pairs. Each key corresponds to an `on_<key>_change` callback parameter in Python.

## Type Aliases

| Type | Description |
| --- | --- |
| `ComponentState = Record<string, unknown>` | The base interface for defining a Streamlit custom component's state shape. |

## Notes

Streamlit Version

## Version

Streamlit Version

## Links

- [Previous: ComponentArgs](/develop/api-reference/custom-components/component-v2-lib-componentargs)
- [Next: OptionalComponentCleanupFunction](/develop/api-reference/custom-components/component-v2-lib-optionalcomponentcleanupfunction)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.

## Footer

© 2025 Snowflake Inc.