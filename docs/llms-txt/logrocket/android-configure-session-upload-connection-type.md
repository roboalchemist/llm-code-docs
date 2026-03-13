# Source: https://docs.logrocket.com/reference/android-configure-session-upload-connection-type.md

# Configure Session Upload Connection Type

Set connection to Mobile or WiFi

## Upload session data via mobile or WiFi

Use this option to set whether session data collected by the LogRocket SDK should be uploaded via mobile network, or only via WiFi.  If this option is left as mobile, WiFi connections will also be allowed for session data upload.

### `options.setConnectionType(SDK.ConnectionType)`

Configure the required connection type for uploading session data: either Mobile (the default) or WiFi.