# Source: https://developers.webflow.com/designer/reference/set-open-graph-description.mdx

***

title: Set Open Graph description
slug: designer/reference/set-open-graph-description
description: Method for setting a page's Open Graph description.
hidden: false
'og:title': Set Open Graph description
'og:description': Method for setting a page's Open Graph description.
---------------------------------------------------------------------

## `page.setOpenGraphDescription(description)`

Sets a page's Open Graph description.

#

### Syntax

```typescript
page.setOpenGraphDescription(description: string | null): Promise<null>
```

### Parameters

* **description**: *string | null* - The Open Graph description to set.

### Returns

**Promise\<`null`>**

A Promise that resolves to null.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set Open Graph Description
await currentPage.setOpenGraphDescription(description)

// Print results
const openGraphDescription = await currentPage.getOpenGraphDescription()
console.log("Open Graph Description", openGraphDescription)
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
