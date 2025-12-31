# Source: https://docs.klarna.com/payments/get-started/integration-checklist.md

# Klarna Payments Integration Checklist

Follow this checklist to ensure a complete integration of **Klarna Payments** for web, mobile, and in-store channels. This guide covers a direct integration with Klarna’s APIs and progresses from initial setup to production readiness, highlighting key decisions and best practices.

## 1. Set up your Klarna account and credentials

- **Create a Klarna test account**: Sign up for a [Klarna developer account](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#accessing-the-test-merchant-portal) and access the Klarna test Merchant Portal.
- **Generate API credentials**: Use the [API key generation instructions](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#getting-test-credentials-for-apis) to retrieve your test and live credentials.
- **Get the correct API endpoints**: Refer to the [API base URLs page](https://docs.klarna.com/api/api-urls/) for the correct environment and regional endpoints.
- **Enable the Klarna test environment**: Use the [Playground environment](https://docs.klarna.com/api/api-urls/#base-urls---testing-playground) for testing.
- **Familiarize yourself with Klarna’s API docs**: Visit the [Klarna API documentation](https://docs.klarna.com/api/payments/) to understand endpoints, data models, and error handling.

## 2. Choose your integration approach

- **Select your platform(s)**: Klarna supports Web, Mobile (iOS/Android), and In-store Payments. See [the Payments overview](https://docs.klarna.com).
- **Plan your Web integration**: Klarna offers solutions for [in-line integration](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-sdk/how-to-integrate-klarna-payments/) and [hosted payment page](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/before-you-start/).
- **Plan your Mobile integration**: Use Klarna’s [Mobile SDKs](https://docs.klarna.com/payments/mobile-payments/before-you-start/introduction-mobile-integrations/) or embed the Web integration via WebView.
- **Plan your In-store integration**: Use Klarna’s [In-store API](https://docs.klarna.com/payments/in-store-payments/before-you-start/what-is-klarna-in-store/) for QR-code-based or link-based payments.
- **Decide on payment scenarios**: See [Recurring Payments guide](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/tokenized-payments/subscriptions-and-on-demand/) for how to handle subscriptions or repeat purchases.

## 3. Build your Online Payments integration

Implement Klarna Payments using the in-line widget integration for Web and the Klarna Mobile SDKs for iOS and Android.

### Web (in-line widget)

- [Initiate a payment](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-sdk/step-1-initiate-a-payment/) creates a session that identifies the purchase towards Klarna.
- [Check out](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-sdk/step-2-checkout/) displays Klarna as a payment method and authorizes the purchase.
- [Create an order](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-sdk/step-3-create-an-order/) uses the authorized payment from the previous step and creates an order.
- The payment process has slight variations according to each [scenario](https://docs.klarna.com/payments/web-payments/before-you-start/what-is-klarna-payments/#payment-scenarios) one-time or recurring payments.

### Mobile (native SDKs)

- **Set up**: Install the Klarna SDK for [iOS](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/native-view/) or [Android](https://docs.klarna.com) using your platform’s package manager.
- **Initiate payment** (Server-side): Your backend [creates a payment session](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-sdk/step-1-initiate-a-payment/) and passes the `client_token` to your app.
- **Render payment view** (Mobile App): [Present Klarna’s native view](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/native-view/#render-payment-view-mobile-app) to display Klarna in your checkout.
- **Authorize the session** (Mobile App): [Trigger the authorization](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/native-view/#authorize-the-session-mobile-app) through the SDK and handle the callback.
- **Create an order** (Server-side): Use the resulting `authorization_token` in your backend to finalize the payment and [create an order](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-sdk/step-3-create-an-order/) .

## 4. Build your Post Purchase integration

- **View and change orders**: Use the Order management API to [read and update the details of an order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/view-and-change-orders/).
- **Capture and track orders**: [capture your orders](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders/) and add shipping information for tracking.
- **Refund orders and manage authorizations**: [refund and manage orders](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-orders-and-manage-authorizations/) efficiently using the Klarna Order Management API.
- **Reconcile settlements**: Settlement reports are provided via the [Merchant Portal Settlements App](https://docs.klarna.com/payments/after-payments/settlements/settlement-files/), the [Settlements API](https://docs.klarna.com/api/settlements/) or via a [pre-configured SFTP](https://docs.klarna.com/payments/after-payments/settlements/additional-resources/how-to-get-settlement-reports-via-sftp/).
- **Customer support readiness**: Learn [dispute handling](https://docs.klarna.com) and refund workflows.

## 5. Test and optimize your integration

- **Exercise all test scenarios**: Complete these [End-to-end test cases](https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases/) in Playground.
- **Follow Klarna’s UX guidelines**: Implement Klarna's [UX Guidelines](https://docs.klarna.com) and improve your conversion with [On-site messaging](https://docs.klarna.com/conversion-boosters/on-site-messaging/before-you-start/), [Express checkout](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start/) and [Sign in with Klarna](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/before-you-start/).
- **Verify frontend behavior**: Test Klarna widget or SDK behavior on all platforms.
- **Escalation and retry policy**: [Ensure all backend calls](https://docs.klarna.com/api/escalation-and-retry-policy/) are as robust and fail-safe as possible.
- **Test failure and recovery paths**: Simulate expired sessions and API errors. See [error codes reference](https://docs.klarna.com/resources/developer-tools/error-handling/error-codes-and-messages-for-klarna-payments/).
- **Review in the Merchant Portal**: Use the [Playground portal](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/) to validate test transactions.
- **Performance and fallback testing**: Performance test your integration, considering Klarna's [rate limit policy](https://docs.klarna.com/api/rate-limit/) and [SLAs](https://docs.klarna.com/api/klarna-service-level/).
- **Security testing**: Ensure no credentials or PII are exposed. All traffic must use HTTPS.

## 6. Go live and monitor

- **Obtain production API credentials**: Use [the live API key](https://docs.klarna.com/resources/developer-tools/testing-payments/go-live-checklist/#set-up-your-production-account-and-prepare-for-the-go-live) in production.
- **Run final verification in production mode**: Complete the [go-live checklist](https://docs.klarna.com/resources/developer-tools/testing-payments/go-live-checklist/) in production.
- **Review compliance and legal requirements**: Ensure checkout and messaging comply with [design and legal standards](https://docs.klarna.com/resources/legal-and-compliance/payment-solutions-guidelines/eu/).
- **Implement Klarna branding**: Add [Klarna promotional assets](https://docs.klarna.com/resources/marketing-tools/global-marketing-assets/marketing-for-integrated-partners/) to your site.
- **Monitor orders and payments**: Check that all orders appear and payouts reconcile.

For more information, see the [Klarna Payments documentation](https://docs.klarna.com).