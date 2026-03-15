# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/ios-webview-support.md

# WebView Support

## Overview

WebViews are components that embed web content within native mobile applications. The Luciq SDK can automatically detect and monitor WebViews in your iOS app.

This feature is available from SDK v**19.2.0**.

When enabled, WebView support allows you to:

* Report **WebView screen loading times** in APM \[already existing]
* Capture **user interactions** inside WebViews (tap, scroll, navigation) \[NEW]
* Log **network requests** (Fetch/XHR) triggered by WebViews \[NEW]

This helps you get full visibility into hybrid app experiences where native and WebView content are combined.

## WebView Data Enrichment

Enabling WebView detection enhances multiple Luciq products:

### WebViews in APM

WebView loading times are reported alongside native screen loading metrics. This helps you measure and optimize performance across both native and web-based content.

### WebViews in Bug Reporting, Crash Reporting, and Session Replay

* **User interactions** inside WebViews are captured (navigation, swipe, tap, scroll)
* **Network logs** from requests made inside WebViews (Fetch/XHR) are automatically captured
* Both appear in the logs section; user interactions also appear in Repro Steps

## Setup

### Enabling WebViews Tracking

To report WebViews screen loading in APM, ensure `webViewsTrackingEnabled` is set to `true`. See [WebViews Screen Loading for iOS](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-loading/webviews-screen-loading) for APM configuration details.

### Master WebView Tracking API

The Master API controls all WebView data collection, including:

* User interactions
* Network logs
* Screen loading in APM

By default, the Master API is **enabled**. To disable all WebView tracking:

**Swift**

```swift
Luciq.webViewMonitoringEnabled = false
```

**Objective-C**

```objective-c
Luciq.webViewMonitoringEnabled = NO;
```

### User Interactions & Network Logs

By default, user interactions and network logs inside WebViews are **disabled**. Enable them at runtime:

**Swift**

```swift
// User interactions
Luciq.webViewUserInteractionsTrackingEnabled = true

// Network logs
Luciq.webViewNetworkTrackingEnabled = true
```

**Objective-C**

```objective-c
// User interactions
Luciq.webViewUserInteractionsTrackingEnabled = YES;

// Network logs
Luciq.webViewNetworkTrackingEnabled = YES;
```

### Screenshot Masking in WebViews

By default, **all WebViews are masked** in screenshots to protect potentially sensitive content.

To unmask WebViews:

**Swift**

```swift
Luciq.setAutoMaskScreenshotsTypes(.maskNothing)
```

**Objective-C**

```objective-c
[Luciq setAutoMaskScreenshotsTypes:IBGAutoMaskScreenshotOptionMaskNothing];
```

If you already use `setAutoMaskScreenshotsTypes()`, WebViews will **not** be masked by default. To mask them explicitly, include the WebViews option:

**Swift**

```swift
Luciq.setAutoMaskScreenshotsTypes([.webViews, .labels])
```

**Objective-C**

```objective-c
[Luciq setAutoMaskScreenshotsTypes:IBGAutoMaskScreenshotOptionWebViews | IBGAutoMaskScreenshotOptionLabels];
```

## API Summary

| API                                      | Purpose                                | Default |
| ---------------------------------------- | -------------------------------------- | ------- |
| `webViewMonitoringEnabled`               | Master switch for all WebView tracking | `true`  |
| `webViewUserInteractionsTrackingEnabled` | Capture user interactions in WebViews  | `false` |
| `webViewNetworkTrackingEnabled`          | Capture network logs from WebViews     | `false` |

> **Note:** If `webViewMonitoringEnabled` is disabled, all other WebView APIs will have no effect.

## Requirements

* Luciq SDK version v19.2.0 or later
* Only `WKWebView` is supported

## Related Reading

* [WebViews Screen Loading for iOS](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-loading/webviews-screen-loading) - APM-specific WebView metrics
