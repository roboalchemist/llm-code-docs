---
---
title: Features
description: "Learn about the features of Sentry's Flutter SDK."
---

Sentry's Flutter SDK enables automatic reporting of errors and exceptions, and identifies performance issues in your application. The below, is a list of features that are available as part of this SDK.

**Features:**

- Under the hood the SDK relies on Sentry's Dart SDK:
    - You need at least Dart `3.5.0` and Flutter `3.24.0`.
    - This SDK includes all the Features of Sentry's Dart SDK.
- Automatic native crash error tracking (using both Android and iOS), including:
    - Java, Kotlin, C, and C++ code for Android.
    - ObjC, Swift, and C for iOS.
- Automatic detection of Application Not Responding (ANR) on Android and App Hangs on iOS.
- Offline storage of events.
- Events enriched with device data.
- Breadcrumbs automatically captured:
    - by the Flutter SDK.
    - via the Native SDKs Automatic Breadcrumbs for Android and Automatic Breadcrumbs for iOS.
    - as well as `http` with the Dart SDK.
- Integrations for sqflite, routing and more. For a complete list, see integrations.
- Release Health tracks crash free users and sessions.
- Attachments that can enrich your event by storing additional files, such as config or log files.
- Tracing that can track:
  - App start time.
  - Time to Initial Display and Time to Full Display.
  - Slow and Frozen Frames.
  - User Interaction which include clicks, long clicks, taps and so on.
  - For a complete list see automatic instrumentations.
- User Feedback, providing the ability to collect user feedback when an unexpected event occurs.
- Screenshot and View Hierarchy attachments for errors.
- Profiling collects detailed information about your code at the function level.
  - Profiling is currently supported on **iOS** and **macOS**.
  - It captures profiles across multiple language layers, including native languages (such as Swift and Objective-C) as well as Dart.
- Source Context shows snippets of code around the location of stack frames.
- Sentry Dart Plugin makes uploading debug symbols easy and automatic.

**Web Limitations:**

Sentry supports Flutter Web as well, with the following limitations:

- Issue titles are not human-readable, as they show the minified name.
- Stack traces aren't symbolicated when compiled using WebAssembly (WASM).
- Stack traces are not symbolicated when loaded as a browser extension.
- Offline caching isn't supported for exceptions.

**Desktop Limitations:**

Sentry supports Flutter on Linux and Windows as well, with the following limitations:

- Native crashes are not supported on Windows.
- [Release Health](/product/releases/health/) isn't supported.

When running on macOS, you can expect the same feature set as on iOS.

