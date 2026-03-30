# Source: https://developers.webflow.com/designer/reference/create-variable-mode.mdx

***

title: Create variable mode
slug: reference/create-variable-mode
description: Learn how to create a variable mode.
hidden: null
'og:title': 'Webflow Designer API: Create variable mode'
'og:description': Create a variable mode in a collection
--------------------------------------------------------

## `collection.createVariableMode(name)`

Create a variable mode in a collection. Variable modes created with the Designer API are always created as "Manual" modes.

#

### Syntax

```typescript
collection.createVariableMode(name: string): Promise<VariableMode>
```

### Parameters

* **name**: *string* - The name of the variable mode to create.

### Returns

**Promise\<*VariableMode*>**

A Promise that resolves to a VariableMode object.

#

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Create Variable Mode
const variableMode = await collection?.createVariableMode("Dark Mode")
console.log(variableMode)
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
