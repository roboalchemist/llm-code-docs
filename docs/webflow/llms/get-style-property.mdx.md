# Source: https://developers.webflow.com/designer/reference/get-style-property.mdx

***

title: Get style property
slug: designer/reference/get-style-property
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get style property'
'og:description': Retrieve the value of a specific property in a Style.
-----------------------------------------------------------------------

## **`style.getProperty(prop, options?)`**

Retrieve the value of a specific css property in a Style object.

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    STYLE_PROPERTY: "StyleProperty",
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
    PROPERTY_MAP: "PropertyMap[p]",

  }}
  tooltips={{
    STYLE_PROPERTY: (
      <p>The property to get. See the <a href="/designer/reference/style-properties">Style Properties</a> reference for a list of supported properties.
    </p>),
      BREAKPOINT_ID: (
      <p>The responsive breakpoint to get styles for.
      <br />
      <code>{`"xxl" | "xl" | "large" | "main" | "medium" | "small" | "tiny"`}</code>
    </p>),
    PSEUDO_STATE_KEY: (
      <p>The CSS pseudo-class to get styles for.
      <br />
      <code>{`"noPseudo" | "nth-child(odd)" | "nth-child(even)" | "first-child" | "last-child" | "hover" | "active" | "pressed" | "visited" | "focus" | "focus-visible" | "focus-within" | "placeholder" | "empty" | "before" | "after"`}</code>
    </p>),
    PROPERTY_MAP: (
      <p>The value of the provided style property, if one exists.
    </p>),
  }}
>
  ```typescript
  style.getProperty(
    prop: {{STYLE_PROPERTY}},
    options?: {
      breakpointId?: {{BREAKPOINT_ID}},
      pseudoStateKey?: {{PSEUDO_STATE_KEY}}
    }
  ): Promise<null | {{PROPERTY_MAP}}>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **`prop`**: *StyleProperty* - The property to get. See the [Style Properties](/designer/reference/style-properties) reference for a list of supported properties.
* **options**: An object that lets you filter properties by breakpoint and/or pseudo-state.

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

**Promise\<*PropertyMap\[p]* | *Variable* | `null`>**

Returns a Promise that resolves to:

* *PropertyMap\[p]* - The value of the provided style property, if one exists.
* A [Variable](/designer/reference/variables-overview) representing the value of the provided style property, if a variable is used as the value of the provided style property.
* `null` - If value doesn't exist for the provided style property, this method will return `null`.

### Example

```typescript
// Get Selected Element
const selectedElement = await webflow.getSelectedElement()

// Get Element Styles
if (selectedElement?.styles) {

    const styles = await selectedElement.getStyles()
    const selectedPropertyList = await Promise.all(styles.map(async style => {

      const styleName = await style.getName()
      const property = await style.getProperty(`box-shadow`)
      console.log(`Style Name: ${styleName}, box-shadow: ${property}`)

    }))

  }
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | An       |
