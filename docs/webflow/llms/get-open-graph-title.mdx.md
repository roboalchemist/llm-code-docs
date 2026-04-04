# Source: https://developers.webflow.com/designer/reference/get-open-graph-title.mdx

***

title: Get Open Graph title
slug: designer/reference/get-open-graph-title
description: Method for getting the open graph title of a page.
hidden: false
'og:title': Get Open Graph title
'og:description': Method for getting the open graph title of a page.
--------------------------------------------------------------------

## `page.getOpenGraphTitle()`

Retrieves the Open Graph title of the page.

#

### Syntax

```typescript
page.getOpenGraphTitle(): Promise<string>
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a string with the Open Graph title of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get Open Graph Title
const openGraphTitle = await currentPage.getOpenGraphTitle()
console.log("Open Graph Title", openGraphTitle)
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
