# Source: https://developers.webflow.com/designer/reference/set-search-image.mdx

***

title: Set search image
slug: /designer/reference/set-search-image
description: Method for setting the search image of a page.
hidden: false
'og:title': Set search image
'og:description': Method for setting the search image of a page.
----------------------------------------------------------------

## `page.setSearchImage(url)`

Set the search image of the page.

#

### Syntax

```typescript
page.setSearchImage(url: string | null): Promise<null>;
```

### Parameters

* **url**: *`string | null`* - The URL of the image to set as the search image.

### Returns

**Promise\<`null`>**

A Promise that resolves to `null`.

#

### Example

```typescript
// Get current page
const currentPage = await webflow.getCurrentPage()

// Set search image
await currentPage?.setSearchImage('https://example.com/image.jpg')
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
