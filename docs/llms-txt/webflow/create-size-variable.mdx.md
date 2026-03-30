# Source: https://developers.webflow.com/designer/reference/create-size-variable.mdx

***

title: Create size variable
slug: designer/reference/create-size-variable
description: 'Create a Size variable with a name for the variable, and size value.'
hidden: false
max-toc-depth: 3
'og:title': 'Webflow Designer API: Create size variable'
'og:description': 'Create a Size variable with a name for the variable, and size value.'
----------------------------------------------------------------------------------------

## `collection.createSizeVariable(name, value)`

Create a Size variable with a name for the variable, and size value.

Once created, you can set size variables for:

| Area                       | Properties                             |
| -------------------------- | -------------------------------------- |
| Margin and padding         | Top, bottom, left, right               |
| Position                   | Top, bottom, left, right               |
| Column and row gaps        | Display settings, Quick Stack          |
| Dimensions                 | Height, width (including min and max)  |
| Grid                       | Column and row sizes                   |
| Typography                 | Font size, line height, letter spacing |
| Border                     | Radius, width                          |
| Filter and backdrop filter | Blur radius                            |

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_MODE:"VariableMode",
    VARIABLE_REFERENCE:"SizeVariable",
    CUSTOM_VALUE:"CustomValue",
    SIZE_VALUE:"SizeValue"
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
      <p>A reference to another size variable
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
      <code>{`{"type": "custom", "value": "clamp(1rem, 2vw, 2rem)"}`}</code>
    </p>),
    SIZE_VALUE: (
      <p>The size value object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{ value: 16, unit: "px" }`}</code>
    </p>)
  }}
>
  ```typescript
  collection.createSizeVariable(
    name: string,
    value: {{SIZE_VALUE}} | {{VARIABLE_REFERENCE}} | {{CUSTOM_VALUE}},
    options?: {
      mode?: {{VARIABLE_MODE}}
    }
  ): Promise<SizeVariable>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **name** : *string* - Name of the variable

* **value**:
  * *SizeValue* - Object with the unit and value of the size. `{unit: SizeUnit, value: number}`
    * **SizeUnit** See the accordion below for the list of supported units.

      <Accordion title="Size Units">
        #### Absolute Units

        | Unit | Name   | Description                                       | Example Usage      |
        | ---- | ------ | ------------------------------------------------- | ------------------ |
        | `px` | Pixels | Absolute unit, 1px equals one pixel on the screen | `font-size: 16px;` |

        #### Relative Units

        | Unit  | Name                | Description                                                   | Example Usage     |
        | ----- | ------------------- | ------------------------------------------------------------- | ----------------- |
        | `em`  | Element-relative Em | Relative to parent element's font size (2em = 2× parent font) | `padding: 1.5em;` |
        | `rem` | Root Em             | Relative to root element's font size                          | `margin: 2rem;`   |
        | `ch`  | Character Units     | Relative to width of '0' (zero) character                     | `width: 20ch;`    |

        #### Viewport-based Units

        | Unit   | Name             | Description                        | Example Usage    |
        | ------ | ---------------- | ---------------------------------- | ---------------- |
        | `vh`   | Viewport Height  | 1% of viewport height              | `height: 50vh;`  |
        | `vw`   | Viewport Width   | 1% of viewport width               | `width: 80vw;`   |
        | `vmin` | Viewport Minimum | 1% of viewport's smaller dimension | `margin: 2vmin;` |
        | `vmax` | Viewport Maximum | 1% of viewport's larger dimension  | `margin: 2vmax;` |

        #### Dynamic Viewport Units

        | Unit  | Name                    | Description                                          | Example Usage         |
        | ----- | ----------------------- | ---------------------------------------------------- | --------------------- |
        | `dvh` | Dynamic Viewport Height | Adjusts to viewport height changes (mobile browsers) | `min-height: 100dvh;` |
        | `dvw` | Dynamic Viewport Width  | Adjusts to viewport width changes                    | `max-width: 50dvw;`   |
        | `svh` | Small Viewport Height   | Viewport height for small screens                    | `height: 60svh;`      |
        | `svw` | Small Viewport Width    | Viewport width for small screens                     | `width: 40svw;`       |
        | `lvh` | Large Viewport Height   | Viewport height for large screens                    | `height: 75lvh;`      |
        | `lvw` | Large Viewport Width    | Viewport width for large screens                     | `width: 100lvw;`      |
      </Accordion>
  * *SizeVariable* - A reference to another size variable
  * [*CustomValue*](/designer/reference/variables-detail-overview#custom-values) - A custom value for the variable

* **options**: *object* - Optional parameters for the variable.
  * **mode**: *VariableMode* - The [variable mode](/designer/reference/variable-modes) object. Get the variable mode by using the [`collection.getVariableModeByName()`](/designer/reference/get-variable-mode-by-name) method.

### Returns

**Promise\<*SizeVariable*>**

A Promise that resolves to a SizeVariable object

### Example

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection()

// Create Size Variable with a Size Value
const mySizeVariable = await collection?.createSizeVariable("Defualt Padding", { unit: "px", value: 50 })
console.log(mySizeVariable)

// Create a Size Variable with a Custom Value
const myCustomSizeVariable = await collection?.createSizeVariable("h1-font-size", {
  type: "custom",
  value: "clamp(1rem, 2vw, 2rem)",
})
console.log(myCustomSizeVariable)


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
