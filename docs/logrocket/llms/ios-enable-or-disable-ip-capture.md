# Source: https://docs.logrocket.com/reference/ios-enable-or-disable-ip-capture.md

# Enable or Disable IP Capture

LogRocket captures IP addresses to enable reverse-IP lookups for location search, and to help you match between back-end logs and captured sessions.

If you'd like LogRocket to not store IP addresses, set this value to false:

```swift
SDK.initialize(configuration: Configuration(
  appID: "<APP_SLUG>",
  ipCaptureEnabled: true,
))
```

```objectivec
LROConfiguration *configuration = [[LROConfiguration alloc] initWithAppID:@"<APP_ID>"];
configuration.ipCaptureEnabled = YES;
[LROSDK initializeWithConfiguration:configuration];
```