# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/api-quickstart.mdx

***

## stoplight-id: uxicydn8nsph0

# API Quickstart

## Prerequisites

Before you get started, make sure that you have:

* Signed up for a merchant account at get.afterpay.com
* Received sandbox credentials from Cash App Afterpay

Cash App Afterpay is available to merchants with businesses in the United States. For businesses in Canada, Australia, and New Zealand, see [Afterpay](https://developers.afterpay.com/docs/api/welcome/getting-started). For UK businesses, see [Clearpay](https://developers.clearpay.co.uk/clearpay-online/docs/getting-started-with-clearpay-online).

## Basic API calls

### Get Configuration (/v2/configuration)

The [Get Configuration](/cash-app-afterpay/api-reference/reference/configuration/get-configuration) endpoint retrieves your Afterpay order limits. We recommend regularly calling this endpoint as part of a scheduled background process and storing the `minimumAmount` and `maximumAmount` values on your server.

### Create Checkout (/v2/checkouts)

The [Create Checkout](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1) endpoint creates a new checkout and returns an order token. When you call the Create Checkout endpoint, you give Cash App Afterpay order details, customer information, and the URL to direct customers to after checkout. Cash App Afterpay responds with a token used to identify the checkout. Use this token to direct the customer to the Cash App Afterpay checkout flow.

### Capture Full Payment (/v2/payments/capture)

To capture the full order value immediately, call the [Capture Full Payment](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment) endpoint. Calling this endpoint completes payment approval, starts the customer's payment plan, and settles the full order to your bank account. When you call this endpoint, you provide the order token and receive a payment object.

### Authorize Payment (/v2/payments/auth)

This is the first endpoint to call when you use the deferred payment flow. To authorize the full payment amount up front and collect funds later, start by calling the [Authorize Payment](/cash-app-afterpay/api-reference/reference/payments/auth) endpoint. Calling this endpoint completes payment approval for a certain amount. When you call this endpoint, you provide the order token and receive a payment object.

### Capture Authorized Payment (/v2/payments/\{orderId}/capture)

This is the second endpoint to call when you use the deferred payment flow. After the payment is authorized, call the [Capture Payment](/cash-app-afterpay/api-reference/reference/payments/capture-payment) endpoint to capture a full or partial payment. When you call this endpoint, you provide a unique request ID and the amount you want to capture (up to the authorized amount) and you receive an updated payment object.

### Create Refund (/v2/payments/\{orderId}/refund)

Call the [Create Refund](/cash-app-afterpay/api-reference/reference/payments/create-refund) endpoint to issue a full or partial refund. When you call this endpoint, you provide a unique request ID and the amount you want to refund (up to the captured amount) and you receive a refund object.

## Post-requisites

While you set up and test your integration, you can view all sandbox orders in the [Business Hub](/cash-app-afterpay/guides/welcome/business-hub).

After you set up your API integration, contact Cash App Afterpay to complete certification testing and receive your live credentials. Once you're given live credentials, you can launch Cash App Afterpay on your website.
