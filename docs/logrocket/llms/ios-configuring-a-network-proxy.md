# Source: https://docs.logrocket.com/reference/ios-configuring-a-network-proxy.md

# Configure a Network Proxy (iOS)

Allow session collection on devices with proxy requirements

If a network proxy is required a configuration builder can be provided when initializing the SDK.  Network proxies may be required if end users generate sessions on devices that have proxy requirements.  To configure, set your proxy and its parameters as a variable and refer to that variable in your proxyConfiguration option in your SDK.initialize() call.

```swift Swift
let proxyConfig = ProxyConfigurationBuilder()
proxyConfig.httpEnable(true);
proxyConfig.httpProxy("127.0.0.1");
proxyConfig.httpPort(8888);
proxyConfig.proxyUsername("username");
proxyConfig.proxyPassword("password");

SDK.initialize(configuration: Configuration(
  appID: "<APP_SLUG>",
  proxyConfiguration: proxyConfig,
))
```

```objectivec Objective-C
LROProxyConfigurationBuilder *proxyConfig = [[LROProxyConfigurationBuilder alloc] init];

[proxyConfig httpEnable:true]
[proxyConfig httpProxy:@"127.0.0.1"]
[proxyConfig httpPort:8888]
[proxyConfig proxyUsername:@"username"]
[proxyConfig proxyPassword:@"password"]

LROConfiguration *configuration = [[LROConfiguration alloc] initWithAppID:@"<APP_ID>"];
configuration.proxyConfiguration = proxyConfig;
[LROSDK initializeWithConfiguration:configuration];
```