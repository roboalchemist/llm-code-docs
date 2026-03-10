# Source: https://developers.webflow.com/designer/reference/get-components.mdx

***

title: Get all components
slug: designer/reference/get-components
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get all components'
'og:description': Retrieves all component objects registered to the site.
-------------------------------------------------------------------------

## `webflow.getAllComponents()`

Retrieves all component objects registered to the site.

### Syntax

```typescript
webflow.getAllComponents(): Promise<Array<Component>>
```

### Returns

**Promise\<Array\<*Component*>>**

A Promise that resolves to an array of components.

### Example

```typescript
// Get all components
const components = await webflow.getAllComponents();

// Print Component Details
if (components.length > 0) {

  console.log("List of registered components:");

  for (let component in components) {
    const currentComponentName = await components[component].getName();
    console.log(`${component + 1}. Component Name: ${currentComponentName}, Component ID: ${components[component].id}`);
  }
} else {
  console.log("No components are currently registered.");
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

***

### Designer Ability

Checks for authorization only

| Designer Ability    | Permission | Locale | Branch | Workflow | Sitemode |
| :------------------ | :--------- | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | any        | any    | any    | any      | any      |
