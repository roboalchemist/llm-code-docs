# Source: https://developers.webflow.com/designer/reference/get-collection-name.mdx

***

title: Get collection name
slug: designer/reference/get-collection-name
description: Get the name of a variable collection using the Webflow Designer API.
hidden: false
'og:title': 'Webflow Designer API: Get collection name'
'og:description': Retrieves the name of the variable collection.
----------------------------------------------------------------

## `collection.getName()`

Retrieves the name of the variable collection.

### Syntax

```typescript
collection.getName(): Promise<string>
```

### Returns

**Promise\< `string`>**

A Promise that resolves to a `string` of the Variable Collection's name

### Example

```typescript
// Get Collection
const defaultVariableCollection = await webflow.getDefaultVariableCollection();

// Get Collection Name
const collectionName = await defaultVariableCollection?.getName()
console.log(collectionName)
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
