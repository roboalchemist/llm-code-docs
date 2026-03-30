# Source: https://developers.webflow.com/designer/reference/exclude-page-from-search.mdx

***

title: Exclude page from search
slug: /designer/reference/exclude-page-from-search
description: Method for excluding a page from internal site search.
hidden: false
'og:title': Exclude page from search
'og:description': Method for excluding a page from internal site search.
------------------------------------------------------------------------

## `page.excludeFromSearch(shouldExclude)`

Exclude the page from [internal site search.](https://help.webflow.com/hc/en-us/articles/33961242348179-Site-search)

#

### Syntax

```typescript
page.excludeFromSearch(shouldExclude: boolean): Promise<null>;
```

### Parameters

* **shouldExclude**: *`boolean`* - Whether the page should be excluded from search engine indexing.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage()

// Exclude from search engine indexing
await currentPage.excludeFromSearch(true)
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
