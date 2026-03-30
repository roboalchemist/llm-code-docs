# Source: https://developers.webflow.com/designer/reference/check-if-page-is-homepage.mdx

***

title: Check if page is homepage
slug: /designer/reference/check-if-page-is-homepage
description: Check if the page is the homepage.
'og:title': Check if page is homepage
'og:description': Check if the page is the homepage.
----------------------------------------------------

## `page.isHomepage()`

Check if the page is set as the homepage.

#

### Syntax

```typescript
page.isHomepage(): Promise<boolean>
```

### Returns

**Promise\<`boolean`>**

A promise that resolves to a boolean value indicating whether the page is the homepage.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Check if current page is the homepage
const isHomepage = await currentPage.isHomepage()

if (isHomepage) {
  console.log('Current page is the Homepage')
} else {
  console.log('Current page is not the Homepage')
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
