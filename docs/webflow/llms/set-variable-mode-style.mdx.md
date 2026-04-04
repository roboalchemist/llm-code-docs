# Source: https://developers.webflow.com/designer/reference/set-variable-mode-style.mdx

***

title: Set variable mode on a style
slug: reference/set-variable-mode-style
description: Set a variable mode for a style
hidden: false
-------------

## `style.setVariableMode(collection, mode, options?)`

Apply a [variable mode](/designer/reference/variable-modes) to a style. Each variable mode belongs to a [variable collection](/designer/reference/variable-collections-overview). To apply a variable mode, you must provide the variable collection that belongs to the variable mode.

<br />

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_MODE: "VariableMode",
    VARIABLE_COLLECTION: "VariableCollection",
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
  }}
  tooltips={{
    VARIABLE_MODE: (
      <p>The variable mode object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "mode-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    VARIABLE_COLLECTION: (
      <p>The variable collection object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "collection-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to set the variable mode for.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to set the variable mode for.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
  }}
>
  ```typescript
   style.setVariableMode(
      collection: {{VARIABLE_COLLECTION}},
      mode: {{VARIABLE_MODE}},
      options?: {
        breakpointId?: {{BREAKPOINT_ID}},
        pseudoStateKey?: {{PSEUDO_STATE_KEY}}
      }
    ): Promise<null>;
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **collection**: *VariableCollection* - The [variable collection](/designer/reference/variable-collections-overview) that belongs to the variable mode.
* **mode**: *VariableMode* - The [variable mode](/designer/reference/variable-modes) to set.
* **options?**: *BreakpointAndPseudo* - An object that lets you filter properties by breakpoint and/or pseudo-state. (Optional)

  * **`BreakpointId`**: Identifies the responsive breakpoint to get styles for.
    ```typescript
    type BreakpointId = "xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"
    ```

  * **`PseudoStateKey`**: Specifies a CSS pseudo-class to get styles for.
    ```typescript
    type PseudoStateKey = "noPseudo" | "nth-child(odd)" | "nth-child(even)" |
      "first-child" | "last-child" | "hover" | "active" | "pressed" |
      "visited" | "focus" | "focus-visible" | "focus-within" |
      "placeholder" | "empty" | "before" | "after"
    ```

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

    if (selectedElement?.styles) {
    // Get Styles
    const styles = await selectedElement.getStyles()
    const primaryStyle = styles[0] // Get the primary style

    // Get Variable Collection
    const variableCollection = await webflow.getDefaultVariableCollection()
    const variableModes = await variableCollection?.getAllVariableModes()
    const variableMode = variableModes[0]

    // Set Variable Mode
    if (primaryStyle && variableCollection) {
        await primaryStyle.setVariableMode(variableCollection, variableMode)
        console.log('Variable mode set successfully')
    }
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer Ability         | Locale | Branch | Workflow | Sitemode |
| :----------------------- | :----- | :----- | :------- | :------- |
| **canModifyStyleBlocks** | Any    | Any    | Canvas   | Design   |
