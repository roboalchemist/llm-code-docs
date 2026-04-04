# Source: https://developers.webflow.com/designer/reference/get-variable-value.mdx

***

title: Get variable value
slug: designer/reference/get-variable-value
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get variable value'
'og:description': Retrieves the value of the variable.
------------------------------------------------------

## `variable.get(options?)`

Retrieves the value of the variable.

### Syntax

```typescript
variable.get(
    options?: {
        mode: VariableMode,
        customValues: boolean,
        doNotInheritFromBase: boolean}
): Promise<string | number | SizeValue | Variable | CustomValue>;
```

### Parameters

* **options**: *object* - An optional parameter to include get specific information.

  | Parameter              | Type         | Description                                                                                                                                 | Default |
  | ---------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
  | `mode`                 | VariableMode | The value of the variable in the specified [variable mode](/designer/reference/variable-modes).                                             | —       |
  | `customValues`         | boolean      | Indicates whether to return the custom value of the variable.                                                                               | `false` |
  | `doNotInheritFromBase` | boolean      | Indicates whether to return the value of the variable without inheriting from the base [variable mode](/designer/reference/variable-modes). | `false` |

{/* <!-- vale off --> */}

<Warning>
  Calling `variable.get()` without `customValues: true` will throw an error if the variable has a [custom value](/designer/reference/variables-detail-overview#custom-values).
</Warning>

{/* <!-- vale on --> */}

### Returns

Returns a Promise that resolves to the current value of the variable. The exact return type depends on the variable’s type, whether it's an alias or a custom value, and the selected variable mode.

See the table below for details on return types for each scenario.

<br />

<Tabs>
  <Tab title="Color">
    Returns a value in one of these formats:

    {/* <!-- vale off --> */}

    | Format         | Examples                                                                     | Return Type     |
    | -------------- | ---------------------------------------------------------------------------- | --------------- |
    | String         | `"red"`, `"#ffcc11"`, `"#fffcc11"`                                           | `string`        |
    | Variable alias | `{ "id": "variable-xyz-123" }`                                               | *ColorVariable* |
    | Custom value   | `{"type":"custom","value":"color-mix(in srgb, var(--blue-500) , #fff 60%)"}` | *CustomValue*   |

    {/* <!-- vale on --> */}
  </Tab>

  <Tab title="Size">
    Returns a value in one of these formats:

    | Format            | Examples                                                    | Return Type    |
    | ----------------- | ----------------------------------------------------------- | -------------- |
    | Size value object | `{ value: 16, unit: "px" }`                                 | *SizeValue*    |
    | Variable alias    | `{ "id": "variable-xyz-123" }`                              | *SizeVariable* |
    | Custom value      | `{ "type": "custom", "value": "calc(var(--spacing) * 2)" }` | *CustomValue*  |

    **Size value example**

    ```typescript
    {
      value: number,  // The size value
      unit: "px" | "rem" | "em" | "vw" | "vh" | "svh" | "svw" | "ch"  // The unit type
    }
    ```
  </Tab>

  <Tab title="Number & Percentage">
    Returns a value in one of these formats:

    | Format         | Examples                                                   | Return Type                              |
    | -------------- | ---------------------------------------------------------- | ---------------------------------------- |
    | Number         | `100`                                                      | `number`                                 |
    | Percentage     | `50`                                                       | `number`                                 |
    | Variable alias | `{ "id": "variable-xyz-123" }`                             | *NumberVariable* or *PercentageVariable* |
    | Custom value   | `{ "type": "custom", "value": "calc(var(--number) * 2)" }` | *CustomValue*                            |
  </Tab>

  <Tab title="FontFamily">
    Returns a value in one of these formats:

    | Format         | Examples                       | Return Type          |
    | -------------- | ------------------------------ | -------------------- |
    | String         | `"Verdana"`                    | `string`             |
    | Variable alias | `{ "id": "variable-xyz-123" }` | *FontFamilyVariable* |
  </Tab>
</Tabs>

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection();

// Get All Variables
const variables = await collection.getAllVariables();

// Get Value of first Variable
const variable = variables[0];
const value = await variable.get();
// value = "#146EF5"

// Get Value of first Variable with custom value
const variable = variables[1];
const value = await variable.get({ customValues: true });
// value = { type: 'custom', value: 'color-mix(in srgb, var(--blue-500), white 50%)' }
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

Checks for Authorization only

{/* <!-- vale off --> */}

| Designer ability     | Locale | Branch | Workflow | Sitemode |
| :------------------- | :----- | :----- | :------- | :------- |
| **canReadVariables** | Any    | Any    | Any      | Any      |
