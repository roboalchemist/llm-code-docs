# Source: https://developers.webflow.com/designer/reference/styles-overview.mdx

***

title: Styles
slug: designer/reference/styles-overview
description: ''
hidden: false
'og:title': 'Webflow Designer API: Styles'
'og:description': >-
The Styles APIs enable Apps to customize the look and feel of Elements,
helping designers create consistent and responsive pro websites. Use these
methods to create styles, use CSS to adjust their look and feel through style
properties, and apply styles to multiple elements throughout a page.
--------------------------------------------------------------------

Customize the look and feel of Elements with Styles. Styles, [also referred to as Classes in the Designer](https://university.webflow.com/lesson/web-styling-using-classes?topics=layout-design), save styling information that can be applied to as many elements as you want across a site.

## Working with styles

<Steps>
  <Step title="Create a style">
    To create a style, you need to provide a unique name. The Webflow API prevents creating styles with duplicate names to maintain uniqueness across your project.

    ```typescript
    // Create new style
    const newStyle = await webflow.createStyle(styleName);
    ```
  </Step>

  <Step title="Add style properties">
    Add CSS properties to a style. [Refer to this list of Style Properties](/designer/reference/style-properties) for a full index of properties that can added to a style in Webflow.

    You can add properties to a style in two ways:

    <Tabs>
      <Tab title="Set a single property">
        The [`set property`](/designer/reference/set-style-property) method requires you to pass a single property name and its corresponding value as `string` parameters. Additionally, you can include an optional `options`  parameter, [which we cover below.](#responsive-styling-with-breakpoints-and-pseudo-states)

        ```typescript
        // Create new style
        const newStyle = await webflow.createStyle("My Custom Style");

        // Set a single property
        await newStyle.setProperty("background-color", "blue")
        ```
      </Tab>

      <Tab title="Set multiple properties">
        The [set properties](/designer/reference/set-style-properties) method allows you to set multiple properties at once through  a *PropertyMap* parameter.

        A ***PropertyMap*** is a TypeScript object that maps CSS property names to their corresponding values. Each key in the object represents a CSS property name, while the value can be either a string literal (like "16px" or "bold") or a Webflow Variable (like a ColorVariable or SizeVariable).

        ```typescript
        // Create new style
        const newStyle = await webflow.createStyle("My Custom Style");

        // Create a variable
        const collection = await webflow.getDefaultVariableCollection()
        const webflowBlue = await collection?.createColorVariable('Webflow Blue', '#146EF5')

        // Create a PropertyMap object
        const propertyMap : PropertyMap = {
                        'background-color': webflowBlue as ColorVariable,
                        'font-size': "16px",
                        'font-weight': "bold",
                      }

        // Set style properties
        await newStyle.setProperties(propertyMap)
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Apply styles to elements">
    Once you've created and modified a style, you can apply it to one or more elements.

    <CodeBlock>
      ```typescript
      // Get selected element
      const selectedElement = await webflow.getSelectedElement()

      // Get style
      const myStyle = await webflow.getStyleByName("My Custom Style");

      // Apply style to element
      await selectedElement.setStyles([newStyle])
      ```
    </CodeBlock>
  </Step>
</Steps>

## Responsive styling with [breakpoints and pseudo states](https://university.webflow.com/lesson/intro-to-breakpoints?topics%3Dlayout-design\&sa=D\&source=docs\&ust=1706631470173943\&usg=AOvVaw1itdh_-wDf_3NgNzP2w-N8)

Webflow's responsive design features enable customization of style properties for different contexts, such as varying screen sizes or specific states like `:hover` or `:active`.

Pass the `options` parameter when setting style properties to customize the style for different breakpoints and pseudo-states.

```typescript
{
  breakpoint?: BreakpointId
  pseudo?: PseudoStateKey
}
```

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

**Example**

```typescript
// Create new style
const newStyle = await webflow.createStyle("My Custom Style");

// Property Map for XXL Breakpoint
const propertyMapXXL = {
  'font-size': "16px",
  'font-weight': "bold",
}

// Property Map for Medium Breakpoint
const propertyMapMedium = {
  'font-size': "12px",
  'font-weight': "bold",
}

// Set style properties for XXL Breakpoint and hover state
await newStyle.setProperties(propertyMapXXL, {breakpoint: "xxl", pseudo: "hover"})

// Set styles for Medium Breakpoint and hover state
await newStyle.setProperties(propertyMapMedium, {breakpoint: "medium", pseudo: "hover"})
```

### Breakpoint IDs

| Breakpoint ID | Description                                    |
| :------------ | :--------------------------------------------- |
| `xxl`         | Very large screens or high-resolution monitors |
| `xl`          | Large desktop monitors                         |
| `large`       | Standard desktop monitors                      |
| `main`        | Suitable for smaller desktops or large tablets |
| `medium`      | Suitable for tablets and some large phones     |
| `small`       | Suitable for larger mobile devices             |
| `tiny`        | Suitable for the smallest mobile devices       |

### Pseudo-State Keys

| Pseudo-State      | Designer State     | Description                                        |
| :---------------- | :----------------- | :------------------------------------------------- |
| `hover`           | Hover              | Element is hovered over by the mouse               |
| `pressed`         | Pressed            | Element is in pressed state                        |
| `visited`         | Visited            | **Link** element has been visited                  |
| `focus`           | Focused            | Element has keyboard/input focus                   |
| `focus-visible`   | Focused (Keyboard) | Element has keyboard focus with visible indicator  |
| `focus-within`    | --                 | Element or its descendant has focus                |
| `placeholder`     | Placeholder        | Placeholder text in form block inputs              |
| `first-child`     | First Item         | First Collection Item in a collection list         |
| `last-child`      | Last Item          | Last Collection Item in a collection list          |
| `nth-child(odd)`  | Odd Items          | Odd-numbered Collection Item in a collection list  |
| `nth-child(even)` | Even Items         | Even-numbered Collection Item in a collection list |

## FAQs

<Accordion title="Can I style HTML Tags with the Webflow API?">
  No, you can't style HTML Tags with the Designer API. Currently, the Designer API only supports creating and applying CSS Classes.
</Accordion>
