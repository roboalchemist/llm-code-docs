# Source: https://developers.webflow.com/designer/reference/get-variable-mode-by-name.mdx

***

title: Get variable mode by name
slug: reference/get-variable-mode-by-name
description: Learn how to get a variable mode by its name.
hidden: null
'og:title': Get variable mode by name
'og:description': Learn how to get a variable mode by its name.
---------------------------------------------------------------

## `collection.getVariableModeByName(string: modeName)`

Get a variable mode by its name.

#

### Syntax

```typescript
collection.getVariableModeByName(modeName: string): Promise<VariableMode>
```

### Parameters

* **modeName**: *string* - The name of the variable mode to get.

### Returns

**Promise\<*VariableMode*>**

A Promise that resolves to a variable mode object.

#

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get Variable Mode by Name
const variableMode = await collection.getVariableModeByName(modeName)
console.log(variableMode)
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
