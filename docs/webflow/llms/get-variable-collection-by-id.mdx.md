# Source: https://developers.webflow.com/designer/reference/get-variable-collection-by-id.mdx

***

title: Get a variable collection by ID
slug: designer/reference/get-variable-collection-by-id
description: Learn how to get a variable collection by ID with the Designer API.
hidden: false
'og:title': Get a variable collection by ID
'og:description': Learn how to get a variable collection by ID with the Designer API.
-------------------------------------------------------------------------------------

## `webflow.getVariableCollectionById(collectionId)`

Retrieves a variable collection by its ID.

#

### Syntax

```typescript
webflow.getVariableCollectionById(collectionId: string)
```

### Parameters

* **collectionId**: *string* - The ID of the variable collection to retrieve.

### Returns

**Promise\<*VariableCollection*>**

The a promise that resolves to a variable collection object.

#

### Example

```typescript
const collection = webflow.getVariableCollectionById("collection-4a393cee-14d6-d927-f2af-44169031a25b");

// returns a collection object
// {
//     "id": "collection-4a393cee-14d6-d927-f2af-44169031a25b",
// }
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
