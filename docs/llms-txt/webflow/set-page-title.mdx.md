# Source: https://developers.webflow.com/designer/reference/set-page-title.mdx

***

title: Set page title
slug: /designer/reference/set-page-title
description: Set the title of the page.
hidden: false
'og:title': Set page title
'og:description': Set the title of the page.
--------------------------------------------

## `page.setTitle(title)`

Set the title of the page.

#

### Syntax

```typescript
page.setTitle(title: string | null): Promise<null>
```

### Parameters

* **title**: `string | null` - The new title of the page.

### Returns

**Promise\<`null`>**

A promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set page Title
await currentPage.setTitle("My New Title")
console.log(pageTitle)
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
