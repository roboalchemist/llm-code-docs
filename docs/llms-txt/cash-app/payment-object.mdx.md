# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/payment-object.mdx

***

## stoplight-id: zsf1uoqrnrv8e

# Payment object

## Attributes

| Attribute           | Type                                                                                         | Description                                                                                                                                                                                                                               |
| ------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                  | string                                                                                       | The unique, permanent, Cash App Afterpay-generated Order ID.                                                                                                                                                                              |
| token               | string                                                                                       | Checkout token that was used to complete payment.                                                                                                                                                                                         |
| status              | string                                                                                       | An order status of "APPROVED" or "DECLINED".                                                                                                                                                                                              |
| created             | string                                                                                       | The UTC timestamp of when the payment was completed, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.                                                                                                        |
| originalAmount      | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object)                 | Total amount charged to the customer for the order.                                                                                                                                                                                       |
| openToCaptureAmount | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object)                 | Remaining amount that can be captured. Will always be zero for immediate payment flow orders.                                                                                                                                             |
| paymentState        | string                                                                                       | Current state for capturing payments. Will be one of: "AUTH\_APPROVED", "AUTH\_DECLINED", "PARTIALLY\_CAPTURED", "CAPTURED", "CAPTURE\_DECLINED","VOIDED".                                                                                |
| merchantReference   | string                                                                                       | The merchant's order id/reference that this payment corresponds to.                                                                                                                                                                       |
| refunds             | [Refund](/cash-app-afterpay/api-reference/reference/data-models/refund-object)               | An array of refunds. Note: in response to a [Capture Full Payment](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment) call, this array will always be empty, since refunds cannot occur until payment is captured. |
| orderDetails        | [Order Details](/cash-app-afterpay/api-reference/reference/data-models/order-details-object) | The details of the order bound to the payment.                                                                                                                                                                                            |
| events              | [Payment Event](/cash-app-afterpay/api-reference/reference/data-models/payment-event-object) | One or more payment events that have occurred against the order.                                                                                                                                                                          |

Link to [Capture Full Payment](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment)

## Example Payment object

```json
{
  "id" : "12345678",
  "token" : "ltqdpjhbqu3veqikk95g7p3fhvcchfvtlsiobah3u4l5nln8gii9",
  "status" : "APPROVED",
  "created" : "2024-01-01T00:00:00.000Z",
  "originalAmount" : {
    "amount" : "100.00",
    "currency" : "USD"
  },
  "openToCaptureAmount" : {
    "amount" : "100.00",
    "currency" : "USD"
  },
  "paymentState" : "AUTH_APPROVED",
  "merchantReference" : "merchantOrderId-1234",
  "refunds" : [
    ...
  ],
  "orderDetails" : {
    ...
  },
  "events" : [ {
    "id" : "1OUR16OTqL3DgJ3ELlwKowU9v6K",
    "created" : "2024-01-01T00:00:00.000Z",
    "expires" : "2024-01-01T00:00:00.000Z",
    "type" : "AUTH_APPROVED",
    "amount" : {
      "amount" : "100.00",
      "currency" : "USD"
    }
  }, ... ]
}
```
