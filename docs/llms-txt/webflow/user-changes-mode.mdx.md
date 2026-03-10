# Source: https://developers.webflow.com/designer/reference/user-changes-mode.mdx

***

title: User changes Designer mode
slug: designer/reference/user-changes-mode
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get Designer capabilities'
'og:description': Determine if the user has a specified list of App abilities.
------------------------------------------------------------------------------

## `webflow.subscribe("currentappmode", callback)`

Subscribe to this event to detect when a user switches modes in the Designer, such as changing to Edit mode or selecting a secondary locale. This event helps you track the user's current mode, allowing your app to adjust the UI or display relevant error messages based on the available actions.

Tracking mode changes ensures your app provides the right experience at the right time, managing user expectations and preventing actions that aren’t allowed in the current mode.

<Info title="What are App Modes?">
  Designer Extensions enhance user functionality while adhering to the Designer's current mode. Each method within the Designer API provides specific capabilities, aligning with actions available in each mode. For more context on this API, see the [App Modes](https://developers.webflow.com/designer/reference/app-modes) docs.
</Info>

### Syntax

```typescript
webflow.subscribe(
  event: 'currrentappmode',
  callback: () => void
): Unsubscribe;
```

### Parameters

**`event`** :   `"currentappmode"`

The name of the event to subscribe to.

***

**callback**: `(() => void)`

The callback function to execute when the event occurs.

***

### Returns

#### ***`Unsubscribe`***

This is a special function returned after subscribing. Call this function when you want to stop listening to the event and discontinue receiving notifications.

### Example

```typescript
// Callback for subscription
    const checkAppModes = async () => {
      const capabilities = await webflow.canForAppMode(Object.values(webflow.appModes))
      console.log(capabilities)
    }

// Subscribe to changes for CMS Pages
 const unsubscribeAppModes = webflow.subscribe('currentappmode', checkAppModes)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
