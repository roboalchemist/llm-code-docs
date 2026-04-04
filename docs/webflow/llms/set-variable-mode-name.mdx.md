# Source: https://developers.webflow.com/designer/reference/set-variable-mode-name.mdx

***

title: Set variable mode name
slug: reference/set-variable-mode-name
description: Learn how to set the name of a variable mode.
hidden: null
'og:title': 'Webflow Designer API: Set variable mode name'
'og:description': Set the name of a variable mode
-------------------------------------------------

## `mode.setName(name)`

Set the name of a variable mode. Variable mode names must be unique within a collection.

#

### Syntax

```typescript
mode.setName(name: string): Promise<null>
```

### Parameters

* **name**: *string* - The name of the variable mode to set.

### Returns

**Promise\<*null*>**

A Promise that resolves to null.

#

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Get Variable Mode
const variableMode = await collection?.getVariableModeByName(modeName)

// Set Variable Mode Name
variableMode?.setName("My Variable Mode")
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
