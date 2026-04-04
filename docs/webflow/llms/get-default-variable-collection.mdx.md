# Source: https://developers.webflow.com/designer/reference/get-default-variable-collection.mdx

***

title: Get default variable collection
slug: designer/reference/get-default-variable-collection
description: >-
Retrieves the default variable collection. The default collection is the first
variable collection created with your site.
hidden: false
'og:title': 'Webflow Designer API: Get default variable collection'
'og:description': >-
Retrieves the default variable collection. The default collection is the first
variable collection created with your site.
-------------------------------------------

## `webflow.getDefaultVariableCollection()`

Retrieves the default variable collection. The default collection is the first variable collection created with your site.

### Syntax

```typescript
webflow.getDefaultVariableCollection(): Promise<null | VariableCollection>;
```

### Returns

**Promise\<*VariableCollection*>**

A Promise that resolves to the default Variable Collection or null if not found.

### Example

```typescript
// Get Collection
const defaultVariableCollection = await webflow.getDefaultVariableCollection();

// Fetch all variables within the default collection
const variables = await defaultVariableCollection?.getAllVariables();
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
