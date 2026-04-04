# Source: https://developers.webflow.com/designer/reference/set-alt-text.mdx

***

title: Set Alt Text
slug: designer/reference/set-alt-text
description: ''
hidden: false
-------------

## `asset.setAltText(altText, localeId?)`

This method sets the Alt Text for a specific Asset.

### Syntax

```typescript
asset.setAltText(altText: string | null; localeId?: string): Promise<null>
```

### Parameters

* **`altText`**:  *string* - The alt text for the Asset. If null is passed as this parameter, Webflow will set the asset alt text to "decorative."
* **`localeId`** *string* (optional) - The Locale ID for the Alt Text.

### Returns

**Promise\<*null*>**

A Promise that resolves to `null`.

### Example

```typescript
// Get Asset by ID
const asset = await webflow.getAssetById(assetId)
console.log(asset)

if (asset) {
  // Get asset URL
  const originalAltText = await asset.getAltText()
  await asset.setAltText(altText)
  const newAltText = await asset.getAltText()
  console.log(`Original Asset Alt Text: ${originalAltText}`)
  console.log(`New Asset Alt Text: ${newAltText}`)
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
| **canManageAssets** | any    | any    | any      | any      |
