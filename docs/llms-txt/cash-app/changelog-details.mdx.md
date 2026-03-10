# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/changelog/changelog-details.mdx

<Note>
   Android and iOS SDK changelogs are found in GitHub. See changelogs here: 

  <br />

  [Android SDK](https://github.com/cashapp/cash-app-pay-android-sdk/blob/main/CHANGELOG.md)

   

  <br />

  [iOS SDK](https://github.com/squareup/cash-app-pay-sdk-ios/blob/main/RELEASE-NOTES.md)

   
</Note>

# Changelog Details

Find all the API changelogs listed below:

<Note>
   The changelogs are listed from newest to oldest (in ascending order) 
</Note>

***

## Added `statement_descriptor` field to `enrichments` when creating a payment

Date: Feb-10-2025
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

[Create payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment)

Description:

**Description:** In the Network API `Create payment`, we have added a new optional `statement_descriptor` field to the `enrichments` sub-resource within the payment resource. This field allows a merchant, via their Payment Service Provider, to add a descriptor for the payment, which will then be reflected in-app within a customer's Activity page.

If the input for this field exceeds the character limit, it will be truncated to the limit, then suffixed with an ellipsis (...).

***

## Added `PAYMENT_DECLINED_CUSTOMER_BLOCKED_BY_MERCHANT` failure code

Date: Apr-15-2025
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

[Create payment authorization](/cash-app-pay-partner-api/api-reference/network-api/create-payment-authorization)

**Description:**

A new standalone error code has been added to payment authorizations, `PAYMENT_DECLINED_CUSTOMER_BLOCKED_BY_MERCHANT`, to indicate that a payment was declined because the customer has blocked the merchant. This error code is returned when a payment is declined due to  a customer-initiated block.

***

## Added `Create payment authorization` endpoint

Date: Feb-28-2025
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

[Create payment authorization](/cash-app-pay-partner-api/api-reference/network-api/create-payment-authorization)

**Description:**

The new Network API `Create payment authorization` enables incremental authorization on previously created payments. Instead of overcapturing, developers can request an additional authorization for an increased amount without putting at risk the original authorization.

Additionally, this adds an optional `authorization_updates` field on all `Payment` schemas that may exist in API responses. This field will contain only incremental authorization updates, and not the authorization from the original request.

***

## Add `initiation` field to `enrichments` when creating a payment

Date: Feb-10-2025
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

[Create payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment)

Description:

**Description:** In the Network API `Create payment`, we have added a new optional `initiation` field to the enrichment sub-resource, within the payment resource that contains information about who initiated a transaction. There is currently one property within this field: `actor`, which can be one of the following values:

* `CUSTOMER`: describe the payment as a customer initiated transaction
* `MERCHANT`: describe the payment as a merchant initiated transaction

***

## Reject requests uploading empty evidence files

Date: Jul-02-2024
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

[Create dispute evidence file](/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-file)

**Description:**

Fail requests to create a dispute evidence file if the file is empty.

***

## Added `List customer grants` endpoint

Date: Jan-31-2024
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

[List customer grants](/cash-app-pay-partner-api/api-reference/network-api/list-customer-grants)

**Description:**

Developers can now retrieve all grants for a customer.

***

## Created alternative signature for multipart/form-data requests

Date: Jan-19-2024
<br />Changelog Type: Improved
<br />Metadata Tag: Network API

**Affected endpoints:**

[Create dispute evidence file](/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-file)

**Description:**

Computing a valid request signature for `multipart/form-data` requests is challenging. A [new signing algorithm](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/signing-requests) for multipart requests is supported that includes an alternative signature in the request body, rather than the existing `X-Signature` header.

***

## Improved Grant flow back navigation update

Date: Dec-15-2023
<br />Changelog Type: Improved
<br />Metadata Tag: Grant Flow

**Description:**

When a customer initiates the Cash App customer registration process, they are deeplinked from the merchant checkout page into Cash App where they are authenticated via the grant flow and then subsequently redirected back to the merchant checkout page.

The mechanism to automatically redirect back to the merchant checkout page after the grant flow was retired in iOS 17; therefore, a new screen has been added to the grant flow which explicitly guides the customer to backward redirect via a button on the top left corner. If the customer doesn’t complete the backward redirect action, they will be prompted to forward redirect back to the merchant checkout page via a separate button within the grant screen.

As before, developers are expected to handle both forward navigation and backward navigation scenarios after the grant flow has been completed.

***

## Fixed stale customer request after grant is revoked

Date: Dec-15-2023 (select partners)
<br />Changelog Type: Improved
<br />Metadata Tag: Customer Request API

**Affected endpoints:**

[Retrieve request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request)

**Description:**

An approved customer request contains grants that can be used to perform actions specified in the request using the Network API. Previously if a grant was consumed or revoked post customer request approval, the Customer Request API would return stale data - the used grant would appear as active even though the grant was consumed or revoked.

With this fix, the Customer Request API will always return the most up-to-date grant status if the customer request is retrievable.

As a reminder, the [Retrieve Customer Grant](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer-grant) endpoint within the Network API will always return the most up-to-date grant status.

***

## Fixed documentation for activity reconciliation report files

Date: Dec-08-2023
<br />Changelog Type: Improved
<br />Metadata Tag: Settlement

**Description:** We removed date ranges from the specifications of the activity reconciliation report file names as generating activity reconciliation reports for a date range is not supported.
We also added clarifications around the semantics of the yyMMdd date prefix in the activity reconciliation report file name.

***

## Improved Grant flow idle detection

Date: Oct-18-2023
<br />Changelog Type: Improved
<br />Metadata Tag: Grant Flow

**Affected endpoints:**

[Retrieve request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request)

**Description:**

During customer registration, the customer may be prompted to complete a subsequent action before the flow is approved and a grant is generated. If the flow is not actioned upon after a specified TTL, the customer request will transition to a `DECLINED` status.

Previously, the customer request would remain in a `PROCESSING` status until the customer request expired.

With this change, developers will have a more straightforward customer request lifecycle where customer requests will reach a terminal status and be declined more quickly when a customer fails to complete the grant flow before the customer request expires.

Because customer request status can be updated without a subsequent redirect back to the merchant checkout page, developers should ensure that they can properly react to a customer request status change with or without a redirect occurring (Pay Kit handles this scenario automatically).

***

## Improved Sandbox App magic value support

Date: Oct-5-2023
<br />Changelog Type: Improved
<br />Metadata Tag: Sandbox

**Description:**
Previously, developers were required to use these [magic values](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox#magic-values) with the [Create Payment API](/cash-app-pay-partner-api/api-reference/network-api/create-payment) to produce certain behaviors within the Cash App Developer Sandbox.

Now, developers can use the Sandbox App to simulate certain behaviors such as payment declined compliance, payment declined insufficient funds, payment declined other, payment declined risk, payment invalid too large, and payment invalid too small.

***

## Added `capture_before` field to payment resource

Date: Oct-04-2023
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

* [Create payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment)
* [Void payment](/cash-app-pay-partner-api/api-reference/network-api/void-payment)
* [Capture payment](/cash-app-pay-partner-api/api-reference/network-api/capture-payment)
* [List payments](/cash-app-pay-partner-api/api-reference/network-api/list-payments)
* [Retrieve payment](/cash-app-pay-partner-api/api-reference/network-api/retrieve-payment)
* [Void payment by idempotency key](/cash-app-pay-partner-api/api-reference/network-api/void-payment-by-idempotency-key)

**Description:** In the Network API, we have added a new `capture_before` field to the payment resource that designates when created payments should be captured by.

***

## Improved Payment Authorization Failure Codes

Date: Sep-19-2023
<br />Changelog Type: Improved
<br />Metadata Tag: Network API

**Affected endpoints:**

* [Create payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment)

**Description:**

Improvements have been made to return a more specific payment authorization failure code when a Cash App Pay payment authorization failure occurs.

More specifically, payments that previously were coded with the `PAYMENT_DECLINED_OTHER` error code have been updated to reflect a more accurate error code such as `PAYMENT_DECLINED_RISK`, `PAYMENT_DECLINED_COMPLIANCE` and `PAYMENT_DECLINED_LIMIT_REACHED`.

***

## Added `Create request chain` endpoint

Date: Aug-4-2023
<br />Changelog Type: Added
<br />Metadata Tag: Management API

**Affected endpoints:**

* [Create request chain](/cash-app-pay-partner-api/api-reference/management-api/create-request-chain)

**Description:**

Clients can improve their performance by implementing request chaining into their integration. For more information, see [Optimizing Performance with Request Chaining](/cash-app-pay-partner-api/guides/technical-guides/integrating-with-cash-app-pay/optimizing-performance-with-request-chaining).

***

## Added `FEE_PLANS_READ` scope to Create API Key’s scope

Date: July-13-2023
<br />Changelog Type: Added
<br />Metadata Tag: Management API

**Affected endpoints:**

* [Create API Key](/cash-app-pay-partner-api/api-reference/management-api/create-api-key)

**Description:**

When creating API keys, clients may add the `FEE_PLANS_READ` scope in order to retrieve their fee plans.

***

## Added `customer.deleted` webhook event

Date: May-30-2023
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

* [RetrieveCustomer](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer)

**Description:**

When a Cash App customer account is deleted, the `customer.deleted` webhook event is delivered with the relevant customer information. Any attempt to retrieve this customer via `RetrieveCustomer` will return the new `CUSTOMER_DELETED_ACCOUNT` error.

***

## Fixed nesting of `object` property of all webhook event schema

Date: May-23-2023
<br />Changelog Type: Fixed
<br />Metadata Tag: Management API, Customer Request API

**Affected webhook events**

* [Event: grant.created](/cash-app-pay-partner-api/api-reference/network-api/grant-created)
* [Event: grant.status.updated](/cash-app-pay-partner-api/api-reference/network-api/grant-status-updated)
* [Event: customer.created](/cash-app-pay-partner-api/api-reference/network-api/customer-created)
* [Event: customer.updated](/cash-app-pay-partner-api/api-reference/network-api/customer-updated)
* [Event: dispute.created](/cash-app-pay-partner-api/api-reference/network-api/dispute-created)
* [Event: dispute.status.updated](/cash-app-pay-partner-api/api-reference/network-api/dispute-status-updated)
* [Event: merchant.status.updated](/cash-app-pay-partner-api/api-reference/network-api/merchant-status-updated)
* [Event: payment.status.updated](/cash-app-pay-partner-api/api-reference/network-api/payment-status-updated)
* [Event: refund.status.updated](/cash-app-pay-partner-api/api-reference/network-api/refund-status-updated)
* [Event: customer\_request.state.updated](/cash-app-pay-partner-api/api-reference/customer-request-api/customer-request-state-updated)

**Description:**

The webhook event schemas now include an additional layer of nesting under the `object` property.

***

## Updated map validation errors

Date: May-15-2023
<br />Changelog Type: Fixed
<br />Metadata Tag: Network API, Customer Request API

**Affected endpoints:**

* [Create brand](/cash-app-pay-partner-api/api-reference/network-api/create-brand)
* [Update brand](/cash-app-pay-partner-api/api-reference/network-api/update-brand)
* [Upsert brand](/cash-app-pay-partner-api/api-reference/network-api/upsert-brand)
* [Create dispute evidence (text)](/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-text)
* [Create dispute evidence (file)](/cash-app-pay-partner-api/api-reference/network-api/create-dispute-evidence-file)
* [Create merchant](/cash-app-pay-partner-api/api-reference/network-api/create-merchant)
* [Update merchant](/cash-app-pay-partner-api/api-reference/network-api/update-merchant)
* [Upsert merchant](/cash-app-pay-partner-api/api-reference/network-api/upsert-merchant)
* [Create payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment)
* [Create refund](/cash-app-pay-partner-api/api-reference/network-api/create-refund)
* [Create request](/cash-app-pay-partner-api/api-reference/customer-request-api/create-request)
* [Update request](/cash-app-pay-partner-api/api-reference/customer-request-api/update-request)

**Description:**

In the Network API and Customer Request API, when the `metadata` field is constructed with too few or too many elements, error codes will be returned. Previously these error codes were: `ARRAY_LENGTH_TOO_SHORT` and `ARRAY_LENGTH_TOO_LONG`. But now, we have changed them to:   `TOO_FEW_MAP_ELEMENTS` and `TOO_MANY_MAP_ELEMENTS`.

***

## Added new fee plan API endpoints

Date: Mar-08-2023
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

* [List fee plans](/cash-app-pay-partner-api/api-reference/network-api/list-fee-plans)
* [Retrieve fee plan](/cash-app-pay-partner-api/api-reference/network-api/retrieve-fee-plan)
* [List merchants](/cash-app-pay-partner-api/api-reference/network-api/list-merchants)
* [Create merchant](/cash-app-pay-partner-api/api-reference/network-api/create-merchant)
* [Upsert merchant](/cash-app-pay-partner-api/api-reference/network-api/upsert-merchant)
* [Retrieve merchant](/cash-app-pay-partner-api/api-reference/network-api/retrieve-merchant)
* [Update merchant](/cash-app-pay-partner-api/api-reference/network-api/update-merchant)
* [List payments](/cash-app-pay-partner-api/api-reference/network-api/list-payments)
* [Create payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment)
* [Retrieve payment](/cash-app-pay-partner-api/api-reference/network-api/retrieve-payment)
* [Capture payment](/cash-app-pay-partner-api/api-reference/network-api/capture-payment)
* [Void payment](/cash-app-pay-partner-api/api-reference/network-api/void-payment)
* [Void payment](/cash-app-pay-partner-api/api-reference/network-api/void-refund-by-idempotency-key)

**Description:**

In the Network API, merchants can now be created/updated to use default fee plans for in-app, in-person, and/or online payments. The fee information used for each payment will be available in the payment APIs as the `fee_rate` and `fee_amount`.

You can find details on the currently applied fee plan by using the new fee plans APIs [List fee plans](/cash-app-pay-partner-api/api-reference/network-api/list-fee-plans)

* [Retrieve fee plan](/cash-app-pay-partner-api/api-reference/network-api/retrieve-fee-plan).

***

## Status field added to the WebhookEndpoint response

Date: Jan-09-2023
<br />Changelog Type: Added
<br />Metadata Tag: Management API, Webhook

**Affected endpoints:**

* [List webhook endpoints](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-endpoints)
* [Create webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint)
* [Retrieve webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/retrieve-webhook-endpoint)
* [Update webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/update-webhook-endpoint)

**Description:**

In the Management API,`WebhookEndpoint` responses now include the approval status of a webhook endpoint. Once a webhook endpoint is approved, Cash App will deliver events to that webhook endpoint.

***

## Customer added as a possible type for WebhookEvent EventData

Date: Nov-29-2022
<br />Changelog Type: Added
<br />Metadata Tag: Management API, Webhook

**Affected endpoints:**

* [List webhook events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events)

**Description:**

<br />

In the Management API, we will now emit the customer events, `customer.created` and `customer.updated`, with the type `customer`.

***

## Documentation for the X-Signature and X-Region header parameters

Date: Nov-29-2022
<br />Changelog Type: Added
<br />Metadata Tag: Management API, Webhook

**Affected endpoints:**

* [List webhook events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events)

**Description:**
In the Management API, the `X-Signature` and `X-Region` header parameters on the `List Webhook Events` endpoint were previously undocumented and we documented them.

***

## Webhook Endpoints default delivery\_timeout and maximum delivery\_timeout updated

Date: Nov-02-2022
<br />Changelog Type: Improved
<br />Metadata Tag: Management API, Webhook

**Affected endpoints:**

* [Create webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint)
* [Update webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/update-webhook-endpoint)

**Description:**
In the Management API, we updated the default `delivery_timeout` of Webhook Endpoints from 30s to 5s and the maximum `delivery_timeout` from 30s to 10s.

***

## Documentation for the Upsert Merchant and Update Merchant endpoints

Date: Nov-01-2022
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

* [Upsert Merchant](/cash-app-pay-partner-api/api-reference/network-api/upsert-merchant)
* [Update Merchant](/cash-app-pay-partner-api/api-reference/network-api/update-merchant)

**Description:**
In the Network API, the `metadata` request parameter for the `Upsert Merchant` and `Update Merchant` endpoints was previously undocumented and we added new documentation for it.

***

## New customer request channel for native mobile applications

Date: Oct-31-2022
<br />Changelog Type: Added
<br />Metadata Tag: Customer Request API

**Affected endpoints:**

* [Create request](/cash-app-pay-partner-api/api-reference/customer-request-api/create-request)
* [Retrieve request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request)
* [Update request](/cash-app-pay-partner-api/api-reference/customer-request-api/update-request)

**Description:** In the Customer Request API, when creating new customer requests, a new channel, `IN_APP`, can be specified if the customer scans a QR code or is redirected to Cash App from a native mobile application.

***

## Documentation for customer\_metadata

Date: Oct-31-2022
<br />Changelog Type: Added
<br />Metadata Tag: Customer Request API

**Affected endpoints:**

* [Create request](/cash-app-pay-partner-api/api-reference/customer-request-api/create-request)
* [Retrieve request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request)
* [Update request](/cash-app-pay-partner-api/api-reference/customer-request-api/update-request)

**Description:** In the Customer Request API, we added missing documentation about `customer_metadata` to the following:

* `Request response` object that included a `customer_metadata` attribute
* `Create request` endpoint that accepted the `request.customer_metadata` attribute

***

## Documentation of 404 responses for Retrieve Refund and Capture Refund operations

Date: Oct-31-2022
<br />Changelog Type: Improved
<br />Metadata Tag: Network API

**Affected endpoints:**

* [Retrieve refund](/cash-app-pay-partner-api/api-reference/network-api/retrieve-refund)
* [Capture refund](/cash-app-pay-partner-api/api-reference/network-api/capture-refund)

**Description:** In the Network API, the 404 responses for `Retrieve Refund` and `Capture Refund` are now correctly documented as `ErrorResponse` objects. The responses were previously documented as generic objects.

***

## Forward redirect a declined Grant to CUSTOMER\_REQUEST\_DECLINED event not firing

Date: Oct-13-2022
<br />Changelog Type: Fixed
<br />Metadata Tag: Pay Kit SDK

**Description:** In Pay Kit SDK, we fixed the error where a forward redirect from a declined Grant of the `CUSTOMER_REQUEST_DECLINED` event was not firing. We now consistently send the `CUSTOMER_REQUEST_DECLINED` event.

***

## Updated the description of Delete webhook endpoint

Date: Aug-17-2022
<br />Changelog Type: Improved
<br />Metadata Tag: Management API, Webhook

**Affected endpoints:**

* [Delete webhook](/cash-app-pay-partner-api/api-reference/management-api/delete-webhook-endpoint)

**Description:** Updated the description of the `Delete webhook` endpoint to add: “**Note:** Events that are created before the webhook endpoint was deleted will still be delivered after the webhook endpoint gets deleted”

***

## Renamed field on the Retrieve Customer endpoint response

Date: Aug-17-2022
<br />Changelog Type: Improved
<br />Metadata Tag: Network API

**Affected endpoints:**

* [Retrieve customer](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer)

**Description:** Renamed the `customer_reference_id` field to `reference_id` on the `Customer` object on the response body of the `Retrieve Customer` endpoint.

***

## URL field of webhook endpoints are now nullable

Date: Aug-17-2022
<br />Changelog Type: Improved
<br />Metadata Tag: Management API, Webhook

**Affected endpoints:**

* [Create webhook](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint)
* [Update webhook](/cash-app-pay-partner-api/api-reference/management-api/update-webhook-endpoint)

**Description:** The `url` field of the `request.webhook_endpoint` object has been changed to be nullable. This allows developers to subscribe to webhook events without needing a destination. The [list webhook events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events) operation can be used to poll for webhook events instead.

***

## Webhooks operations in the Management API

Date: Aug-17-2022
<br />Changelog Type: Added
<br />Metadata Tag: Management API, Webhook

**Affected endpoints:**

* [List webhook endpoints](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-endpoints)
* [Create webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint)
* [Retrieve webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/retrieve-webhook-endpoint)
* [Update webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/update-webhook-endpoint)
* [Delete webhook endpoint](/cash-app-pay-partner-api/api-reference/management-api/delete-webhook-endpoint)
* [List webhook events](/cash-app-pay-partner-api/api-reference/management-api/list-webhook-events)

**Description:** Added webhooks operations in the Management API to allow developers to manage their webhook endpoints and events.

***

## Customer credited amount for Disputes

Date: Aug-11-2022
<br />Changelog Type: Added
<br />Metadata Tag: Network API

**Affected endpoints:**

* [List disputes](/cash-app-pay-partner-api/api-reference/network-api/list-disputes)
* [Retrieve dispute](/cash-app-pay-partner-api/api-reference/network-api/retrieve-dispute)
* [Challenge dispute](/cash-app-pay-partner-api/api-reference/network-api/challenge-dispute)
* [Accept dispute](/cash-app-pay-partner-api/api-reference/network-api/accept-dispute)

**Description:** Added `customer_credited_amount` to the `dispute` object on the response body of the affected endpoints. `customer_credited_amount` shows the amount credited to the Customer after resolving the dispute.

<Note>
   The amount will be in the lowest denomination of the currency used on the associated payment. 
</Note>

***

## SVG QR Codes for Customer Requests

Date: Aug-10-2022
<br />Changelog Type: Added
<br />Metadata Tag: Customer Request API

**Affected endpoints:**

* [Create request](/cash-app-pay-partner-api/api-reference/customer-request-api/create-request)
* [Retrieve request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request)
* [Update request](/cash-app-pay-partner-api/api-reference/customer-request-api/update-request)

**Description:** Added `qr_code_svg_url` to the `request.auth_flow_triggers` object on the response body of the affected endpoints. This field contains a link to the QR code that launches the customer request flow in Cash App when scanned, encoded as an SVG file. Additionally, the `qr_code_image_url` field is now guaranteed to return a URL that links to a PNG file.

***

## Channel for Grants

Date: Jun-30-2022
<br />Changelog Type: Added
<br />Metadata Tag: Customer Request API, Network API

**Affected endpoints:**

* [Retrieve request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request)
* [Retrieve customer grant](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer-grant)
* [Revoke customer grant](/cash-app-pay-partner-api/api-reference/network-api/revoke-customer-grant)

**Description:** Added `channel` to the `request.grants[]` object on the response body of the affected request endpoints; added `channel` to the `grant` object on the response body of the affected grant endpoints. This field contains the value of the channel set on the customer request that was approved to create the grant.
