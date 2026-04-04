# Source: https://developers.webflow.com/designer/reference/set-open-graph-image-url.mdx

***

title: Set Open Graph image URL
slug: designer/reference/set-open-graph-image-url
description: Method for setting a page's Open Graph image URL.
hidden: false
'og:title': Set Open Graph image URL
'og:description': Method for setting a page's Open Graph image URL.
-------------------------------------------------------------------

## `page.setOpenGraphImageUrl(url)`

Sets a page's Open Graph image URL.

#

### Syntax

```typescript
page.setOpenGraphImage(url: string | null): Promise<null>
```

### Parameters

* **url**: *string | null* - The URL of the Open Graph image to set.

### Returns

**Promise\<`null`>**

A Promise that resolves to null.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

//  Set open graph image and print details
await currentPage.setOpenGraphImage("example.com/image.jpg")
const openGraphImage = currentPage.getOpenGraphImage()
console.log(openGraphImage)
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
