# Accept BLIK payments

## Table of Contents

* [How it works](#how-it-works)
* [Eligibility](#eligibility)
* [Integration methods](#integration-methods)

## How it works

![Alternative,payment,methods,diagram](https://www.paypalobjects.com/ppdevdocs/img/docs/apm/unbranded-flow.svg)

1. Your checkout page offers alternative payment methods.
2. The buyer enters their personal details and selects an alternative payment method from your checkout page.
3. The buyer is redirected to their selected issuing bank to confirm the purchase.
4. The buyer authorizes and completes the payment.
5. The buyer returns to your website to see the confirmation of the purchase.
6. The merchant completes the payment process. PayPal transfers the funds to the merchant, and the transaction shows up in your PayPal account with the buyer's chosen payment method.

## Eligibility

- Available to merchants globally (excluding Russia, Japan, and Brazil).
- Billing agreements, multiple seller payments, and shipping callbacks are not supported.
- Only supports order capture (order authorization is not supported). See [authorised and captured payments](https://developer.paypal.com/api/nvp-soap/paypal-payments-standard/integration-guide/authcapture/) for details.
- Chargebacks are not supported.
- Transactions must be online purchases (buy online, pay in-store is not supported).

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI components called payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API to fully customize the checkout experience.