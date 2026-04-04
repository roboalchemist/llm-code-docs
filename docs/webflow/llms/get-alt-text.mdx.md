# Source: https://developers.webflow.com/designer/reference/get-alt-text.mdx

***

title: Get Alt Text
slug: designer/reference/get-alt-text
description: ''
hidden: false
-------------

## `asset.getAltText()`

This method retrieves the Alt Text for a specific Asset.

### Syntax

```typescript
asset.getAltText(): Promise<string>
```

### Returns

**Promise\<*string*>**

A Promise that resolves to the Alt Text string.

### Example

```typescript
// Get Asset by ID
const asset = await webflow.getAssetById(asset_id)
console.log(asset)

if (asset) {
  // Get asset URL
  const altText = await asset.getAltText()
  console.log(`Asset Alt Text: ${altText}`)
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
| **canAccessAssets** | any    | any    | any      | any      |
