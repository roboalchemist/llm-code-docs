# Source: https://developers.webflow.com/designer/reference/set-asset-folder-parent.mdx

***

title: Set folder for an Asset
slug: /reference/set-asset-folder-parent
description: Set the folder of the current Asset in the Webflow Designer
hidden: null
'og:title': Set folder for an Asset
'og:description': Set the folder of the current Asset in the Webflow Designer
-----------------------------------------------------------------------------

## `Asset.setParent(assetFolder)`

Sets the folder of the current Asset in the Webflow Designer

#

### Syntax

```typescript
Asset.setParent(assetFolder: AssetFolder): Promise<null>
```

### Returns

**`null`**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get all Assets
const assets = await webflow.getAllAssets()
const myAsset = assets[0]

const folders = await webflow.getAllAssetFolders()
const folder = folders[0]

if (folder) {
await myAsset.setParent(folder)
console.log(`Asset: ${myAsset.id} moved to ${folder.id}`)
} else {
webflow.notify({ type: 'Error', message: 'Folder not found' })
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
| **canManageAssets** | Any    | Any    | Any      | Any      |
