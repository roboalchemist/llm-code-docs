# Source: https://developers.webflow.com/designer/reference/get-page-name.mdx

***

title: Get page name
slug: /designer/reference/get-page-name
description: Get the name of the page.
hidden: false
'og:title': Get page name
'og:description': Get the name of the page.
-------------------------------------------

## `page.getName()`

Get the name of the page.

#

### Syntax

```typescript
page.getName(): Promise<string>
```

### Returns

**Promise\<`string`>**

A promise that resolves to the name of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get page name
const pageName = await currentPage.getName()
console.log(pageName)
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
