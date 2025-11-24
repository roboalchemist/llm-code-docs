# Source: https://docs.klarna.com/payments/mobile-payments/before-you-start/choose-your-integration.md

# Choose your integration

## Integrate Klarna into your mobile app using the Klarna Mobile SDK, choosing between native or WebView options to balance seamless user experience with flexibility and security.

## <span>Overview</span>

The Klarna Mobile SDK is the only recommended way to integrate Klarna products in mobile apps. It ensures optimal performance, security, and feature coverage across all supported platforms and regions.

To guarantee a seamless customer experience and maintain integration quality over time, consider the following for all mobile applications:

- Klarna Mobile SDK is the **primary integration approach** for full feature and product coverage, click here to get started on [iOS](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/klarna-payments/), [Android](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/native-view/) or [React Native](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/reactnative/native-view/).

<!-- -->

- If Mobile SDK usage is not possible, the only acceptable secondary approach is to use **[System WebViews](https://docs.klarna.com/payments/mobile-payments/before-you-start/introduction-mobile-integrations/)** (e.g. `SFSafariViewController`, `ASWebAuthenticationSession`, `Android Custom Tabs`).

<em>Embedded/Custom WebViews (e.g. WKWebView, Android WebView) are strictly prohibited.</em> To ensure secure, reliable, and future-proof integrations, Klarna **does not support** Embedded WebViews for purchase flows. Use the Klarna Mobile SDK or System WebViews as described instead.

​There are different implementation approaches for checkout experience in mobile applications on top of different mobile frameworks and platforms. To address our integrators needs, Klarna Mobile SDK provides multiple alternative approaches to offer the best user experience in any kind of mobile app integration with tailored native APIs. For Klarna products such as **Sign in with Klarna** and **On-site Messaging** you can refer to their mobile integration guidelines:

- [Sign in with Klarna on mobile](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/)
- [On-site Messaging on mobile](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/)

## Native Integrations

You have a fully native app. You’ll likely want to add views and interact with Klarna content via APIs from your app. We call this a native integration.

For these situations, the SDK offers a fully native API towards our products. As the SDK owns these views entirely, it can provide the best experience, offer direct native API interfaces and notify you when relevant events have occurred. For Klarna Payments, Mobile SDK offers **Payment View** integration and this is the integration that we recommend for most mobile applications.

Native integrations are available for Klarna products in the Klarna Mobile SDK.


![native_integration_layers_numbers.png](native_integration_layers_numbers.png)
*native_integration_layers_numbers.png*

1.  **Checkout Screen:** Your native checkout screen and views
2.  **Payment View:** Klarna Payment View with the payment widget

### Payment View

Payment View integration of the Mobile SDK is the most straight forward solutions as it gives you native APIs to initiate a view and authorize the payment session. Upon completed authorization, it notifies you with the result in a callback and the whole flow is completed on the client side.

#### Integration Steps

How it works: At a high level, integrating Klarna Payments in your app involves a few key steps:

1.  **Create a Klarna session** (Server-side) – Your server calls Klarna’s API to create a payment session with the customer’s order details. Klarna responds with a client_token that represents this session.
2.  **Rendering the payment view** (Client-side) – Using the client_token, your app displays Klarna’s KlarnaPaymentView (a pre-built UI component) for the available payment method(s). This view is essentially Klarna’s payment widget optimized for mobile.
3.  **Authorizing the session** (Client-side) – The customer reviews the Klarna payment option and confirms the payment. The SDK notifies your app (via callbacks) when the payment is authorized, providing an authorization_token if approval was successful.
4.  **Creating an order** (Server-side) – Your server uses the authorization token to finalize the purchase by creating an order through Klarna’s API. Upon success, you can show an order confirmation in your app.

These steps mirror Klarna’s web integration flow (session creation → render payment options → authorization → order creation), but the Mobile SDK makes it native. In the following sections, we’ll guide you through setting up the SDK on [iOS](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/klarna-payments/), [Android](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/native-view/) and [React Native](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/reactnative/native-view/), implementing the payment view, handling events, and completing the end-to-end flow.


![mobile-sdk-payments-diagram.png](mobile-sdk-payments-diagram.png)
*mobile-sdk-payments-diagram.png*
## 
Continue to integrate Payment View now:

- **Android integration**: Follow our guide for Android apps.
- **iOS integration**: Follow our guide for iOS apps.
- **React native integration**: Follow our guide for React native apps.
- **Android integration**: Follow our guide for Android apps.
- **iOS integration**: Follow our guide for iOS apps.
- **React native integration**: Follow our guide for React native apps.
- **Android integration**: Follow our guide for Android apps.
- **iOS integration**: Follow our guide for iOS apps.