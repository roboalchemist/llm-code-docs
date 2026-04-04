# Source: https://docs.logrocket.com/reference/react-native-disable-ip-capture.md

# Enable or Disable IP Capture (React Native)

Control whether or not a users IP address is sent to LogRocket

## Disable IP Address capture

LogRocket captures IP addresses to enable reverse-IP lookups for location search, and to help you match between back-end logs and captured sessions.

If you'd like LogRocket to not store IP addresses, add this option to your configuration:

This option should be provided as the second argument to `LogRocket.init`.

```javascript IP Capture Disabled
LogRocket.init(YOUR_APP_ID, {
  enableIPCapture: false,
});
```

To disable capturing a User's IP Address set this to `false`.