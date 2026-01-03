---
---
title: Experimental features
description: "Learn about the experimental features available for Sentry's Apple SDK."
---

  Experimental features are still a work-in-progress and may have bugs. We
  recognize the irony.

Do you want to try some new experimental features? On the latest version of the Apple SDK, you can:

- Enable App Launch Profiling to get detailed profiles for your app launches.
- Enable Continuous Profiling to get full coverage of your app's execution.

- Enable AppHangsV2 to get more detailed app hangs. This differentiates between fully-blocking and non-fully-blocking app hangs, and also tells you the duration of app hangs.

- If you use Swift concurrency, stitch together stack traces of your async code with the `swiftAsyncStacktraces` option. Note that you can enable this in your Objective-C project, but only async code written in Swift will be stitched together.
- Enable the `enablePersistingTracesWhenCrashing` option to link ongoing transactions to a crash event when your app crashes.
- Enable the `enableUnhandledCPPExceptionsV2` option to capture fatal CPPExceptions via hooking into `cxa_throw`

Let us know if you have feedback through [GitHub issues](https://github.com/getsentry/sentry-cocoa/issues).
