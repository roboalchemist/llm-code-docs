# Source: https://developers.webflow.com/designer/reference/set-selected-element.mdx

***

title: Set selected element
slug: designer/reference/set-selected-element
description: ''
hidden: false
-------------

## `webflow.setSelectedElement()`

Set the selected element on the current page, or on the current component when the Designer is [entered into a component.](/designer/reference/enter-component)

The returned element object can be further queried using [element-level properties](/designer/reference/elements/children) (e.g. type, styles)  and methods (e.g. `getChildren()`)

### Syntax

```typescript
webflow.setSelectedElement(element: AnyElement): Promise<AnyElement>
```

### Parameters

* **Element**:  *AnyElement* - Any element that is on the current canvas, or is with the current component when the designer is [entered into a component.](/designer/reference/enter-component)

### Returns

*Promise\<*AnyElement*>*

A Promise that resolves to `AnyElement`.

### Example

```typescript
// Get the Root Element
const rootElement = await webflow.getRootElement();

if (rootElement) {

  // Select the root element
  const selectedElement = await webflow.setSelectedElement(rootElement);

  if (selectedElement?.children) {

    // Start building elements on the selected element
    await selectedElement?.append(webflow.elementPresets.DOM)

  }
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
