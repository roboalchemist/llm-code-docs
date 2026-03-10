# Source: https://developers.webflow.com/designer/reference/set-variable-value.mdx

***

title: Set variable value
slug: designer/reference/set-variable-value
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set variable value'
'og:description': Set the value of the selected variable.
---------------------------------------------------------

## `variable.set(value, options?)`

Set the value of the selected variable.

**Syntax**

<Template
  data={{
    VARIABLE_MODE: "VariableMode",
    CUSTOM_VALUE: "CustomValue",
    SIZE_VALUE: "SizeValue",
  }}
  tooltips={{
    VARIABLE_MODE: (
      <p>The variable mode object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "mode-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    CUSTOM_VALUE: (
      <p>The custom value object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"type": "custom", "value": "color-mix(in srgb, #146EF5, white 75%)"}`}</code>
    </p>),
    SIZE_VALUE: (
      <p>The size value object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{ value: 16, unit: "px" }`}</code>
    </p>),
  }}
>
  ```typescript
  variable.set(
      value: string | number | {{SIZE_VALUE}} | Variable | {{CUSTOM_VALUE}},
      options?: {
          mode: {{VARIABLE_MODE}},
      }
  ): Promise<null>;
  ```
</Template>

### Parameters

| Parameter   | Description                                                                                                                                                                                                                                                                         | Type                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **value**   | The value to set for the variable. Must match the variable's type. You can also pass a Variable object to create an alias, a [CustomValue](/designer/reference/variables-detail-overview#custom-values) for custom values, or `null` to reset a mode-specific value to its default. | `string` \| `number` \| `SizeValue` \| `Variable` \| `CustomValue` \| `null` |
| **options** | An optional parameter to set the [mode value](/designer/reference/variable-modes) of the variable.                                                                                                                                                                                  | `{mode: VariableMode}`                                                       |

<Note title="Resetting a mode-specific value">
  To reset a mode-specific value back to the default base value, pass `null`
  when calling `variable.set()` along with the mode you want to reset. Variables
  without a mode-specific value won't be affected.
</Note>

<br />

### Variable values by type

{/* <!-- vale off --> */}

<Tabs>
  <Tab title="Color">
    ```typescript
    collection.createColorVariable(name: string, value: string | ColorVariable | CustomValue): Promise<ColorVariable>
    ```

    | Accepted Formats for Value | Examples                                                 |
    | -------------------------- | -------------------------------------------------------- |
    | Color name                 | `collection.createColorVariable("primary", "red");`      |
    | RGB Hex                    | `collection.createColorVariable("primary", "#ffcc11");`  |
    | RGBA Hex                   | `collection.createColorVariable("primary", "#fffcc11");` |
  </Tab>

  <Tab title="Size">
    ```typescript
    collection.createSizeVariable(name: string, value: SizeValue | SizeVariable | CustomValue): Promise<SizeVariable>
    ```

    | Format                | Unit  | Examples                        |
    | --------------------- | ----- | ------------------------------- |
    | Pixels                | `px`  | `{ unit: "px", value: 50 });`   |
    | Root EM               | `rem` | `{ unit: "rem", value: 2 });`   |
    | EM Units              | `em`  | `{ unit: "em", value: 1.5 });`  |
    | Viewport Width        | `vw`  | `{ unit: "vw", value: 100 });`  |
    | Viewport Height       | `vh`  | `{ unit: "vh", value: 100 });`  |
    | Small Viewport Height | `svh` | `{ unit: "svh", value: 100 });` |
    | Small Viewport Width  | `svw` | `{ unit: "svw", value: 100 });` |
    | Character Units       | `ch`  | `{ unit: "ch", value: 80 });`   |
  </Tab>

  <Tab title="Number & Percentage">
    ```typescript
    collection.createNumberVariable(name: string, value: number | NumberVariable | CustomValue): Promise<NumberVariable>
    ```

    | Accepted Formats for Value     | Examples                                              |
    | ------------------------------ | ----------------------------------------------------- |
    | Number value between 0 and 100 | `collection.createPercentageVariable("opacity", 50);` |
  </Tab>

  <Tab title="FontFamily">
    ```typescript
    collection.createFontFamilyVariable(name: string, value: string | FontFamilyVariable | CustomValue): Promise<FontFamilyVariable>
    ```

    | Accepted Formats for Value                       | Examples                                                         |
    | ------------------------------------------------ | ---------------------------------------------------------------- |
    | String of the font family name (e.g., "Verdana") | `collection.createFontFamilyVariable("defaultFont", "Verdana");` |
  </Tab>
</Tabs>

{/* <!-- vale on --> */}

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`

### Examples

<Tabs>
  <Tab title="Color">
    ```typescript
    // Get Collection
    const collection = await webflow.getDefaultVariableCollection();

    // Get Variable
    const variable = await collection?.getVariableByName("MyColorVariable");

    // Check Variable type and set color
    if (variable?.type === "Color") await variable.set("#fffcc11");
    ```
  </Tab>

  <Tab title="Size">
    ```typescript
    // Get Collection
    const collection = await webflow.getDefaultVariableCollection();

    // Get Variable
    const variable = await collection?.getVariableByName("MySizeVariable");

    // Check Variable type and set size
    if (variable?.type === "Size") await variable.set({ value: 16, unit: "px" });
    ```
  </Tab>

  <Tab title="Number & Percentage">
    ```typescript
    // Get Collection
    const collection = await webflow.getDefaultVariableCollection();

    // Get Variable
    const variable = await collection?.getVariableByName("MyNumberVariable");

    // Check Variable type and set number
    if (variable?.type === "Number") await variable.set(100);
    ```
  </Tab>

  <Tab title="Font family">
    ```typescript
    // Get Collection
    const collection = await webflow.getDefaultVariableCollection();

    // Get Variable
    const variable = await collection?.getVariableByName("MyFontVariable");

    // Check Variable type and set font family
    if (variable?.type === "FontFamily") await variable.set("Verdana");
    ```
  </Tab>

  <Tab title="Alias">
    ```typescript
    // Get Collection
    const collection = await webflow.getDefaultVariableCollection();

    // Get Variables
    const variableToSet = await collection?.getVariableByName("MyAliasVariable");
    const variableToAlias = await collection?.getVariableByName("MyColorVariable");

    // Check that Variable types are compatible and set alias
    if (variableToSet?.type === "Color" && variableToAlias) {
        await variableToSet.set(variableToAlias);
    }
    ```
  </Tab>

  <Tab title="Custom value">
    ```typescript
    // Get Collection
    const collection = await webflow.getDefaultVariableCollection();

    // Get Variable
    const variable = await collection?.getVariableByName("MyCustomVariable");

    // Check Variable type and set custom value
    if (variable?.type === "Color") {
        await variable.set({
            type: "custom",
            value: "color-mix(in srgb, var(--blue-500), #fff 60%)"
        });
    }
    ```
  </Tab>
</Tabs>

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer Ability       | Locale | Branch | Workflow | Sitemode |
| :--------------------- | :----- | :----- | :------- | :------- |
| **canModifyVariables** | Any    | Main   | Canvas   | Design   |
