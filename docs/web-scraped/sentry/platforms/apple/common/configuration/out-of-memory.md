---
---
title: Out Of Memory
description: "Learn how to turn off Out Of Memory tracking"
---

We renamed this integration to watchdog terminations in the 8.0.0 release. The out of memory integration and the watchdog terminations integration are the same thing. The only difference is the name.

If you'd like to opt out of this feature, you can do so using options:

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.enableOutOfMemoryTracking = false
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.enableOutOfMemoryTracking = NO;
}];
```
