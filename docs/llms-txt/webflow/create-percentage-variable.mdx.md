# Source: https://developers.webflow.com/designer/reference/create-percentage-variable.mdx

***

title: Create percentage variable
slug: designer/reference/create-percentage-variable
description: Create a percentage variable with a name and value for the variable.
hidden: false
'og:title': 'Webflow Designer API: Create percentage variable'
'og:description': Create a percentage variable with a name and value for the variable.
--------------------------------------------------------------------------------------

## `collection.createPercentageVariable(name, value)`

Create a percentage variable with a name and value for the variable.

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_MODE:"VariableMode",
    VARIABLE_REFERENCE:"PercentageVariable",
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
      <p>A reference to another percentage variable
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
      <code>{`{"type": "custom", "value": calc(100vh - var(--header-height))"}`}</code>
    </p>)
  }}
>
  ```typescript
  collection.createPercentageVariable(
    name: string,
    value: number | {{VARIABLE_REFERENCE}} | {{CUSTOM_VALUE}},
    options?: {
      mode?: {{VARIABLE_MODE}}
    }
  ): Promise<PercentageVariable>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **name** : *string* - Name of the variable
* **value**: *number* | *PercentageVariable* | [*CustomValue*](/designer/reference/variables-detail-overview#custom-values) - Value of the variable.
* **options**: *object* - Optional parameters for the variable.
  * **mode**: *VariableMode* - The [variable mode](/designer/reference/variable-modes) object. Get the variable mode by using the [`collection.getVariableModeByName()`](/designer/reference/get-variable-mode-by-name) method.

### Returns

**Promise\<*PercentageVariable*>**

A Promise that resolves to a PercentageVariable object.

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Create Percentage Variable of 50 Percent
const myPercentageVariable = await collection?.createPercentageVariable("50%", 50)
console.log(myPercentageVariable)
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
