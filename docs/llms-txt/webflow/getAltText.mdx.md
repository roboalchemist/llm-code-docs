# Source: https://developers.webflow.com/designer/reference/image-element/getAltText.mdx

***

title: Get Alt Text
slug: designer/reference/image-element/getAltText
description: Retrieve the Alt Text for an Image element on the canvas.
hidden: false
'og:title': 'Webflow Designer API: Image Element - getAltText()'
'og:description': Retrieve the alt text for an Image element on the canvas.
---------------------------------------------------------------------------

## `element.getAltText()`

Retrieve the alt text for an Image element on the canvas. If the Image element doesn't have alt text, the API will retrieve the alt text from the associated Asset.

## Syntax

```typescript
element.getAltText(): Promise<string>
```

## Returns

**Promise\<*String*>**

A Promise that resolves to the string of alt text.

## Example

```typescript
// Get Selected Element
const el = await webflow.getSelectedElement()
if (el?.type === 'Image') {
  // Get alt text
  const alt = await el.getAltText()
  console.log(alt)
} else {
  console.error('Please select an image element')
  await webflow.notify({
    type: 'Error',
    message: 'Please select an Image Element',
  })
}
```

## Designer Ability

Checks for authorization only

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| canAccessAssets  | any    | any    | any      | any      |

```
```
