# Source: https://developers.webflow.com/designer/reference/set-page-name.mdx

***

title: Set page name
slug: /designer/reference/set-page-name
description: Set the name of the page.
hidden: false
'og:title': Set page name
'og:description': Set the name of the page.
-------------------------------------------

## `page.setName(name)`

Set the name of the page.

#

### Syntax

```typescript
page.setName(name: string): Promise<null>
```

### Parameters

* **name**: `string` - The new name of the page.

### Returns

**Promise\<`null`>**

A promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set page name
await currentPage.setName("My New Page")
console.log(pageName)
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
