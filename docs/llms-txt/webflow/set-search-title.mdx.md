# Source: https://developers.webflow.com/designer/reference/set-search-title.mdx

***

title: Set search title
slug: /designer/reference/set-search-title
description: Method for setting the search title of a page.
hidden: false
'og:title': Set search title
'og:description': Method for setting the search title of a page.
----------------------------------------------------------------

## `page.setSearchTitle(title)`

Set the search title of the page.

#

### Syntax

```typescript
page.setSearchTitle(title: string | null): Promise<null>;
```

### Parameters

* **title**: *`string | null`* - The search title of the page.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set search engine title and print details
await currentPage.setSearchTitle("My New Title")
const searchTitle = await currentPage.getSearchTitle()
console.log(searchTitle)
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
