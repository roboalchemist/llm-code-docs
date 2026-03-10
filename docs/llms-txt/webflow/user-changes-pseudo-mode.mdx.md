# Source: https://developers.webflow.com/designer/reference/user-changes-pseudo-mode.mdx

***

title: User changes pseudo mode of Designer
slug: reference/user-changes-pseudo-mode
description: >-
User Event. Use this method to start listening for specific events in your
App. In this case, we're listening for when a user changes the pseudo mode of
the Designer.
hidden: false
'og:title': 'Webflow Designer API: User changes pseudo mode of Designer'
'og:description': >-
User Event. Use this method to start listening for specific events in your
App. In this case, we're listening for when a user changes the pseudo mode of
the Designer.
-------------

## `webflow.subscribe("pseudomode", callback)`

Use this method to start listening for when a user changes the [pseudo-state](https://help.webflow.com/hc/en-us/articles/33961301727251-States) of the Designer.

### Syntax

```typescript
webflow.subscribe(
  event: "pseudomode",
  callback: (pseudoState: PseudoStateKey) => void
): Unsubscribe;
```

<Accordion title="Pseudo-State Key Values">
  | Pseudo-State      | Designer State     | Description                                        |
  | :---------------- | :----------------- | :------------------------------------------------- |
  | `hover`           | Hover              | Element is hovered over by the mouse               |
  | `pressed`         | Pressed            | Element is in pressed state                        |
  | `visited`         | Visited            | **Link** element has been visited                  |
  | `focus`           | Focused            | Element has keyboard/input focus                   |
  | `focus-visible`   | Focused (Keyboard) | Element has keyboard focus with visible indicator  |
  | `focus-within`    | --                 | Element or its descendant has focus                |
  | `placeholder`     | Placeholder        | Placeholder text in form block inputs              |
  | `first-child`     | First Item         | First Collection Item in a collection list         |
  | `last-child`      | Last Item          | Last Collection Item in a collection list          |
  | `nth-child(odd)`  | Odd Items          | Odd-numbered Collection Item in a collection list  |
  | `nth-child(even)` | Even Items         | Even-numbered Collection Item in a collection list |
</Accordion>

### Parameters

* **event**: `"pseudomode"` - The event to listen for.
* **callback**: `(pseudoState: PseudoStateKey) => void` - The callback function to execute when the event occurs. The `pseudoState` parameter is the new pseudo-state of the Designer.

### Returns

**Return Value**

***`Unsubscribe`***

This is a special function you receive after subscribing. When you no longer want to listen to the event, call this function to stop receiving notifications.

#

### Example

```typescript
// Subscribe to changes in the pseudo state
const pseudoStateCallback = (pseudoState: PseudoStateKey) => {
  console.log('Pseudo State:', pseudoState);
}

const unsubscribePseudoState = webflow.subscribe('pseudomode', pseudoStateCallback);
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
