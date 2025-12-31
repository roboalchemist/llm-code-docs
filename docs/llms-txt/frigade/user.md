# Source: https://docs.frigade.com/sdk/hooks/user.md

# useUser

The `useUser()` hook enables you to add properties and send tracking events to the current user.

## About this hook

The hook contains the following methods:
<ParamField body="track(eventName: string, properties?: Record<string, unknown>)">Promise that sends tracking events for the current user</ParamField>
<ParamField body="addProperties(properties: Record<string, unknown>)">Promise that adds properties to the current user</ParamField>

<Info>Update the `userID` in the top-level `Frigade.Provider` component to change users</Info>

## Example use cases:

* Tracking events and adding properties to the current user for using with [Targeting](/platform/targeting/)
* Wrapping the `track` method with your existing tracking/analytics methods

### Tracking events example

```tsx
import { useUser } from "@frigade/react";

function MyComponent() {
  const { track } = useUser();

  useEffect(() => {
    track("MyComponent Viewed");
  }, []);

  return <div>My Component</div>;
}
```

### Adding properties example

```tsx
import { useUser } from "@frigade/react";

function MyComponent() {
  const { addProperties } = useUser();

  useEffect(() => {
    addProperties({
      email: "test@test.com",
      firstName: "John",
      lastName: "Doe",
      imageUrl: "https://example.com/image.png",
    });
  }, []);
}
```

Properties can also be added to the `userProperties` object via the `Frigade.Provider` component:

```tsx
<Frigade.Provider 
  apiKey="YOUR_API_KEY"
  userID="1234567890"
  userProperties={{ 
    email: "test@test.com", 
    firstName: "John", 
    lastName: "Doe", 
    imageUrl: "https://example.com/image.png" 
  }}
>
  <App />
</Frigade.Provider>
```

<Tip>Make sure to call any Frigade hook within the context of `<Frigade.Provider />`</Tip>

## Standardized properties

The following standardized properties are automatically added to the user object if provided via `addProperties`:

* `email` - The user's email address
* `name` - The user's full name
* `firstName` - The user's first name
* `lastName` - The user's last name
* `imageUrl` - The user's profile image URL
