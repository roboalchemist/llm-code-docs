# Handle funding failures

If your payer's funding source fails, the Orders API returns an `INSTRUMENT_DECLINED` error. A funding source might fail for the following reasons:

- The billing address associated with the payment method is incorrect.
- The transaction exceeds the card limit.
- The card issuer denied the transaction.

To handle this error, restart the payment so the payer can select a different payment option.

## Know before you code

### PayPal Checkout

Complete the steps in [Get started](/api/rest/) to get your sandbox account login information and access token from the Developer Dashboard.

This feature modifies an existing [PayPal Checkout integration](/docs/checkout/standard/) and uses the following:

- [PayPal JavaScript SDK](/sdk/js/configuration/)
- [Orders REST API](/docs/api/orders/v2/) - [Create order](/docs/api/orders/v2/#orders_create) endpoint

### Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

## Restart the payment

Restarting the payment is required if you directly call the Orders API from your server. If you use `actions.order.capture()`, the script automatically restarts the checkout flow and prompts the payer to select a different funding source.

Restart the payment in the `onApprove` function as follows:

```javascript
paypal.Buttons({
  onApprove: function (data, actions) {
    return fetch('/my-server/capture-paypal-transaction', {
      headers: {
        'content-type': 'application/json'
      },
      body: JSON.stringify({
        orderID: data.orderID
      })
    }).then(function(res) {
      return res.json();
    }).then(function(captureData) {
      if (captureData.error === 'INSTRUMENT_DECLINED'); // Your server response structure and key names are what you choose
        return actions.restart();
      }
    });
  }
}).render('#paypal-button-container');
```