# Source: https://developers.webflow.com/designer/reference/check-description-is-used-as-search-description.mdx

***

title: Check if page description is used as search description
slug: /designer/reference/check-description-is-used-as-search-description
description: Method for checking if the page description is used as the search description.
hidden: false
'og:title': Check if page description is used as search description
'og:description': Method for checking if the page description is used as the search description.
------------------------------------------------------------------------------------------------

## `page.usesDescriptionAsSearchDescription()`

Check if the page description is used as the search description.

#

### Syntax

```typescript
page.usesDescriptionAsSearchDescription(): Promise<boolean>;
```

### Returns

**Promise\<`boolean`>**

A Promise that resolves to a `boolean` value.

#

### Example

```typescript
// Get current page
const currentPage = await webflow.getCurrentPage()

// Check search engine description
const isSearchDescription = await currentPage?.usesDescriptionAsSearchDescription()

if(isSearchDescription){
  console.log("This page uses its description as the search engine description")
} else {
  console.log("This page has a custom search engine description")
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
