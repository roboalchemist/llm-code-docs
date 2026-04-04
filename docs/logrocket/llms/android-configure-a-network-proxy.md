# Source: https://docs.logrocket.com/reference/android-configure-a-network-proxy.md

# Configure a Network Proxy (Android)

If a network proxy is required a configuration builder can be provided when initializing the SDK.  Network proxies may be required if end users generate sessions on devices that have proxy requirements.  To configure, set your proxy parameters when initializing the SDK.

```java
SDK.init(..., options -> {
  // ... other options

  options.setProxyHost('10.0.2.2');
  options.setProxyPort(8888);

  // For proxies that need an Authorization header:
  options.setProxyHeaderName('Proxy-Authorization');
  options.setProxyHeaderValue('Basic authorizationKey');
});
```