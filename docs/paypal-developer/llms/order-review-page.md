# Populate an Order Review Page

**Important:** PayPal Plus for Mexico is not available for new integrations. PayPal provides this documentation to support existing integrations.

For PayPal Plus for Brazil, see the [Brazilian integration](/docs/regional/br/) guide.

You have the option of including an order review page in your checkout flow so that a buyer can review details of the purchase before executing the payment.

The buyer can not change the order details, but they can edit the shipping address if it is submitted in the execute payment call. You can also add shipping and handling charges.

## Example

This example request shows how to look up a payment to populate an order review page:

### Request

```bash
curl -v -X GET https://api-m.sandbox.paypal.com/v1/payments/payment/<Payment-Id>
  -H 'Content-Type: application/json'
  -H 'Authorization: Bearer <Access-Token>'
```

### Response

```json
{
  "id": "PAY-79281421TB351034WKP2JXZA",
  "create_time": "2014-08-20T13:00:20Z",
  "update_time": "2014-08-20T13:00:20Z",
  "state": "created",
  "intent": "sale",
  "payer": {
    "payment_method": "paypal",
    "status": "UNVERIFIED",
    "payer_info": {
      "email": "privatkunde@paypal.de",
      "first_name": "Max",
      "last_name": "Santos",
      "payer_id": "QTTRJRG478D9W",
      "shipping_address": {
        "line1": "Greg?rio Rolim de Oliveira, 42",
        "city": "Votorantim",
        "postal_code": "18117-134",
        "country_code": "BR",
        "recipient_name": "Max Santos"
      }
    }
  },
  "transactions": [
    {
      "amount": {
        "total": 25.0,
        "currency": "BRL",
        "details": {
          "subtotal": 25.0
        }
      },
      "item_list": {
        "items": [
          {
            "name": "Rugby Ball, Size 5",
            "price": 25,
            "currency": "BRL",
            "quantity": 1
          }
        ],
        "shipping_address": {
          "recipient_name": "Max Santos",
          "line1": "Greg?rio Rolim de Oliveira, 42",
          "city": "Votorantim",
          "postal_code": "18117-134",
          "country_code": "BR"
        }
      }
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-79281421TB351034WKP2JXZA",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments//cgi-bin/webscr?cmd=_express-checkout&token=EC-2BA876161J833444B",
      "rel": "approval_url",
      "method": "REDIRECT"
    },
    {
      "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-79281421TB351034WKP2JXZA/execute",
      "rel": "execute",
      "method": "POST"
    }
  ]
}