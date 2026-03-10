# Source: https://developers.webflow.com/designer/reference/uses-description-as-open-graph-description.mdx

***

title: Check if page uses description as Open Graph description
slug: designer/reference/uses-description-as-open-graph-description
description: >-
Method for checking if a page uses its description as its open graph
description.
hidden: false
'og:title': Check if page uses description as Open Graph description
'og:description': >-
Method for checking if a page uses its description as its Open Graph
description.
------------

## `page.usesDescriptionAsOpenGraphDescription()`

Checks if the page uses its description as its Open Graph description.

#

### Syntax

```typescript
page.usesDescriptionAsOpenGraphDescription(): Promise<boolean>
```

### Returns

**Promise\<`boolean`>**

A Promise that resolves to a boolean indicating whether the page uses its description as its Open Graph description.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Check page status
const isOpenGraphDescription = await currentPage.usesDescriptionAsOpenGraphDescription()

// Print page status
if (isOpenGraphDescription) {

  console.log('Page uses Page Description as Open Graph Description')
} else {
  console.log('This page has a custom Open Graph Description')
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
