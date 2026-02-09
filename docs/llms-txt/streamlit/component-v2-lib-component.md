# Component

The Streamlit v2 Component signature.

```typescript
import { Component } from '@streamlit/component-v2-lib';
```

This type represents the function signature for the default export from your component's JavaScript or TypeScript code. This function gets called by Streamlit when your component is mounted in the frontend, and it receives all the necessary arguments to build and manage your component's UI and state.

## Arguments

- **componentArgs (ComponentArgs<TComponentState, TDataShape>)**

  The inputs and utilities provided by Streamlit to your component.

## Returns

- **OptionalComponentCleanupFunction**

  An optional cleanup function that Streamlit will call when the component is unmounted.

[Previous: component-v2-lib](/develop/api-reference/custom-components/component-v2-lib) [Next: ComponentArgs](/develop/api-reference/custom-components/component-v2-lib-componentargs)