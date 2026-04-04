# Source: https://developers.webflow.com/designer/reference/get-asset-folder-name.mdx

***

title: Get Asset folder name
slug: /reference/get-asset-folder-name
description: Get the name of the current Asset folder
hidden: null
'og:title': Get Asset folder name
'og:description': Get the name of the current Asset folder
----------------------------------------------------------

## `assetFolder.getName()`

Get the name of the current AssetFolder object

#

### Syntax

```typescript
AssetFolder.getName(): Promise<string>
```

### Returns

**String**

A Promise that returns the name of the AssetFolder object

#

### Example

```typescript
// Create Asset Folder
const newFolder = await webflow.createAssetFolder(name)
const folderName = await newFolder.getName()

console.log(folderName)
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
