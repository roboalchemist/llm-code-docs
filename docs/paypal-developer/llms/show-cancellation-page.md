# Show cancellation page

## Know before you code

### Expanded Checkout

- Complete the steps in **Get started** to get your sandbox account login information and access token from the Developer Dashboard.
- This feature modifies an existing [Checkout integration](/docs/checkout/advanced/) and uses the following:
  - [PayPal JavaScript SDK](/sdk/js/configuration/)
  - [Orders REST API](/docs/api/orders/v2/) - [Create order](/docs/api/orders/v2/#orders_create) and [Update order](/docs/api/orders/v2/#orders_patch)

### Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

---

## Display a cancellation page

Add the `onCancel` function to the JavaScript that renders the PayPal buttons to show a cancellation page when a payer cancels a payment:

```javascript
paypal.Buttons({
    onCancel: function(data) {
        // Show a cancel page or return to cart
    }
}).render('#paypal-button-container');
```