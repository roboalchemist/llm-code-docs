# Source: https://developers.webflow.com/designer/reference/get-variable-by-name.mdx

***

title: Get variable by name
slug: designer/reference/get-variable-by-name
description: Retrieve a variable by its name with the Webflow Designer API.
hidden: false
'og:title': 'Webflow Designer API: Get variable by name'
'og:description': Retrieve a variable by its name.
--------------------------------------------------

## `collection.getVariableByName(name)`

Retrieve a variable by its name.

### Syntax

```typescript
collection.getVariableByName(name: string): Promise<null | Variable>>
```

### Parameters

* **name** : *string* - Name of the variable you'd like to retrieve

### Returns

**Promise\< *Variable* | `null`>**

A Promise that resolves to a Variable object, or `null` if not found

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get Variable by Name
const variableByName = await collection?.getVariableByName('Space Cadet')
console.log(variableByName)
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
