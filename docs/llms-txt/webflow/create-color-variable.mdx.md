# Source: https://developers.webflow.com/designer/reference/create-color-variable.mdx

***

title: Create color variable
slug: designer/reference/create-color-variable
description: Create a color variable with a name and value for the variable.
hidden: false
'og:title': 'Webflow Designer API: Create color variable'
'og:description': Create a color variable with a name and value for the variable.
---------------------------------------------------------------------------------

## `collection.createColorVariable(name, value)`

Create a color variable with a name and value for the variable.

Once created, you can set color variables for: Text colors, Background colors, Border and text stroke colors, and Gradient color stops

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_MODE:"VariableMode",
    VARIABLE_REFERENCE:"ColorVariable",
    CUSTOM_VALUE:"CustomValue"
  }}
  tooltips={{
    VARIABLE_MODE: (
      <p>The variable mode object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "mode-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    VARIABLE_REFERENCE: (
      <p>A reference to another color variable
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "variable-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    CUSTOM_VALUE: (
      <p>A custom value for the variable
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"type": "custom", "value": "color-mix(in srgb, #146EF5, white 75%)"}`}</code>
    </p>)
  }}
>
  ```typescript
  collection.createColorVariable(
    name: string,
    value: string | {{VARIABLE_REFERENCE}} | {{CUSTOM_VALUE}},
    options?: {
      mode?: {{VARIABLE_MODE}}
    }
  ): Promise<ColorVariable>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **name** : *string* - Name of the variable
* **value**: *string* | *ColorVariable* | [*CustomValue*](/designer/reference/variables-detail-overview#custom-values) - Value of the variable. Value can be a string in one of four formats:
  * Color Name
  * Color RGB hex value
  * Color RGBA hex value
  * [Custom value](/designer/reference/variables-detail-overview#custom-values)
* **options**: *object* - Optional parameters for the variable.
  * **mode**: *VariableMode* - The [variable mode](/designer/reference/variable-modes) object. Get the variable mode by using the [`collection.getVariableModeByName()`](/designer/reference/get-variable-mode-by-name) method.

### Returns

**Promise\<*ColorVariable*>**

A Promise that resolves to a ColorVariable object.

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Create Color Variable with a HEX Codre
const myColorVariable = await collection?.createColorVariable("primary", "#ffcc11")
console.log(myColorVariable)
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
