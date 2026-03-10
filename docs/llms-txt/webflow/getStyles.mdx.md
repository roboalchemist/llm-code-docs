# Source: https://developers.webflow.com/designer/reference/element-styles/getStyles.mdx

***

title: Get Styles
slug: designer/reference/element-styles/getStyles
description: Retrieve the current style properties of the element for analysis or changes.
hidden: false
'og:title': 'Webflow Designer API: Get Styles'
'og:description': Retrieve the current style properties of the element for analysis or changes.
-----------------------------------------------------------------------------------------------

## `element.getStyles()`

Retrieve the current style properties of the element for analysis or changes.

## Syntax

```typescript
element.getStyles(): Promise<Array<Style>>
```

## Returns

**Promise\<*Style*>**

A Promise that resolves to an array of [Style Objects](/designer/reference/styles-overview).

## Example

```javascript
// Get Selected Element
const selectedElement = await Webflow.getSelectedElement()

if (selectedElement?.styles) {

  // Get Styles
  const styles = await selectedElement.getStyles()

  // Get Style Details
  const styleDetails = styles.map(async style => {

    const styleName = await style.getName()
    const styleProperties = await style.getProperties()

    return {
      Name: styleName,
      Properties: styleProperties,
      ID: style.id,
    }

  })

  // Print Style Details
  console.log(await Promise.all(styleDetails))
}
```

## Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | Any      |

```
```
