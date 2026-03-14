# Source: https://docs.logrocket.com/reference/webviews-on-android.md

# Capturing Web Views

Display the contents of a WebView in Android recordings

<HTMLBlock>
  {`
  If your Android app uses a
  <a href="https://developer.android.com/reference/android/webkit/WebView" target="_blank">web view</a>
  to render content from a URL, the view’s contents will be included in the mobile session playback
  as long as the following is true:
  `}
</HTMLBlock>

* The app is on version 1.18.0 or higher of the mobile SDK
* The Android SDK has been initialized in the mobile app ([see docs](https://docs.logrocket.com/reference/android))
* The Web SDK is initialized in the rendered web page, using the same app ID as the surrounding mobile session ([see docs](https://docs.logrocket.com/reference/init))
* The WebView has JavaScript enabled. Our Web SDK requires JavaScript to function and communicate with the Android SDK.
* The WebView has been attached to the LogRocket SDK using the registerWebView function:

```java
/** example: */

final WebView myWebView = rootView.findViewById(R.id.webview);
myWebView.getSettings().setJavaScriptEnabled(true);
SDK.registerWebView(myWebView);
```

```kotlin
/** example: */

val myWebView: WebView = rootView.findViewById(R.id.webview);
SDK.registerWebView(myWebView);
```

The events we record for web sessions (clicks, site navigation, etc.) will appear alongside mobile events in session playback. The linked recordings will only count as a single session against your quota.