# Source: https://developers.webflow.com/designer/reference/get-variable.mdx

***

title: Get variable by ID
slug: designer/reference/get-variable
description: Retrieve a variable by its ID with the Webflow Designer API.
hidden: false
'og:title': 'Webflow Designer API: Get variable by ID'
'og:description': Retrieve a variable by its ID.
------------------------------------------------

## `collection.getVariable(id)`

Retrieve a variable by its ID.

### Syntax

```typescript
collection.getVariable(id: VariableId): Promise<null | Variable>
```

### Parameters

* **ID** : *string* - ID of the variable you'd like to retrieve

### Returns

**Promise\<*Variable* | `null`>**

A promise that resolves to a Variable object, or `null` if not found

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get variable by ID
const variableById = await collection?.getVariable('id-123')
console.log(variableById)
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
