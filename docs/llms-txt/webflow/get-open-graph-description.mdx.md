# Source: https://developers.webflow.com/designer/reference/get-open-graph-description.mdx

***

title: Get Open Graph description
slug: designer/reference/get-open-graph-description
description: Method for getting a page's Open Graph description.
hidden: false
'og:title': Get Open Graph description
'og:description': Method for getting a page's Open Graph description.
---------------------------------------------------------------------

## `page.getOpenGraphDescription()`

Retrieves the Open Graph description of the page.

#

### Syntax

```typescript
page.getOpenGraphDescription(): Promise<string>
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a string containing the Open Graph description of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get Open Graph Description
const openGraphDescription = await currentPage.getOpenGraphDescription()
console.log("Open Graph Description", openGraphDescription)
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
