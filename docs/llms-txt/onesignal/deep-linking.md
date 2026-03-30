# Source: https://documentation.onesignal.com/docs/en/deep-linking.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deep Linking

> Set up deep linking to route users from push notifications, emails, and in-app messages to specific screens in your Android or iOS app using Universal Links, App Links, or custom URI schemes.

## Overview

Deep linking routes users to a specific screen in your app when they tap a link — whether from an email, SMS, website, push notification, or in-app message. If the app is not installed, the operating system can redirect users to the app store or a fallback web page.

This guide covers:

* **Types of deep links** and when to use each
* **Platform setup** for Android and iOS
* **Handling deep links** in your app with the OneSignal SDK
* **Channel-specific behavior** for push, email, and in-app messages

<Info>
  For general URL and link configuration (Launch URLs, UTM parameters, dynamic URLs, link tracking), see [URLs, links, & deep links](./links).
</Info>

***

## Prerequisites

Before setting up deep links, you need:

* A [OneSignal account](https://dashboard.onesignal.com) with an app configured
* The [OneSignal SDK](./mobile-sdk-setup) installed in your mobile app
* A domain you control, hosted over **HTTPS**, for Universal Links or App Links
* Access to your app's source code and build configuration (Xcode for iOS, Android Studio for Android)

***

## Types of deep links

There are three common deep linking mechanisms. Each has different behavior depending on whether the app is installed.

| Type                   | Platform      | Format                        | App not installed                |
| ---------------------- | ------------- | ----------------------------- | -------------------------------- |
| **Universal Links**    | iOS 9+        | `https://yourdomain.com/path` | Opens the URL in Safari          |
| **App Links**          | Android 6.0+  | `https://yourdomain.com/path` | Opens the URL in the browser     |
| **Custom URI schemes** | iOS & Android | `myapp://path`                | Fails silently or shows an error |

**Recommendation:** Use Universal Links (iOS) and App Links (Android) for the most reliable experience. These use standard `https://` URLs, work across channels (push, email, SMS), and provide fallback behavior when the app is not installed. Custom URI schemes (`myapp://`) are simpler to set up but do not provide fallback behavior and may not work in all contexts (e.g., email clients).

<Warning>
  Universal Links and App Links require hosting a verification file on your domain. Without this file, the OS treats the link as a regular web URL.
</Warning>

***

## Android setup (App Links)

Use Android Studio's [App Links Assistant](https://developer.android.com/training/app-links) to generate the required configuration.

### Configure intent filters

Add an intent filter to the Activity that should handle the deep link:

```xml  theme={null}
<activity android:name=".DeepLinkActivity" android:exported="true">
  <intent-filter android:autoVerify="true">
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="https" android:host="yourdomain.com" />
  </intent-filter>
</activity>
```

### Handle the incoming intent

```java  theme={null}
Intent appLinkIntent = getIntent();
String appLinkAction = appLinkIntent.getAction();
Uri appLinkData = appLinkIntent.getData();
```

### Host the Digital Asset Links file

Generate the `assetlinks.json` file using Android Studio's App Links Assistant and host it at:

```
https://yourdomain.com/.well-known/assetlinks.json
```

See Google's [Verify App Links](https://developer.android.com/training/app-links/verify-android-applinks) documentation for the full file format and verification steps.

***

## iOS setup (Universal Links)

Apple [Universal Links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) open your app when a user taps a matching `https://` URL. For simpler use cases where the app is guaranteed to be installed, you can use [URL Schemes](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app) instead.

### Enable Associated Domains

1. In Xcode, select your target → **Signing & Capabilities** → add **Associated Domains**
2. Add your domain: `applinks:yourdomain.com`

### Handle the Universal Link in your app

<CodeGroup>
  ```swift Swift theme={null}
  func application(_ application: UIApplication,
                   continue userActivity: NSUserActivity,
                   restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
          let url = userActivity.webpageURL else {
      return false
    }
    // Route to the correct screen based on the URL path
    return true
  }
  ```

  ```objectivec Objective-C theme={null}
  - (BOOL)application:(UIApplication *)application
      continueUserActivity:(NSUserActivity *)userActivity
      restorationHandler:(void (^)(NSArray *))restorationHandler {
    if ([userActivity.activityType isEqualToString:NSUserActivityTypeBrowsingWeb]) {
      NSURL *url = userActivity.webpageURL;
      // Route to the correct screen based on the URL path
      return YES;
    }
    return NO;
  }
  ```

</CodeGroup>

### Host the Apple App Site Association file

Create an `apple-app-site-association` (AASA) file and host it at:

```
https://yourdomain.com/.well-known/apple-app-site-association
```

Replace `TEAMID` with your Apple Team ID and `com.example.app` with your bundle identifier:

```json  theme={null}
{
  "applinks": {
    "apps": [],
    "details": [{
      "appID": "TEAMID.com.example.app",
      "paths": ["/path/*", "/another-path"]
    }]
  }
}
```

See Apple's [Supporting Associated Domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) documentation for the full specification.

### iOS Launch URL behavior

OneSignal's iOS SDK uses `openURL` to handle the Launch URL (`url` property). This causes the link to open in the browser first, then redirect back into the app — which can be a poor user experience.

To avoid this, use one of these approaches:

1. **Use `data` instead of `url`** in the API payload and handle the deep link in your [Push Notification Click Listener](./mobile-sdk-reference#addclicklistener-push)
2. **Suppress Launch URLs** by adding `OneSignal_suppress_launch_urls` to your `Info.plist` as a Boolean with value `YES`, then handle all navigation in the click listener

<Tip>
  Approach 1 (using `data` + click listener) is recommended because it gives you full control over navigation without relying on the OS to resolve the URL.
</Tip>

***

## Handle deep links with the OneSignal SDK

The most reliable way to handle deep links from OneSignal messages is to use the SDK's click listeners rather than relying on OS-level link resolution. This gives you full control over navigation in your app.

### Push notification click listener

Use `addClickListener` to intercept notification clicks and route the user based on the deep link URL or additional data:

<CodeGroup>
  ```kotlin Kotlin theme={null}
  OneSignal.Notifications.addClickListener { event ->
    val url = event.notification.launchURL
    val data = event.notification.additionalData
    // Route to the correct screen based on url or data
  }
  ```

  ```swift Swift theme={null}
  class AppDelegate: UIResponder, UIApplicationDelegate, OSNotificationClickListener {
    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
      OneSignal.Notifications.addClickListener(self)
      return true
    }

    func onClick(event: OSNotificationClickEvent) {
      let url = event.notification.launchURL
      let data = event.notification.additionalData
      // Route to the correct screen based on url or data
    }
  }
  ```

  ```javascript React Native theme={null}
  OneSignal.Notifications.addEventListener('click', (event) => {
    const url = event.notification.launchURL;
    const data = event.notification.additionalData;
    // Route to the correct screen based on url or data
  });
  ```

  ```dart Flutter theme={null}
  OneSignal.Notifications.addClickListener((event) {
    final url = event.notification.launchUrl;
    final data = event.notification.additionalData;
    // Route to the correct screen based on url or data
  });
  ```

  ```csharp Unity (C#) theme={null}
  OneSignal.Notifications.Clicked += (sender, e) => {
    var url = e.Notification.LaunchURL;
    var data = e.Notification.AdditionalData;
    // Route to the correct screen based on url or data
  };
  ```

</CodeGroup>

For the full API reference including Java, Objective-C, and Cordova/Ionic, see [`addClickListener()` Push](./mobile-sdk-reference#addclicklistener-push).

### In-app message click listener

Use the in-app message click listener to handle deep links from in-app message buttons and actions:

<CodeGroup>
  ```kotlin Kotlin theme={null}
  OneSignal.InAppMessages.addClickListener { event ->
    val actionId = event.result.actionId
    // Route based on the action ID (your deep link URI)
  }
  ```

  ```swift Swift theme={null}
  func onClick(event: OSInAppMessageClickEvent) {
    let actionId = event.result.actionId
    // Route based on the action ID (your deep link URI)
  }
  ```

  ```javascript React Native theme={null}
  OneSignal.InAppMessages.addEventListener('click', (event) => {
    const actionId = event.result.actionId;
    // Route based on the action ID (your deep link URI)
  });
  ```

  ```dart Flutter theme={null}
  OneSignal.InAppMessages.addClickListener((event) {
    final actionId = event.result.actionId;
    // Route based on the action ID (your deep link URI)
  });
  ```

</CodeGroup>

For the full API reference, see [`addClickListener()` In-App](./mobile-sdk-reference#addclicklistener-in-app).

***

## Push notifications

Include the deep link in one of two ways:

| Method                            | API property                         | Behavior                                                                           |
| --------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------- |
| **Launch URL**                    | `url` (or `app_url` for mobile-only) | OS opens the URL directly. On iOS, this opens the browser first unless suppressed. |
| **Additional Data** (recommended) | `data`                               | URL is passed to your click listener. You control navigation entirely.             |

### Platform behavior

* **Android**: Opens the matching Activity directly via App Links
* **iOS**: Opens Safari, then the app (unless you [suppress Launch URLs](#ios-launch-url-behavior) and handle navigation in the click listener)

See [URLs, links, & deep links](./links) for details on `url`, `web_url`, and `app_url` targeting.

***

## Emails

By default, OneSignal rewrites email links for click tracking. This changes the URL, which breaks deep linking because the OS no longer recognizes the domain as matching your app's Associated Domain.

### Enable deep links in email

To preserve deep links, disable click tracking using one of these methods:

* **Dashboard**: Uncheck **Track link clicks** in the email editor
* **API**: Set `disable_email_click_tracking: true`
* **Per-link**: Use the Liquid filter `{{ 'https://yourdomain.com/path' | do_not_track_link }}` to disable tracking on individual links while keeping it enabled for others

<Frame caption="Track link clicks disabled in the email editor.">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/787e21d-Screenshot_2024-05-29_at_2.21.43_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=f7e1079f4860ecf34fd95375a4332573" width="1756" height="492" data-path="images/docs/787e21d-Screenshot_2024-05-29_at_2.21.43_PM.png" />
</Frame>

<Warning>
  Disabling click tracking means you lose click metrics in [Email Reports](./email-message-reports). Consider using per-link tracking exclusions to preserve analytics on non-deep-link URLs.
</Warning>

### Email deep link behavior

| Scenario                                          | Result                               |
| ------------------------------------------------- | ------------------------------------ |
| iOS + Safari + Universal Link + Tracking disabled | Opens app directly                   |
| iOS + Safari + Universal Link + Tracking enabled  | Opens Safari, prompts to open app    |
| iOS + non-Safari mail client + Universal Link     | Opens App Store if app not installed |
| Android + App Link + Tracking disabled            | Opens app directly                   |
| Android + App Link + Tracking enabled             | Opens browser first, then app        |

***

## In-app messages

Deep links in in-app messages use the click listener pattern. You set a custom action identifier in the message editor, then handle it in your app code.

### Drag-and-drop editor

1. Add a button or clickable element
2. Set the click action to [Custom Action ID](./iam-click-actions#custom-action-id)
3. Enter your deep link URI as the **Action Name** (e.g., `https://yourdomain.com/promo` or `myapp://promo`)

### HTML editor

Use the [`openUrl`](./in-app-message-api#click-name) method in the In-App JS Library to trigger deep links from custom HTML.

### Handle the click

Use the [in-app message click listener](#in-app-message-click-listener) to intercept the action and navigate the user in your app.

***

## Testing deep links

### Android

Use `adb` to test App Links without sending a notification:

```bash  theme={null}
adb shell am start -a android.intent.action.VIEW \
  -d "https://yourdomain.com/path" \
  com.your.package
```

Verify your `assetlinks.json` is reachable:

```bash  theme={null}
curl -I https://yourdomain.com/.well-known/assetlinks.json
```

### iOS

Use Apple's [Associated Domains validation tool](https://search.developer.apple.com/appsearch-validation-tool/) to verify your AASA file. You can also test Universal Links by:

1. Pasting the link in the Notes app
2. Long-pressing the link to confirm the "Open in \[App]" option appears
3. Tapping the link to verify it opens your app

<Note>
  Universal Links do not work when typed directly into Safari's address bar — they must be tapped from another app (Notes, Mail, Messages, etc.).
</Note>

### OneSignal test messages

1. Send a test push from the OneSignal dashboard with a deep link URL as the Launch URL or in Additional Data
2. Verify the notification opens the correct screen in your app
3. Check your click listener logs to confirm the URL or data was received

***

## Troubleshooting

### iOS deep link opens Safari instead of the app

This is the most common issue. Possible causes:

* **AASA file not hosted correctly** — Verify it's at `https://yourdomain.com/.well-known/apple-app-site-association` with `Content-Type: application/json` and no redirects
* **Associated Domains not configured** — Check Xcode → Signing & Capabilities → Associated Domains includes `applinks:yourdomain.com`
* **Launch URL behavior** — OneSignal's iOS SDK uses `openURL` for the `url` property, which triggers browser-first behavior. Use `data` + click listener or [suppress Launch URLs](#ios-launch-url-behavior) instead
* **Testing in Safari** — Universal Links don't activate from the Safari address bar. Test from Notes, Mail, or another app.

### Android deep link opens the browser

* **`autoVerify` missing** — Ensure your intent filter includes `android:autoVerify="true"`
* **`assetlinks.json` not found** — Verify the file is at `https://yourdomain.com/.well-known/assetlinks.json` and returns HTTP 200
* **SHA256 fingerprint mismatch** — The fingerprint in `assetlinks.json` must match your app's signing certificate. Debug and release builds use different certificates.

### Deep link works in push but not email

Email click tracking rewrites URLs, breaking domain verification. [Disable click tracking](#enable-deep-links-in-email) for emails that contain deep links.

### Deep link received but app doesn't navigate

* Verify your click listener is registered early in the app lifecycle (e.g., in `Application.onCreate()` or `AppDelegate.didFinishLaunchingWithOptions`)
* Check that the URL or action ID matches what your routing logic expects
* On iOS, confirm you're not relying on `url` without suppressing Launch URLs — the browser may consume the link before your listener fires

***

## FAQ

### What happens if the app is not installed?

With Universal Links (iOS), the URL opens in Safari as a regular web page. With App Links (Android), the URL opens in the default browser. In both cases, you can configure your web page to redirect to the appropriate app store. Custom URI schemes (`myapp://`) fail silently or show an error if the app is not installed.

### Should I use Launch URL or Additional Data for deep linking?

Additional Data (`data`) is recommended for mobile deep links because it gives you full control over navigation via the click listener. Launch URL (`url`) is simpler but has limitations on iOS (browser redirect) and does not allow custom routing logic.

### Can I personalize deep links with user data?

Yes. Use [Dynamic URLs](./links#dynamic-urls) with Liquid syntax to inject user properties, tags, or custom data into your deep link URLs. For example: `https://yourdomain.com/profile/{{subscription.external_id}}`.

### Can I use deep links with custom URI schemes?

Yes. Set your custom scheme (e.g., `myapp://screen`) as the Launch URL or Additional Data value. Custom schemes work well for push and in-app messages but may not work in email clients. They also provide no fallback if the app is not installed.

### Do deep links work with OneSignal Journeys?

Yes. When configuring a message step in a Journey, set the Launch URL or Additional Data to your deep link. The behavior is the same as a standalone push or in-app message.

***

<Columns cols={2}>
  <Card title="URLs, links, & deep links" icon="link" href="./links">
    Launch URLs, UTM parameters, dynamic URLs, and link tracking configuration.
  </Card>

  <Card title="Mobile SDK reference" icon="code" href="./mobile-sdk-reference">
    Full API reference for click listeners and notification event handling.
  </Card>

  <Card title="In-App Click Actions" icon="hand-pointer" href="./iam-click-actions">
    Configure click actions for in-app message buttons and elements.
  </Card>

  <Card title="Mobile push setup" icon="mobile" href="./mobile-push-setup">
    Platform-specific push notification setup for Android and iOS.
  </Card>
</Columns>

Built with [Mintlify](https://mintlify.com).
