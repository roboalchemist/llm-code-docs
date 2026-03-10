# Source: https://developers.webflow.com/designer/reference/element-styles/setStyles.mdx

***

title: Set Styles
slug: designer/reference/element-styles/setStyles
description: Set styles on an element.
hidden: false
'og:title': 'Webflow Designer API: Set Styles'
'og:description': Set styles on an element.
-------------------------------------------

## `element.setStyles(styles)`

Set styles on an element.

## Syntax

```typescript
element.setStyles(styles: Array<Style>): Promise<null>>
```

## Parameters

* **`Styles`**: *Array* of [Style Objects](/designer/reference/styles-overview) - The array of styles to set.

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

## Example

```javascript
// Get Selected Element
const selectedElement = await Webflow.getSelectedElement()

if (selectedElement?.styles) {

  // Create a new style
  const newStyle = await Webflow.createStyle("MyCustomStyle");

  // Set properties for the style
  newStyle.setProperties({
    'background-color': "blue",
    'font-size': "32px",
    'font-weight': "bold",
  });

  // Set style on selected element
  selectedElement.setStyles([newStyle])

}
```
