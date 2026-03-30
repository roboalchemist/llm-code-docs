# Source: https://docs.logrocket.com/reference/android-disable-ip-capture.md

# Enable or Disable IP Capture (Android)

Control whether or not a users IP address is sent to LogRocket

## Disable IP Address capture

LogRocket captures IP addresses to enable reverse-IP lookups for location search, and to help you match between back-end logs and captured sessions.

If you'd like LogRocket to not store IP addresses, add this option to your configuration:

### `options.setEnableIPCapture(boolean enable)`

To disable capturing a User's IP Address set this to `false`.