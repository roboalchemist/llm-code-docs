# Source: https://developers.webflow.com/designer/reference/remove-all-variable-modes.mdx

***

title: Remove all variable modes
slug: reference/remove-all-variable-modes
description: Remove all variable modes from a style
hidden: false
-------------

## `style.removeAllVariableModes(options)`

Remove all [variable modes](/designer/reference/variable-modes) from a style.

<br />

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
  }}
  tooltips={{
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
  style.emoveAllVariableModes(
    options?: {
      breakpointId?: BreakpointId
      pseudoStateKey?: PseudoStateKey
    }
  ): Promise<null>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **options?**: *BreakpointAndPseudo* - The [breakpoint and pseudo state](/designer/reference/styles-overview#responsive-styling-with-breakpoints-and-pseudo-states) for the style.
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

A promise that resolves to `null`.

#

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

if (selectedElement?.styles) {

// Get Styles
const styles = await selectedElement.getStyles()
const primaryStyle = styles[0] // Get the primary style

// Get Variable Modes
const remove = await primaryStyle?.removeAllVariableModes()
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability         | Locale | Branch | Workflow | Sitemode |
| :----------------------- | :----- | :----- | :------- | :------- |
| **canModifyStyleBlocks** | Any    | Any    | Canvas   | Design   |
