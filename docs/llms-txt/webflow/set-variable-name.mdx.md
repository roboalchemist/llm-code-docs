# Source: https://developers.webflow.com/designer/reference/set-variable-name.mdx

***

title: Set variable name
slug: designer/reference/set-variable-name
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set variable name'
'og:description': Sets the name of the variable.
------------------------------------------------

## `variable.setName(name)`

Sets the name of the variable.

### Syntax

```typescript
variable.setName(name: string): Promise<null>;
```

### Parameters

* **name** : *string*   - Name of the variable

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get All Variables
const variables = await collection.getAllVariables()

// Get Value of first Variable
const variable = variables[0]
const value = await variable.setName("Primary")
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
