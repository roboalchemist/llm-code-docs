# Source: https://developers.webflow.com/designer/reference/get-search-title.mdx

***

title: Get search title
slug: /designer/reference/get-search-title
description: Method for getting the search title of a page.
hidden: false
'og:title': Get search title
'og:description': Method for getting the search title of a page.
----------------------------------------------------------------

## `page.getSearchTitle()`

Get the search title of the page.

#

### Syntax

```typescript
page.getSearchTitle(): Promise<string>;
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a `string` value.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get Search engine title and print details
const searchEngineTitle = currentPage.getSearchTitle()
console.log(searchEngineTitle)
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
