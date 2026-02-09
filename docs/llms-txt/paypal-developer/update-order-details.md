# Update order details

For increased flexibility when obtaining payments from buyers, you can update an existing order. Updating orders allows you to:

- Determine additional amounts, including shipping and tax.
- Capture a different total amount without the payer re-approving the order.
- Update fields, such as shipping address, after collecting them from the payer.

## Know before you code

### Expanded Checkout
- Complete the steps in **Get started** to get your sandbox account login information and access token from the Developer Dashboard.
- This feature modifies an existing [Checkout integration](/docs/checkout/advanced/) and uses the following:
  - [PayPal JavaScript SDK](/sdk/js/configuration/)
  - [Orders REST API](/docs/api/orders/v2/) - [Create order](/docs/api/orders/v2/#orders_create) and [Update order](/docs/api/orders/v2/#orders_patch)

### Explore PayPal APIs with Postman
You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

If you update the final amount of the order after the payer approves the payment, or update other amount fields, such as shipping or tax, show a **Continue** button during checkout instead of a **Pay Now** button. A **Continue** button indicates to the payer that the amount or other details might change before they complete the order.

To show a **Continue** button, add `commit=false` in the script tag as shown in the following example:

```javascript
<script src="https://www.paypal.com/sdk/js?client-id=CLIENT-ID&commit=false"></script>
```

**info**
**Tip:** Using `commit=false` reduces the number of payment methods that are shown to your payer because not all funding sources can be used when modifying the order. When possible, determine the final amount before the payer approves the transaction, and avoid using `PATCH`.