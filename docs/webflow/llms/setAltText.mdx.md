# Source: https://developers.webflow.com/designer/reference/image-element/setAltText.mdx

***

title: Set Alt Text
slug: designer/reference/image-element/setAltText
description: Set the Alt Text for an Image element on the canvas.
hidden: false
'og:title': 'Webflow Designer API: Image Element - setAltText()'
'og:description': Set the Alt Text for an Image element on the canvas.
----------------------------------------------------------------------

## `element.setAltText(altText)`

Set the Alt Text for an Image element on the canvas.

## Syntax

```typescript
element.setAltText(altText: string | null): Promise<null>
```

## Parameters

* **alt text**:  *string* - The alternate text for an image

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`

## Example

```typescript
// Get Selected Element
const el = await webflow.getSelectedElement()

// Check element type
if (el?.type === 'Image') {
  // Set alt text
  await el.setAltText('Descriptive alternative text for this image')

  // Verify by getting the alt text
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

| Designer Ability      | Locale | Branch | Workflow | Sitemode |
| :-------------------- | :----- | :----- | :------- | :------- |
| canModifyImageElement | any    | main   | canvas   | any      |

```
```
