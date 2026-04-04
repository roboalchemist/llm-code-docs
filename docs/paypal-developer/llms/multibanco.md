# Accept Multibanco payments

Multibanco is an interbank network in Portugal.

| Country | Payment type | Payment flow | Currency | Maximum amount | Refunds |
| --- | --- | --- | --- | --- | --- |
| Portugal (PT) | voucher | redirect | EUR | 99,999.99 | N/A |

## How it works

![Alternative,payment,methods,diagram](https://www.paypalobjects.com/ppdevdocs/img/docs/apm/unbranded-flow-non-instant.svg)

1. The buyer chooses to pay with Multibanco.
2. The buyer provides their first name and last name.
3. The payment instruction is presented to the buyer.
4. The buyer completes the payment via online banking or at a Multibanco ATM.
5. The merchant receives the successful payment completion webhook notification and PayPal moves the funds to the merchant account.
6. The merchant ships the goods.

## Integration methods

### JavaScript SDK

Use PayPal-hosted UI components called payment fields to collect payment information for alternative payment methods.

### Orders REST API

Integrate directly using the Orders API to fully customize the checkout experience.