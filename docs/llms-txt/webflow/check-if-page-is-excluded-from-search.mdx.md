# Source: https://developers.webflow.com/designer/reference/check-if-page-is-excluded-from-search.mdx

***

title: Check if page is excluded from search
slug: /designer/reference/check-if-page-is-excluded-from-search
description: Method for checking if a page is excluded from internal site search.
hidden: false
'og:title': Check if page is excluded from search
'og:description': Method for checking if a page is excluded from internal site search.
--------------------------------------------------------------------------------------

## `page.isExcludedFromSearch()`

Check if the page is excluded from [internal site search.](https://help.webflow.com/hc/en-us/articles/33961242348179-Site-search)

#

### Syntax

```typescript
page.isExcludedFromSearch(): Promise<boolean>;
```

### Returns

**Promise\<`boolean`>**

A Promise that resolves to a `boolean` value.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage()

// Check if page is excluded from webflow's internal site search
const isExcluded = await currentPage?.isExcludedFromSearch()

if (isExcluded){
  console.log("Current page is excluded from Webflow's internal site search")
} else {
  "Current page is included in included in Webflow's internal site search"
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
