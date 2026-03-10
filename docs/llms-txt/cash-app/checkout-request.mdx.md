# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/checkouts/schemas/checkout-request.mdx

<EndpointSchemaSnippet endpoint="GET /checkout-request-schema-test" selector="response.body" />

<Aside>
  ```json Example
  {
    "amount": {
      "amount": "100.00",
      "currency": "AUD"
    },
    "consumer": {
      "email": "test@example.com",
      "givenNames": "Joe",
      "surname": "Consumer",
      "phoneNumber": "0400 000 000"
    },
    "merchantReference": "string",
    "billing": {
      "name": "Joe Consumer",
      "line1": "Level 5",
      "line2": "390 Collins Street",
      "area1": "Melbourne",
      "region": "VIC",
      "postcode": "3000",
      "countryCode": "AU",
      "phoneNumber": "0400 000 000"
    },
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
    "merchant": {
      "redirectConfirmUrl": "https://example.com/checkout/confirm",
      "redirectCancelUrl": "https://example.com/checkout/cancel",
      "popupOriginUrl": "https://merchant.com/cart",
      "name": "string"
    },
    "items": [
      {
        "name": "Blue Carabiner",
        "sku": "12341234",
        "quantity": 1,
        "pageUrl": "https://merchant.example.com/carabiner-354193.html",
        "imageUrl": "https://merchant.example.com/carabiner-7378-391453-1.jpg",
        "price": {
          "amount": "40.00",
          "currency": "AUD"
        },
        "categories": [
          [
            "Sporting Goods",
            "Climbing Equipment",
            "Climbing",
            "Climbing Carabiners"
          ],
          [
            "Sale",
            "Climbing"
          ]
        ],
        "estimatedShipmentDate": "2023-08-01"
      }
    ],
    "courier": {
      "shippedAt": "2025-08-24T14:15:22Z",
      "name": "USA Post",
      "tracking": "AA0000000000000",
      "priority": "STANDARD"
    },
    "taxAmount": {
      "amount": "100.00",
      "currency": "AUD"
    },
    "shippingAmount": {
      "amount": "100.00",
      "currency": "AUD"
    },
    "discounts": [
      {
        "displayName": "New Customer Coupon",
        "amount": {}
      }
    ],
    "description": "string",
    "mode": "standard"
  }
  ```
</Aside>
