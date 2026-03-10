# Source: https://developers.webflow.com/designer/reference/get-open-graph-image.mdx

***

title: Get Open Graph image
slug: designer/reference/get-open-graph-image
description: Method for getting a page's Open Graph image.
hidden: false
'og:title': Get Open Graph image
'og:description': Method for getting a page's Open Graph image.
---------------------------------------------------------------

## `page.getOpenGraphImage()`

Retrieves the Open Graph image of the page.

#

### Syntax

```typescript
page.getOpenGraphImage(): Promise<string>
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a string containing the Open Graph image of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

//  Get Open Graph image and Print Details
const openGraphImage = await currentPage.getOpenGraphImage()
console.log(openGraphImage)
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
