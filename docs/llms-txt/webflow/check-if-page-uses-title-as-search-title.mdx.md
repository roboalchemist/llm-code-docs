# Source: https://developers.webflow.com/designer/reference/check-if-page-uses-title-as-search-title.mdx

***

title: Check if page uses title as search title
slug: /designer/reference/check-if-page-uses-title-as-search-title
description: Method for checking if a page uses the page title as the search title.
hidden: false
'og:title': Check if page uses title as search title
'og:description': Method for checking if a page uses the page title as the search title.
----------------------------------------------------------------------------------------

## `page.usesTitleAsSearchTitle()`

Check if the page uses the page title as the search title.

#

### Syntax

```typescript
page.usesTitleAsSearchTitle(): Promise<boolean>;
```

### Returns

**Promise\<`boolean`>**

A Promise that resolves to a `boolean` value.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage()

// Check title
const usesTitle = await currentPage?.usesTitleAsSearchTitle()

if (usesTitle){
  console.log('This page uses its Title as the Search Engine title')
} else {
  console.log( "This page has a custom search engine title")
}
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
