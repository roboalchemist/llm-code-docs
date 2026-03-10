# Source: https://developers.webflow.com/designer/reference/delete-component-definition.mdx

***

title: Delete a component
slug: designer/reference/delete-component-definition
description: ''
hidden: false
'og:title': 'Webflow Designer API: Delete a component'
'og:description': Removes a component definition from the site.
---------------------------------------------------------------

## `webflow.unregisterComponent(component)`

Removes a component definition from the site.

### Syntax

```typescript
webflow.unregisterComponent(component: Component): Promise<null>
```

### Parameters

* **`component`** :   *Component* - The component to delete

### Returns

**Promise\<`null`>**

A promise that resolves to `null`.

### Example

```typescript
// Get selected element
const selectedElement = await webflow.getSelectedElement();

if (selectedElement) {

  // Create component from selected element
  const myNewComponent = await webflow.registerComponent('Hero Component', selectedElement);

  // Delete Component
  await webflow.unregisterComponent(myNewComponent);

} else {
  console.log("No element is currently selected. Please select a root element first.");
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

***

### Designer Ability

| Designer Ability        | Locale  | Branch | Workflow | Sitemode |
| :---------------------- | :------ | :----- | :------- | :------- |
| **canCreateComponents** | Primary | any    | Canvas   | any      |
