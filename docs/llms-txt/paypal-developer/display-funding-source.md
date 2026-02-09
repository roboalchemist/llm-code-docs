# Display Funding Source Used

Display the funding source used to your buyers to provide a unique experience.

If you have a confirmation page or notification in your checkout workflow, display the payment source the payer selected.

For example, if the payer paid with Venmo, show Venmo as the payment source on the confirmation page or notification.

## Know Before You Code

### You Need a Developer Account to Get Sandbox Credentials

PayPal uses the following REST API credentials, which you can get from the developer dashboard:

- **Client ID**: Authenticates your account with PayPal and identifies an app in your sandbox.
- **Client Secret**: Authorizes an app in your sandbox. Keep this secret safe and don't share it.

## PayPal Checkout

This feature modifies an existing PayPal Checkout integration and uses the following:

- [JavaScript SDK](/sdk/js/): Adds PayPal-supported payment methods.
- [Orders REST API](/docs/api/orders/v2/): Create, update, retrieve, authorize, and capture orders.

## Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

## Show Funding Source

Your Checkout experience might have a confirmation page or a notification to the user that they're paying with PayPal. Ensure the funding source the user chose, such as Venmo, shows as expected or it might lead to confusion and reduced Checkout conversion.

Use an `onClick` handler to get the funding source and display it on a confirmation page.

```javascript
let fundingSource;

paypal.Buttons({
    onClick: (data) => {
        // fundingSource = "venmo"
        fundingSource = data.fundingSource;

        // Use this value to determine the funding source used to pay
        // Update your confirmation pages and notifications from "PayPal" to "Venmo"
    }
})
```

The following table shows supported `fundingSource` values:

| Funding source | Description |
| --- | --- |
| `paypal.FUNDING.PAYPAL` | PayPal |
| `paypal.FUNDING.CARD` | Credit or debit cards |
| `paypal.FUNDING.PAYLATER` | Pay Later (US, UK), Pay in 4 (AU), 4X PayPal (France), Paga en 3 plazos (Spain), Paga in 3 rate (Italy), Später Bezahlen (Germany) |
| `paypal.FUNDING.CREDIT` | PayPal Credit |
| `paypal.FUNDING.VENMO` | Venmo |

## Next Steps and Customizations

### Test Integration

Test in the sandbox environment before going live.

### Go Live

Move from PayPal's production environment to go live.

### JavaScript SDK Reference

Customize your integration with script config parameters.