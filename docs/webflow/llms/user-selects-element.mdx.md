# Source: https://developers.webflow.com/designer/reference/user-selects-element.mdx

***

title: User selects element
slug: designer/reference/user-selects-element
description: ''
hidden: false
'og:title': 'Webflow Designer API: User selects element'
'og:description': >-
User Event. Use this method to start listening for specific events in your
App. In this case, we're listening for when a user selects an element on a
page.
-----

## `subscribe("selectedelement", callback)`

Use this method to start listening for specific events in your App. In this case, we're listening for when a user selects an element on a page.

### Syntax

```typescript
 webflow.subscribe(
  event: 'selectedelement',
  callback: (element: null | AnyElement) => void
): Unsubscribe;
```

### Parameters

**`event`** :   `"selectedlement"`

The name of the event to subscribe to.

***

**callback**:  `(element: null | AnyElement => void )`

This is the function that will be called each time the event occurs. It takes an `element` as a parameter. A `null` element signifies that no element is selected. Use this function to define what should happen when the event is triggered.

***

### Returns

#### ***`Unsubscribe`***

This is a special function you receive after subscribing. When you no longer want to listen to the event, call this function to stop receiving notifications.

### Example

```typescript
// Subscribe to changes in the selected element
const selectedElementCallback = (element: AnyElement | null) => {
  if (element) {
    console.log('Selected Element:', element);
  } else {
    console.log('No element is currently selected.');
  }
}

const unsubscribeSelectedElement = webflow.subscribe('selectedelement', selectedElementCallback);
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>
