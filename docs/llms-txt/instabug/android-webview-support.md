# Source: https://docs.instabug.com/android/set-up-luciq-for-android/android-webview-support.md

# WebView Support

## Overview

WebViews are components that embed web content within native mobile applications. The Luciq SDK can automatically detect and monitor WebViews in your Android app.

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

### Gradle Configuration

To enable WebView tracking, add the following to your `build.gradle` (Groovy) or `build.gradle.kts` (Kotlin DSL):

{% tabs %}
{% tab title="Groovy / Kotlin DSL" %}

```groovy
luciq {
    webViewsTrackingEnabled = true
}
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
This Gradle configuration is **required** for WebView tracking to work. Without it, no WebView tracking code is added to your app.
{% endhint %}

### Master WebView Tracking API

The Master API controls all WebView data collection at runtime, including:

* User interactions
* Network logs
* Screen loading in APM

By default, the Master API is **enabled**. To disable all WebView tracking at runtime:

{% tabs %}
{% tab title="Kotlin" %}

```kotlin
Luciq.setWebViewMonitoringEnabled(false)
```

{% endtab %}

{% tab title="Java" %}

```java
Luciq.setWebViewMonitoringEnabled(false);
```

{% endtab %}
{% endtabs %}

### Relationship Between Gradle Config and Master API

WebView tracking has **two layers of control**:

| Layer                                            | Purpose                                                | When Applied |
| ------------------------------------------------ | ------------------------------------------------------ | ------------ |
| **Gradle Config** (`webViewsTrackingEnabled`)    | Enables/disables including the WebView tracking module | Build time   |
| **Master API** (`setWebViewMonitoringEnabled()`) | Controls whether WebView tracking runs                 | Runtime      |

Both must be enabled for WebView tracking to work:

* Gradle config = adds the feature to your build
* Master API = turns it on or off while the app runs

{% hint style="info" %}
The Master API alone doesn't enable tracking—it only allows these features to work. You still need to explicitly enable each feature (user interactions, network logs) using their respective APIs.
{% endhint %}

### User Interactions & Network Logs

By default, user interactions and network logs inside WebViews are **disabled**. Enable them at runtime:

{% tabs %}
{% tab title="Kotlin" %}

```kotlin
// User interactions
Luciq.setTrackingWebViewUserInteractionsEnabled(true)

// Network logs
Luciq.setWebViewNetworkLogsEnabled(true)
```

{% endtab %}

{% tab title="Java" %}

```java
// User interactions
Luciq.setTrackingWebViewUserInteractionsEnabled(true);

// Network logs
Luciq.setWebViewNetworkLogsEnabled(true);
```

{% endtab %}
{% endtabs %}

### Screenshot Masking in WebViews

By default, **all WebViews are masked** in screenshots to protect potentially sensitive content.

To unmask WebViews:

{% tabs %}
{% tab title="Kotlin / Java" %}

```kotlin
Luciq.setAutoMaskScreenshotsTypes(MaskingType.MASK_NOTHING)
```

{% endtab %}
{% endtabs %}

If you already use `setAutoMaskScreenshotsTypes()`, WebViews will **not** be masked by default. To mask them explicitly, include `MaskingType.WEBVIEWS`:

{% tabs %}
{% tab title="Kotlin / Java" %}

```kotlin
Luciq.setAutoMaskScreenshotsTypes(MaskingType.WEBVIEWS, MaskingType.LABELS)
```

{% endtab %}
{% endtabs %}

## API Summary

| API                                           | Purpose                                           | Default |
| --------------------------------------------- | ------------------------------------------------- | ------- |
| `webViewsTrackingEnabled` (Gradle)            | Include WebView tracking module at build time     | `false` |
| `setWebViewMonitoringEnabled()`               | Master switch for all WebView tracking at runtime | `true`  |
| `setTrackingWebViewUserInteractionsEnabled()` | Capture user interactions in WebViews             | `false` |
| `setWebViewNetworkLogsEnabled()`              | Capture network logs from WebViews                | `false` |

{% hint style="warning" %}
If `setWebViewMonitoringEnabled(false)` is called, all other WebView APIs will have no effect.
{% endhint %}

## Migration from Older Versions

If you are upgrading from a version **before v19.2.0**, update your Gradle configuration:

**Old (Removed)**

```groovy
luciq {
    apm {
        webViewsTrackingEnabled = true
    }
}
```

**New (from v19.2.0)**

```groovy
luciq {
    webViewsTrackingEnabled = true
}
```

## Requirements

* Luciq SDK version v19.2.0 or later
* Only Android's native `WebView` class is supported

## Related Reading

* [WebViews Screen Loading for Android](https://docs.luciq.ai/android/set-up-luciq-for-android/set-up-application-performance-monitoring/set-up-screen-loading/webviews-screen-loading) - APM-specific WebView metrics
