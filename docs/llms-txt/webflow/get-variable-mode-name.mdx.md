# Source: https://developers.webflow.com/designer/reference/get-variable-mode-name.mdx

***

title: Get variable mode name
slug: reference/get-variable-mode-name
description: Learn how to get the name of a variable mode.
hidden: null
'og:title': 'Webflow Designer API: Get variable mode name'
'og:description': Get the name of a variable mode
-------------------------------------------------

## `mode.getName()`

Get the name of a variable mode

#

### Syntax

```typescript
mode.getName(): Promise<string>
```

### Returns

**Promise\<*string*>**

A Promise that resolves to the name of the variable mode.

#

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get Variable Mode
const variableMode = await collection?.getVariableModeById(modeId)

// Get Variable Mode Name
const name = await variableMode?.getName()
console.log(name)
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
