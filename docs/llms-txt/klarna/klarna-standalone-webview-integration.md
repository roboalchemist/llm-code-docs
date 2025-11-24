# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/klarna-standalone-webview-integration.md

# Klarna WebView - Android

## In this step-by-step guide you will learn how to integrate the KlarnaStandaloneWebView into your Android app.

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

​

#### <span>Integration Steps</span>

- [Prepare](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/klarna-standalone-webview-integration.md): Make sure you have a web checkout integrated with Klarna Payments.
- [Set up your app](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/klarna-standalone-webview-integration.md) (Mobile App): Set up return URL to your application.
- [Present your web checkout](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/klarna-standalone-webview-integration.md) (Mobile App): Present you web checkout using System WebView.

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

### Create Klarna WebView

To add the `KlarnaStandaloneWebView` to your app's layout, there are two distinct ways. The following sections provide a detailed explanation of each approach.

#### Creating the View from XML

You can add the `KlarnaStandaloneWebView` to your XML layout as below.

``` xml
<com.klarna.mobile.sdk.api.standalonewebview.klarnastandalonewebview ...="" android:id="@+id/webView" app:klarnareturnurl="..."></com.klarna.mobile.sdk.api.standalonewebview.klarnastandalonewebview>
```

``` kotlin
val klarnaWebView = findViewById(R.id.webView)
```

#### Creating the View from Code

If you instead want to create the `KlarnaStandaloneWebView` in code, you can use its constructor to create an instance and then add it to your layout.

``` kotlin
val klarnaStandaloneWebView = KlarnaStandaloneWebView(
    context = ...,
    attrs = ...,
    defStyleAttr = ...,
    webViewClient = ...,
    eventHandler = ...,
    environment = ...,
    region = ...,
    theme = ...,
    resourceEndpoint = ...,
    returnURL = ...
)
```

In the following table you can see the parameters that the constructor expects. The required parameters are marked with an asterisk.

| Parameter | Type | Description |
|----|----|----|
| context | Context | The context of the Activity the KlarnaStandaloneWebView is in. |
| attrs | AttributeSet | The AtttributeSet that you usually pass when creating a View from code. Its default value is null. |
| defStyleAttr | Int | An integer value that you usually pass when creating a View from code. Its default value is 0. |
| returnURL | String | The return URL which is used for navigating users back to your app if necessary. |
| webViewClient | KlarnaStandaloneWebViewClient | It's used to receive callbacks from the `KlarnaStandaloneWebView`. Its default value is null. |
| eventHandler | KlarnaEventHandler | It's used to get notified of Klarna-related events. Its default value is null. |
| environment | KlarnaEnvironment | An enumeration that is used to configure the endpoints and other behaviors that the `KlarnaStandaloneWebView` will be operating with. Its default value is null which means the environment will be `production` by default. |
| region | KlarnaRegion | An enumeration that defines the regional API endpoints to which the `KlarnaStandaloneWebView` will send/receive requests. Its default value is null which means the region will be `EU` by default. |
| theme | KlarnaTheme | An enumeration that defines the theming for the Klarna-related components that are displayed inside the KlarnaStandaloneWebView. Its default value is null which means it will be `light` by default. |
| resourceEndpoint | KlarnaResourceEndpoint | An enumeration that defines the cloud provider to which the KlarnaStandaloneWebView will send/receive requests. Please note that this should not be changed or overridden. It's default value is null. |

### <span>Load your checkout page</span>

`KlarnaStandaloneWebView` is just like any other WebView component, thus you can easily load your web checkout or any other web page with it.

``` kotlin
klarnaWebView.loadUrl("https://www.merchant.com/checkout") // Load your checkout page where Klarna Payments is integrated
```

## Optional

### Additional Methods

As previously mentioned, the `KlarnaStandaloneWebView` can be perceived as a specialized `WebView` developed specifically for displaying Klarna-related content. Consequently, it inherits many methods and properties from the standard `WebView` with the addition of some Klarna-specific methods and properties. In essence, this means that while the `KlarnaStandaloneWebView` functions similarly to a typical `WebView` and maintains its broad functionality, it also includes certain distinct features that cater specifically to the Klarna content, enhancing its usability and performance within a Klarna context.

### WebView Methods and Properties

Below is a set of methods from the `KlarnaStandaloneWebView`that are also available in a standard `WebView`. Please be aware that this list is not comprehensive, serving only as a highlight of commonly shared methods:

- `loadUrl`
- `postUrl`
- `loadData`
- `loadDataWithBaseUrl`
- `reload`
- `stopLoading`
- `goBack`
- `goForward`
- `canGoBack`
- `canGoForward`
- `clearCache`

### Klarna-specific Methods and Properties

Below is a set of methods and properties from the `KlarnaStandaloneWebView` that are Klarna-specific. Please be aware that this list is not exhaustive.

- `eventHandler`: a mutable property that allows setting or getting the `KlarnaEventHandler`.
- `loggingLevel`: a mutable property that allows setting or getting the `KlarnaLoggingLevel`. You can use this property to set the logging level of the `KlarnaStandaloneWebView`.
- `productOptions`: a mutable property that allows setting the options for some of the Klarna products.
- `sendEvent`: a method that can be used to send a message to a Klarna component which is loaded in the `KlarnaStandaloneWebView`.

### Enable logging

The SDK will log events and errors while it’s running, which you can read in **logcat** console. You can set the logging level for the SDK through the `loggingLevel` property of integration instance.

``` swift
klarnaWebView.loggingLevel = KlarnaLoggingLevel.Verbose
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