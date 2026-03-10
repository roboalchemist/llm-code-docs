# Source: https://developers.webflow.com/designer/reference/get-asset-folder-parent.mdx

***

title: Get folder of an Asset
slug: /reference/get-asset-folder-parent
description: Get the folder of the current Asset in the Webflow Designer
hidden: null
'og:title': Get folder of an Asset
'og:description': Get the folder of the current Asset in the Webflow Designer
-----------------------------------------------------------------------------

## `Asset.getParent()`

Gets the folder of the current Asset in the Webflow Designer

#

### Syntax

```typescript
Asset.getParent(): Promise<AssetFolder | null>
```

### Returns

**`AssetFolder` | `null`**

A Promise that resolves to the parent Asset folder, or `null` if a parent folder does not exist for the Asset.

#

### Example

```typescript
// Get all Assets
const assets = await webflow.getAllAssets()
const asset = assets[0]

const folder = await asset.getParent()

if (folder) {
    console.log(folder)
} else {
    console.log("A parent folder does not exist for this asset")
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessAssets** | Any    | Any    | Any      | Any      |
