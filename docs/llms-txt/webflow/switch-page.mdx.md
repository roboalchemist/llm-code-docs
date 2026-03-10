# Source: https://developers.webflow.com/designer/reference/switch-page.mdx

***

title: Switch to a page
slug: designer/reference/switch-page
description: ''
hidden: false
'og:title': 'Webflow Designer API: Switch page'
'og:description': Switch the Designer to a specified page.
----------------------------------------------------------

## `webflow.switchPage(page)`

Switch the Designer to a specified page.

### Syntax

```typescript
webflow.switchPage(page: Page): Promise<null>
```

### Parameters

**`page`** :   *Page* - The page to switch to.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null` when the page switch is complete.

### Example

```typescript
// Get All Pages and Folders
const pagesAndFolders = await webflow.getAllPagesAndFolders()
const pages = pagesAndFolders?.filter((i): i is Page => i.type === "Page")

// Switch Page
const newPage = pages[2]
await webflow.switchPage(newPage)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

Checks for authorization only

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **canAccessCanvas** | Any    | Any    | Any      | An       |
