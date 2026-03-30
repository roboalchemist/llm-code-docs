# Source: https://developers.webflow.com/designer/reference/remove-element.mdx

***

title: Remove element
slug: designer/reference/remove-element
description: ''
hidden: false
'og:title': 'Webflow Designer API: Remove element'
'og:description': Remove element from the canvas.
-------------------------------------------------

## `element.remove()`

Remove element from the canvas.

### Syntax

```typescript
element.remove(): Promise<null>
```

### Returns

**Promise\<`null`>**

A Promise that resolves to `null` when the Element is removed from the canvas.

### Example

```typescript
// Get Selected Element
const el = await webflow.getSelectedElement();

// Remove the selected element
await el?.remove();
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability | Locale  | Branch | Workflow | Sitemode |
| :--------------- | :------ | :----- | :------- | :------- |
| **canDesign**    | Primary | Main   | Canvas   | Design   |
