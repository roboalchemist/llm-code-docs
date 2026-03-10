# Source: https://developers.webflow.com/designer/reference/use-open-graph-image-as-search-image.mdx

***

title: Use Open Graph image as search image
slug: /designer/reference/use-open-graph-image-as-search-image
description: Method for using the Open Graph image as the search image.
hidden: false
'og:title': Use Open Graph image as search image
'og:description': Method for using the Open Graph image as the search image.
----------------------------------------------------------------------------

## `page.useOpenGraphImageAsSearchImage(use)`

Use the Open Graph image as the search image.

#

### Syntax

```typescript
page.useOpenGraphImageAsSearchImage(use: boolean): Promise<null>;
```

### Parameters

* **use**: *`boolean`* - Whether to use the Open Graph image as the search image.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get current page
const currentPage = await webflow.getCurrentPage()

// Set Open Graph image as search image
await currentPage?.useOpenGraphImageAsSearchImage(true)
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
