# Source: https://developers.webflow.com/designer/reference/get-folder-slug.mdx

***

title: Get folder slug
slug: designer/reference/get-folder-slug
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get folder slug'
'og:description': Get the folder's slug.
----------------------------------------

## `folder.getSlug()`

Get the folder's slug.

### Syntax

```typescript
folder.getSlug(): Promise<string>
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a `string` value of the folder slug.

### Example

```typescript
// Get all Pages and folders
const pagesAndFolders = await webflow.getAllPagesAndFolders()

for (let folder of pagesAndFolders) {

  const folderSlug = await folder.getSlug()
  console.log("Slug", folderSlug)
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
