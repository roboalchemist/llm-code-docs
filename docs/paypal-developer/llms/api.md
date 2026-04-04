# Enable 3D Secure with Orders API for Payments

Enable 3D Secure for advanced credit and debit cards. This integration uses Orders API.

**Info:** PayPal handles 3D Secure authentication for standard payment integrations. No changes are required for standard integrations.

## Know before you code

### If you are based in Europe, you may be subject to PSD2:

- Include 3D Secure as part of your integration.
- Pass the cardholder's billing address as part of the transaction processing.

### Explore PayPal APIs with Postman
You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

## Include a contingency for 3D Secure

Use the following code to request either `SCA_ALWAYS` or `SCA_WHEN_REQUIRED` as a verification attribute for the card object.

- `SCA_ALWAYS` triggers 3D Secure for every transaction, regardless of SCA requirements.
- `SCA_WHEN_REQUIRED` returns a 3D Secure contingency when it is a mandate in the region where you operate. This is the default when neither parameter is explicitly passed.

### `Include a contingency for 3D Secure`

```javascript
"request": {
  "method": "POST",
  "path": "v2/checkout/orders/5O190127TN364715T/authorize",
  "headers": {
    "PayPal-Request-Id": "7b92603e-77ed-4896-8e78-5dea2050476a",
    "Authorization: Bearer <Access-Token>"
  },
  "body": {
    "payment_source": {
      "card": {
        "number": "4111111111111111",
        "expiry": "2010-02",
        "name": "John Doe",
        "billing_address": {
          "address_line_1": "2211 N First Street",
          "address_line_2": "17.3.160",
          "admin_area_1": "CA",
          "admin_area_2": "San Jose",
          "postal_code": "95131",
          "country_code": "US"
        },
        "attributes": {
          "verification": {
            "method": "SCA_WHEN_REQUIRED"
          }
        }
      }
    }
  }
}
```

## Launch authentication flow with HATEOAS link

The merchant needs to redirect the payer back to PayPal to complete 3D Secure authentication.

To trigger the authentication:

- Redirect the buyer to the `"rel": "payer-action"` HATEOAS link returned as part of the response before authorizing or capturing the order.
- Append `"redirect_uri"` to the `payer-action` URL so that PayPal returns the payer to the merchant's checkout page after they complete 3D Secure authentication.

### `Sample URL`

https://example.com/webapp/myshop?action=verify&flow=3ds&cart_id=ORDER-ID&redirect_uri=MERCHANT-LANDING-PAGE

- The issuing bank verifies authentication.
- Device data is collected, and JavaScript is posted directly to the issuing bank.

## Buyer completes authentication

### Single-step API request

After the 3D Secure contingency is thrown during the [create order](/api/orders/v2/#orders_create) response, and contingency is resolved by the buyer, the merchant or partner must invoke the [authorize order](/docs/api/orders/v2/#orders_authorize) and [capture order](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) endpoints with an empty payload to complete the transaction.

### Multi-step API request

After the 3D Secure contingency is thrown during the [authorize order](/docs/api/orders/v2/#orders_authorize) and [capture order](/docs/api/orders/v2/#orders_capture) response and contingency is resolved by the buyer, the merchant or partner must invoke the authorize order and capture order endpoints again with an empty payload to complete the transaction.

## Proceed with the transaction

### Single-step API request

After the 3D Secure contingency is thrown during the [create order](/api/orders/v2/#orders_create) response, and contingency is resolved by the buyer, the merchant or partner must invoke the [authorize order](/docs/api/orders/v2/#orders_authorize) and [capture order](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) endpoints with an empty payload to complete the transaction.

### Multi-step API request

After the 3D Secure contingency is thrown during the [authorize order](/docs/api/orders/v2/#orders_authorize) and [capture order](/docs/api/orders/v2/#orders_capture) response and contingency is resolved by the buyer, the merchant or partner must invoke the authorize order and capture order endpoints again with an empty payload to complete the transaction.

## See also

- [Response parameters](/docs/checkout/advanced/customize/3d-secure/response-parameters/)
  - Learn more about handling 3D Secure responses.
- [Test scenarios](/docs/checkout/advanced/customize/3d-secure/test/)
  - Simulate 3D Secure scenarios and responses.