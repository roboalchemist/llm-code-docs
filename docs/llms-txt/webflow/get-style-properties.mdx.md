# Source: https://developers.webflow.com/designer/reference/get-style-properties.mdx

***

title: Get style properties
slug: designer/reference/get-style-properties
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get style properties'
'og:description': Retrieves the CSS properties of the specified Style Object.
-----------------------------------------------------------------------------

## **`style.getProperties(options?)`**

Retrieves the CSS properties of the specified Style Object. Additionally, you can get properties on a style for a specific breakpoint or pseudo-state.

See the [style properties list](/designer/reference/style-properties) for an index of CSS properties to set on a style.

### Syntax

{/* <!-- vale off --> */}

<Template
  data={{
    BREAKPOINT_ID: "BreakpointId",
    PSEUDO_STATE_KEY: "PseudoStateKey",
    PROPERTY_MAP: "PropertyMap",
  }}
  tooltips={{
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
      <p>A dictionary of style properties and their values.
      <br />
      <code>{`{
        'background-color': "blue",
        'font-size': "16px",
        'font-weight': "bold",
      }`}</code>
    </p>),
  }}
>
  ```typescript
  style.getProperties(
    options?: {
      breakpoint?: {{BREAKPOINT_ID}},
      pseudo?: {{PSEUDO_STATE_KEY}}
    }
  ): Promise<{{PROPERTY_MAP}}>
  ```
</Template>

{/* <!-- vale on --> */}

### Parameters

* **options**:  An object that lets you filter properties by breakpoint and pseudo-state. (optional)

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

**Promise\<*PropertyMap*>**

A Promise that resolves to a [*PropertyMap* ](/designer/reference/style-properties)object. A dictionary of style properties and their values.

#### Example

```typescript
// Get selected element
const element = await webflow.getSelectedElement()

if (element?.styles) {

  // Get Element Styles
  const styles = await element.getStyles()

  // Initialize an empty object to store all properties
  const allProperties: { [key: string]: any } = {};

  for (let style of styles) {
    // Use string type for styleName
    const styleName: string = await style.getName();
    const breakpoint : BreakpointAndPseudo = {breakpoint: 'xxl'}
    const properties = await style.getProperties(breakpoint);
    allProperties[styleName] = properties;
  }

  console.log(allProperties);

}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | An       |
