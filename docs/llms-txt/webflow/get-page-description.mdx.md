# Source: https://developers.webflow.com/designer/reference/get-page-description.mdx

***

title: Get page description
slug: /designer/reference/get-page-description
description: Get the description of the page.
hidden: false
'og:title': Get page description
'og:description': Get the description of the page.
--------------------------------------------------

## `page.getDescription()`

Get the description of the page.

#

### Syntax

```typescript
page.getDescription(): Promise<null | string>
```

### Returns

**Promise\<`null | string`>**

A promise that resolves to the description of the page.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get page Description
const pageDescription = await currentPage.getDescription()
console.log(pageDescription)
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
