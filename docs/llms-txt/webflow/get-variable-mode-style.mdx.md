# Source: https://developers.webflow.com/designer/reference/get-variable-mode-style.mdx

***

title: Get variable mode
slug: reference/get-variable-mode-style
description: Learn how to get a variable mode applied to a style.
hidden: null
------------

## `style.getVariableMode(VariableCollecton, options?)`

Retrieve the [variable mode](/designer/reference/variable-modes) applied to a style for a given [variable collection](/designer/reference/variable-collections-overview). A collection can define multiple modes, but a style can have only one variable mode applied per collection.

<br />

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
    VARIABLE_COLLECTION: "VariableCollection",
    VARIABLE_MODE: "VariableMode",
  }}
  tooltips={{
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to get the variable mode for.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to get the variable mode for.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
    VARIABLE_COLLECTION: (
      <p>The variable collection to get the variable mode for.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "collection-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    VARIABLE_MODE: (
      <p>The variable mode object.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "mode-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
  }}
>
  ```typescript
  style.getVariableMode(
      collection: {{VARIABLE_COLLECTION}},
      options?: {
        breakpointId?: {{BREAKPOINT_ID}},
        pseudoStateKey?: {{PSEUDO_STATE_KEY}}
      }
  ): Promise<{{VARIABLE_MODE}} | null>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **collection**: *VariableCollection* - The variable collection of the variable mode.
* **options?**: *BreakpointAndPseudo* - The [breakpoint and pseudo state](/designer/reference/styles-overview#responsive-styling-with-breakpoints-and-pseudo-states) for the style.
  * **`BreakpointId`**: Identifies the responsive breakpoint to get styles for.
    ```typescript
    type BreakpointId = "xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"
    ```

  * **`PseudoStateKey`**: Specifies a CSS pseudo-class to get styles for.
    ```typescript
    type PseudoStateKey = "noPseudo" | "nth-child(odd)" | "nth-child(even)" |
      "first-child" | "last-child" | "hover" | "active" | "pressed" |
    ```

### Returns

A Promise that resolves to a `VariableMode` object or `null` if the variable mode isn't found.

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

    if (selectedElement?.styles) {
    // Get Styles
    const styles = await selectedElement.getStyles()
    const primaryStyle = styles[0] // Get the primary style

    // Get Variable Mode
    if (primaryStyle && variableCollection) {
        const variableMode =
        await primaryStyle.getVariableMode(variableCollection)
        const variableModeName = await variableMode?.getName()
        console.log(variableModeName)
    }
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
