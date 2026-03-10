# Source: https://developers.webflow.com/designer/reference/set-folder-slug.mdx

***

title: Set folder slug
slug: designer/reference/set-folder-slug
description: ''
hidden: false
'og:title': 'Webflow Designer API: Set folder slug'
'og:description': Choose a new slug for your folder.
----------------------------------------------------

## `folder.setSlug(slug)`

Choose a new slug for your folder.

### Syntax

```typescript
folder.setSlug(slug: string): Promise<null>
```

### Parameters:

* **slug**: `string` - The new slug to set for the folder.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

### Example

```coffeescript TypeScript
// Create and give slug to new folder
const newFolder = await webflow.createPageFolder()
await newFolder.setSlug(slug)

// Print details
const newSlug = await newFolder.getSlug()
console.log("My New Slug", newSlug)
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
