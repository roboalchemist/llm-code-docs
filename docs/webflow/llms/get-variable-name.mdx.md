# Source: https://developers.webflow.com/designer/reference/get-variable-name.mdx

***

title: Get variable name
slug: designer/reference/get-variable-name
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get variable name'
'og:description': Retrieves the name of the variable.
-----------------------------------------------------

## `variable.getName()`

Retrieves the name of the variable.

### Syntax

```typescript
variable.getName(): Promise<string>;
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a `string` with the variable name

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get All Variables
const variables = await collection.getAllVariables()

// Get Value of first Variable
const variable = variables[0]
const value = await variable.getName()
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

Checks for Authorization only

| Designer Ability     | Locale | Branch | Workflow | Sitemode |
| :------------------- | :----- | :----- | :------- | :------- |
| **canReadVariables** | Any    | Any    | Any      | Any      |
