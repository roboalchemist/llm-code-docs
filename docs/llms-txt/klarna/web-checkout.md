# Source: https://docs.klarna.com/payments/mobile-payments/integrate-without-mobile-sdk/android/web-checkout.md

# Source: https://docs.klarna.com/payments/mobile-payments/integrate-without-mobile-sdk/ios/web-checkout.md

# Source: https://docs.klarna.com/payments/mobile-payments/integrate-without-mobile-sdk/android/web-checkout.md

# Web Checkout - Android

## When the recommended integration approach of Klarna Mobile SDK is not possible, the guide below will guide you through how to integrate your web checkout in your mobile app without the Mobile SDK.

<table>
<tbody>
<tr>
<td>
![Draft:android_web_checkout.png](Draft:android_web_checkout.png)
*Draft:android_web_checkout.png*</td>
<td>
![android-system-webview-opf-shield.png](android-system-webview-opf-shield.png)
*android-system-webview-opf-shield.png*</td>
<td>
![Draft:android_web_confirmation.png](Draft:android_web_confirmation.png)
*Draft:android_web_confirmation.png*</td>
</tr>
<tr>
<td><p>Your checkout screen when Klarna is selected as payment method.</p></td>
<td><p>Hosted Payment Page flow starts when customer confirms to <strong>Continue with Klarna</strong>.</p></td>
<td><p>Your order confirmation screen after a successful payment.</p></td>
</tr>
</tbody>
</table>

#### <span>Integration Steps</span>

