# Source: https://developers.webflow.com/designer/reference/get-asset-url.mdx

***

title: Get Asset URL
slug: designer/reference/get-asset-url
description: ''
hidden: false
-------------

## `asset.getUrl()`

This method retrieves the hosted URL of an asset hosted on Webflow's CDN.

### Syntax

```typescript
asset.getUrl(): Promise<string>
```

### Returns

**Promise\<*string*>**

A Promise that resolves to the URL string of the hosted asset.

### Example

```typescript
// Get Asset by ID
const asset = await webflow.getAssetById(asset_id)
console.log(asset)

if (asset) {
  // Get asset URL
  const url = await asset.getUrl()
  console.log(`Asset URL: ${url}`)
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
