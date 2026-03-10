# Source: https://developers.webflow.com/designer/reference/get-root-element.mdx

***

title: Get root element
slug: designer/reference/get-root-element
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get root element'
'og:description': Retrieves the root element of the component.
--------------------------------------------------------------

## `component.getRootElement()`

Retrieves the root element of the component.

### Syntax

```typescript
webflow. getRootElement(): Promise<null | AnyElement>;
```

### Returns

**Promise\< *AnyElement*>**

A Promise that resolves to the root element.

### Example

```typescript
// Get Component
const all = await webflow.getAllComponents()
const firstComponent = all[0]

// Get Root Element of Component
const root = await firstComponent?.getRootElement()
console.log(root)
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
| **canAccessCanvas** | any    | any    | any      | any      |
