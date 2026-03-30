# Source: https://developers.webflow.com/designer/reference/remove-variable-modes-style.mdx

***

title: Remove variable modes
slug: reference/remove-variable-modes-style
description: Remove multiple variable modes from a style
hidden: false
-------------

## `style.removeVariableModes(props, options)`

Remove multiple [variable modes](/designer/reference/variable-modes) from a style. Each variable mode is associated with a [variable collection](/designer/reference/variable-collections-overview). To remove multiple variable modes, provide an array of variable mode objects.

<br />

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_MODES: "VariableModes",
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
  }}
  tooltips={{
    VARIABLE_MODES: (
      <p>The variable modes to remove.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`[{"id": "mode-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}]`}</code>
    </p>),
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to remove the variable modes from.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to remove the variable modes from.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
  }}
>
  ```typescript
  style.removeVariableModes(
      modes: Array<{{VARIABLE_MODES}}>,
      options?: {
        breakpointId?: {{BREAKPOINT_ID}},
        pseudoStateKey?: {{PSEUDO_STATE_KEY}}
      }
  ): Promise<null>;
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **`modes`**: *Array\<VariableMode>* - An array of [variable modes](/designer/reference/variable-modes) to remove.
* **`options?`**: *BreakpointAndPseudo* - An object t hat lets you filter properties by breakpoint and/or pseudo-state. (Optional)

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

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.styles) {
// Get Styles
const styles = await selectedElement.getStyles()
const primaryStyle = styles[0] // Get the primary style

// Get Variable Modes from Collection
const variableModes = await variableCollection?.getAllVariableModes()
const remove = await primaryStyle?.removeVariableModes(variableModes)

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
