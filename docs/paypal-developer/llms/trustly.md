# Accept Trustly payments

With Trustly, buyers can initiate payments directly from their bank accounts. During the online checkout process, customers select their bank, log into their online account, choose their payment method, and verify their purchase.

Trustly integrates with banks to collect funds locally across Europe and offers real-time reconciliation through proprietary integrations. Trustly natively supports payments on merchant checkout and is optimized for most devices. Merchants receive credit notifications after payments are completed. Payment completion happens within 7 days of payment authorization, depending on the bank used for the payment.

| Countries | Payment type | Payment flow | Currencies | Minimum amount | Refunds |
| --- | --- | --- | --- | --- | --- |
| Austria (AT) Germany (DE) Denmark (DK) Estonia (EE) Spain (ES) Finland (FI) Great Britain (GB) Lithuania (LT) Latvia (LV) Netherlands (NL) Norway (NO) Sweden (SE) | bank redirect | redirect | EUR,DKK,SEK,GBP,NOK | 0.01EUR(or equivalent) | Up to 365 days |

## How it works

![Alternative,payment,methods,diagram](https://www.paypalobjects.com/ppdevdocs/img/docs/apm/unbranded-flow.svg)

1. Your checkout page offers alternative payment methods.
2. The buyer provides their personal details and selects an alternative payment method from your checkout page.
3. The buyer is transferred from your checkout page to the third-party bank to confirm the purchase.
4. The merchant receives the successful payment initiation webhook notification and the payment is in a pending state.
5. The buyer authorizes and confirms payment.
6. The buyer returns to your site.
7. The merchant receives the successful payment completion webhook notification and PayPal moves the funds to the merchant account.
8. The merchant ships the goods.

## Eligibility

- Available to merchants globally, except in Russia, Brazil, Belgium, Czechia, Poland, Slovakia, and Slovenia.
- Billing agreements, multiple seller payments, and shipping callback aren't supported.
- Only supports order capture. Doesn't support order authorization. See [Payments webhooks](https://developer.paypal.com/api/rest/webhooks/event-names/#link-payments).
- Chargebacks aren't supported.
- Payment must be an online purchase. Doesn't support in-store payments.

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI components called payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API to fully customize the checkout experience.