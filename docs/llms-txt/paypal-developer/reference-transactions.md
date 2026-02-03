# Initiate future transactions

Website Payments Pro merchants can initiate future transactions using a transaction ID.

Use your payer's original transaction ID to charge them later with reference transactions. A reference transaction is a transaction that you initiate through an established contract with the payer and from which you can derive subsequent payments.

You need a reference transaction to start a future transaction using the same payment method. Get the following information:

- A previous order ID.
- The payment amount.
- The payer’s original transaction ID.

Process- The payer generates a transaction ID when they purchase an item on your site.
- The payer agrees to a reference transaction.
- Use the transaction ID in future reference transactions using the same payment method.

Use cases

- Save payer's card details for a future payer-initiated transaction.
- Initiate transactions to charge the payment method based on a previously-agreed contract.

## Know before you code

To complete this server-side integration, you will need:

- An [Expanded Checkout integration](https://developer.paypal.com/docs/checkout/advanced/).
- The [Orders v2 REST API](https://developer.paypal.com/docs/api/orders/v2/) : Create, update, retrieve, authorize, and capture orders.

Use Postman to explore and test PayPal APIs.

NVP and SOAP integrations

You can get reference transactions from an existing NVP or SOAP integration of the `DoReferenceTransaction` API.

Provide an order ID from a previous transaction or create a new one.

API endpoint used: [Create order](https://developer.paypal.com/docs/api/orders/v2/#orders_create)

#### `cURL`

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H "Content-Type: application/json" \
-H "Authorization: Bearer Access-Token" \
-d '{
  "intent": "CAPTURE",
  "purchase_units": [
    {
      "amount": {
        "currency_code": "USD",
        "value": "100.00"
      }
    }
  ]
}'
```

Modify the code

After you copy the code in the sample request, modify the following:

- Access-Token : Your [access token](https://developer.paypal.com/api/rest/authentication/).
- The intent in this sample is CAPTURE, which captures the payment immediately. You can choose to separate the authorize and capture actions by changing the intent to AUTHORIZE.
- Order ID - In the URI for the API call, replace the sample ID with your order ID. In the example, the order ID is 5O190127TN364715T.
- Payment source - Replace the payment_source sample ID with your transaction ID. In the example, the transaction ID is 67N9717781765035V.

Step result

A successful request results in the following:

- A return status code of HTTP 201 Created.
- A JSON response body that contains an order ID, for example, 5O190127TN364715T: