# Source: https://developers.webflow.com/designer/reference/use-page-title-as-search-title.mdx

***

title: Use page title as search title
slug: /designer/reference/use-page-title-as-search-title
description: Method for setting the page title as the search title.
hidden: false
'og:title': Use page title as search title
'og:description': Method for setting the page title as the search title.
------------------------------------------------------------------------

## `page.useTitleAsSearchTitle(shouldUseTitle)`

Set the page title as the search title.

#

### Syntax

```typescript
page.useTitleAsSearchTitle(use: boolean): Promise<null>;
```

### Parameters

* **shouldUseTitle**: *`boolean`* - Whether the page title should be used as the search title.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage()

// Set title as search title
await currentPage?.useTitleAsSearchTitle(true)
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
