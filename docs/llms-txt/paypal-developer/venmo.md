# Save Venmo with the JavaScript SDK

After customers save their Venmo account, they can select it for faster checkout. Customers won't have to enter payment details for future transactions.

## Availability
Venmo is available in the US only.

## Know before you code
This integration requires a PayPal Developer account.

**info**
**Note** : The API URLs shown in the following examples point to a live environment. Venmo is not fully supported in the sandbox environment. For more information, refer to the [Venmo testing guidelines](/docs/checkout/pay-with-venmo/integrate/#link-testandgolive).

## How it works
PayPal encrypts payment method information and stores it in a digital vault for that customer.

- The payer saves their payment method.
- For a first-time payer, PayPal creates a customer ID. Store this within your system for future use.
- When the customer returns to your website and is ready to check out, pass their PayPal-generated customer ID to the JavaScript SDK. The customer ID tells the JavaScript SDK to save or reuse a saved payment method.
- The payer completes a billing agreement.
- The JavaScript SDK populates the checkout page with each saved payment method. Each payment method appears as a one-click button next to other ways to pay.

The checkout process is now shorter because it uses saved payment information.

### First-time payer experience
![User,flow,to,save,Venmo](https://www.paypalobjects.com/devdoc/venmo_vault_flow.png)

- The payer chooses Venmo as a payment method.
- The payer is directed to the Venmo app and agrees to save their Venmo.
- The payer returns to the merchant app or site and completes their purchase.

### Return payer experience
The following is an example of what a payer sees after they save their Venmo account on your site. Returning payers can select their saved payment method at checkout to pay faster.

![Phone,screen.,Venmo,button,is,highlighted,at,checkout.](https://www.paypalobjects.com/devdoc/save_venmo_sdk.png)

## Save payment method
- On your checkout page, click the Venmo button.
- Log in to the payer account and approve the payment. Refer to the [Venmo testing guidelines](/docs/checkout/pay-with-venmo/integrate/#link-testandgolive) for more details.
- Capture the transaction.
- Store the PayPal-generated customer ID in your system.
- Log in to [your live environment](https://www.paypal.com/) with your merchant account and verify the transaction.
- Refresh the page that contains the Venmo button. Ensure the JavaScript SDK is initialized with the PayPal-generated customer ID.
- Ensure the Venmo button displays the payer's Venmo ID and user handle (@firstnamelastname).
- Ensure that the payment method you just saved is visible with the other buttons.
- Select the Venmo button again to test the return payer flow.

## Next steps
- [Test and go live](/api/rest/production/) with this integration. Note that Venmo is not available in the sandbox environment.
- You can [create orders](/docs/api/orders/v2/#orders_create) without the payment_source.venmo.attributes.vault for subsequent or recurring transactions.
- You can [get a payment token](/docs/api/payment-tokens/v3/#payment-tokens_get) , [list all payment tokens](/docs/api/payment-tokens/v3/#payment-tokens_payment-tokens) , [delete a payment token](/docs/api/payment-tokens/v3/#payment-tokens_delete) , and more with the Payment Method Tokens API.

## Test your integration
Run the following tests in your live environment to ensure you can save Venmo as a payment method:

### Save payment method
- On your checkout page, click the Venmo button.
- Log in to the payer account and approve the payment. Refer to the [Venmo testing guidelines](/docs/checkout/pay-with-venmo/integrate/#link-testandgolive) for more details.
- Capture the transaction.
- Store the PayPal-generated customer ID in your system.
- Log in to [your live environment](https://www.paypal.com/) with your merchant account and verify the transaction.
- Refresh the page that contains the Venmo button. Ensure the JavaScript SDK is initialized with the PayPal-generated customer ID.
- Ensure the Venmo button displays the payer's Venmo ID and user handle (@firstnamelastname).
- Ensure that the payment method you just saved is visible with the other buttons.
- Select the Venmo button again to test the return payer flow.

## Save approved payment source
- If the payment has been authorized or captured, the payer does not need to be present to save a payment_source . To keep checkout times as short as possible, the Orders API responds as soon as payment is captured.
- If the attributes.vault.status returned after payment is APPROVED , you won't have a vault.id yet. An example of the attributes object from this scenario is in the following sample:

```javascript
{
  "attributes": {
    "vault": {
      "status": "APPROVED",
      "links": [
        {
          "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
          "rel": "up",
          "method": "GET"
        }
      ]
    }
  }
}
```

The Payment Method Tokens API still saves the payment source even after the Orders API returns its response and sends a webhook after the payment source is saved.

In order to retrieve a vault_id when an APPROVED status is returned, you'll need to subscribe to the VAULT.PAYMENT-TOKEN.CREATED [webhook](/api/rest/webhooks/). The Payment Method Tokens API sends a webhook after the payment source is saved. An example of the VAULT.PAYMENT-TOKEN.CREATED webhook payload is shown in the following sample:

```javascript
{
  "id": "WH-54U753518P812093G-3GD69489S94654234",
  "event_version": "1.0",
  "create_time": "2022-10-13T23:04:17.378Z",
  "resource_type": "payment_token",
  "resource_version": "3.0",
  "event_type": "VAULT.PAYMENT-TOKEN.CREATED",
  "summary": "A payment token has been created.",
  "resource": {
    "create_time": "2018-12-11T21:21:49.000Z",
    "update_time": "2018-12-11T21:21:49.000Z",
    "id": "ckfmsf",
    "customer": {
      "id": "4029352050"
    },
    "payment_source": {
      "venmo": {
        "description": "Description for Venmo to be shown to Venmo payer",
        "shipping": {
          "name": {
            "full_name": "Firstname Lastname"
          },
          "address": {
            "address_line_1": "2211 N First Street",
            "address_line_2": "Floor 6",
            "admin_area_2": "San Francisco",
            "admin_area_1": "CA",
            "postal_code": "94107",
            "country_code": "US"
          }
        },
        "usage_pattern": "IMMEDIATE",
        "usage_type": "MERCHANT",
        "customer_type": "CONSUMER",
        "email_address": "firstname.lastname@example.com",
        "payer_id": "VYYFH3WJ4JPJQ",
        "user_name": "firstnamelastname"
      }
    },
    "links": [
      {
        "rel": "self",
        "href": "https://api-m.paypal.com/v3/vault/payment-tokens/ckfmsf",
        "method": "GET"
      },
      {
        "rel": "delete",
        "href": "https://api-m.paypal.com/v3/vault/payment-tokens/ckfmsf",
        "method": "DELETE"
      },
      {
        "rel": "up",
        "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
        "method": "GET"
      }
    ]
  },
  "links": [
    {
      "rel": "self",
      "href": "https://api-m.paypal.com/v1/notifications/webhooks-events/WH-54U753518P812093G-3GD69489S94654234",
      "method": "GET"
    },
    {
      "rel": "resend",
      "href": "https://api-m.paypal.com/v1/notifications/webhooks-events/WH-54U753518P812093G-3GD69489S94654234/resend",
      "method": "POST"
    }
  ]
}
```