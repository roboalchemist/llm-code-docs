---
---
title: Features
description: "Here's a list of Sentry's Apple SDK features."
---

Sentry's Apple SDK enables automatic reporting of errors and exceptions, and identifies performance issues in your application.

The SDK builds a crash report that persists to disk. While it attempts to send the report right after the crash, it may not always work because the environment may be unstable at the time of the crash. If this is the case, the report will be sent upon application start.

**Features:**

- Multiple types of errors are captured, including:
  - Mach exceptions
  - Fatal signals
  - Unhandled exceptions
  - C++ exceptions
  - Objective-C exceptions
  - Error messages of fatalError, assert, and precondition
  - App Hang Detection
  -  Watchdog Terminations
  - HTTP Client Errors
  - Start-up crashes. The SDK init waits synchronously for up to 5 seconds to flush out events if the app crashes within 2 seconds after the SDK init.
- Events enriched with device data
- Offline caching when a device is unable to connect; we send a report once we receive another event
- Breadcrumbs automatically captured for
  - Application lifecycle events (`didBecomeActive`, `didEnterBackground`, `viewDidAppear`)
  - Touch events
  - System events (battery level or state changed, memory warnings, device orientation changed, keyboard did show and did hide, screenshot taken, time zone changed or significant time change)
  - Outgoing HTTP requests
- Release health tracks crash free users and sessions
- Automatic Performance Tracking
  - Rendering of UIViewControllers
  - Performance of HTTP requests
  - Distributed tracing
  - Insights for Mobile Vitals
    - Cold and warm start
    - Slow and frozen frames
    - Prewarmed App Start Tracing
  - Performance of File I/O operations
  - Performance of Core Data queries
  - User Interaction transactions for UI clicks
- Attachments enrich your event by storing additional files, such as config or log files
- User Feedback provides the ability to collect user information when an event occurs

- [View Hierarchy](/platforms/apple/guides/ios/enriching-events/viewhierarchy/) and [Screenshot](/platforms/apple/guides/ios/enriching-events/screenshots/) attachments for errors
- Source Context shows snippets of code around the location of stack frames
- MetricKit integration
