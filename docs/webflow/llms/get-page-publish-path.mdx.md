# Source: https://developers.webflow.com/designer/reference/get-page-publish-path.mdx

***

title: Get page publish path
slug: /designer/reference/get-page-publish-path
description: Get the publish path of the page.
hidden: false
'og:title': Get page publish path
'og:description': Get the publish path of the page.
---------------------------------------------------

## `page.getPublishPath()`

Get the publish path of the page.

#

### Syntax

```typescript
page.getPublishPath(): Promise<null | string>
```

### Returns

**Promise\<`null | string`>**

A promise that resolves to the publish path of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get page publish path
const pagePublishPath = await currentPage.getPublishPath()
console.log(pagePublishPath)
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
