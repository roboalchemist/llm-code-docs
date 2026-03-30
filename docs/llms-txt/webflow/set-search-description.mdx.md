# Source: https://developers.webflow.com/designer/reference/set-search-description.mdx

***

title: Set search description
slug: /designer/reference/set-search-description
description: Method for setting the search description of a page.
hidden: false
'og:title': Set search description
'og:description': Method for setting the search description of a page.
----------------------------------------------------------------------

## `page.setSearchDescription(description)`

Set the search description of the page.

#

### Syntax

```typescript
page.setSearchDescription(description: string | null): Promise<null>;
```

### Parameters

* **description**: *`string | null`* - The search description to set.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set search engine description and print details
await currentPage.setSearchDescription("My New Description")
const searchDescription = await currentPage.getSearchDescription()
console.log(searchDescription)
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
