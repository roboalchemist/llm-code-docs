# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/api-quickstart/deferred-capture.mdx

***

## stoplight-id: osb59mh1b442q

# Auth and capture

Deferred capture lets you authorize the full payment amount up front and collect the funds later. The transaction is approved and the customer's payment plan is started. Then, you can capture full or partial payments. If a portion of the order can’t be fulfilled, you can void uncaptured amounts.

This flow is recommended for merchants who ship orders in multiple parts or who charge the full order amount upon delivery.

| **Action**                                                                             | **Endpoint**                     | **Purpose**                                                             |
| -------------------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------- |
| [Authorize Payment](/cash-app-afterpay/api-reference/reference/payments/auth)          | `/v2/payments/auth`              | Authorize a payment amount for an Afterpay order.                       |
| [Capture Payment](/cash-app-afterpay/api-reference/reference/payments/capture-payment) | `/v2/payments/{orderId}/capture` | Capture full or partial order payments against a payment authorization. |
| [Void](/cash-app-afterpay/api-reference/reference/payments/void-payment)               | `/v2/payments/{orderId}/void`    | Void a full or partial order value and refund the customer.             |

## Implement deferred capture

### Launch checkout and authorize payment

1. [Create a checkout](/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout). If the customer confirms their order with Cash App Afterpay, they're returned to your website with an order token and the `SUCCESS` status.
2. Use the order token to call the [Authorize Payment](/cash-app-afterpay/api-reference/reference/payments/auth) endpoint. Once the authorization completes, you'll receive a Payment object with a status of `APPROVED` or `DECLINED`.
   * If Cash App Afterpay authorizes the payment, store the payment `id` and the `expires` value of the `AUTH_APPROVED` payment event. Present the customer with an order confirmation page.
   * If Cash App Afterpay declines the payment (for example, if the customer’s credit card details are incorrect), present the customer with suggested corrections or alternative payment methods at checkout.

### Capture payment

If an order is given `APPROVED` status during the authorization flow, you can now capture the payment. This happens after the customer has seen their order confirmation page and may have left your website.

<Warning title="Important">
  You must capture payment for authorized orders within 13 days. After 13 days, the authorization expires and is automatically voided. At this point, you aren’t able to capture any order value (partial or full). You can’t reopen or update voided transactions; you must call the Checkouts endpoint to create a new order.
</Warning>

#### If you can completely fulfill the order:

Once you determine that the entire order will be fulfilled, call the [Capture Payment](/cash-app-afterpay/api-reference/reference/payments/capture-payment) endpoint with the entire amount.

The capture amount will match both the `originalAmount` and `openToCaptureAmount` for the Payment object, as it was returned in the Auth response.

#### If you can partially fulfill the order:

Once you determine that only part of the order will be fulfilled (for example, if some items are permanently out of stock):

1. Call the [Capture Payment](/cash-app-afterpay/api-reference/reference/payments/capture-payment) endpoint with the amount for all items that will be fulfilled.
2. Call the [Void](/cash-app-afterpay/api-reference/reference/payments/void-payment) endpoint to finalize the order. Refund the `openToCapture` amount to the customer; this will reduce the `openToCapture` amount to zero.

#### If you fulfill the order incrementally:

1. Once a shipment is dispatched, call the [Capture Payment](/cash-app-afterpay/api-reference/reference/payments/capture-payment) endpoint with the amount of all items in the shipment.
2. If you determine that a shipment can't be dispatched, call the [Void](/cash-app-afterpay/api-reference/reference/payments/void-payment) endpoint with the amount of all applicable items.

You can capture or void payments multiple times. Requests that exceed the `openToCapture` amount will fail. Once the `openToCapture` amount equals zero, any further Capture or Void requests will fail.

#### If you can’t fulfill any part of the order:

Once you determine that you can't fulfill any part of the order, call the [Void](/cash-app-afterpay/api-reference/reference/payments/void-payment) endpoint. This refunds the `openToCapture` amount to the customer, reduces the `openToCapture` amount to zero, and finalizes the order.

<Note>
  We don't recommend waiting for the authorization to automatically expire. Even though an approved authorization will automatically be voided after 13 days, the customer begins their payment plan at the time of authorization approval.
</Note>

<div>
  ```mermaid
  %%{
    init: {
      'theme': 'base',
      'themeVariables': {
        'primaryColor': '#FFF',
        'primaryTextColor': '#000',
        'primaryBorderColor': '#000',
        'lineColor': '#000',
        'secondaryColor': '#fff',
        'tertiaryColor': '#fff',
        'noteBkgColor': '#fff',
        'noteBorderColor': '#000'
      }
    }
  }%%
  sequenceDiagram
      Merchant ->> Cash App Afterpay: Create Order
      Cash App Afterpay -->> Merchant: Token
      Note over Merchant, Cash App Afterpay: Cash App Afterpay checkout flow
      Merchant ->> Cash App Afterpay: Auth
      Cash App Afterpay -->> Merchant: Success
      Note over Merchant, Cash App Afterpay: A period of time passes...
      Merchant ->> Cash App Afterpay: Capture
      Cash App Afterpay -->> Merchant: Success
  ```
</div>

### Considerations

* Deferred capture is supported on the Afterpay v2 API, Salesforce Commerce Cloud, and Adobe Commerce (Magento).
* The minimum capture amount is \$1.00; capture requests below \$1.00 are rejected.
* If an order still has a `paymentState` of `AUTH_APPROVED` or `PARTIALLY_CAPTURED` when the authorization expires, the remaining order amount will automatically be voided.
* The Capture Payment call is idempotent. It’s safe to retry requests using the same unique requestId.
