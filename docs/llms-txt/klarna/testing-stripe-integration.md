# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/testing-stripe-integration.md

# Testing Stripe integration

## Testing

We recommend testing the integration before launching Klarna’s payment method in live mode. When in [Stripe test mode](https://stripe.com/docs/keys#test-live-modes), confirm that all information requested from the customer is passed through to Klarna at checkout. You can do that by placing sample orders in the test environment and validating the information displayed on the Klarna hosted payment page. Check out the [Stripe guidelines](https://stripe.com/docs/payments/klarna/accept-a-payment?platform=web&ui=API#testmode-guide) for information on how to best leverage test mode to verify your integration.