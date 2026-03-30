# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/api-quickstart/immediate-capture.mdx

***

## stoplight-id: xpxzn52bs0o84

# Immediate capture

Immediate capture provides a simplified and efficient payment process. It’s ideal for merchants who want to finalize and settle payments immediately upon order confirmation, or who want to minimize complexity. It combines the following actions into a single API call:

* Completing payment approval.
* Starting the customer’s payment plan.
* Settling the full order value into the merchant's bank account.

| **Action**                                                                                       | **Endpoint**           | **Purpose**                                  |
| ------------------------------------------------------------------------------------------------ | ---------------------- | -------------------------------------------- |
| [Capture Full Payment](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment) | `/v2/payments/capture` | Capture order payment and confirm the order. |

## Implement immediate capture

1. [Create a checkout](/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout). If the customer confirms their order with Cash App Afterpay, they're returned to your website with an order token and the `SUCCESS` status.
2. Use the order token to call the [Capture Full Payment](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment) endpoint. Once the capture completes, you'll receive a Payment object with a status of `APPROVED` or `DECLINED`.
   * If Cash App Afterpay approves the payment, present the customer with an order confirmation page. The full payment is captured.
   * If Cash App Afterpay declines the payment (for example, if the customer’s credit card details are incorrect), present the customer with suggested corrections or alternative payment methods at checkout.

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
      Merchant ->> Cash App Afterpay: Capture
      Cash App Afterpay -->> Merchant: Success
  ```
</div>

### Considerations

* Immediate capture is supported by all platforms.
* You must call the Capture Full Payment endpoint within 180 minutes of receiving the token from the Create Checkout call.
* The Capture Full Payment call is idempotent. It’s safe to retry requests within 24 hours using the same unique requestId.
* Express checkout requires additional data. See [Express Checkout Integration](/cash-app-afterpay/guides/api-development/additional-features/express-checkout) to learn more.
