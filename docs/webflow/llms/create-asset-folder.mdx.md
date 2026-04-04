# Source: https://developers.webflow.com/designer/reference/create-asset-folder.mdx

***

title: Create an Asset folder
slug: reference/create-asset-folder
description: Create an Asset Folder in a Designer Extension
hidden: null
'og:title': Create an asset folder
'og:description': Create an Asset Folder in a Designer Extension
----------------------------------------------------------------

## `webflow.createAssetFolder(name, parentFolderId)`

Creates a folder in the Assets panel, which can also be nested within an existing folder for better organization.

#

### Syntax

```typescript
createAssetFolder(name: string, parentFolderId?: string): Promise<AssetFolder>
```

### Parameters

* **name**: *string* - The display name of the new folder
* **parentFolderId**: *string* - (optional) - The ID of the desired parent folder. Get existing folder IDs from [webflow.getAllAssetFolders()](/designer/reference/get-all-asset-folders)

### Returns

**Return Value**

A Promise resolving to an *AssetFolder* object.

#

### Example

```typescript
// Get All Asset Folders
    const folders = await webflow.getAllAssetFolders()

    const parentFolderName = "My Parent Folder Name"

    // Find Parent Folder by Name
    if (parentFolderName && parentFolderName !== '') {
      const parentFolder = await Promise.all(
        folders.map(async (folder) => {
          const folderName = await folder.getName()
          if (folderName === parentFolderName) {
            return folder
          }
          return null
        }),
      ).then((results) => results.find((folder) => folder !== null))

      // Create Asset Folder with parent folder
      if (parentFolder) {
        const newFolder = await webflow.createAssetFolder(name, parentFolder.id)
        console.log(newFolder)
      }
    } else {
      // Crate Asset Folder
      const newFolder = await webflow.createAssetFolder(name)
      console.log(newFolder)
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
