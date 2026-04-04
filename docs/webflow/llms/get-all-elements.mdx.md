# Source: https://developers.webflow.com/designer/reference/get-all-elements.mdx

***

title: Get all elements
slug: designer/reference/get-all-elements
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get all elements'
'og:description': Retrieve all elements present on the current page of the Designer.
------------------------------------------------------------------------------------

## `webflow.getAllElements()`

Retrieve all elements present on the current page of the Designer.

If the Designer is editing a component, the elements returned are those present in that Component.

### Syntax

```typescript
webflow.getAllElements(): Promise<Array<AnyElement>>
```

### Returns

**Promise\<*AnyElement*>**

A Promise that resolves to an array of `AnyElement` objects.

`AnyElement` represents the various element types available in a Webflow project. See a full list of supported element types in the [Designer Extension type definitions.](https://www.npmjs.com/package/@webflow/designer-extension-typings?activeTab=code)

### Example

```typescript
// Retrieve all elements in the current context
const allElements = await webflow.getAllElements();

// Print element list
if (allElements.length > 0) {
  console.log("List of all elements:");

  allElements.forEach((element, index) => {
    console.log(`${index + 1}. Element ID: ${element.id}, Element Type: ${element.type}`);
  });
} else {
  console.log("No elements found in the current context.");
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
