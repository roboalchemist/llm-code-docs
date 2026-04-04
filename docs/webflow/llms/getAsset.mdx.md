# Source: https://developers.webflow.com/designer/reference/image-element/getAsset.mdx

***

title: Get Asset
slug: designer/reference/image-element/getAsset
description: Retrieve an asset from an Image element.
hidden: false
'og:title': 'Webflow Designer API: Image Element - getAsset()'
'og:description': Retrieve an asset from an Image element.
----------------------------------------------------------

## `element.getAsset()`

Retrieve an asset from an Image element.

## Syntax

```typescript
element.getAsset(): Promise<Asset | null>
```

## Returns

**Promise\<*Asset*>** | `null`

A Promise that resolves to an Asset. If an element doesn't have an asset, the method will return `null`

## Example

```typescript
// Get Selected Element
const el = await webflow.getSelectedElement()

// Check if element can have children
if (el?.children) {
  // Create a new Image Element using Element Presets
  const imgEl = await el.append(webflow.elementPresets.Image)

  // Check element type
  if (imgEl.type === 'Image') {
    // Get asset from Image element
    const myAsset = await imgEl.getAsset()
    console.log(myAsset)
    }
}
```

## Designer Ability

Checks for authorization only

| Designer Ability | Locale | Branch | Workflow | Sitemode |
| :--------------- | :----- | :----- | :------- | :------- |
| canAccessAssets  | any    | any    | any      | any      |

```
```
