---
---
title: Features
description: "Learn about the features of Sentry's Android SDK."
---

Sentry's Android SDK enables automatic reporting of errors and exceptions, and identifies performance issues in your application. The below, is a list of features that are available as part of this SDK.

We released Performance-V2,
a set of experimental features to give you more details about app start performance and frame delay on a span level.

We released Source Context, which shows snippets of code around the location of stack frames.

Let us know if you have feedback by filing a GitHub issue.

- Native Development Kit (NDK), the set of tools that allows you to use C and C++ with Android.
- Events enriched with device data.
- Offline caching. (If a device is offline, we'll send a report once the application has been restarted.)
- Automatic breadcrumbs for:
  - Android activity lifecycle events.
  - Application lifecycle events.
  - System events such as: low battery, low storage space, airplane mode started, shutdown, changes of the configuration, and so forth.
  - Application component callbacks.
  - User Interactions such as: view click, scroll, swipe, and so on.
  - Android fragment lifecycle events.
  - OkHttp requests.
  - Apollo requests.
  - Timber logs.
  - Navigation destination changes.
- Release health, tracking crash-free users and sessions.
- Attachments that can enrich your event by storing additional files, such as config or log files.
- User Feedback, providing the ability to collect user information when an event occurs.
- Tracing that can track:
    - Android activity transactions.
    - User interaction transactions such as: view click, scroll, swipe, and so on.
    - Navigation transactions.
    - Android fragment spans.
    - Cold and warm app starts.
    - Slow and frozen frames.
    - OkHttp request spans.
    - SQLite and Room query spans.
    - File I/O spans.
    - Apollo request spans.
    - Distributed tracing through OkHttp and Apollo integrations.
- Application Not Responding (ANR), reported if the application is blocked for more than five seconds.
- HTTP Client Errors.
- Screenshot attachments for errors.
- View Hierarchy attachments for errors.
- Code samples provided in both Kotlin and Java (since the Android SDK uses both languages).
- A sample application for our Android users.
