# Source: https://docs.datadoghq.com/error_tracking/frontend/mobile/kotlin-multiplatform.md

---
title: Kotlin Multiplatform Crash Reporting and Error Tracking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Error Tracking > Frontend Error Tracking > Mobile Crash Reporting >
  Kotlin Multiplatform Crash Reporting and Error Tracking
---

# Kotlin Multiplatform Crash Reporting and Error Tracking

## Overview{% #overview %}

Error Tracking processes errors collected from the Kotlin Multiplatform SDK.

Enable Kotlin Multiplatform Crash Reporting and Error Tracking to get comprehensive crash reports and error trends. With this feature, you can access:

- Aggregated Kotlin Multiplatform crash dashboards and attributes
- Deobfuscated Kotlin Multiplatform (iOS and Android) crash reports
- Trend analysis with Kotlin Multiplatform error tracking

Your crash reports appear in [**Error Tracking**](https://app.datadoghq.com/rum/error-tracking).

## Setup{% #setup %}

If you have not set up the Kotlin Multiplatform SDK yet, follow the [in-app setup instructions](https://app.datadoghq.com/rum/application/create) or see the [Kotlin Multiplatform setup documentation](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/kotlin_multiplatform/setup).

For any given error, you can access the file path, line number, and a code snippet for each frame of the related stack trace.

### Android{% #android %}

All uncaught exceptions and ANRs resulting in a crash are reported by the Kotlin Multiplatform SDK (see limitations). On top of these crashes, you can configure the SDK to report NDK crashes, and control the reporting of non-fatal ANRs.

#### Add NDK crash reporting{% #add-ndk-crash-reporting %}

Your Android application may be running native code (C/C++) for performance or code reusability. To enable NDK crash reporting, use the Datadog NDK library.

1. Add the Gradle dependency to your Android source set by declaring the library as a dependency in your `build.gradle.kts` file:

```kotlin
kotlin {
  sourceSets {
    androidMain.dependencies {
      implementation("com.datadoghq:dd-sdk-android-ndk:x.x.x")
    }
  }
}
```
Enable NDK crash collection after initializing the SDK.
```kotlin
// in Android source set
NdkCrashReports.enable()
```

#### Add ANR reporting{% #add-anr-reporting %}

An "Application Not Responding" ([ANR](https://developer.android.com/topic/performance/vitals/anr)) is an Android-specific type of error that gets triggered when the application is unresponsive for too long.

For any Android version, you can override the default setting for reporting non-fatal ANRs by setting `trackNonFatalAnrs` (available from Android source set only) to `true` or `false` when initializing the SDK.

ANRs are only reported through RUM (not through logs). For more information, see [Android Crash Reporting and Error Tracking - Add ANR Reporting](https://docs.datadoghq.com/real_user_monitoring/error_tracking/mobile/android/#add-anr-reporting).

### iOS{% #ios %}

**Note**: Kotlin 2.0.20 or higher is required if crash tracking is enabled on iOS. Otherwise, due to the compatibility with `PLCrashReporter`, the application may hang if crash tracking is enabled. See other dependencies in the [setup](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/kotlin_multiplatform/setup/#add-native-dependencies-for-ios) instructions.

All uncaught exceptions resulting in a crash are reported by the Kotlin Multiplatform SDK.

#### Add app hang reporting{% #add-app-hang-reporting %}

App hangs are an iOS-specific type of error that happens when the application is unresponsive for too long.

By default, app hangs reporting is **disabled**, but you can enable it and set your own threshold to monitor app hangs that last more than a specified duration by using the `setAppHangThreshold` (available from iOS source set only) initialization method.

App hangs are only reported through RUM (not through logs). For more information, see [iOS Crash Reporting and Error Tracking - Add ANR Reporting](https://docs.datadoghq.com/real_user_monitoring/error_tracking/mobile/ios/#add-app-hang-reporting).

## Get deobfuscated stack traces{% #get-deobfuscated-stack-traces %}

Mapping files are used to deobfuscate stack traces, which helps in debugging errors. Using a unique build ID that gets generated, Datadog automatically matches the correct stack traces with the corresponding mapping files. This ensures that regardless of when the mapping file was uploaded (either during pre-production or production builds), the correct information is available for efficient QA processes when reviewing crashes and errors reported in Datadog.

Use the following guides to see how you can upload mapping files (Android) or dSYMs (iOS) to Datadog: [Android](https://docs.datadoghq.com/real_user_monitoring/error_tracking/mobile/android/#get-deobfuscated-stack-traces), [iOS](https://docs.datadoghq.com/real_user_monitoring/error_tracking/mobile/ios/#get-deobfuscated-stack-traces).

## Limitations{% #limitations %}

### File sizing{% #file-sizing %}

Mapping files are limited in size to **500 MB** each, while dSYM files can go up to **2 GB** each.

### Collection{% #collection %}

The SDK handles crash reporting with the following behaviors:

- The crash can only be detected after the SDK is initialized. Because of this, Datadog recommends that you initialize the SDK as soon as possible in your application.
- RUM crashes must be attached to a RUM view. If a crash occurs before a view is visible, or after the app is sent to the background by the end-user navigating away from it, the crash is muted and isn't reported for collection. To mitigate this, use the `trackBackgroundEvents()` [method](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/kotlin_multiplatform/setup/#track-background-events) in your `RumConfiguration` builder.
- Only crashes that occur in sampled sessions are kept.

## Test your implementation{% #test-your-implementation %}

To verify your Kotlin Multiplatform Crash Reporting and Error Tracking configuration, you need to trigger a crash in your application and confirm that the error appears in Datadog.

To test your implementation:

1. Run your application on an Kotlin Multiplatform emulator or a real device.

1. Execute some code containing an error or crash. For example:

   ```kotlin
   fun onEvent() {
       throw RuntimeException("Crash the app")
   }
   ```

1. After the crash happens, restart your application and wait for the Kotlin Multiplatform SDK to upload the crash report in [**Error Tracking**](https://app.datadoghq.com/rum/error-tracking).

## Further Reading{% #further-reading %}

- [Get started with Error Tracking](https://docs.datadoghq.com/real_user_monitoring/error_tracking/)
- [Visualize Error Tracking data in the Explorer](https://docs.datadoghq.com/real_user_monitoring/error_tracking/explorer)
