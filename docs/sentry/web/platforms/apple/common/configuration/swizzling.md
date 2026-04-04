---
---
title: Swizzling
description: "Learn which features use swizzling"
---

The Cocoa SDK uses [swizzling](https://nshipster.com/method-swizzling/) to provide some features out of the box without boilerplate code. The following features use swizzling:

**macOS**

- Breadcrumbs for touch events
- Auto instrumentation for HTTP requests
- Auto instrumentation for File I/O operations
- Auto instrumentation for Core Data operations
- Automatically added sentry-trace header to HTTP requests for distributed tracing
- HTTP Client Errors

**iOS, tvOS and Catalyst**

- Breadcrumbs for touch events and navigation with UIViewControllers
- Auto instrumentation for UIViewControllers
- Auto instrumentation for HTTP requests
- Auto instrumentation for File I/O operations
- Auto instrumentation for Core Data operations
- Automatically added sentry-trace header to HTTP requests for distributed tracing
- User interaction transactions for UI clicks
- HTTP Client Errors

Since Cocoa 7.5.0, you can opt out of swizzling using options. When you disable swizzling, the SDK disables the features above:

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.dsn = "___PUBLIC_DSN___"
    options.enableSwizzling = false
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.dsn = @"___PUBLIC_DSN___";
    options.enableSwizzling = NO;
}];
```

## Deactivate Swizzling for Specific Classes

To deactivate swizzling for specific classes, you can use the option `swizzleClassNameExcludes`, which is available with Sentry Cocoa SDK version `8.23.0` and above. The SDK checks if the name of a class it intends to swizzle contains any class name configured using this option. For example, if you add `MyUIViewController` to this list, the Sentry Cocoa SDK excludes the following classes from swizzling:

- `YourApp.MyUIViewController`
- `YourApp.MyUIViewControllerA`
- `MyApp.MyUIViewController`

```swift {tabTitle:Swift}
import Sentry

SentrySDK.start { options in
    options.swizzleClassNameExcludes = [
      "MyUIViewController",
    ]
}
```

```objc {tabTitle:Objective-C}
@import Sentry;

[SentrySDK startWithConfigureOptions:^(SentryOptions *options) {
    options.swizzleClassNameExcludes = [NSSet setWithObjects:
      @"MyUIViewController",
      nil
    ];
}];
```
