# Source: https://docs.logrocket.com/reference/ios-capture-network-data.md

# Capture Network Data

Network requests in iOS are automatically captured by default.

### Disable Network Capture

To disable the automatic network capture initialize the SDK with the `networkCaptureEnabled` set to `false`.

```swift
let configuration = Configuration(
  appID: "<APP_SLUG>",
  networkCaptureEnabled: false)

SDK.initialize(configuration: configuration)
```

### Disabling Network Capture on Specific Domains

<Callout icon="📘" theme="info">
  We recommend using [request and response sanitizers](https://docs.logrocket.com/reference/ios-capturing-network-traffic#/) for fine-grained redaction of request data. Domain redaction results in complete exclusion of all requests and request data to that domain from network capture.
</Callout>

The SDK accepts an array of `networkCaptureRedactedOrigins` in its `Configuration` object at initialization. Requests to resources on these domains will completely bypass LogRocket's network capture at runtime. This is useful for running LogRocket alongside other third-party tools with network requests that would otherwise cause conflicts when intercepted by the SDK.

Requests to domains included in `networkCaptureRedactedOrigins` will be executed normally within the app, but will not appear in session replay.

If specifying a specific subdomain for network capture exclusion, supply the subdomain within the configuration array. Requests to other subdomains or higher-level domains (e.g. `example.com` of `redactedsubdomain.example.com`) will still be captured. Likewise, if `example.com` is redacted, its subdomains will still be captured unless specifically supplied within `networkCaptureRedactedOrigins`.

```swift
let configuration = Configuration(
  appID: "<APP_SLUG>",
  networkCaptureRedactedOrigins: ["redactedsubdomain.example.com"]
)

SDK.initialize(configuration: configuration)
```

### Manual Network Capture

If you have disabled automatic network capture and would like to only capture specific requests, you can use our `RequestBuilder` object.

```swift
import LogRocket

let requestBuilder = SDK.newRequestBuilder()
requestBuilder.headers = ["Header": "Value"]
requestBuilder.method = "GET"
requestBuilder.url = "https://www.example.com"
let responseBuilder = requestBuilder.capture()
responseBuilder.status = 200
responseBuilder.capture()
```

For the request builder, the headers, method and URL are required fields. For the response builder, only the headers are required.