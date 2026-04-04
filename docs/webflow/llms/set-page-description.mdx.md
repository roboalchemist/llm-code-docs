# Source: https://developers.webflow.com/designer/reference/set-page-description.mdx

***

title: Set page description
slug: /designer/reference/set-page-description
description: Set the description of the page.
hidden: false
'og:title': Set page description
'og:description': Set the description of the page.
--------------------------------------------------

## `page.setDescription(description)`

Set the description of the page.

#

### Syntax

```typescript
page.setDescription(description: string | null): Promise<null>
```

### Parameters

* **description**: `string | null` - The new description of the page.

### Returns

**Promise\<`null`>**

A promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set page Description
await currentPage.setDescription("My New Description")
console.log(pageDescription)
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
