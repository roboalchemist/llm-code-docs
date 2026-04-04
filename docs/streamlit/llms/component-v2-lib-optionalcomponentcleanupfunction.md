# ComponentState

TypeScript type alias for custom components v2 state management, enabling type-safe state persistence and data flow between component renders and user interactions.

## ComponentCleanupFunction

The cleanup function returned by a Streamlit v2 Component.

This type alias isn't exported. Use `OptionalComponentCleanupFunction` instead.

This type represents the cleanup function that your component can return from its top-level `export default` function. If provided, Streamlit will call this function when your component is unmounted from the app, allowing you to perform any necessary cleanup tasks, such as removing event listeners or canceling network requests.

## Example Usage

```typescript
import { OptionalComponentCleanupFunction } from '@streamlit/component-v2-lib';

const cleanupFunction = () => void 0;

export default {
  export default {
    cleanupFunction,
  },
};
```

## Versioning

Streamlit Version

- Version 1.52.0
- Version 1.51.0
- Version 1.50.0
- Version 1.49.0
- Version 1.48.0
- Version 1.47.0
- Version 1.46.0
- Version 1.45.0
- Version 1.44.0
- Version 1.43.0
- Version 1.42.0
- Version 1.41.0
- Version 1.40.0
- Version 1.39.0
- Version 1.38.0
- Version 1.37.0
- Version 1.36.0
- Version 1.35.0
- Version 1.34.0
- Version 1.33.0
- Version 1.32.0
- Version 1.31.0
- Version 1.30.0
- Version 1.29.0
- Version 1.28.0
- Version 1.27.0
- Version 1.26.0
- Version 1.25.0
- Version 1.24.0
- Version 1.23.0
- Version 1.22.0

## Related Links

- [Previous: ComponentState](/develop/api-reference/custom-components/component-v2-lib-componentstate)
- [Next: declare_component](/develop/api-reference/custom-components/st.components.v1.declare_component)

## Forum

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.