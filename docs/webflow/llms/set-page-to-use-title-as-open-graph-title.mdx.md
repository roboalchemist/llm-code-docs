# Source: https://developers.webflow.com/designer/reference/set-page-to-use-title-as-open-graph-title.mdx

***

title: Set page to use title as Open Graph title
slug: designer/reference/set-page-to-use-title-as-open-graph-title
description: Method for setting the page to use the page title as the Open Graph title.
hidden: false
'og:title': Set page to use title as Open Graph title
'og:description': Method for setting the page to use the page title as the Open Graph title.
--------------------------------------------------------------------------------------------

## `page.setUsesTitleAsOpenGraphTitle(value)`

Indicate whether the page should use its title as the Open Graph (OG) title.

#

### Syntax

```typescript
page.useTitleAsOpenGraphTitle(use: boolean): Promise<null>
```

### Parameters

* **use**: *boolean* - Set to `true` to use the page title as the Open Graph title, otherwise set to `false`.

### Returns

**Promise\<`null`>**

Returns `null` if successful.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page
// Set page title as open graph title
await currentPage.useTitleAsOpenGraphTitle(true)
const title = await currentPage.getOpenGraphTitle()
console.log(title)
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
