# Source: https://developers.webflow.com/designer/reference/set-style-properties.mdx

***

title: Set style properties
slug: designer/reference/set-style-properties
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set style properties'
'og:description': Set multiple style-properties on a style.
-----------------------------------------------------------

## **`style.setProperties(props, options?)`**

Set multiple style-properties on a Style object.

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    PROPERTY_MAP: "PropertyMap",
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
  }}
  tooltips={{
    PROPERTY_MAP: (
      <p>An object of style properties and their values. See the <a href="/designer/reference/style-properties">Style Properties</a> reference for a list of supported properties.
      <br />
      <strong>Example:</strong>
      <br />
      <code>{`{
        'background-color': "blue",
        'font-size': "16px",
        'font-weight': "bold",
      }`}</code>
    </p>),
    BREAKPOINT_ID: (
      <p>The responsive breakpoint to set the properties for.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to set the properties for.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
  }}
>
  ```typescript
   style.setProperties(
    props: {{PROPERTY_MAP}},
    options?: {
      breakpointId?: {{BREAKPOINT_ID}},
      pseudoStateKey?: {{PSEUDO_STATE_KEY}}
    }
  ): Promise<void>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **`props`**: *PropertyMap* - An object of style properties and their values. See the [Style Properties](/designer/reference/style-properties) reference for a list of supported properties.
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

**Promise\<`null`>**

A Promise that resolves to `null`

### Example

```typescript
// Create a new style
const newStyle = await webflow.createStyle('MyCustomStyle')

const propertyMap : PropertyMap = {
    'background-color': "blue",
    'font-size': "16px",
    'font-weight': "bold",
  }
const myBreakpoint = {breakpoint: "medium"} as BreakpointAndPseudo

// Set and save properties for the style
await newStyle.setProperties(propertyMap, myBreakpoint);
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
