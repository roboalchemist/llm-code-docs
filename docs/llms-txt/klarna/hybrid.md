# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/hybrid.md

# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/hybrid.md

# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/hybrid.md

# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/hybrid.md

# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/hybrid.md

# Hybrid - Android

## ​​​You can hook up your web view to the SDK in only a few steps and immediately provide a much more pleasant experience when using Klarna products on mobile.

<table>
<tbody>
<tr>
<td>
![hybrid_android_checkout.png](hybrid_android_checkout.png)
*hybrid_android_checkout.png*</td>
<td>
![3_overview.png](3_overview.png)
*3_overview.png*</td>
<td>
![hybrid_android_confirmation.png](hybrid_android_confirmation.png)
*hybrid_android_confirmation.png*</td>
</tr>
<tr>
<td><p>Your checkout screen when Klarna is selected as payment method.</p></td>
<td><p>Klarna purchase flow starts when customer confirms to <strong>Continue with Klarna</strong>.</p></td>
<td><p>Your order confirmation screen after a successful payment.</p></td>
</tr>
</tbody>
</table>

#### <span>Integration Steps</span>

- [Prepare](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/hybrid.md): Make sure you have a web checkout integrated with Klarna Payments.
- [Set up your app](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/hybrid.md) (Mobile App): Set up return URL to your application.
- [Present your web checkout](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/hybrid.md) (Mobile App): Present you web checkout using System WebView.

## <span>Prepare</span>

This guide will lead you through all the steps required to accept Klarna Payments in your mobile app using your web integration. At the end, you will be able to accept payments with Klarna with very few native changes.This guide assumes that you already have a web checkout integrated with Klarna Payments and you intend to use it in your mobile application. If you haven't done such web integration, we suggest you to check the [web payments documentation](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-2-checkout.md).

## <span>Set up your app</span>

### <span>Import the SDK</span>

#### <span>Add the Repository</span>

Add the Klarna Mobile SDK maven repository: 

### Kotlin


``` kotlin
repositories {
    maven("https://x.klarnacdn.net/mobile-sdk/")
}
```



### Groovy


``` groovy
repositories {
    maven {
        url 'https://x.klarnacdn.net/mobile-sdk/'
    }
}
```

#### <span>Add the Dependency</span>

Add the SDK as a dependency to your app: 

### Kotlin


``` kotlin
dependencies {
    implementation("com.klarna.mobile:sdk:2.x.x")
}
```



### Groovy


``` groovy
dependencies {
    implementation 'com.klarna.mobile:sdk:2.x.x'
}
```

