# Source: https://developers.webflow.com/designer/reference/remove-variable-mode-style.mdx

***

title: Remove variable mode on a style
slug: reference/remove-variable-mode-style
description: Remove a variable mode from a style
hidden: false
-------------

## `style.removeVariableMode(collection, options)`

Remove a [variable mode](/designer/reference/variable-modes) from a style, by using the [variable collection](/designer/reference/variable-collections-overview) that belongs to the variable mode.

<br />

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    VARIABLE_COLLECTION: "VariableCollection",
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
  }}
  tooltips={{
    VARIABLE_COLLECTION: (
      <p>The variable collection to remove the variable mode from.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{"id": "collection-81b8fa46-aa26-f1ef-e265-a87ef3be63a5"}`}</code>
    </p>),
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to remove the variable mode from.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to remove the variable mode from.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
  }}
>
  ```typescript
  style.removeVariableMode(
    collection: {{VARIABLE_COLLECTION}},
    options?: {
      breakpointId?: {{BREAKPOINT_ID}},
      pseudoStateKey?: {{PSEUDO_STATE_KEY}}
    }
  ): Promise<null>;
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **collection**: *VariableCollection* - The variable collection that belongs to the variable mode.
* **options?**: *BreakpointAndPseudo* - The [breakpoint and pseudo state](/designer/reference/styles-overview#responsive-styling-with-breakpoints-and-pseudo-states) for the style.

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

await primaryStyle?.removeVariableMode(variableCollection)
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
