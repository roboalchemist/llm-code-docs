# Source: https://developers.webflow.com/designer/reference/image-element/setAsset.mdx

***

title: Set Asset
slug: designer/reference/image-element/setAsset
description: Add an asset to an Image element.
hidden: false
'og:title': 'Webflow Designer API: Image Element - setAsset()'
'og:description': Add an asset to an Image element.
---------------------------------------------------

## `element.setAsset(asset)`

Add an asset to an Image element.

## Syntax

```typescript
element.setAsset(asset: Asset | null): Promise<null>
```

## Parameters

* **Asset**:  *Asset* - The asset to be inserted into the Image Element. Can be retrieved with the method `webflow.getAssetById`

## Returns

**Promise\<`null`>**

A Promise that resolves to `null`

## Example

```typescript
// Get Selected Element
const el = await webflow.getSelectedElement()

// Check if element can have children
if (el?.children) {
  // Create a new Image Element using Element Presets
  const imgEl = await el.append(webflow.elementPresets.Image)

  // Get asset by ID
  const asset = await webflow.getAssetById(assetId)

  // Check element type
  if (imgEl.type === 'Image') {
    // Set asset as the "src" of the Image Element
    await imgEl.setAsset(asset)
  }
}
```

## Designer Ability

| Designer Ability      | Locale | Branch | Workflow | Sitemode |
| :-------------------- | :----- | :----- | :------- | :------- |
| canModifyImageElement | any    | main   | canvas   | any      |

```
```
