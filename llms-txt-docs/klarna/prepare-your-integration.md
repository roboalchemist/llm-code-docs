# Source: https://docs.klarna.com/payments/web-payments/before-you-start/prepare-your-integration.md

# Source: https://docs.klarna.com/payments/in-store-payments/before-you-start/prepare-your-integration.md

# Source: https://docs.klarna.com/payments/web-payments/before-you-start/prepare-your-integration.md

# Prepare your integration web

## Ready to offer a smoooth purchase experience to your customers? Here's what you need to know before integrating Klarna payments into your store's website or mobile app.

When you integrate Klarna payments into your online store, your customers see Klarna as an option when they select a payment method for their purchases. If your customers select Klarna for their purchase, they are redirected to log into their Klarna account. Your customers select their preferred Klarna payment option (pay now, pay later, pay in parts) once they're logged into their Klarna account. We handle the Klarna account user flow, so you don't have to worry about it.

## Integration options

​​​​​​​​You can integrate Klarna payments in two ways: as an in-line widget or as a browser redirect. The customer experience will differ based on the option you choose. ​This is how the two integration options look like:


![ Klarna payments offers 2 integration types: in-line widget and browser redirect. Both are seamlessly integrated with the end-to-end purchase process. ](7552f4_Screenshot_2024_03_22_at_15_06_12.jpeg)
*Klarna payments offers 2 integration types: in-line widget and browser redirect. Both are seamlessly integrated with the end-to-end purchase process.*

Klarna payments covers the process of initiating a payment, checking out, and creating an order. To learn how to handle created orders, see our [Order management section.](https://docs.klarna.com/order-management.md)

### In-line widget

With this option, you present the Klarna widget in line on your checkout page. This integration is a mix of server-side calls, happening through the Payments API, and client-side calls, happening through Klarna’s Javascript SDK library. Adding Klarna payments as an in-line widget ensures the best user experience as your customer interactions take place within your website. For this reason, this is our recommended solution.

### Browser redirect

With this option, your customer is redirected to the Klarna Hosted Payment Page (HPP). This is a server-side-only integration. You can offer Klarna payments to your customers without storing any web components on your website. This Klarna payments guide focuses on the in-line widget integration. To learn more about browser redirect, see our [HPP documentation](https://docs.klarna.com/hosted-payment-page.md). Selecting between the in-line widget or browser redirect solutions depends on your business needs. By displaying the widget, you gain ownership of the front end that your customers interact with. On the other hand, by redirecting to Klarna HPP, you use a pre-built front end solution that does not require integrating through the JavaScript SDK. Klarna strongly recommends using the Mobile SDK for all mobile application integrations. If Mobile SDK integration is not possible, only secure System WebViews (e.g. ASWebAuthenticationSession, SFSafariViewController, Custom Tabs) must be used to maintain security, compliance, and feature support. Custom or embedded WebView solutions (e.g., WKWebView, Android WebView) should **not be used** to load Klarna payment flows. To learn more about payments in mobile apps, please refer to the [In-app SDK section.](https://docs.klarna.com/payments/mobile-payments/before-you-start/overview-and-concepts.md).

## Prerequisites

Before you start integrating Klarna payments, there are a few things you need to prepare in advance:

- Access to the Merchant portal
  - To access the test Merchant portal, you can [sign up to create a new test account](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test.md) or log in with a test existing account.
- API keys for the Klarna Payments API
  - To test your Klarna API integration, you need a set of [test credentials](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test.md).
- [The API reference](https://docs.klarna.com/api/payments.md). You can download the Open API specification for the Klarna payments API and use the specification to [generate](https://openapi-generator.tech/) an API SDK for your programming language.
- [Sample customer data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data.md) and [sample payment data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-payment-data.md)