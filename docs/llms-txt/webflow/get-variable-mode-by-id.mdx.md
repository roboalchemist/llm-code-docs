# Source: https://developers.webflow.com/designer/reference/get-variable-mode-by-id.mdx

***

title: Get variable mode by ID
slug: reference/get-variable-mode-by-id
description: Learn how to get a variable mode by its ID.
hidden: null
'og:title': 'Get variable mode by ID  '
'og:description': Learn how to get a variable mode by its ID.
-------------------------------------------------------------

## `collection.getVariableModeById(string: modeId)`

Get a variable mode by its ID.

#

### Syntax

```typescript
collection.getVariableModeById(modeId: string): Promise<VariableMode>
```

### Parameters

* **modeId**: *string* - The ID of the variable mode to get.

### Returns

**Promise\<*VariableMode*>**
A Promise that resolves to a variable mode object.

#

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get Variable Mode by ID
const variableMode = await collection?.getVariableModeById(modeId)
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
