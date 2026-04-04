# Source: https://developers.webflow.com/designer/reference/uses-title-as-open-graph-title.mdx

***

title: Check if page uses title as Open Graph title
slug: designer/reference/uses-title-as-open-graph-title
description: Method for checking if the title is used as the open graph title in Webflow.
'og:title': Check if page uses title as Open Graph title
'og:description': Method for checking if the title is used as the Open Graph title in Webflow.
----------------------------------------------------------------------------------------------

## `page.usesTitleAsOpenGraphTitle()`

Checks if the page uses the page title as the Open Graph title.

#

### Syntax

```typescript
page.usesTitleAsOpenGraphTitle(): Promise<boolean>
```

### Returns

**Promise\<`boolean`>**

Returns `true` if the page uses the page title as the Open Graph title, otherwise returns `false`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page
// Check if page is using the Title as the Open Graph title
const isOpenGraphTitle = await currentPage.usesTitleAsOpenGraphTitle()
// Print results
if (isOpenGraphTitle) {
  console.log('Page uses Title as Open Graph Title')
} else {
  console.log('This page has a custom Open Graph Title')
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
