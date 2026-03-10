# Source: https://developers.webflow.com/designer/reference/check-if-page-is-draft.mdx

***

title: Check if page is draft
slug: /designer/reference/check-if-page-is-draft
description: Method for checking if a page is a draft.
hidden: false
'og:title': Check if page is draft
'og:description': Method for checking if a page is a draft.
-----------------------------------------------------------

## `page.isDraft()`

Check if the page is a draft.

#

### Syntax

```typescript
page.isDraft(): Promise<boolean>;
```

### Returns

**Promise\<Boolean>**

A promise that resolves to a boolean value indicating whether the page is a draft.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Check page status
const isDraft = await currentPage.isDraft()

// Print page status
if (isDraft) {

  console.log('Page is draft')
} else {
  console.log('Page is not a draft')
}
```

<div>
  <a href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62">
    Try this example
  </a>
</div>

### Designer Ability

| Designer Ability    | Locale | Branch | Workflow | Sitemode |
| :------------------ | :----- | :----- | :------- | :------- |
| **designerAbility** | Any    | Any    | Any      | Any      |
