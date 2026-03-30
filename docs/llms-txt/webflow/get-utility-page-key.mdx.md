# Source: https://developers.webflow.com/designer/reference/get-utility-page-key.mdx

***

title: Get utility page key
slug: /designer/reference/get-utility-page-key
description: Get the utility page key of the page.
hidden: true
'og:title': Get utility page key
'og:description': Get the utility page key of the page.
-------------------------------------------------------

## `page.getUtilityPageKey()`

Get the page key of a [Webflow utility page.](https://help.webflow.com/hc/en-us/articles/33961362705171-Page-URLs#utility-pages)

#

### Syntax

```typescript
page.getUtilityPageKey(): Promise<null | UtilKey>
```

### Returns

**Promise\<`null` | `UtilKey`>**

A promise that resolves to one of the following utility page keys, or `null` if the page is not a utility page:

* `'401'` - Unauthorized access page
* `'404'` - Not found page
* `'search'` - Search results page
* `'ecommerce-checkout'` - Main checkout page
* `'ecommerce-paypal-checkout'` - PayPal checkout flow
* `'ecommerce-confirmation'` - Order confirmation page
* `'usys-log-in'` - User login page
* `'usys-sign-up'` - User registration page
* `'usys-reset-password'` - Password reset request page
* `'usys-user-account'` - User account management
* `'usys-update-password'` - Password update page
* `'usys-access-denied'` - Access denied error page

#

### Example

```typescript
// Get Current Page
const currentPage = await webflow.getCurrentPage() as Page

// Get utility page key
const utilityKey = await currentPage.getUtilityPageKey()
console.log("Utility Key", utilityKey)
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
