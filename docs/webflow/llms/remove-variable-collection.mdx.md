# Source: https://developers.webflow.com/designer/reference/remove-variable-collection.mdx

***

title: Remove a variable collection
slug: designer/reference/remove-variable-collection
description: Learn how to remove a variable collection with the Designer API.
hidden: false
'og:title': Remove a variable collection
'og:description': Learn how to remove a variable collection with the Designer API.
----------------------------------------------------------------------------------

## `webflow.removeVariableCollection(collectionId)`

Removes a variable collection by its ID.

#

### Syntax

```typescript
webflow.removeVariableCollection(collectionId: string)
```

### Parameters

* **collectionId**: *string* - The ID of the variable collection to remove.

### Returns

**`Promise<Boolean>`**

`true` if the variable collection was removed successfully, `false` otherwise.

#

### Example

```typescript
const success = webflow.removeVariableCollection("collection-4a393cee-14d6-d927-f2af-44169031a25b");

// returns true
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
