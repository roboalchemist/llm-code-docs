# Source: https://developers.webflow.com/designer/reference/get-all-pages-and-folders.mdx

***

title: Get all pages and folders
slug: designer/reference/get-all-pages-and-folders
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get all pages and folders'
'og:description': Retrieves all pages and folders in the current site.
----------------------------------------------------------------------

## `webflow.getAllPagesAndFolders()`

Retrieves all pages and folders in the current site.

### Syntax

```typescript
webflow.getAllPagesAndFolders(): Promise<Array<Page | Folder>>
```

### Returns

**Promise\<Array\<*Folder* | *Page*>>**

A Promise that resolves to an array of page and/or folder objects.

### Example

```typescript
// Get all pages and folders
const pagesAndFolders = await webflow.getAllPagesAndFolders()

// Print Page Details
const pages = pagesAndFolders?.filter(i => i.type === "Page")
await Promise.all(pages.map(async page => {

  const pageName = await page.getName()
  console.log(`Page: ${pageName}`)

}))

const folders = pagesAndFolders?.filter(i => i.type === "PageFolder")
await Promise.all(folders.map(async folder => {

  const folderName = await folder.getName()
  console.log(`Folder: ${folderName}`)

}))
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
