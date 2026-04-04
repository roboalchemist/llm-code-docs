# Source: https://developers.webflow.com/designer/reference/get-search-description.mdx

***

title: Get search description
slug: /designer/reference/get-search-description
description: Method for getting the search description of a page.
hidden: false
'og:title': Get search description
'og:description': Method for getting the search description of a page.
----------------------------------------------------------------------

## `page.getSearchDescription()`

Get the search description of the page.

#

### Syntax

```typescript
page.getSearchDescription(): Promise<string>;
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a `string` value.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get search engine description and print details
const searchEngineDescription = await currentPage.getSearchDescription()
console.log(searchEngineDescription)
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
