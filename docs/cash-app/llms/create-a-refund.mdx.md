# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/api-quickstart/create-a-refund.mdx

***

## stoplight-id: ax158nvltulp8

# Refunds

| **Action**                                                                         | **Endpoint**                    | **Purpose**                                    |
| ---------------------------------------------------------------------------------- | ------------------------------- | ---------------------------------------------- |
| [Create Refund](/cash-app-afterpay/api-reference/reference/payments/create-refund) | `/v2/payments/{orderId}/refund` | Refunds a full or partial amount for an order. |

Perform a full refund or partial refunds (up to the original order total) based on your refund or cancellation policies. The same Order ID can be used for multiple partial refunds.

Refunds can be used for:

* Full or partial order cancellation
* Returns
* Other scenarios where you want to issue funds back to the customer

### Considerations

* Refunds can't be issued after 120 days from the date of purchase. After 120 days, refund requests are rejected and return a 422 error.
* If using deferred capture, only captured funds can be refunded.
* You can also process refunds from the Cash App Afterpay Business Hub.
