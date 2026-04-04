# Source: https://developers.webflow.com/designer/reference/create-component-definition.mdx

***

title: Create a component
slug: designer/reference/create-component-definition
description: ''
hidden: false
'og:title': 'Webflow Designer API: Create a component'
'og:description': Registers a new component definition with the specified name and root element.
------------------------------------------------------------------------------------------------

## `webflow.registerComponent(name, root)`

Registers a new [component definition](/designer/reference/components-overview#component-definition) with the specified name and root element.

### Syntax

```typescript
webflow.registerComponent(
  name: string,
  root: AnyElement | ElementPreset<AnyElement> | Component
): Promise<Component>
```

### Parameters

* **`name`** :   *string* - The name of the component.
* **`root`** :   *AnyElement* - The root element of the component.

### Returns

**Promise\< *Component*>**

A Promise that resolves to the registered component.

### Example

```typescript
// Get selected element
const rootElement = await webflow.getSelectedElement();

if (rootElement) {

  // Create a component from the Root Element
  const component = await webflow.registerComponent('MyCustomComponent', rootElement);
  console.log(`Component registered with ID: ${component.id}`);

} else {
  console.log("No element is currently selected. Please select a root element first.");
}

},~
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
