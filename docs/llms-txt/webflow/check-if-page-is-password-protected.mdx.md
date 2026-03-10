# Source: https://developers.webflow.com/designer/reference/check-if-page-is-password-protected.mdx

***

title: Check if page is password protected
slug: /designer/reference/check-if-page-is-password-protected
description: Check if the page is password protected.
hidden: true
'og:title': Check if page is password protected
'og:description': Check if the page is password protected.
----------------------------------------------------------

## `page.isPasswordProtected()`

Check if the page is password protected.

#

### Syntax

```typescript
page.isPasswordProtected(): Promise<boolean>
```

### Returns

**Promise\<`boolean`>**

A promise that resolves to a boolean value indicating whether the page is password protected.

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Check if current page is the homepage
const isPasswordProtected = await currentPage.isPasswordProtected()

if (isPasswordProtected) {
  console.log('Current page is PasswordProtected')
} else {
  console.log('Current page is not PasswordProtected')
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
