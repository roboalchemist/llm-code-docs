# Source: https://developers.webflow.com/designer/reference/set-parent-folder.mdx

***

title: Set parent folder
slug: designer/reference/set-parent-folder
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set parent folder'
'og:description': Assign a new parent folder to the selected folder.
--------------------------------------------------------------------

## `folder.setParent(parent: Folder)`

Assign a new parent folder to the selected folder.

### Syntax

```typescript
folder.setParent(parent: Folder): Promise<null>
```

### Parameters

* **parent** : `Folder` - The parent folder to set for the current folder.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null` when the parent folder is set.

### Example

```typescript
// Get all Pages and folders
const pagesAndFolders = await webflow.getAllPagesAndFolders()

// Create and name new folder
const newFolder = await webflow.createPageFolder()
await newFolder.setName("Parent Folder")

for (let folder of pagesAndFolders) {

  await folder.setParent(newFolder)

}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability          | Locale | Branch | Workflow | Sitemode |
| :------------------------ | :----- | :----- | :------- | :------- |
| **canManagePageSettings** | Any    | Any    | Any      | Any      |
