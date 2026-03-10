# Source: https://developers.webflow.com/designer/reference/use-page-description-as-search-description.mdx

***

title: Use page description as search description
slug: /designer/reference/use-page-description-as-search-description
description: Method for setting the page description as the search description.
hidden: false
'og:title': Use page description as search description
'og:description': Method for setting the page description as the search description.
------------------------------------------------------------------------------------

## `page.useDescriptionAsSearchDescription(use)`

Set the page description as the search description.

#

### Syntax

```typescript
page.useDescriptionAsSearchDescription(use: boolean): Promise<null>;
```

### Parameters

* **use**: *`boolean`* - Whether the page description should be used as the search description.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set description as search description
await currentPage.useDescriptionAsSearchDescription(true)
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability               | Locale | Branch | Workflow | Sitemode |
| :----------------------------- | :----- | :----- | :------- | :------- |
| \*\*canManagePageSettings	\*\* | Any    | Any    | Any      | Any      |
