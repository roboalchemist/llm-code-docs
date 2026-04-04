# Source: https://developers.webflow.com/designer/reference/set-page-slug.mdx

***

title: Set page slug
slug: /designer/reference/set-page-slug
description: Set the slug of the page.
hidden: false
'og:title': Set page slug
'og:description': Set the slug of the page.
-------------------------------------------

## `page.setSlug(slug)`

Set the slug of the page.

#

### Syntax

```typescript
page.setSlug(slug: string): Promise<null>
```

### Parameters

* **slug**: `string` - The new slug of the page.

### Returns

**Promise\<`null`>**

A promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set page Description
await currentPage.setSlug(slug)
const newSlug = await currentPage.getSlug()
console.log("Slug",newSlug)
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
