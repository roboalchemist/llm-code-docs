# Source: https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-crash-reporting/capturing-launch-crashes.md

# Capturing Launch Crashes

This page explains how to enable and configure Luciq to capture crashes that occur early in your application's lifecycle on iOS.

## Overview

Persistent crashes that occur on app launch are a very frustrating experience for end-users and a critical blind spot for developers. Normally, if an app crashes early in its lifecycle, the Luciq SDK may not have enough time to send the crash report before the app terminates again.

This feature provides a special mechanism to reliably capture these launch crashes, giving you the visibility you need to diagnose and fix them.

## How It Works

When launch crash capturing is enabled, the SDK detects on the next app run if a crash occurred during the previous launch. If it did, the SDK would briefly pause the app's main thread to synchronously send a lightweight crash report. This pause ensures the report is successfully sent before the app has a chance to crash again, delivering the crash data to your dashboard.

## Enabling the Feature

To enable capturing launch crashes, you must call the following method **before** `Luciq.startWithToken`. This feature is opt-in and disabled by default.

{% hint style="info" %}
This method enables the synchronous sending of launch crashes. You can optionally provide a custom timeout in milliseconds for how long the main thread can be paused.
{% endhint %}

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
// With default timeout of 2000ms
CrashReporting.enableSendingLaunchCrashesSynchronously()

// OR with a custom timeout
CrashReporting.enableSendingLaunchCrashesSynchronously(withTimeout: 3000)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// With default timeout of 2000ms
[LCQCrashReporting enableSendingLaunchCrashesSynchronously];

// OR with a custom timeout
[LCQCrashReporting enableSendingLaunchCrashesSynchronouslyWithTimeout:3000];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**Limitations**

* This method **must** be called before `Luciq.startWithToken`.
* The `timeout` value must be between **1000ms** and **5000ms**. Values outside this range will be ignored, and the **default timeout of 2000ms** will be used instead.
  {% endhint %}

## Configuration

You can configure what the SDK considers a "launch" period by setting the `launchDuration` property. When `enableSendingLaunchCrashesSynchronously` is enabled, any crash that occurs within the defined `launchDuration` will be classified as a launch crash and sent synchronously.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
CrashReporting.launchDuration = 10000 // Duration in milliseconds
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQCrashReporting.launchDuration = 10000; // Duration in milliseconds
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Details**

* **Default Value:** The default launch duration is **5000 milliseconds.**
* **API Timing:** This property **must** be set before `Luciq.startWithToken`.
* **Valid Range:** The set duration must be between **0** and **20,000 milliseconds.**
* Any value outside of this range will be ignored, and **defaulted to 5000 milliseconds.**
  {% endhint %}

## Limitations & Behavior

To ensure launch crash reports are sent as quickly as possible, this feature has some specific behaviors you should be aware of:

* **Essential Diagnostic Data:** To optimize sending time, launch crash reports contain only essential diagnostic data: stack trace, device details, and OS version.
* **Crash Consent Callback:** The `onWillSendCrashReportHandler` is intentionally **skipped** for launch crashes. This is because the main thread is paused, which prevents any UI (like a consent alert) from being displayed.
  * Consent can be skipped in said case since a crash at launch means no user specific data (interactions, screenshots, etc.) has been captured yet.
  * Find more about the consent callback here: [Crash Reporting User Consent for iOS.](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-crash-reporting/crash-reporting-user-consent)
* **Session Replay:** Similarly, Session Replay data is not evaluated nor attached to launch crash reports, to ensure the lightweight payload is sent as fast as possible in the paused window.
