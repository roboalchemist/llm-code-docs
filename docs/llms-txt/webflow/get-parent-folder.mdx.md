# Source: https://developers.webflow.com/designer/reference/get-parent-folder.mdx

***

title: Get parent folder
slug: designer/reference/get-parent-folder
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get parent folder'
'og:description': Get parent folder of selected folder.
-------------------------------------------------------

## `folder.getParent()`

Get parent folder of selected folder.

### Syntax

```typescript
folder.getParent(): Promise<null | Folder>
```

### Returns

**Promise\<`null` | *Folder*>**

A Promise that resolves to a `Folder` object if a parent exists, or `null` if no parent is found.

### Example

```coffeescript TypeScript
// Get all Pages and folders
const pagesAndFolders = await webflow.getAllPagesAndFolders()

for (let folder of pagesAndFolders) {

  const childName = await folder.getName()
  const parent = await folder.getParent()
  const parentName = await parent?.getName()
  console.log(`Folder: ${childName}`, `Parent: ${parentName}`)
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability        | Locale | Branch | Workflow | Sitemode |
| :---------------------- | :----- | :----- | :------- | :------- |
| **canReadPageSettings** | Any    | Any    | Any      | Any      |
