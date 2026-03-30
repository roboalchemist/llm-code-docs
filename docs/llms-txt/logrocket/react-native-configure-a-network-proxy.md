# Source: https://docs.logrocket.com/reference/react-native-configure-a-network-proxy.md

# Configure a Network Proxy (React Native)

If a network proxy is required a configuration builder can be provided when initializing the SDK.  Network proxies may be required if end users generate sessions on devices that have proxy requirements.  To configure, set your proxy parameters when initializing the SDK.

```javascript
LogRocket.init('<APP_SLUG>', {
  // To configure the iOS proxy use:
  iosProxyConfiguration: {
    proxyUsername: 'username',
    proxyPassword: 'password',
    httpEnable: true,
    httpProxy: '10.0.2.2',
    httpPort: 8888,
  },
  // To configure the Android proxy use:
  androidProxy: {
    host: '10.0.2.2',
    port: 8888,
    authHeaderName: 'Proxy-Authorization',
    authHeaderValue: 'Basic authorizationToken',
  },
});
```