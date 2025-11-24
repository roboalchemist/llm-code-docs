# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/tokenized-payments/mixed-payments.md

# Mixed payments

## Learn more about Mixed payments here.

## What is Mixed payments?

Mixed Payments allows customers to make one-time purchases and add an additional service during checkout. Customers can choose any available payment option within Klarna ecosystem for their initial purchase and tokenize another payment option for future transactions.

Common scenarios:

- **Mixed basket**: Includes a one-time product and a monthly subscription.
- **Additional charge**: Includes a one-time product with an additional service charged separately.

### How to enable

The Mixed payments flow is enabled by the customer token, with the `intent` set to `buy_and_default_tokenize` during the payment session. For further instructions on using the customer token with the correct `intent` and how to group multiple line items, refer to the FAQ below.

If you want to learn more about customer tokens, check out this [section](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/subscriptions-and-on-demand/).

### What can I do with a customer token for Mixed payments?

You can use the Klarna payments API to perform three actions related to a customer token:

1.  [Create an order](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/tokenized-payments/subscriptions-and-on-demand/) in a payment session with `intent` set to `buy_and_default_tokenize`.
2.  [Check the details](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/other-actions/check-the-details-of-a-customer-token/) of a customer token.
3.  [Cancel](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/other-actions/cancel-a-customer-token/) a customer token.

In the case of Mixed payments, Klarna will not tokenize the chosen payment option at checkout. Instead, Klarna aims to tokenize a Pay Now option based on the selected payment method (funding source).

**For example:**

If a customer selects Pay-in-4 (backed by a card) for their initial purchase, Pay Now (backed by the same card) will be tokenized for the additional item. Similarly, if a customer chooses Financing (backed by direct debit) for their initial purchase, Klarna will tokenize a Pay Now version of direct debit.

If a payment option is selected that does not have a payment method (funding source) (e.g., Pay Later Invoice or Direct Bank Transfer), Pay Later 30 will be tokenized.

### How do I combine the mixed products in the same basket?

We recommend creating a session with separate line items. This means only passing the one-time line item during the `create_session` call, allowing the customer to first pay for their one-time item within the Klarna flow.

Upon successful authorization, the customer token is created and shared with you for any subsequent charges. These additional charges will contain the second line item and be charged by the same merchant id or another.

Use this approach when:

- The additional line item has legal constraints for the use of credit (e.g., insurances that may only be settled via debit).
- A customer token is \[<https: #customer-token-can-i-share-a-customer-token-with-another-merchant-id="" docs.klarna.com="" integrate-with-klarna-payments="" payments="" subscriptions-and-on-demand="" tokenized-payments="" web-payments="">? shared\] among several merchant ids.

## Sharing subscription details with Klarna

### Example 1: One-time purchase + subscription

1.  [Create session](https://docs.klarna.com/api/payments/#operation/createCreditSession)
    - `intent`: `buy_and_default_tokenize`
    - `order_lines`: line 1 with physical item (one-time purchase)
2.  Authorize: full payload with line 1
3.  [Create customer token](https://docs.klarna.com/api/payments/#operation/purchaseToken)
4.  [Create order](https://docs.klarna.com/api/payments/#operation/createOrder) with line 1
5.  [Create recurring order with customer token](https://docs.klarna.com/api/customertoken/#operation/createOrder)
    - Include [subscription object](https://docs.klarna.com/api/customertoken/#operation/createOrder!path=order_lines/subscription&t=request)`subscription` object
    - Include amount

### Example 2: One-time purchase + subscription (free trial)

1.  [Create session](https://docs.klarna.com/api/payments/#operation/createCreditSession)
    - `intent`: `buy_and_default_tokenize`
    - `order_lines`: line 1 with physical item (one-time purchase)
2.  Authorize: full payload with line 1
3.  [Create customer token](https://docs.klarna.com/api/payments/#operation/purchaseToken)
4.  [Create order](https://docs.klarna.com/api/payments/#operation/createOrder) with line 1
5.  [Create recurring order with customer token](https://docs.klarna.com/api/customertoken/#operation/createOrder) (once the trial period is over)
    - Include [subscription object](https://docs.klarna.com/api/customertoken/#operation/createOrder!path=order_lines/subscription&t=request)
    - Include amount

### Example 3: One-time purchase + additional charge/on-demand

1.  [Create session](https://docs.klarna.com/api/payments/#operation/createCreditSession)
    - `intent`: `buy_and_default_tokenize`
    - `order_lines`: line 1 with physical item (one-time purchase)
2.  Authorize: full payload with line 1
3.  [Create customer token](https://docs.klarna.com/api/payments/#operation/purchaseToken)
4.  [Create order](https://docs.klarna.com/api/payments/#operation/createOrder) with line 1
5.  [Create recurring order with customer token](https://docs.klarna.com/api/customertoken/#operation/createOrder) for the additional charge</https:>