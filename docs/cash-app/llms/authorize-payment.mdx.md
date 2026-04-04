# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/schemas/authorize-payment.mdx

<EndpointSchemaSnippet endpoint="GET /authorize-payment-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
    "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
    "merchantReference": "merchant-order-123",
    "amount": {
      "amount": "100.00",
      "currency": "AUD"
    },
    "isCheckoutAdjusted": true,
    "paymentScheduleChecksum": "string",
    "items": [],
    "shipping": {
      "name": "Joe Consumer",
      "line1": "Level 5",
      "line2": "390 Collins Street",
      "area1": "Melbourne",
      "region": "VIC",
      "postcode": "3000",
      "countryCode": "AU",
      "phoneNumber": "0400 000 000"
    },
    "enrichments": {
      "initiation": {
        "actor": "CUSTOMER"
      },
      "subscription": {
        "type": "FIXED",
        "interval": "DAY",
        "intervalCount": 1
      }
    }
  }
  ```
</Aside>
