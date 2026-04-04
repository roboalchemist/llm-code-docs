# Source: https://developers.webflow.com/designer/reference/set-asset-file.mdx

***

title: Set Asset File
slug: reference/set-asset-file
description: Set the file of an asset.
hidden: false
'og:title': 'Webflow Designer API: Set Asset File'
'og:description': Set the file of an asset.
-------------------------------------------

## `asset.setFile(fileBlob)`

Set the file of an asset. Use this method to replace the file of an existing asset with a new file.

## Syntax

```typescript
asset.setFile(fileBlob: File): Promise<null>
```

## Parameters

* **`fileBlob`**: *File* - The file to set the asset to.

## Returns

A Promise that resolves to `null`.

#

### Example

```typescript
const assets = await webflow.getAllAssets();
const asset = assets[0];
const newFile = new File([blob], 'marvin-smiling.png', { type: 'image/png' });
await asset.setFile(newFile);
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canManageAssets** | Any    | Any    | Any      | Any      |
