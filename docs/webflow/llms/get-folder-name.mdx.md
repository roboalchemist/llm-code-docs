# Source: https://developers.webflow.com/designer/reference/get-folder-name.mdx

***

title: Get folder name
slug: designer/reference/get-folder-name
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get folder name'
'og:description': Retrieve the name of the folder.
--------------------------------------------------

## `folder.getName()`

Retrieve the name of the folder.

### Syntax

```typescript
folder.getName(): Promise<string>
```

### Returns

**Promise\<*String*>**

A Promise that resolves to a `string` value of the folder name.

### Example

```typescript
// Get all Pages and folders
const pagesAndFolders = await webflow.getAllPagesAndFolders()

for (let folder of pagesAndFolders) {

  const folderName = await folder.getName()
  const type = folder.type
  console.log(folderName, type)
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