- **[Prepare](https://docs.klarna.com/payments/mobile-payments/integrate-without-mobile-sdk/android/web-checkout/#prepare)**: Make sure you have a web checkout integrated with Klarna Payments.
- **[Set up your app](https://docs.klarna.com/payments/mobile-payments/integrate-without-mobile-sdk/android/web-checkout/#set-up-your-app)** (Mobile App): Set up return URL to your application.
- **[Present your web checkout](https://docs.klarna.com/payments/mobile-payments/integrate-without-mobile-sdk/android/web-checkout/#present-your-web-checkout)** (Mobile App): Present you web checkout using System WebView.

## <span>Prepare</span>

This guide will lead you through all the steps required to accept Klarna Payments in your mobile app using your web integration. At the end, you will be able to accept payments with Klarna with very few native changes. Klarna still recommends Klarna Mobile SDK as first choice for Web Checkout integrations in mobile apps, [Mobile SDK WebView integrations](https://docs.klarna.com/payments/mobile-payments/before-you-start/choose-your-integration/#webview20integrations) can be utilized instead of System WebViews in such cases. This guide assumes that you already have a web checkout integrated with Klarna Payments and you intend to use it in your mobile application. If you haven't done such web integration, we suggest you to check the recommended [integration approaches here](https://docs.klarna.com/payments/mobile-payments/before-you-start/choose-your-integration/). These will also help you offer better UX and more stable integration than System WebViews.

## Set up your app

### Return URL

​Klarna purchase flows might require authorizations in other applications (e.g. bank apps) or do a handover to the Klarna app. In such cases, a return URL to your application ensures seamless return to the flow in your app, hence setting up a return URL is required. It is expected that redirects to this URL should only open your application without any changes in the UI state, ensuring the customer can continue the flow prior to external navigation. You can read more about how deep links and intent filters work [on the Android Developers site](https://developer.android.com/training/app-links/deep-linking). You can set up a Return URL app scheme for your application by registering an `intent-filter` for the Activity you integrated Klarna, in your app’s `AndroidManifest.xml`:

``` xml
<application...>
<activity...>
<intent-filter>
<action android:name="android.intent.action.VIEW"></action>
<category android:name="android.intent.category.DEFAULT"></category>
<category android:name="android.intent.category.BROWSABLE"></category>
<data android:scheme="&lt;your-custom-scheme&gt;"></data>
<data android:host="&lt;your-custom-host&gt;"></data>
</intent-filter>


```

**Important:** Construct the return URL string passed to Klarna by combining the attributes defined in your <intent-filter>'s `<data>` tags, following the standard URL format: <your-custom-scheme>`://`<your-custom-host>

``` kotlin
override fun onNewIntent(intent: Intent?) {
    super.onNewIntent(intent)
    intent?.data?.let { uri -&gt;
        if (uri.host == Contants.klarnaReturnUrl.host &amp;&amp; uri.host == Contants.klarnaReturnUrl.host) {
            // This is a return URL for Klarna – skip deep linking
            return
        }
        // This was not a return URL for Klarna
    }
}
```

The hosting `Activity` should be using `launchMode` of type `singleTask` or `singleTop` to prevent a new instance from being created when returning from an external application. As Android Custom Tabs will be shown to the customer during the flow, we require Activity set up for intent-filter to finish immediately and retain Custom Tabs on top.

``` kotlin
class RedirectActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        handleRedirect(intent)
    }
    override fun onNewIntent(intent: Intent?) {
        super.onNewIntent(intent)
        handleRedirect(intent)
    }
    private fun handleRedirect(intent: Intent?) {
        intent?.data?.let { uri -&gt;
            if (uri.scheme == "<your-custom-scheme>" &amp;&amp; uri.host == "<your-custom-host>") {
                // Returned to Klarna from external applications, keep purchase flow presented
                // Call finish() if this is an empty redirect Activity
                // Retain current state if it's hosting the purchase flow
            }
        }
    }
}
```

When creating a payment session, make sure you backend sets [`merchant_urls.`<span>`app_return_url`</span>](https://docs.klarna.com/api/payments/#operation/createCreditSession!path=merchant_urls/app_return_url&amp;t=request) <span>to return URL set up for the app.</span>

## Present your web checkout

On Android, system WebViews are commonly implemented using [Android Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs). By default, Custom Tabs share cookies and session data with the device’s default browser (e.g., Chrome or Firefox). This shared session capability is essential for Klarna, as it allows us to recognize returning customers across sessions and provide a seamless checkout experience. While it's possible to disable session sharing using <span>**[Ephemeral Custom Tabs](https://developer.chrome.com/docs/android/custom-tabs/guide-ephemeral-tab)**</span>, we require **persistent (non-ephemeral) sessions** <span>as this functionality enables Klarna</span> to maintain customer context across the device.

``` groovy
dependencies {
    implementation 'androidx.browser:browser:<latestversion>'
}
```

``` kotlin
val customTabsIntent = CustomTabsIntent.Builder()
    .setEphemeralBrowsingEnabled(false) // only available in android.browser version 1.9.0
    .build()
customTabsIntent.launchUrl(this, sessionUrl.toUri()) // URL of your web checkout for this customer session
```

#### Redirect back to your app

After the purchase is completed, Klarna payment flow will be closed and the customer will be taken back to your checkout page where you will be notified for the authorized session in your web integration. From your checkout or the confirmation page, you can choose to redirect the customer back to your application. To get the user back to your application from System WebViews, you can redirect to any `intent-filter` set for the `Activity` that you want to return to from your checkout or confirmation pages, as those will be loaded in the System WebView.

<table>
<tbody>
<tr>
<td>
![android-system-webview-opf-shield.png](android-system-webview-opf-shield.png)
*android-system-webview-opf-shield.png*</td>
<td>
![android-system-webview-checkout-postselection.png](android-system-webview-checkout-postselection.png)
*android-system-webview-checkout-postselection.png*</td>
<td>
![android-system-webview-confirmation.png](android-system-webview-confirmation.png)
*android-system-webview-confirmation.png*</td>
</tr>
<tr>
<td><p>Klarna purchase flow in System WebView.</p></td>
<td><p>Your checkout page in System WebView.</p></td>
<td><p>Your confirmation page in System WebView.</p></td>
</tr>
</tbody>
</table>

As you are re-using your web integration, this integration approach assumes that you have implemented order creation via the integration that exists in web. Hence, this documentation does not cover this step, if you would like to learn more about authorizing a session and creating an order in web, check out these documentations:

- [Web Payments: Authorization callback](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-2-checkout/#authorization-callback)
- [Web Payments: Creating an order](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-3-create-an-order/)

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

- **On-site Messaging**: Show contextual messaging let your customers know about the available payment options in pre-checkout: click [here](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/) to learn more.
- **Sign in with Klarna**: Seamlessly identify and let users login via their Klarna account: click [here](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/) to learn more.
- **Express Checkout**: Accelerate your checkout process and boost conversion by offering a one-click checkout, click [here](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start/) to learn more.

Complete your integration with

- [Order management](https://docs.klarna.com/payments/after-payments/order-management/before-you-start/what-is-order-management/)
- [Settlements](https://docs.klarna.com/payments/after-payments/settlements/settlement-files/)
- [End-to-end testing](https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases/)
- [Prepare for go live](https://docs.klarna.com/resources/developer-tools/testing-payments/go-live-checklist/)</latestversion></your-custom-host></your-custom-scheme></your-custom-host></your-custom-scheme></data></intent-filter></activity...></application...>