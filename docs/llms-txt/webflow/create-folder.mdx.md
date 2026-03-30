# Source: https://developers.webflow.com/designer/reference/create-folder.mdx

***

title: Create folder
slug: designer/reference/create-folder
description: ''
hidden: false
'og:title': 'Webflow Designer API: Create folder'
'og:description': Creates a new folder on the site.
---------------------------------------------------

## `webflow.createPageFolder()`

Creates a new folder on the site.

### Syntax

```typescript
webflow.createPageFolder(): Promise<Folder>
```

### Returns

**Promise\<*Folder*>**

A Promise that resolves to the newly created folder.

### Example

```typescript
// Create and name new folder
const newFolder = await webflow.createPageFolder()
await newFolder.setName(name)

// Print details
const folderName = await newFolder.getName()
console.log(folderName)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability  | Locale | Branch | Workflow | Sitemode |
| :---------------- | :----- | :----- | :------- | :------- |
| **canCreatePage** | Any    | Any    | Any      | Design   |
