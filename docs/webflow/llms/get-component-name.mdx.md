# Source: https://developers.webflow.com/designer/reference/get-component-name.mdx

***

title: Get component name
slug: designer/reference/get-component-name
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get component name'
'og:description': Get the name of the Component Object.
-------------------------------------------------------

## **`component.getName()`**

Get the name of the Component Object.

### Syntax

```typescript
component.getName(): Promise<string>
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a `string` representing the name of a component.

```typescript
const myComponentName = "Hero-Component";
const components = await webflow.getAllComponents();

// Check if component exists
for (const c in components) {
  const currentComponentName = await components[c].getName();
  if (myComponentName === currentComponentName) {
    console.log("Found Hero Component");
  }
}
```

### Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | any    | any    | any      | any      |
