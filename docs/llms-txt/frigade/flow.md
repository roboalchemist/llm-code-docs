# Source: https://docs.frigade.com/sdk/js/flow.md

# Source: https://docs.frigade.com/sdk/hooks/flow.md

# Source: https://docs.frigade.com/sdk/js/flow.md

# Source: https://docs.frigade.com/sdk/hooks/flow.md

# Source: https://docs.frigade.com/sdk/js/flow.md

# Source: https://docs.frigade.com/sdk/hooks/flow.md

# Source: https://docs.frigade.com/sdk/js/flow.md

# Source: https://docs.frigade.com/sdk/hooks/flow.md

# Source: https://docs.frigade.com/sdk/js/flow.md

# Source: https://docs.frigade.com/sdk/hooks/flow.md

# useFlow

The `useFlow(<flowId>)` hook makes it easy to build headless components or manipulate the state of a Flow for an existing component.
It exports a single field, `flow`, which contains the current state of the Flow, as well as a set of methods to manipulate the Flow.
[View the Flow class docs](../js/flow) to see the available fields and methods.

## About this hook

The `useFlow` hook is especially useful if you want to build a highly custom experience with your UI and/or components. You can find some example of how to build custom Flows in our [Custom Components guide](/guides/custom).

### Example use cases:

* Building a custom onboarding progress widget for your sidebar navigation
* Building a custom Kanban-style onboarding experience
* Building a highly custom onboarding checklist interface

### Example usage:

```tsx
import { useFlow } from "@frigade/react";

function MyComponent() {
  // Replace "myFlowId" with the ID of your Flow
  const { flow } = useFlow("myFlowId");

  return (
    <div>
      <h1>{flow.title}</h1>
      <p>{flow.subtitle}</p>
      <p>Currently on step {flow.getCurrentStep().id}</p>
      <button onClick={flow.next}>Next</button>
      <button onClick={flow.back}>Previous</button>
      <button onClick={flow.reset}>Reset</button>
    </div>
  );
}
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>
