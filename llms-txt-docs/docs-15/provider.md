# Source: https://docs.frigade.com/sdk/provider.md

# Provider

The `<Frigade.Provider />` component is the root component of the Frigade SDK. It initializes the SDK and keeps track of the user's session and state in all Frigade Flows.a

See the [Quickstart Guide](/sdk/quickstart) to see an example of how to use the Provider.

# Properties

### apiKey

**apiKey**: `string`

Your public API key from the Frigade dashboard. Do not ever use your private API key here.

***

### apiUrl

`Optional` **apiUrl**: `string`

The URL prefix of the API to use. By default, Frigade will use the production API: [https://api.frigade.com/v1/public](https://api.frigade.com/v1/public)

***

### children

`Optional` **children**: `ReactNode`

***

### css

`Optional` **css**: `Record`\<`string`, `unknown`>

Global CSS properties to attach to the :root element.

**See**

[https://emotion.sh/docs/css-prop#object-styles](https://emotion.sh/docs/css-prop#object-styles)

***

### defaultCollection

`Optional` **defaultCollection**: `boolean`

By default, Frigade.Provider will render a built-in Collection to allow no-code deploys of Announcements and other floating Components. Set this to `false` if you want to manually control the rendering of the default Collection.

***

### generateGuestId

`Optional` **generateGuestId**: `boolean`

Whether to generate a Guest ID and session if no userId is provided at render time.
If set to false, Frigade will not initialize or render any Flows until a userId is provided.
Defaults to true.

***

### groupId

`Optional` **groupId**: `string`

The group ID to use for this context (optional).

***

### groupProperties

`Optional` **groupProperties**: `PropertyPayload`

Optional group properties to attach to the groupId on initialization.

***

### navigate

`Optional` **navigate**: [`NavigateHandler`](#navigatehandler)

A function to handle navigation. By default, Frigade will use `window.open` if not provided.
[https://docs.frigade.com/v2/sdk/navigation](https://docs.frigade.com/v2/sdk/navigation)

***

### preloadImages

`Optional` **preloadImages**: `boolean`

Whether to preload images in Flows. Defaults to true.

***

### syncOnWindowUpdates

`Optional` **syncOnWindowUpdates**: `boolean`

Whether to sync state with Frigade on URL or focus change. Defaults to true.

***

### theme

`Optional` **theme**

The global theme to use across components. See docs on styling: [https://docs.frigade.com/v2/sdk/styling/theming](https://docs.frigade.com/v2/sdk/styling/theming)

***

### userId

`Optional` **userId**: `string`

The user ID of the user who is interacting with Frigade. If not provided, Frigade will generate a random guest ID and persist it in local storage.

***

### userProperties

`Optional` **userProperties**: `PropertyPayload`

Optional user properties to attach to the userId on initialization.

***

### variables

`Optional` **variables**: `Record`\<`string`, `unknown`>

Global variables to apply to all Flows, including Collections.
If the individual Collection or Flow has its own variables, the two objects will be merged, with the Flow/Collection having high priority.
Example:

```tsx
variables={{
  name: "Bobby Nerves",
  occupation: "Vocalist",
}}
```

This prop can conveniently be used to pass entire i18n objects as well, which will allow all Flows to access i18n strings as needed.

[View definition](https://github.com/FrigadeHQ/frigade-react/blob/b8996ad7/packages/react/src/components/Provider/Provider.tsx#L119)
