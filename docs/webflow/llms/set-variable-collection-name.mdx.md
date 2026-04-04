# Source: https://developers.webflow.com/designer/reference/set-variable-collection-name.mdx

***

title: Set a variable collection name
slug: designer/reference/set-variable-collection-name
description: Learn how to set a variable collection name with the Designer API.
hidden: false
'og:title': Set a variable collection name
'og:description': Learn how to set a variable collection name with the Designer API.
------------------------------------------------------------------------------------

## `collection.setName(name)`

Sets the name of a variable collection.

#

### Syntax

```typescript
collection.setName(name: string)
```

### Parameters

* **name**: *string* - The new name for the variable collection.

### Returns

**`null`**

Returns `null` if the name was set successfully.

### Example

```typescript
const collection = webflow.getVariableCollectionById("collection-4a393cee-14d6-d927-f2af-44169031a25b");

collection.setName("My New Collection");

// returns null
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
