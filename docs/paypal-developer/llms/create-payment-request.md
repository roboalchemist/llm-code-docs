# Create a Payment Request

**Important:** PayPal Plus for Mexico is not available for new integrations. PayPal provides this documentation to support existing integrations.

For PayPal Plus for Brazil, see the [Brazilian integration](/docs/regional/br/) guide.

After receiving your access token, use it to issue a request to create a payment. Set the following request fields to these values:

| Parameter | Value |
| --- | --- |
| intent | sale |
| payment_method | paypal |
| allowed_payment_method | IMMEDIATE_PAY |

## Example request

```bash
curl -v https://api-m.sandbox.paypal.com/v1/payments/payment \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <Access-Token>' \
  -d '{
  "intent": "sale",
  "payer": {
    "payment_method": "paypal"
  },
  "transactions": [{
    "amount": {
      "currency": "BRL",
      "total": "93.00",
      "details": {
        "shipping": "11",
        "subtotal": "75",
        "shipping_discount": "1.00",
        "insurance": "1.00",
        "handling_fee": "1.00",
        "tax": "6.00"
      }
    },
    "description": "This is the payment transaction description",
    "payment_options": {
      "allowed_payment_method": "IMMEDIATE_PAY"
    },
    "item_list": {
      "shipping_address": {
        "recipient_name": "PP Plus Recipient",
        "line1": "Gregório Rolim de Oliveira, 42",
        "line2": "JD Serrano II",
        "city": "Votorantim",
        "country_code": "BR",
        "postal_code": "18117-134",
        "state": "São Paulo",
        "phone": "0800-761-0880"
      },
      "items": [{
        "name": "handbag",
        "description": "red diamond",
        "quantity": "1",
        "price": "75",
        "currency": "BRL",
        "discount": "6.00"
      }]
    }
  }],
  "redirect_urls": {
    "return_url": "https://example.com/return",
    "cancel_url": "https://example.com/cancel"
  }
}'
```

## Example response

The response returns the `approval_url` link, which is required when you are integrating the payment selection page.

```json
{
  "id": "PAY-3A3234483P2338009KTTFX7Q",
  "create_time": "2015-02-19T21:56:14Z",
  "update_time": "2015-02-19T21:56:14Z",
  "state": "created",
  "intent": "sale",
  "payer": {
    "payment_method": "paypal",
    "payer_info": {
      "shipping_address": {}
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
            "price": "75",
            "currency": "BRL",
            "quantity": "1",
            "description": "red diamond",
            "discount": "6.00"
          }
        ],
        "shipping_address": {
          "recipient_name": "Max Santos",
          "line1": "Gregório Rolim de Oliveira, 42",
          "line2": "JD Serrano II",
          "city": "Votorantim",
          "state": "São Paulo",
          "phone": "0800-761-0880",
          "postal_code": "18117-134",
          "country_code": "BR"
        }
      }
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-3A3234483P2338009KTTFX7Q",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-82237386YH588524U",
      "rel": "approval_url",
      "method": "REDIRECT"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-3A3234483P2338009KTTFX7Q/execute",
      "rel": "execute",
      "method": "POST"
    }
  ]
}
```

## Next

[Integrate a payment selection page](/docs/regional/mx/payment-selection-page/)