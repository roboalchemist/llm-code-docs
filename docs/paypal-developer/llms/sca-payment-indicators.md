# SCA payment indicators

If you process payments that require [Strong Customer Authentication](https://www.paypal.com/uk/webapps/mpp/psd2) (SCA), you need to provide additional context about the transaction with [payment indicators](/docs/multiparty/checkout/advanced/customize/sca-payment-indicators/). The payment indicators ensure that buyer authentication, card on file, and other factors are appropriately handled. Pass these payment indicators to avoid rejected transactions.

To provide additional transaction context, include `stored_payment_source` in your create order request.

## Know before you code

### Required integration:

- Expanded Checkout integration

### Sample request

API endpoint used: [Create order](/docs/api/orders/v2/#orders_create)

1. curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders 
2. -H "Content-Type: application/json"
3. -H "Authorization: Bearer <Access-Token>"
4. -H "PayPal-Partner-Attribution-Id: <BN-Code>"
5. -d '{ "intent": "CAPTURE", "purchase_units": [{" "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b", "amount": {" "currency_code": "USD", "value": "100.00" }, "payment_source": {" "card": {" "number": "4111111111111111", "expiry": "2020-02", "name": "John Doe", "billing_address": {" "address_line_1": "2211 N First Street", "address_line_2": "17.3.160", "admin_area_1": "CA", "admin_area_2": "San Jose", "postal_code": "95131", "country_code": "US" }, "stored_credential": {" "payment_initiator": "MERCHANT", "payment_type": "RECURRING", "usage": "SUBSEQUENT", "previous_transaction_reference": "53963906K75832009" } } } ] } }'

### Modify the code

Copy the code snippet and modify the values for `stored_payment_source` as follows:

`payment_initiator`

`Required`

## Add request parameter

Update the `POST v2/checkout/orders` request body to include `stored_payment_source`.

### Sample request

API endpoint used: [Create order](/docs/api/orders/v2/#orders_create)

1. curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders 
2. -H "Content-Type: application/json"
3. -H "Authorization: Bearer <Access-Token>"
4. -H "PayPal-Partner-Attribution-Id: <BN-Code>"
5. -d '{ "intent": "CAPTURE", "purchase_units": [{" "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b", "amount": {" "currency_code": "USD", "value": "100.00" }, "payment_source": {" "card": {" "number": "4111111111111111", "expiry": "2020-02", "name": "John Doe", "billing_address": {" "address_line_1": "2211 N First Street", "address_line_2": "17.3.160", "admin_area_1": "CA", "admin_area_2": "San Jose", "postal_code": "95131", "country_code": "US" }, "stored_credential": {" "payment_initiator": "MERCHANT", "payment_type": "RECURRING", "usage": "SUBSEQUENT", "previous_transaction_reference": "53963906K75832009" } } } ] } }'

### Modify the code

Copy the code snippet and modify the values for `stored_payment_source` as follows:

`payment_initiator`

`Required`

## Step result

A successful request results in the following:

- A return status code of HTTP 201 Created .
- A JSON response body that contains the processor response.

## Use cases

You can use these common scenarios to determine how you'll update your integration.

### One time transaction

| Scenario | Payment initiator | Payment type | Usage |
| --- | --- | --- | --- |
| Single payment. Payer doesn't intend to make another purchase or save their card. | CUSTOMER | ONE_TIME | DERIVED |
| Single payment. Payer saves their card details for a future single payment. | CUSTOMER | ONE_TIME | FIRST |
| Single payment. Payer uses a previously-saved card to complete the transaction. | CUSTOMER | ONE_TIME | SUBSEQUENT |

### Recurring plan or subscription

| Scenario | Payment initiator | Payment type | Usage |
| --- | --- | --- | --- |
| Initial transaction to sign up for the recurring charges. Payer hasn't saved their card. | CUSTOMER | RECURRING | FIRST |
| Initial transaction to sign up for the recurring charges. Payer has already saved their card. | CUSTOMER | RECURRING | SUBSEQUENT |
| Subsequent payments as part of a recurring plan. | MERCHANT | RECURRING | SUBSEQUENT |
| Initial customer-initiated transaction wasn't processed with PayPal. Merchant processes recurring charge with PayPal. | MERCHANT | RECURRING | SUBSEQUENT |

### Unscheduled payment

| Scenario | Payment initiator | Payment type | Usage |
| --- | --- | --- | --- |
| Initial transaction to sign up for an unscheduled payment. Payer has not saved their card. | CUSTOMER | UNSCHEDULED | FIRST |
| Initial transaction to sign up for an unscheduled payment. Payer has already saved their card. | CUSTOMER | UNSCHEDULED | SUBSEQUENT |
| Subsequent payments as part of the unscheduled contract. | MERCHANT | UNSCHEDULED | SUBSEQUENT |
| Initial payer-initiated transaction wasn't processed with PayPal. Merchant processes unscheduled charge with PayPal. | MERCHANT | UNSCHEDULED | SUBSEQUENT |

## Next steps

[.css-32eus9-badge_base-text_caption-neutral{color:#001435;font-family:PayPalOpen-Regular,\"Helvetica Neue\",Arial,sans-serif;font-size:0.875rem;line-height:1.25rem;font-weight:400;max-width:18rem;overflow:hidden;word-break:break-word;text-transform:none;-webkit-line-clamp:2;display:-webkit-inline-box;-webkit-box-orient:vertical;height:auto;padding:0.125rem 0.5rem;border-radius:0.5rem;color:#001435;background-color:#e6e0d9;}@media screen and (max-width: 752px){.css-32eus9-badge_base-text_caption-neutral{font-size:min(0.875rem, 28px);line-height:min(1.25rem, 40px);}}[dir='rtl'] .css-32eus9-badge_base-text_caption-neutral{text-align:right;}Optional](/tools/sandbox/)[Test in PayPal Sandbox](/tools/sandbox/)A self-contained, virtual testing environment.

[.css-32eus9-badge_base-text_caption-neutral{color:#001435;font-family:PayPalOpen-Regular,\"Helvetica Neue\",Arial,sans-serif;font-size:0.875rem;line-height:1.25rem;font-weight:400;max-width:18rem;overflow:hidden;word-break:break-word;text-transform:none;-webkit-line-clamp:2;display:-webkit-inline-box;-webkit-box-orient:vertical;height:auto;padding:0.125rem 0.5rem;border-radius:0.5rem;color:#001435;background-color:#e6e0d9;}@media screen and (max-width: 752px){.css-32eus9-badge_base-text_caption-neutral{font-size:min(0.875rem, 28px);line-height:min(1.25rem, 40px);}}[dir='rtl'] .css-32eus9-badge_base-text_caption-neutral{text-align:right;}Optional](/api/rest/production/)[Go Live](/api/rest/production/)Move from PayPal's production environment to go live.