# Source: https://developers.webflow.com/designer/reference/user-changes-current-page.mdx

***

title: User changes current page
slug: designer/reference/user-changes-current-page
description: ''
hidden: false
'og:title': 'Webflow Designer API: User changes current page'
'og:description': >-
Use this method to start listening for specific events in your App. In this
case, we're listening for when a user selects a new page in the Designer.
-------------------------------------------------------------------------

## `webflow.subscribe("currentpage", callback)`

Use this method to start listening for specific events in your App. In this case, we're listening for when a user selects a new page in the Designer.

### Syntax

```typescript
 webflow.subscribe(
  event: 'currentpage',
  callback: (element: null | AnyElement) => void
): Unsubscribe;
```

### Parameters

**`event`** :   `"currentpage"`

The name of the event to subscribe to.

***

**callback**: `(page: Page => void)`

The callback function to execute when the event occurs. The page parameter should be the page you're watching.

***

### Returns

#### ***`Unsubscribe`***

This is a special function you receive after subscribing. When you no longer want to listen to the event, call this function to stop receiving notifications.

### Example

```typescript
// Subscribe to changes in the selected page
const selectedPageCallback = (page: Page | null) => {
  if (page) {
    console.log('Selected Page:', page);
  } else {
    console.log('No element is currently selected.');
  }
}

const unsubscribeSelectedElement = webflow.subscribe('currentpage', selectedPageCallback);
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
