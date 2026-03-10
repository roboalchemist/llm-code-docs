# Source: https://developers.webflow.com/designer/reference/variable-modes.mdx

***

title: Variable Modes
slug: reference/variable-modes
description: Learn how to create and manage variable modes with the Designer API.
hidden: null
'og:title': 'Webflow Designer API: Variable Modes'
'og:description': Learn how to create and manage variable modes with the Designer API.
--------------------------------------------------------------------------------------

Variable modes let you define multiple values for individual variables, creating distinct sets of values (“modes”) that can be switched and applied across a site.

![Variable Modes](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/5423fb175d908862510c828470828d7cb30aa612f2e3e3d3632534f44c7a04ae/assets/images/variable-modes.jpg)

## Create a variable mode

Create a variable mode for a specific collection using the [`collection.createVariableMode()` method](/designer/reference/create-variable-mode). All variable modes created with the Designer API will be created as 'manual' modes.

```typescript
// Get the default variable collection
const collection = await webflow.getDefaultVariableCollection()

// Create a variable mode
const variableMode = await collection.createVariableMode("Dark Mode")

```

## Set a mode-specific value on a variable

Once you've created a variable mode, you can set a mode-specific value on a variable using the [`variable.set()` method](/designer/reference/set-variable-value).

To reset a mode-specific value back to the default base value, pass `null` when calling `variable.set()` along with the mode you want to reset.

```typescript

// Get the default variable collection
const collection = await webflow.getDefaultVariableCollection()

// Create variable for the collection with a default value
const colorVariable = await collection.createColorVariable("Body Text", "#ccc")

// Create a variable mode
const variableMode = await collection.createVariableMode("Dark Mode")

// Set a mode-specific value on the variables
await colorVariable.set("#FFF", {mode: variableMode})

// Reset the mode-specific value back to the default base value
await colorVariable.set(null, {mode: variableMode}) // This mode value is now "#ccc"

```
