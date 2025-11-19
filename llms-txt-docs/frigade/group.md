# Source: https://docs.frigade.com/sdk/hooks/group.md

# useGroup

The `useGroup()` hook enables you to add properties and send tracking events to the current group.

## About this hook

The hook contains the following methods:
<ParamField body="track(eventName: string, properties?: Record<string, unknown>)">Promise that sends tracking events for the current group</ParamField>
<ParamField body="addProperties(properties: Record<string, unknown>)">Promise that adds properties to the current group</ParamField>
<ParamField body="setGroupId(groupId: string, properties?: Record<string, unknown>)">Promise that sets the current group ID. Using this hook can cause unexpected behaviors if also setting the group ID at the `<Frigade.Provider />` level.</ParamField>

### Example use cases:

* Tracking events and adding properties to the current group for using with [Targeting](/platform/targeting/)
* Wrapping the `track` method with your existing tracking/analytics methods

### Example usage:

```tsx
import { useGroup } from '@frigade/react';

function MyComponent() {
  const { addProperties } = useGroup();

  return (
    <button
      onClick={() => {
        addProperties({ orgHasConnectedBankAccount: true });
      }}
    >
      Connect Bank Account
    </button>
  );
}
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>

## Standardized properties

The following standardized properties are automatically added to the group object if provided via `addProperties`:

* `name`: The name of the group/company/organiation
* `imageUrl`: The URL of the group/company/organiation's logo
