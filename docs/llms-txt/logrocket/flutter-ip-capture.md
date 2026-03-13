# Source: https://docs.logrocket.com/reference/flutter-ip-capture.md

# Enable and Disable IP Capture (Flutter)

Flutter app IP capture configuration

## Disable IP Address capture

LogRocket captures IP addresses to enable reverse-IP lookups for location search, and to help you match between back-end logs and captured sessions.

By default, this IP capture is enabled. If you'd like LogRocket to not store IP addresses, add `ipCaptureEnabled: false` to your configuration:

```dart Flutter
LogRocketInitConfiguration(
  appID: '<APP_SLUG>',
  ipCaptureEnabled: false,
)
```