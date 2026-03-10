# Source: https://developers.webflow.com/designer/reference/get-all-assets.mdx

***

title: Get All Assets
slug: designer/reference/get-all-assets
description: ''
hidden: false
-------------

## `webflow.getAllAssets()`

Retrieve all assets on a site.

### Syntax

```typescript
webflow.getAllAssets(): Promise<Asset[]>
```

### Returns

**Promise\<*Asset\[]*>**

A Promise that resolves to an array of Assets.

### Example

```typescript
// Get all assets
const assets = await webflow.getAllAssets()

// Loop to list assets in the console
for (const asset of assets) {
  const name = await asset.getName()
  const mimeType = await asset.getMimeType()
  console.log(name, mimeType)
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
