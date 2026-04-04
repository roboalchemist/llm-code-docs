# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/network-api.mdx

***

## stoplight-id: 2982fc657d14b

# Network API

The Network API helps developers manage payment processing, merchant registration, and dispute handling on Cash App Pay. It is an entirely server-side API, and cannot be called from a browser or point of sale device directly.

It requires API key authentication for every request, as well as a [X-Region](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/regions-and-localization) header.

## Endpoints

* Payments
  * [List payments](/cash-app-pay-partner-api/api-reference/network-api/list-payments)
  * [Retrieve payment](/cash-app-pay-partner-api/api-reference/network-api/retrieve-payment)
  * [Create payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment)
  * [Void payment](/cash-app-pay-partner-api/api-reference/network-api/void-payment)
  * [Capture payment](/cash-app-pay-partner-api/api-reference/network-api/capture-payment)
  * [Void payment by idempotency key](/cash-app-pay-partner-api/api-reference/network-api/void-payment-by-idempotency-key)
* Refunds
  * [List refunds](/cash-app-pay-partner-api/api-reference/network-api/list-refunds)
  * [Retrieve refund](/cash-app-pay-partner-api/api-reference/network-api/retrieve-refund)
  * [Create refund](/cash-app-pay-partner-api/api-reference/network-api/create-refund)
  * [Void refund](/cash-app-pay-partner-api/api-reference/network-api/void-refund)
  * [Capture refund](/cash-app-pay-partner-api/api-reference/network-api/capture-refund)
  * [Void refund by idempotency key](/cash-app-pay-partner-api/api-reference/network-api/void-refund-by-idempotency-key)
* Merchants
  * [Create merchant](/cash-app-pay-partner-api/api-reference/network-api/create-merchant)
  * [Upsert merchant](/cash-app-pay-partner-api/api-reference/network-api/upsert-merchant)
  * [Retrieve merchant](/cash-app-pay-partner-api/api-reference/network-api/retrieve-merchant)
  * [Update merchant](/cash-app-pay-partner-api/api-reference/network-api/update-merchant)
  * [List merchants](/cash-app-pay-partner-api/api-reference/network-api/list-merchants)
* Brands
  * [Create brand](/cash-app-pay-partner-api/api-reference/network-api/create-brand)
  * [Upsert brand](/cash-app-pay-partner-api/api-reference/network-api/upsert-brand)
  * [Retrieve brand](/cash-app-pay-partner-api/api-reference/network-api/retrieve-brand)
  * [Update brand](/cash-app-pay-partner-api/api-reference/network-api/update-brand)
  * [List brands](/cash-app-pay-partner-api/api-reference/network-api/list-brands)
* Customers
  * [Retrieve customer](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer)
  * [List customers](/cash-app-pay-partner-api/api-reference/network-api/list-customers)
  * [Retrieve customer grant](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer-grant)
  * [List customer grants](/cash-app-pay-partner-api/api-reference/network-api/list-customer-grants)
  * [Revoke customer grant](/cash-app-pay-partner-api/api-reference/network-api/revoke-customer-grant)
* Disputes
  * [List disputes](/cash-app-pay-partner-api/api-reference/network-api/list-disputes)
  * [Retrieve dispute](/cash-app-pay-partner-api/api-reference/network-api/retrieve-dispute)
  * [Challenge dispute](/cash-app-pay-partner-api/api-reference/network-api/challenge-dispute)
  * [Accept dispute](/cash-app-pay-partner-api/api-reference/network-api/accept-dispute)
  * [List dispute evidence](/cash-app-pay-partner-api/api-reference/network-api/list-dispute-evidence)
  * [Retrieve dispute evidence](/cash-app-pay-partner-api/api-reference/network-api/retrieve-dispute-evidence)
  * [Create dispute evidence text](/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-text)
  * [Create dispute evidence file](/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-file)
  * [Delete dispute evidence](/cash-app-pay-partner-api/api-reference/network-api/delete-dispute-evidence)
* Fee Plans
  * [List fee plans](/cash-app-pay-partner-api/api-reference/network-api/list-fee-plans)
  * [Retrieve fee plan](/cash-app-pay-partner-api/api-reference/network-api/retrieve-fee-plan)
