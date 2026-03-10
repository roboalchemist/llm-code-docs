# Source: https://developers.webflow.com/designer/reference/set-draft.mdx

***

title: Set draft status
slug: /designer/reference/set-draft
description: Set the draft status of the page.
'og:title': Set draft status
'og:description': Set the draft status of the page.
---------------------------------------------------

## `page.setDraft()`

Set the draft status of the page.

#

### Syntax

```typescript
page.setDraft(isDraft: boolean): Promise<null>
```

### Parameters

* **isDraft**: *boolean* - Whether the page should be set to draft mode.

### Returns

**Promise\<`null`>**

A promise that resolves to `null`.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Set page as draft
await currentPage.setDraft(true)
const isDraft = await currentPage.isDraft()

// Print status
console.log(isDraft)
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
