# Source: https://developers.webflow.com/designer/reference/create-font-family-variable.mdx

***

title: Create font family variable
slug: designer/reference/create-font-family-variable
description: >-
Create a Font Family variable with a name for the variable, and name for the
Font Family.
hidden: false
'og:title': 'Webflow Designer API: Create font family variable'
'og:description': >-
Create a Font Family variable with a name for the variable, and name for the
Font Family.
------------

## `collection.createFontFamilyVariable(name, value)`

Create a Font Family variable with a name for the variable, and name for the Font Family.

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_MODE:"VariableMode",
    VARIABLE_REFERENCE:"FontFamilyVariable"
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
      <p>A reference to another font family variable
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "variable-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>)
  }}
>
  ```typescript
  collection.createFontFamilyVariable(
    name: string,
    value: string | {{VARIABLE_REFERENCE}},
    options?: {
      mode?: {{VARIABLE_MODE}}
    }
  ): Promise<FontFamilyVariable>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **name** : *string* - Name of the variable
* **value**: *string* | FontFamilyVariable  - Font Name
* **options**: *object* - Optional parameters for the variable.
  * **mode**: *VariableMode* - The [variable mode](/designer/reference/variable-modes) object. Get the variable mode by using the [`collection.getVariableModeByName()`](/designer/reference/get-variable-mode-by-name) method.

### Returns

**Promise\<*FontFamilyVariable*>**

A Promise that resolves to a FontFamilyVariable object

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Create Font Family Variable with a Font Family Name
const myFontFamilyVariable = await collection?.createFontFamilyVariable("Default Font", "Inter")
console.log(myFontFamilyVariable)
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
