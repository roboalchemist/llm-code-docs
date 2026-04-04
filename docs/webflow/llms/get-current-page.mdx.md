# Source: https://developers.webflow.com/designer/reference/get-current-page.mdx

***

title: Get the current page
slug: designer/reference/get-current-page
description: ''
hidden: false
'og:title': 'Webflow Designer API: Get the current page'
'og:description': Retrieves the current page open in the Designer.
------------------------------------------------------------------

## `webflow.getCurrentPage()`

Retrieves the current page open in the Designer.

### Syntax

```typescript
webflow.getCurrentPage(): Promise<Page>
```

### Returns

**Promise\<*Page*>**

A Promise that resolves to the current page.

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage()
const pageName = await currentPage?.getName()

// Print page details
console.log(currentPage, pageName)
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
| **canAccessCanvas** | Any    | Any    | Any      | Any      |
