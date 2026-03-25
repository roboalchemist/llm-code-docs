# Source: https://docs.logrocket.com/reference/enabling-bidirectional-text-rendering.md

# Enabling Bidirectional Text Rendering

If your iOS Application contains bidirectional text we currently require a configuration flag to correctly capture and render this text.

```swift Swift
SDK.initialize(configuration: Configuration(
  appID: "<APP_SLUG>",
  experimentalBidiCapture: true,
))
```

```objectivec Objective-C
LROConfiguration *configuration = [[LROConfiguration alloc] initWithAppID:@"<APP_ID>"];
configuration.experimentalBidiCapture = YES;
[LROSDK initializeWithConfiguration:configuration];
```