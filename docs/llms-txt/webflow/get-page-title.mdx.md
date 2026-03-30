# Source: https://developers.webflow.com/designer/reference/get-page-title.mdx

***

title: Get page title
slug: /designer/reference/get-page-title
description: Get the title of the page.
hidden: false
'og:title': Get page title
'og:description': Get the title of the page.
--------------------------------------------

## `page.getTitle()`

Get the title of the page.

#

### Syntax

```typescript
page.getTitle(): Promise<string>
```

### Returns

**Promise\<`string`>**

A promise that resolves to the title of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get page title
const pageTitle = await currentPage.getTitle()
console.log(pageTitle)
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
