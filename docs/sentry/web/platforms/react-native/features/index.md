---
---
title: Features
description: "Learn about the features of Sentry's React Native SDK."
---

Sentry's React Native SDK enables automatic reporting of errors and exceptions, and identifies performance issues in your application. The below, is a list of features that are available as part of this SDK.

- Automatic Native Crash Error Tracking (using both `sentry-cocoa` & `sentry-android`).
- Automatic detection of Application Not Responding (ANR) on Android and App Hangs on iOS.
- Offline storage of events:
  - Android: Offline caching when a device is offline; we send a report once the application is restarted.
  - iOS: Offline caching when a device is unable to connect; we send a report once we receive another event.
- Events enriched with device data.
- Source Context shows snippets of your code around the location of stack frames.
- Autolinking.
- Breadcrumbs created for outgoing `http` request with XHR and Fetch; UI and system events; and console logs.
- Release health tracks crash free users and sessions.
- Tracing creates transactions automatically for:
  - App Start time.
  - Routing Instrumentation (React Navigation v4 and above and React Native Navigation).
  - XHR and Fetch requests.
  - User Interaction events (touch, gesture).
  - Slow and Frozen frames tracking.
  - Stall Tracking of the JavaScript loop.
  - React Profiler tracks React components.
- Under the hood the SDK relies on our JavaScript SDK, which makes all functions available for JavaScript also available in this SDK.
- On Device symbolication for JavaScript (in Debug).
- RAM bundle support.
- Hermes support.
- Expo support out of the box.
- Attachments enrich your event by storing additional files, such as config or log files.
- User Feedback provides the ability to collect user information when an event occurs.
- View Hierarchy shows the structure of native components at the time an error occurred.
