# Source: https://docs.frigade.com/sdk/js/frigade.md

# Source: https://docs.frigade.com/sdk/hooks/frigade.md

# Source: https://docs.frigade.com/sdk/js/frigade.md

# Source: https://docs.frigade.com/sdk/hooks/frigade.md

# Source: https://docs.frigade.com/sdk/js/frigade.md

# Source: https://docs.frigade.com/sdk/hooks/frigade.md

# useFrigade

The `useFrigade()` hook exposes the underlying [Frigade JS SDK]() instance that powers the React SDK.
[View the Frigade class docs](../js/frigade) to see the available fields and methods.

## About this hook

The `useFrigade` hook can be used to access the underlying Frigade JS SDK instance and interact with it directly.
It should rarely be used as the provided [useFlow](./flow), [useUser](./user), and [useGroup](./group) hooks should be sufficient for most use cases.

### Example usage:

```tsx
import { useFrigade } from "@frigade/react";

function MyComponent() {
  const { frigade } = useFrigade();

  useEffect(() => {
  	const myHandler = (flow) => {
      console.log(`Detected change in ${flow.id}`);
    }
    frigade.onStateChange(myHandler);
    return () => {
      frigade.removeStateChangeHandler(myHandler);
    }
  }, []);
}
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>