To read more about Mobile SDK versioning policy, check out [this section.](https://docs.klarna.com)

### <span>Set up your app</span>

#### <span>Return URL</span>

Klarna purchase flows might require authorizations in other applications (e.g. bank apps) or do a handover to the Klarna app. In such cases, a return URL to your application ensures seamless return to the flow in your app, hence setting up a return URL is required. It is expected that redirects to this URL should only open your application without any changes in the UI state, ensuring the customer can continue the flow prior to external navigation. You can read more about how deep links and intent filters work [on the Android Developers site](https://developer.android.com/training/app-links/deep-linking). You can set up a Return URL app scheme for your application by registering an `intent-filter` for the Activity you integrated Klarna, in your app’s `AndroidManifest.xml`:

``` xml
<application...>
<activity...>
<intent-filter>
<action android:name="android.intent.action.VIEW"></action>
<category android:name="android.intent.category.DEFAULT"></category>
<category android:name="android.intent.category.BROWSABLE"></category>
<data android:scheme="<your-custom-scheme>"></data>
<data android:host="<your-custom-host>"></data>
</intent-filter>


```

**Important:** Construct the return URL string passed to Klarna by combining the attributes defined in your <intent-filter>'s `<data>` tags, following the standard URL format: <your-custom-scheme>`://`<your-custom-host>

``` kotlin
override fun onNewIntent(intent: Intent?) {
    super.onNewIntent(intent)
    intent?.data?.let { uri ->
        if (uri.host == Contants.klarnaReturnUrl.host && uri.host == Contants.klarnaReturnUrl.host) {
            // This is a return URL for Klarna – skip deep linking
            return
        }
        // This was not a return URL for Klarna
    }
}
```

The hosting `Activity` should be using `launchMode` of type `singleTask` or `singleTop` to prevent a new instance from being created when returning from an external application.

## Present your web checkout

### Create a WebView

In order to use your web integration in the app, first step would be to create a WebView for loading your checkout URLs. You can simply do this by initiating the WebView first.

#### Retrieve WebView inflated from XML

``` swift
val webView = findViewById(R.id.webView)
webView.webViewClient = this
webView.loadUrl("https://www.merchant.com/checkout") // Load your checkout page where Klarna Payments is integrated
```

#### Create a new WebView from code

``` kotlin
webView = WebView(context)
webView.webViewClient = this
webView.loadUrl("https://www.merchant.com/checkout") // Load your checkout page where Klarna Payments is integrated
```

Having an implementation for `WebViewClient` is important as you will need it in the following steps.

### Create an Hybrid SDK instance

Initialize the Hybrid SDK by creating a new instance of `KlarnaHybridSDK`. You should hold a strong reference to the SDK. It will deallocate all its resources if you null it. You only need a single instance of the SDK, regardless of how many web views you have, but if you need to, you can create several SDKs.

``` kotlin
val hybridSDK = KlarnaHybridSDK(returnUrl, null, null)
hybridSDK.eventHandler = this
```

### Creating an Instance

| **Param** | **Type** | **Description** |
|----|----|----|
| returnUrl | String | A URL that the SDK can use to return customers to your app. |
| eventCallback | KlarnaEventCallback? | Event Callback interface that will notify you about messages and errors. This is not required as you will be using the KlarnaEventHandler. |
| fullscreenEventCallback | KlarnaFullscreenEventCallback? | Fullscreen event Callback interface that will notify you about fullscreen transition events. This is not required. |

### KlarnaEventHandler

The SDK will notify you of events and errors via event callback object that you’ll need to implement. The SDK also notifies you about different events during fullscreen transition via fullscreen event callback. You will need to implement the `KlarnaEventHandler` interface in order to receive events and errors from the SDK. This will let your app be notified about relevant events and errors that happen inside the web view that the SDK is observing.

``` kotlin
    class MyActivity: AppCompatActivity(), KlarnaEventHandler {
        override fun onEvent(klarnaComponent: KlarnaComponent, event: KlarnaProductEvent) {
            // Implementation for dispatched event
        }
        override fun onError(klarnaComponent: KlarnaComponent, error: KlarnaMobileSDKError) {
            // Implementation for encountered error
        }
    }
```

### <span>Add your WebView</span>

You need to add the web views that the SDK should track. The SDK will hold weak references to these web views, so if they’re deallocated, the SDK will lose track of them.

``` kotlin
hybridSDK.addWebView(webView)
```

### <span>Notify the SDK</span>

There are two instances at which you’ll need to notify the SDK of events in your web view (as we don’t override your `WebViewClient`).

#### Before a Navigation

You should notify the SDK about upcoming navigations by calling the SDK’s `shouldFollowNavigation` from your `WebViewClient`.

``` kotlin
class MyWebViewClient(): WebViewClient() {
    override fun shouldOverrideUrlLoading(view: WebView, url: String): Boolean {
        return !hybridSDK.shouldFollowNavigation(url)
    }
}
```

#### After a Navigation

You need to notify the SDK after a page has loaded by calling the SDK’s `newPageLoad` from your `WebViewClient`.

``` kotlin
class MyWebViewClient(): WebViewClient() {
    override fun onPageFinished(view: WebView, url: String) {
        hybridSDK.newPageLoad(view)
    }
}
```

As you are re-using your web integration, this integration approach assumes that you have implemented order creation via the integration that exists in web. Hence, this documentation does not cover this step, if you would like to learn more about authorizing a session and creating an order in web, check out these documentations:

- [Web Payments: Authorization callback](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-2-checkout.md)
- [Web Payments: Creating an order](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-3-create-an-order.md)

### Optional

### Enable logging

The SDK will log events and errors while it’s running, which you can read in **logcat** console. You can set the logging level for the SDK through the `loggingLevel` property of integration instance.

``` swift
hybridSdk.loggingLevel = KlarnaLoggingLevel.Verbose
```

#### KlarnaLoggingLevel

| Value                      | Description                        |
|----------------------------|------------------------------------|
| KlarnaLoggingLevel.Off     | No logging                         |
| KlarnaLoggingLevel.Error   | Log error messages only            |
| KlarnaLoggingLevel.Verbose | Log all messages (debug and error) |

## What's next

Klarna Mobile SDK provides a full suite of mobile-first integrations, including Klarna products like:

<table>
<tbody>
<tr>
<td>
![Pink_Standard_Consumer_(1).png](Pink_Standard_Consumer_(1).png)
*Pink_Standard_Consumer_(1).png*</td>
<td>
![Pink_Standard_Consumer_(2).png](Pink_Standard_Consumer_(2).png)
*Pink_Standard_Consumer_(2).png*</td>
<td>
![Pink_Standard_Consumer_(3).png](Pink_Standard_Consumer_(3).png)
*Pink_Standard_Consumer_(3).png*</td>
</tr>
<tr>
<td style="vertical-align:middle;text-align:center;"><p>Sign in with Klarna</p></td>
<td style="vertical-align:middle;text-align:center;"><p>On-site Messaging</p></td>
<td style="vertical-align:middle;text-align:center;"><p>Express Checkout</p></td>
</tr>
</tbody>
</table>

- **On-site Messaging**: Show contextual messaging let your customers know about the available payment options in pre-checkout: click [here](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration.md) to learn more.
- **Sign in with Klarna**: Seamlessly identify and let users login via their Klarna account: click [here](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile.md) to learn more.
- **Express Checkout**: Accelerate your checkout process and boost conversion by offering a one-click checkout, click [here](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start.md) to learn more (Mobile SDK support available soon).

Complete your integration with

- [Order management](https://docs.klarna.com/payments/after-payments/order-management/before-you-start/what-is-order-management.md)
- [Settlements](https://docs.klarna.com/payments/after-payments/settlements/settlement-files.md)
- [End-to-end testing](https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases.md)
- [Prepare for go live](https://docs.klarna.com/resources/developer-tools/testing-payments/go-live-checklist.md)</your-custom-host></your-custom-scheme></data></intent-filter></activity...></application...>