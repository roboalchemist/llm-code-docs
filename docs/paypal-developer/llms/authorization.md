# Authorize a payment and capture funds later

The PayPal Checkout integration supports a 2-step authorize and capture payment model.

Authorize a buyer's funds before you capture them, then settle the purchase later. An authorization places a hold on the funds and is valid for 29 days. For example, use authorize and capture to complete a task before finalizing the payment, such as verifying that you have the item in stock.

## How it works

- The payer checks out and provides a payment method.
- You authorize the payment.
- A hold is placed on the payment method until you are ready to capture payment.
- You finalize the transaction and capture the payment.
- The payer's payment method is charged.

## Know before you code

### You need a developer account to get sandbox credentials

PayPal uses the following REST API credentials, which you can get from the developer dashboard:

- Client ID : Authenticates your account with PayPal and identifies an app in your sandbox.
- Client secret : Authorizes an app in your sandbox. Keep this secret safe and don't share it.

### PayPal Checkout

This feature modifies an existing PayPal Checkout integration and uses the following:

- [JavaScript SDK:](/sdk/js/) Adds PayPal-supported payment methods.
- [Orders REST API:](/docs/api/orders/v2/) Create, update, retrieve, authorize, and capture orders.
- [Payments REST API:](/docs/api/payments/v2/) Authorize, capture, retrieve, and refund payments.

### Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

The default approval intent of the JavaScript SDK is to both authorize the transaction and capture payment immediately. To split authorize and capture into separate actions, add `intent=authorize` to the JavaScript SDK script tag, as shown in the following example:

#### **`Change intent sample code`**

```javascript
<script
  src="https://www.paypal.com/sdk/js?client-id=CLIENT_ID&amp;intent=authorize"
```

The onApprove function in the default integration captures the payment immediately. Replace the existing onApprove function with the following code. This code authorizes the payment but doesn't capture it.

#### **`onApprove code sample`**

```javascript
onApprove: function(data) {
  // Authorize the transaction
  return fetch('/my-server/authorize-paypal-order', {
    method: 'post',
    body: JSON.stringify({
      orderID: data.orderID
    })
  })
  .then(response =>
    response.json()
  )
  .then((authorizePayload) =>
    // Get the authorization id from your payload
    const authorizationID = authorizePayload.authorizationID;
    // Optional message given to purchaser
    alert(`You have authorized this transaction.
        Order ID: ${data.orderID}
        Authorization ID: ${authorizationID}`)
    // Later you can use your server to validate and capture the transaction
  });
}
```

### Step result

A successful authorization results in:

- A Pending transaction in your business account.
- A hold on the money that is valid for 29 days. After a successful authorization, capture the payment within the 3-day honor period. Payment capture is subject to risk and money availability.

You can use your server-side code to capture the order ID and authorization ID passed in the fetch method in the onApprove function.

## Capture order and authorization IDs

Each server implementation is different. Make sure you have logic in your server-side code to receive the order ID and authorization ID that you pass from the client-side JavaScript fetch function.

Copy the following code and modify it to save the details to your server-side database:

#### **`Save order information sample request code sample`**

```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/48S239579N169645 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ACCESS-TOKEN" \
```

**Modify the code**

After you copy the code in the sample request, modify the following:

- Access-Token - Your access token.
- Order ID - In the URI for the API call, replace the sample ID with your order ID. In this example, the sample order ID is 48S239579N169645 .
- PAYPAL-REQUEST-ID - Replace the sample ID with a unique alphanumeric ID that you generate. The PayPal request ID helps prevent duplicate authorizations if the API call is interrupted. For more information, see [API idempotency](/reference/guidelines/idempotency/) .

### Step result

A successful request results in the following:

- A return status code of HTTP 200 OK .
- A JSON response body containing order details that you can save to your server-side database.

After you capture the order details, you can complete any business tasks, such as verifying you have the item in stock, before you capture the payment.

## Next steps and customizations

### Test integration

Test in the sandbox environment before going live.

### Go live

Move from PayPal's production environment to go live.

### Implement 3D Secure

Authenticate cardholders through card issuers.

### Authorization and honor period

Authorization and capture timing for 2-step payments.

### Payments API

Learn more about the Payments API.

### Void an authorization

Cancel an authorized payment using the Payments API.

### Handle a refund

Refund a captured payment using the Payments API.