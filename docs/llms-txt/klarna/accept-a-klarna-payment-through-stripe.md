# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/stripe/payments/accept-a-klarna-payment-through-stripe.md

# Accept a Klarna payment through Stripe

## You can choose from multiple integration options to accept a Klarna payment through Stripe. Pick the method best suited to your needs and the details of your Stripe integration.

The most common methods of integrating Klarna are presented below. Regardless of the integration method, your customers will be redirected to a Klarna hosted payment page to complete the purchase.

- [Stripe Checkout](https://stripe.com/docs/payments/checkout) is a low-code integration solution you can use to build a customized payment page hosted on Stripe. If you’re already integrated with Stripe Checkout, almost no additional development is required apart from enabling Klarna as a payment method. You can find more information on the \[<https: accept-a-payment?platform="web&ui=checkout#enable-klarna-as-a-payment-method" docs="" klarna="" payments="" stripe.com="">. Accept a Klarna payment\] page.
- [Stripe's Payment Element](https://stripe.com/docs/payments/customize-payment-element) is another low-code option where you can enable Klarna in your Stripe dashboard.
- The [Direct API](https://stripe.com/docs/payments/klarna/accept-a-payment?platform=web&ui=API) integration is a full back-end integration. Use it if you want to build a custom checkout and have more flexibility and control.
- [Payment links](https://stripe.com/docs/payments/payment-links) are the easiest way to offer a one-time payment or a recurring payment without writing a line of code. You can generate a payment link from the Stripe dashboard and share that link with your customers.
- You can enable Klarna in your [mobile app](https://stripe.com/docs/payments/klarna/accept-a-payment?platform=mobile) for React Native, iOS, and Android. When a customer selects Klarna in your app, a WebView appears where the payment is verified.

**Private Preview** Klarna is currently available in private preview on [Link](https://stripe.com/payments/link). Link is a wallet built by Stripe that enables consumers to check out faster with their preferred payment method. If you're interested in getting access, enter your email on [Stripe docs](https://docs.stripe.com/payments/link#request-access)</https:>