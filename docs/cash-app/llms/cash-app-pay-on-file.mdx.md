# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/add-cash-app-pay-to-your-site/cash-app-pay-on-file.mdx

***

## stoplight-id: ikt556oor1jme

# Cash App Pay on file

## Overview

Cash App Pay on file allows customers to save their Cash App accounts with specific merchants. This makes it easy for merchants to take Cash App Pay payments and for buyers to make Cash App Pay payments.

Merchants can take a payment with the customer's prior approval. Customers can authorize merchants to charge them in the future, without having to go through a Cash App payment flow.

This setup allows for smooth, more convenient payment experiences and enables various use-cases such as frequent purchases or recurring subscriptions. See the [Overview of Cash App Pay on file](#overview-of-cash-app-pay-on-file) below.

## Terminology

* **Cash App Pay:** A digital payment method where customers can make payments with their Cash App account

* **Grant:** A payment token associated with a specific customer that merchants can use to initiate payments. Grants can be scoped to different payment methods (Cash App Afterpay, Cash App Pay) and can be consumed one or more times (one-time, on file)

* **[\$Cashtag:](https://cash.app/help/3123-what-is-a-cashtag)** A publicly-accessible, unique identifier (username) for individuals and businesses using Cash App. \$Cashtags can be changed up to three times for each Cash App account

* **Customer ID:** A non-public, unique identifier for developers to identify Cash App accounts. Customer ID is not accessible to Cash App customers and will not change if the associated \$cashtag is updated

## Common Uses of Cash App Pay on file

There are many common uses of Cash App Pay on file, several include:

* **Ecommerce Retailers:** Ecommerce merchants offer Cash App Pay on file to facilitate faster checkouts and enable more delightful payment experiences for their customers. It can also reduce cart abandonment, increase average transaction value, and boost sales

* **Subscription Services:** These are for merchants who offer goods and services that need regular payments, such as monthly subscriptions or recurring orders. You can use Cash App Pay on file to receive a customer payment during each billing cycle. This setup reduces the need for a manual payment each time, which allows for uninterrupted service and improved cash flow

* **Pre-orders:** Pre-orders allow customers to order products before they are released or restocked. Cash App Pay on file provides flexibility for merchants and empowers them to decide when and how to charge customers after a customer has placed a pre-order

* **Hospitality and Rentals:** Hospitality and rental merchants typically use Cash App Pay on file to cover advanced reservations and incidental charges such as room service

## Overview of Cash App Pay on file

Here is an overview of the Cash App Pay on file process:

1. **Storing Cash App Pay on file:** First, customers must successfully link their Cash App account and authorize merchants to store Cash App Pay on file on their behalf. Once successfully completed, merchants have access to a Cash App Pay on file grant and the customer's associated \$cashtag and customer ID.

2. **Taking Payments with Cash App Pay on file:** Once a Cash App Pay on file grant is approved and active, merchants can use the grant to initiate Cash App Pay payments on behalf of the customer.

3. **Managing Cash App Pay on file:** After a customer successfully links their Cash App account with a specific merchant, they may take specific actions. These actions include updating their \$cashtag or revoking their Cash App Pay on file grant. When these actions occur, it is important for merchants to get these updates and update relevant Cash App Pay on file details for customers.

### Pros and Cons of Cash App Pay on file

Storing Cash App Pay on file is standard practice for many merchants, but there are benefits and drawbacks to consider:

#### Pros

* **Increased Customer Convenience:** Merchant checkout is quicker and easier for returning customers as they can save Cash App Pay on file once and use it for subsequent payments. This can lead to more sales opportunities, lower cart abandonment, increased average transaction value, and more

* **Improved Customer Transparency:** Customers can track and manage merchants they have linked their Cash App account with directly within Cash App. Specifically, customers can unlink Cash App Pay on file tokens with specific merchants to prevent future unwanted payments. Fewer unwanted payments mean fewer refunds and chargebacks

* **Stronger Integration Resilience:** Cash App Pay on file customers only link to their Cash App account once, whereas one-time payments require customers to link their Cash App account for each payment. Integration issues that affect the Cash App linking process will not affect customers who have already successfully stored Cash App Pay on file with a particular merchant

#### Cons

* **Managing Cash App Pay Updates:** Merchants need to keep track of Cash App Pay on file expirations and updates. Failing to update Cash App Pay information on time can lead to declined payments and interrupted service. This may affect customer relationships

## How Cash App Pay on file Works in Detail

### Storing Cash App Pay on file

To store Cash App Pay on file, merchants first need to retrieve their Cash App Pay brand ID. Use the [Retrieve Mapping](/cash-app-afterpay/api-reference/reference/configuration/get-configuration-mappings) endpoint for this task:

#### Example Response

```JavaScript
[ 
  { 
    "name": "default", 
    "externalBrandId": "BRAND_xxxxxxxxxx" 
  } 
]
```

<Note>The Retrieve Mapping API response calls the brand ID `externalBrandId` whereas in the front-end JavaScript below, the `externalBrandId` is called `cashAppBrandId`.</Note>
Once the brand ID has been retrieved, merchants should initialize `Afterpay.js` for a Cash App on file grant request. The `cashAppBrandId` is set to the brand ID retrieved previously.

**Example code:**

```JavaScript
function initializeForCashAppOnFileGrant() { 
  var cashAppPayOnFileOptions = { 
    button: false, // set to false if using custom button 
    onComplete: function(event) { 
      const { cashtag, expiresAt, grantId, id } = event.data; 
      console.log("Data object: ", event.data); 
      console.log("Cashtag: ", cashtag); 
      console.log("ExpiresAt: ", expiresAt); 
      console.log("GrantId: ", grantId); 
      console.log("Id: ", id); }, 
    redirectUrl: "https://www.example.com", // where mobile customers should be redirected to 
    cashAppBrandId: "BRAND_xxxxxxxxxx" 
  } 

  AfterPay.initializeForCashAppOnFileGrant({ 
    countryCode: "US", 
    cashAppPayOnFileOptions 
  }); 
}
```

Once the customer successfully links their Cash App account, the `onComplete` callback returns with the Cash App Pay on file grant, together with  the associated customer's \$cashtag and customer ID. Merchants should store this data for future use.

### Suggested copy for Cash App Pay on file disclaimer

For best practice, Cash App recommends you add the following disclaimer wherever customers can store Cash App Pay on file:

*By continuing, you authorize `{{Merchant Name}}` to debit your Cash App account for this payment and future payments in accordance with `{{Merchant Name}}`'s terms, until this authorization is revoked. You can change this authorization anytime in your Cash App Settings.*

## Taking Payments with Cash App Pay on file

1. To initiate a Cash App Pay on file payment, merchants must use a valid Cash App Pay on file grant and create a new Cash App Afterpay Checkout with the `isCashAppPay: true` parameter.

2. Use the Create Checkout endpoint to generate a checkout token. Then use this checkout token and grant ID to authorize a new payment via the direct capture or auth endpoint.

<Note>
  Customers do not need to complete the checkout flow for new payments once an on file grant has been generated and is active.
</Note>

## Storing Cash App Pay on file within Checkout flow

This flow is useful if a customer is completing a merchant's checkout flow while also attempting to store their Cash App Pay on file. The flow enables merchants to complete the store Cash App Pay on file and take payments with Cash App Pay on file in a more streamlined way. Do the following:

1. Call the `Create Checkout` endpoint and add the `isCashAppPay: true` parameter.

2. Use the token in combination with the Standard Checkout flow, but call `AfterPay.initializeForCashAppPay` instead of Cash App Afterpay. Include the `requestOnFileGrant: true` within `cashAppPayOptions` for `Afterpay.initializeForCashAppPay`.

3. Store the Cash App Pay on file grant, \$cashtag, and customer ID returned in the `onComplete` callback.

4. Call the [Auth](/cash-app-afterpay/api-reference/reference/payments/auth) or [Direct Capture](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment) endpoints and make sure to include the Cash App Pay on file grant in the request.

Example code:

```javascript
function initAfterPay() { 
  var cashAppPayOptions = { 
    requestOnFileGrant: true, 
    button: { size: 'small', // "medium" | "small" width: 'full', // "full" | "static" theme: 'dark', // "dark" | "light" shape: 'round' // "round" | "semiround" }, 
    redirectUrl: window.location.href, // where mobile customers should be redirected to 
    onComplete: function(event) { 
      const { cashtag, expiresAt, grantId, id, token } = event.data; 
      console.log("Data object: ", event.data); 
      console.log("Cashtag: ", cashtag); 
      console.log("ExpiresAt: ", expiresAt); 
      console.log("GrantId: ", grantId); 
      console.log("Id: ", id); 
      console.log("Token: ", token); }, /* Optional event listeners for merchants to track customer behavior and listen for transaction events in the lifecycle */ 
  eventListeners: { 
    "CUSTOMER_INTERACTION": ({ isMobile }) => { 
      console.log(`CUSTOMER_INTERACTION`) 
      if (isMobile) { // captureMobileMetrics() } 
      else { // captureDesktopMetrics() } }, 
        "CUSTOMER_REQUEST_DECLINED": () => { console.log(`CUSTOMER_REQUEST_DECLINED`) }, 
        "CUSTOMER_REQUEST_APPROVED": () => { console.log(`CUSTOMER_REQUEST_APPROVED`) }, 
        "CUSTOMER_REQUEST_FAILED": () => { console.log(`CUSTOMER_REQUEST_FAILED`) } } } ​ 
  AfterPay.initializeForCashAppPay({ countryCode: "US", token: "ORDER_TOKEN_PLACEHOLDER", cashAppPayOptions }); 
}
```

## Managing Cash App Pay on file

Once a customer has authorized a Cash App Pay on file grant, merchants should ensure they implement the following features. These features ensure optimal Cash App Pay on file functionality:

* **Revoke Cash App Pay on file grant via Merchant:** Customers should be able to revoke their Cash App Pay on file grant directly within the merchant account settings or the merchant checkout flow. This ensures that on file grants are deactivated once they are no longer needed. It  builds customer trust as customers can manage their payment method availability directly with the merchant, versus making changes within Cash App

  * Use the [**Revoke Grant**](/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/revoke-grant) endpoint to revoke an active Cash App Pay on file grant when a customer unlinks their Cash App Pay on file

* **Revoke Cash App Pay on file grant via Cash App:** Customers can revoke their Cash App Pay on file grants with specific merchants within their Cash App settings. Therefore, merchants should subscribe to these events and unlink Cash App Pay on file for customers who have unlinked their on file grants within Cash App

  * Use the [**Event: Grant Updated**](/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/schemas/grant-status-updated) webhook to remove Cash App Pay on file grants that were unlinked within Cash App

* **Cash App Pay Updates:** Customers can make changes to their Cash App account details such as updating their \$cashtag. Also, on file grants expire after 10 years. Therefore, it is important that merchants subscribe to Cash App Pay grant updates, and keep their own records up to date

  * Use the [**Event: Grant Status Updated**](/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/schemas/grant-status-updated) webhook to subscribe to Cash App Pay updates associated with specific Cash App Pay on file grants

  * Use the [**Retrieve Grant**](/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/retrieve-grant) endpoint to retrieve the current state of Cash App Pay on file grants
