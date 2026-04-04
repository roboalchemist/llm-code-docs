# Source: https://developers.webflow.com/designer/reference/get-page-slug.mdx

***

title: Get page slug
slug: /designer/reference/get-page-slug
description: Get the slug of the page.
hidden: false
'og:title': Get page slug
'og:description': Get the slug of the page.
-------------------------------------------

## `page.getSlug()`

Get the slug of the page.

#

### Syntax

```typescript
page.getSlug(): Promise<string>
```

### Returns

**Promise\<`string`>**

A promise that resolves to the slug of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get page slug
const pageSlug = await currentPage.getSlug()
console.log(pageSlug)
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
