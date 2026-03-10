# Source: https://developers.webflow.com/designer/reference/get-all-variables.mdx

***

title: Get all variables
slug: designer/reference/get-all-variables
description: Get all variables in a collection using the Webflow Designer API.
hidden: false
'og:title': 'Webflow Designer API: Get all variables'
'og:description': Get all variables in a collection
---------------------------------------------------

## `collection.getAllVariables()`

Get all variables in a collection

### Syntax

```typescript
collection.getAllVariables(): Promise<Array<Variable>>
```

### Returns

**Promise\<*Variable*>**

A Promise that resolves to an array of Variable objects

### Example

```typescript
// Fetch the default variable collection
const defaultVariableCollection = await webflow.getDefaultVariableCollection();

if (defaultVariableCollection) {

  // Print Collection ID
  console.log("Default Variable Collection ID:", defaultVariableCollection.id);

  // Fetch all variables within the default collection
  const variables = await defaultVariableCollection.getAllVariables();

  if (variables.length > 0) {

    console.log("List of Variables in Default Collection:");

    // Print variable details
    for (var i in variables) {
      console.log(`${i}. Variable Name: ${await variables[i].getName()}, Variable ID: ${variables[i].id}`);
    };
  } else {
    console.log("No variables found in the default collection.");
  }
} else {
  console.log("Default Variable Collection not found.");
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
