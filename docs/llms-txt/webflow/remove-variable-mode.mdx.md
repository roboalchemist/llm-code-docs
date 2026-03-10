# Source: https://developers.webflow.com/designer/reference/remove-variable-mode.mdx

***

title: Remove variable mode
slug: reference/remove-variable-mode
description: Learn how to remove a variable mode.
hidden: null
'og:title': 'Webflow Designer API: Remove variable mode'
'og:description': Remove a variable mode from a collection
----------------------------------------------------------

## `mode.remove()`

Remove a variable mode from a collection

#

### Syntax

```typescript
mode.remove(): Promise<boolean>
```

### Returns

**Promise\<*boolean*>**

A Promise that resolves to boolean.

#

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get Variable Mode
const variableMode = await collection?.getVariableModeByName(modeName)

// Remove Variable Mode
variableMode?.remove()
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
