# Source: https://developers.webflow.com/designer/reference/set-component-name.mdx

***

title: Set component name
slug: designer/reference/set-component-name
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set component name'
'og:description': Set the name of the Component Object.
-------------------------------------------------------

## **`component.setName(name)`**

Set the name of the Component Object.

### Syntax

```typescript
component.setName(name: string): Promise<void>
```

### Parameters

* **`name`** : *string* - Then name you wish to give your component

### Returns

**Promise\<null>**

A promise that resolves to `null` once the name has been set.

```typescript
// Get Component
const components = await webflow.getAllComponents()
const myComponent = components[0]

// Set Component Name
await myComponent.setName("My New Component Name")
```

### Designer Ability

| Designer Ability        | Locale | Branch | Workflow | Sitemode |
| :---------------------- | :----- | :----- | :------- | :------- |
| **canModifyComponents** | any    | any    | Canvas   | Design   |
