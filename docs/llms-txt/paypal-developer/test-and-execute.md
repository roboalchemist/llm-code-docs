# Test Your Integration and Execute the Payment

**Important:** PayPal Plus for Mexico is not available for new integrations. PayPal provides this documentation to support existing integrations.

For PayPal Plus for Brazil, see the [Brazilian integration](/docs/regional/br/) guide.

To complete the payment flow, you should issue a request to execute the payment. Payment execution can be initiated from the final order review page or in the background upon return from the hosted pages (when there is no order review page).

When you execute the payment, submit any updates to the shipping address and the shipping and handling charges with the request. Do not change item list.

The payer_id needed to execute the payment is provided in the response from the `doContinue` function together with the `rememberedCards`.

## Example

The following sample shows how to issue a request to execute payment in the sandbox environment.

### Request

```bash
curl -v https://api-m.sandbox.paypal.com/v1/payments/payment/<Payment-Id>/execute/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <Access-Token>" \
  -d '{
  "payer_id": "SUYCECXSW5XMA"
}'
```

### Response

```json
{
  "id": "PAY-7V4081612V751425TKS7OPEQ",
  "create_time": "2015-01-20T23:41:06Z",
  "update_time": "2015-01-20T23:43:58Z",
  "state": "approved",
  "intent": "sale",
  "payer": {
    "payment_method": "paypal",
    "payer_info": {
      "email": "test123456781111@paypal.com",
      "first_name": "Max",
      "last_name": "Santos",
      "payer_id": "SUYCECXSW5XMA",
      "shipping_address": {
        "line1": "Gregório Rolim de Oliveira, 42",
        "line2": "JD Serrano II",
        "city": "Votorantim",
        "state": "São Paulo",
        "postal_code": "18117-134",
        "country_code": "BR",
        "recipient_name": "Max Santos"
      }
    }
  },
  "transactions": [
    {
      "amount": {
        "total": "95.00",
        "currency": "BRL",
        "details": {
          "subtotal": "75.00",
          "tax": "6.00",
          "shipping": "11.00",
          "handling_fee": "1.00",
          "insurance": "1.00",
          "shipping_discount": "1.00"
        }
      },
      "description": "This is the payment transaction description",
      "item_list": {
        "items": [
          {
            "name": "handbag",
            "sku": "product34",
            "price": "75.00",
            "currency": "BRL",
            "quantity": "1",
            "description": "red diamond",
            "tax": "6.00"
          }
        ],
        "shipping_address": {
          "recipient_name": "Max Santos",
          "line1": "Gregório Rolim de Oliveira, 42",
          "line2": "JD Serrano II",
          "city": "Votorantim",
          "state": "São Paulo",
          "postal_code": "18117-134",
          "country_code": "BR"
        }
      },
      "related_resources": [
        {
          "sale": {
            "id": "2KV752851V792590K",
            "create_time": "2015-01-20T23:41:07Z",
            "update_time": "2015-01-20T23:43:58Z",
            "amount": {
              "total": "95.00",
              "currency": "BRL"
            },
            "payment_mode": "INSTANT_TRANSFER",
            "state": "completed",
            "protection_eligibility": "ELIGIBLE",
            "protection_eligibility_type": "ITEM_NOT_RECEIVED_ELIGIBLE,UNAUTHORIZED_PAYMENT_ELIGIBLE",
            "parent_payment": "PAY-7V4081612V751425TKS7OPEQ",
            "links": [
              {
                "href": "https://api-m.sandbox.paypal.com/v1/payments/sale/2KV752851V792590K",
                "rel": "self",
                "method": "GET"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v1/payments/sale/2KV752851V792590K/refund",
                "rel": "refund",
                "method": "POST"
              },
              {
                "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-7V4081612V751425TKS7OPEQ",
                "rel": "parent_payment",
                "method": "GET"
              }
            ]
          }
        }
      ]
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-7V4081612V751425TKS7OPEQ",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```