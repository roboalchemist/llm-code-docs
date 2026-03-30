# Source: https://developers.webflow.com/designer/reference/set-variable-modes-style.mdx

***

title: Set variable modes on a style
slug: reference/set-variable-modes-style
description: Apply multiple variable modes to a style
hidden: false
-------------

## `style.setVariableModes(props, options?)`

Apply multiple [variable modes](/designer/reference/variable-modes) to a style. Each variable mode belongs to a [variable collection](/designer/reference/variable-collections-overview). To apply multiple variable modes, you must provide a map of variable collection IDs to their corresponding variable mode IDs.

<br />

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_MODE_STYLE_PROPERTY_MAP: "VariableModeStylePropertyMap",
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
  }}
  tooltips={{
    VARIABLE_MODE_STYLE_PROPERTY_MAP: (
      <p>The variable mode style property map object.
      <br />
      <code>{`{"collection-81b8fa46-aa26-f1ef-e265-a87ef3be63a5": "mode-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to set the variable modes for.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to set the variable modes for.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
  }}
>
  ```typescript
  style.setVariableModes(
      props: {{VARIABLE_MODE_STYLE_PROPERTY_MAP}},
      options?: {
        breakpointId?: {{BREAKPOINT_ID}},
        pseudoStateKey?: {{PSEUDO_STATE_KEY}}
      }
  ): Promise<null>;
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **props**: *VariableModeStylePropertyMap* - A map of variable collection IDs to their corresponding variable mode IDs.
  ```typescript title="VariableModeStylePropertyMap"
  // Example
  const props: VariableModeStylePropertyMap = {
  "collection-09e4110d-f4b6-45f9-3c1b-614c748a01c6": "mode-2a4f8a4e-eb9b-be56-f773-9e88c3669955",
  "collection-b799d4ac-670a-8296-0f2c-e153c4b1b46b": "base",
  "collection-cd77d4e3-58e8-aac2-e2e4-4f567d399c4b": "mode-f780f7e7-1b41-b353-f931-13de2c4a1234",
  "collection-e4fba320-a8ce-aad6-a302-8f95cdac2c6a": "mode-a4a9e6df-f2a6-f5e8-97e9-59f264e37b90"
  }
  ```
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
// This example gets variable modes from the style of the currently selected element, then sets them a chosen style

// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.styles) {
    // Get Styles
    const styles = await selectedElement.getStyles()
    const primaryStyle = styles?.[0] // Get the primary style
    const variableModes = await primaryStyle?.getVariableModes()

    // Set Variable Modes on Selected Style
    if (variableModes) {
        await selectedStyle?.setVariableModes(variableModes)
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
