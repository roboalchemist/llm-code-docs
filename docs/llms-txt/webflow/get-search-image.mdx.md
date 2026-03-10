# Source: https://developers.webflow.com/designer/reference/get-search-image.mdx

***

title: Get search image
slug: /designer/reference/get-search-image
description: Method for getting the search image of a page.
hidden: false
'og:title': Get search image
'og:description': Method for getting the search image of a page.
----------------------------------------------------------------

## `page.getSearchImage()`

Get the search image of the page.

#

### Syntax

```typescript
page.getSearchImage(): Promise<string>;
```

### Returns

**Promise\<`string`>**

A Promise that resolves to a `string` value.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get search engine Image and print details
const searchEngineImage = await currentPage.getSearchImage()
console.log(searchEngineImage)`
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
