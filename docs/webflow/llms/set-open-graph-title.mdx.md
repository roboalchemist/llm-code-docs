# Source: https://developers.webflow.com/designer/reference/set-open-graph-title.mdx

***

title: Set Open Graph title
slug: designer/reference/set-open-graph-title
description: Method for setting the open graph title of a page.
hidden: false
'og:title': Set Open Graph title
'og:description': Method for setting the open graph title of a page.
--------------------------------------------------------------------

## `page.setOpenGraphTitle(title)`

Sets the Open Graph title of the page.

#

### Syntax

```typescript
page.setOpenGraphTitle(title: string | null): Promise<null>
```

### Parameters

* **title**: *string | null* - The new Open Graph title for the page.

### Returns

**Promise\<`null`>**

Returns `null` if successful.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set Open Graph Title
await currentPage.setOpenGraphTitle("My New Title")

// Print results
const openGraphTitle = await currentPage.getOpenGraphTitle()
console.log("Open Graph Title", openGraphTitle)
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
