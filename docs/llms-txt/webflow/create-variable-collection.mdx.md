# Source: https://developers.webflow.com/designer/reference/create-variable-collection.mdx

***

title: Create a variable collection
slug: designer/reference/create-variable-collection
description: Learn how to create a variable collection with the Designer API.
hidden: false
'og:title': Create a variable collection
'og:description': Learn how to create a variable collection with the Designer API.
----------------------------------------------------------------------------------

## `webflow.createVariableCollection(collectionName)`

Creates a new variable collection with the given name.

#

### Syntax

```typescript
webflow.createVariableCollection(collectionName: string)
```

### Parameters

* **collectionName**: *string* - The name of the variable collection to create.

### Returns

**Promise\<*VariableCollection*>**

The newly created collection object.

#

### Example

```typescript
const collection = webflow.createVariableCollection("My Collection");

// returns a collection object
// {"id": "collection-4a393cee-14d6-d927-f2af-44169031a25b"}
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
