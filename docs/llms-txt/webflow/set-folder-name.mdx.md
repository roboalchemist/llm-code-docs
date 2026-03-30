# Source: https://developers.webflow.com/designer/reference/set-folder-name.mdx

***

title: Set folder name
slug: designer/reference/set-folder-name
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set folder name'
'og:description': Set the folder name.
--------------------------------------

## `folder.setName(name)`

Set the folder name.

### Syntax

```typescript
folder.setName(name: string): Promise<null>
```

### Parameters

* **name**: `string` - The new name to set for the folder.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

### Example

```coffeescript TypeScript
// Create and name new folder
const newFolder = await webflow.createPageFolder()
await newFolder.setName(name)

// Print details
const folderName = await newFolder.getName()
console.log("My New Folder", folderName)
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
