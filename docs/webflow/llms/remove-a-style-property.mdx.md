# Source: https://developers.webflow.com/designer/reference/remove-a-style-property.mdx

***

title: Remove a style property
slug: designer/reference/remove-a-style-property
description: ''
hidden: false
'og:title': 'Webflow Designer API: Remove a style property'
'og:description': Remove a single style-property from a Style object.
---------------------------------------------------------------------

## **`style.remove(prop, options?)`**

Remove a single style-property from a Style object.

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    STYLE_PROPERTY: "StyleProperty",
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
  }}
  tooltips={{
    STYLE_PROPERTY: (
      <p>The property to remove. See the <a href="/designer/reference/style-properties">Style Properties</a> reference for a list of supported properties.
    </p>),
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to remove the property from.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to remove the property from.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
  }}
>
  ```typescript
  style.removeProperty(
    prop: {{STYLE_PROPERTY}},
    options?: {
      breakpointId?: {{BREAKPOINT_ID}},
      pseudoStateKey?: {{PSEUDO_STATE_KEY}}
    }
  ): Promise<void>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **`prop`**: *StyleProperty* - The name of the property to remove from the style. See the [Style Properties](/designer/reference/style-properties) reference for a list of supported properties.
* **`options`**: *BreakpointAndPseudo* - An object that lets you filter properties by breakpoint and/or pseudo-state. (Optional)

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

**Promise\<`void`>**

A Promise that resolves to `undefined`

### Example

```typescript
removeSingleStyleProperty: async (property: StyleProperty) => {

  // Get Selected Element
  const selectedElement = await webflow.getSelectedElement()

  if (selectedElement?.styles) {

    // Get Element Styles
    const styles = await selectedElement.getStyles()
    const primaryStyle = styles[0]
    await primaryStyle.removeProperty(property) // Remove the property from the style

  }
},
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
