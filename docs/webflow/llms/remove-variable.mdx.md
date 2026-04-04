# Source: https://developers.webflow.com/designer/reference/remove-variable.mdx

***

title: Remove variable
slug: designer/reference/remove-variable
description: ''
hidden: false
'og:title': 'Webflow Designer API: Remove variable'
'og:description': Delete and remove variable from collection.
-------------------------------------------------------------

## `variable.remove()`

Delete and remove variable from collection.

### Syntax

```typescript
variable.remove(): Promise<boolean>
```

### Returns

**Promise\<`boolean`>**

A Promise that resolves to a `boolean` value

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get All Variables
const variables = await collection.getAllVaraiables

// Remove first variable
const variable = variables[0]
await variable.remove()
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability       | Locale | Branch | Workflow | Sitemode |
| :--------------------- | :----- | :----- | :------- | :------- |
| **canModifyVariables** | Any    | Main   | Canvas   | Design   |
