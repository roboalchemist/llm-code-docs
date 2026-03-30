# Source: https://developers.webflow.com/designer/reference/get-page-category.mdx

***

title: Get page category
slug: /designer/reference/get-page-category
description: Get the category of the page.
hidden: false
'og:title': Get page category
'og:description': Get the category of the page.
-----------------------------------------------

## `page.getKind()`

Get the category of the page.

#

### Syntax

```typescript
page.getKind(): Promise<string>
```

### Returns

**Promise\<`string`>**

A promise that resolves to a string indicating the kind of the current page. The possible values are:

* `'static'`
* `'ecommerce'`
* `'cms'`
* `'userSystems'`
* `'utility'`
* `'staticTemplate'`

#

### Example

```typescript
// Get Current Page
const currentPage = (await webflow.getCurrentPage()) as Page

// Get the page
const pageKind = await currentPage.getKind()
console.log(`Page Category: ${pageKind}`)
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
