# Source: https://developers.webflow.com/designer/reference/get-all-variable-modes.mdx

***

title: Get all variable modes
slug: reference/get-all-variable-modes
description: Learn how to get all variable modes.
hidden: null
'og:title': 'Webflow Designer API: Get all variable modes'
'og:description': Get all variable modes in a collection
--------------------------------------------------------

## `collection.getAllVariableModes()`

Get all variable modes in a collection.

#

### Syntax

```typescript
collection.getAllVariableModes(): Promise<Array<VariableMode>>
```

### Returns

**Promise\<*Array\<VariableMode>*>**

A Promise that resolves to an array of VariableMode objects.

#

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get All Variable Modes
const variableModes = await collection.getAllVariableModes()
console.log(variableModes)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability     | Locale | Branch | Workflow | Sitemode |
| :------------------- | :----- | :----- | :------- | :------- |
| **canReadVariables** | Any    | Any    | Any      | Any      |
