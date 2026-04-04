# Source: https://docs.logrocket.com/reference/shouldcaptureip.md

# Enable or Disable IP Capture (Web)

Control whether or not a users IP address is sent to LogRocket

## Disable IP Address capture

#### `shouldCaptureIP` - Boolean

##### optional (default - `true`)

LogRocket captures IP addresses to enable reverse-IP lookups for location search, and to help you match between back-end logs and captured sessions.

If you'd like LogRocket to not store IP addresses, add this option to your configuration:

```javascript
LogRocket.init(YOUR_APP_ID, {
  shouldCaptureIP: false,
});
```