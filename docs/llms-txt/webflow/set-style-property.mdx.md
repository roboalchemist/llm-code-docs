# Source: https://developers.webflow.com/designer/reference/set-style-property.mdx

***

title: Set style property
slug: designer/reference/set-style-property
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set style property'
'og:description': >-
Manage the CSS of a Style by setting a specific style property at the given
breakpoint and pseudo-state.
----------------------------

## **`style.setProperty(prop, value, options?)`**

Manage the CSS of a Style by setting a specific style property at the given breakpoint and pseudo-state.

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
      <p>The property to set. See the <a href="/designer/reference/style-properties">Style Properties</a> reference for a list of supported properties.
    </p>),
    VALUE: (
      <p>The value to set. You can set the value to a string or a [variable reference](/designer/reference/variables-overview).
    </p>),
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to set the style property for.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to set the style property for.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
  }}
>
  ```typescript
   style.setProperty(
    prop: {{STYLE_PROPERTY}},
    value: string | VariableReference,
    options?: {
      breakpointId?: {{BREAKPOINT_ID}},
      pseudoStateKey?: {{PSEUDO_STATE_KEY}}
    }
  ): Promise<void>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **`prop`**: *StyleProperty* - The property to set. See the [Style Properties](/designer/reference/style-properties) reference for a list of supported properties.
* **`value`**: *String* | *VariableReference* - The value to set. You can set the value to a string or a [variable reference](/designer/reference/variables-overview).
* **`options`**: *BreakpointAndPseudo* - An object that lets you filter properties by breakpoint and/or pseudo-state. (Optional)

  * **`BreakpointId`**: Identifies the responsive breakpoint to set the style property for.
    ```typescript
    type BreakpointId = "xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"
    ```

  * **`PseudoStateKey`**: Specifies a CSS pseudo-class to set the style property for.
    ```typescript
    type PseudoStateKey = "noPseudo" | "nth-child(odd)" | "nth-child(even)" |
      "first-child" | "last-child" | "hover" | "active" | "pressed" |
      "visited" | "focus" | "focus-visible" | "focus-within" |
      "placeholder" | "empty" | "before" | "after"
    ```

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`

### Example

```typescript
// Retrieve the style by name
const retrievedStyle = await webflow.getStyleByName(styleName);

// Set Style Properties
const options: BreakpointAndPseudo = { breakpoint: "xl", pseudo: "hover" }
await retrievedStyle?.setProperty('background-color', 'blue', options)
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
