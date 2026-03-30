# Source: https://developers.webflow.com/designer/reference/get-all-asset-folders.mdx

***

title: Get all Asset folders
slug: /reference/get-all-asset-folders
description: Get all Asset folders for a site in the designer
hidden: null
'og:title': Get all asset folders
'og:description': Get all Asset folders for a site in Webflow
-------------------------------------------------------------

## `webflow.getAllAssetFolders()`

Get all folders in the Assets panel.

#

### Syntax

```typescript
getAllAssetFolders(): Promise<Array<AssetFolder>>
```

### Returns

**Array\<AssetFolder>**

An array of AssetFolders

#

### Example

```typescript
const folders = await webflow.getAllAssetFolders()
    console.log(folders)
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
