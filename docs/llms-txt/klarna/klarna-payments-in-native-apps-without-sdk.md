# Source: https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/klarna-payments-in-native-apps-without-sdk.md

# Klarna Payments Webview

## This section content outline known issues when integrating Klarna Payments in the merchant iOS and Android Apps without Klarna SDK. Providing a troubleshooting guide and recommended actions and implementation patterns for your app developers to ensure that Klarna Payments flow works properly.

In case your mobile app is integrated with Klarna Payments and it is not using Klarna SDK, the payment flow could be interrupted getting the customer experience “stuck” on a page with the animated Klarna logo and not allowing to proceed with the payment. ​In order to understand what might cause the issue described above please ask your engineering team to follow the steps below. It is important to have all of the recommendations below implemented to make sure that Klarna Payments flow is working correctly.

## Use OAuth2-compatible webview component

**This step is recommended for best performance.** If your application has integration with "*Sign In with Google"*or*any other social sign-in provider*, we recommend using the same webview component for running the Klarna Payments flow. In detail it means:

- Use [ASWebAuthenticationSession](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession) on iOS
- Use [CustomTabs](https://developer.chrome.com/docs/android/custom-tabs) on Android

## Allow all Klarna domains to be loaded in your application

It is best to allow ‘**\*.klarna.com**’ domains to be loaded in your webview, but if you need to have a specific list, use the following:

- js.klarna.com
- pay.klarna.com
- payments.klarna.com
- login.klarna.com

### Example

If you are using the \`[react-native-webview](https://github.com/react-native-webview/react-native-webview/tree/master)\` library, it is configured in the \`[originWhitelist](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md#originwhitelist)\` property and in the \`[onShouldStartLoadWithRequest](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md#onshouldstartloadwithrequest)\` property.

## Allow redirects

It is crucial that your webview does not block any response codes, like 302 and 303 that are commonly used for browser redirections. Klarna Payments flow relies on this capability in order to run correctly.

### Example

If you are using the \`[react-native-webview](https://github.com/react-native-webview/react-native-webview/tree/master)\` library, check that you allow both Klarna Domains and the redirect status codes in the \`[onShouldStartLoadWithRequest](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md#onshouldstartloadwithrequest)\` handler and \`[onNavigationStateChange](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md#onnavigationstatechange)\` handler.

## Allow running OAuth2 flows

Klarna Payments flow uses OAuth2 protocol to securely log the user in, so it is crucial that this flow is not blocked in your webview component. OAuth2 protocol is an industry standard for running user login flows, used by Google, Apple, Facebook and others.

### Example

If you are using the \`[react-native-webview](https://github.com/react-native-webview/react-native-webview/tree/master)\` library, check that you allow both Klarna Domains and the redirect status codes in the \`[onShouldStartLoadWithRequest](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md#onshouldstartloadwithrequest)\` handler and \`[onNavigationStateChange](https://github.com/react-native-webview/react-native-webview/blob/master/docs/Reference.md#onnavigationstatechange)\` handler.

## Allow InlineMediaPlayback for identification and verification flows

Klarna Payments flow requires the capability to perform real time **identification and verification** **(ID&V)** for fraud prevention, underwriting, and KYC purposes, so it is crucial that your webview has the required configurations to support ID&V.

### Example

To provide correct ID&V flows, standard user agent info is crucial. If there’s a need to customize user agent, the customized info should be added at the end of the standard user agent without overwriting it, as below:

    Mozilla/[version] ([system and browser information]) [platform details] [engine details] [browser details]; example.app/[version]

If you’re using an iframe to integrate with Klarna, it’s **not recommended**. But if you do, check that you configure the following permissions correctly:

    <iframe allow="camera *;microphone *;geolocation *;clipboard-read *;clipboard-write *" src="..."></iframe>

If you are using the \`[react-native-webview](https://github.com/react-native-webview/react-native-webview/tree/master)\` library, check that you configure the following 2 properties correctly as below:

- `allowsInlineMediaPlayback` = **true**
- `mediaPlaybackRequiresUserAction` = **false**

And also apply the changes suggested below for each platform. For **iOS** app, 1 - Set the permissions below in the Info.plist file as below:

    <key>NSCameraUsageDescription</key>
<string>Camera Access</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>Location Access</string>

2 - \[Native App only\] Set WKWebView configuration as below example:

    func createWebView() -> WKWebView {
    let config = WKWebViewConfiguration()
    config.allowsInlineMediaPlayback = true
    config.mediaTypesRequiringUserActionForPlayback = []
    let webview = WKWebView(frame: .zero, configuration: config)
    return webview
    }

For **Android** app, 1 - Update permission setting in AndroidManifest.xml as below,

    <uses-permission android:name="android.permission.INTERNET"></uses-permission>
<uses-permission android:name="android.permission.CAMERA"></uses-permission>
<uses-feature android:name="android.hardware.camera" android:required="true"></uses-feature>
<uses-feature android:name="android.hardware.camera.autofocus"></uses-feature>

2 - \[Native App only\] Allow runtime permissions requests while accessing camera from the webview by setting WebChromeClient to your WebView and implementing **'[onPermissionRequest](https://developer.android.com/reference/kotlin/android/webkit/WebChromeClient#onpermissionrequest)** callback. Example of a WebChromeClient implementation would look similar to the following: The code snippet accepts that requestPermissions method is using a callback, checking the current state of the permissions and requesting consent of the user if needed.

    public class CustomWebChromeClient : WebChromeClient() {
    override fun onPermissionRequest(request: PermissionRequest?) {
    if (Build.VERSION.SDK_INT>= Build.VERSION_CODES.LOLLIPOP) {
    val requiredPermissions = getRequiredPermissions(request)
    requestPermissions(requiredPermissions) { accepted ->
    if (accepted) {
    request?.grant(request.resources)
    } else {
    request?.deny()
    }
    }
    } else {
    super.onPermissionRequest(request)
    }
    }
    @RequiresApi(Build.VERSION_CODES.LOLLIPOP)
    fun getRequiredPermissions(request: PermissionRequest?): Collection<string> {
    val cameraNeeded = request?.resources?.asList()
    ?.contains(PermissionRequest.RESOURCE_VIDEO_CAPTURE) == true
    val audioNeeded = request?.resources?.asList()
    ?.contains(PermissionRequest.RESOURCE_AUDIO_CAPTURE) == true
    val permissions = mutableListOf<string>()
    if (cameraNeeded) permissions.add(Manifest.permission.CAMERA)
    if (audioNeeded) permissions.add(Manifest.permission.RECORD_AUDIO)
    return permissions
    }
    }

3 - \[Native App only\] Make sure to also enable playback without user input via WebView settings.

    webview.settings.mediaPlaybackRequiresUserGesture = false</string></string>