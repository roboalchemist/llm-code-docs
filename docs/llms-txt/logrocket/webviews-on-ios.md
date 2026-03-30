# Source: https://docs.logrocket.com/reference/webviews-on-ios.md

# Capturing Web Views

Display the contents of a WKWebView in iOS recordings

<HTMLBlock>
  {`
  If your iOS app uses a
  <a href="https://developer.apple.com/documentation/webkit/wkwebview" target="_blank">WebView</a>
  to render content from a URL, the view’s contents will be included in the mobile session
  playback as long as the following is true:
  `}
</HTMLBlock>

* The app is on version 1.18.0 or higher of the iOS SDK
* The iOS SDK has been initialized in the mobile app ([see docs](https://docs.logrocket.com/reference/ios))
* The web SDK is initialized in the rendered web page, using the same app ID as the surrounding mobile session ([see docs](https://docs.logrocket.com/reference/init))

The events we record for web sessions (clicks, site navigation, etc.) will appear alongside mobile events in session playback. The linked recordings will only count as a single session against your quota.