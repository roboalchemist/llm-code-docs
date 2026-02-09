# Update the Payment Selection Page

**Important:** PayPal Plus for Mexico is not available for new integrations. PayPal provides this documentation to support existing integrations.

For PayPal Plus for Brazil, see the [Brazilian integration](/docs/regional/br/) guide.

When a payment selection causes changes to the displayed fields in your payment flow, you might `PATCH` the payment and reload the payment selection page.

This example demonstrates how to issue a patch request.

```bash
curl -v -X PATCH https://api-m.sandbox.paypal.com/v1/payments/payment/<Payment-Id>
  -H 'Content-Type: application/json'
  -H 'Authorization: Bearer <Access-Token>'
  -d '{
  {
    "op": "replace",
    "path": "/transactions/0/amount",
    "value": {
      "total": "25.00",
      "currency": " BRL ",
      "details": {
        "subtotal": "20.00",
        "shipping": "5.00"
      }
    }
  }, {
    "op": "add",
    "path": "/transactions/0/item_list/shipping_address",
    "value": {
      "recipient_name": "Max Santos",
      "line1": "Greg?rio Rolim de Oliveira, 42",
      "city": "Votorantim",
      "postal_code": "18117-134",
      "country_code": "BR"
    }
  }
}'
```

If the call succeeds, the response returns the HTTP `204 No Content` status code.

## Next

- Optional: [Populate an order review page](/docs/regional/mx/order-review-page/)
- Required: [Test your integration and execute the payment](/docs/regional/mx/test-and-execute/)