# Source: https://docs.datadoghq.com/feature_flags/client/ios.md

# Source: https://docs.datadoghq.com/error_tracking/frontend/mobile/ios.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/ios.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/ios.md

---
title: Tracing iOS Applications
description: Collect traces from your iOS applications.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Add the Datadog Tracing Library >
  Tracing iOS Applications
---

# Tracing iOS Applications

Send [traces](https://docs.datadoghq.com/tracing/visualization/#trace) to Datadog from your iOS applications with [Datadog's `dd-sdk-ios` client-side tracing library](https://github.com/DataDog/dd-sdk-ios) and leverage the following features:

- Create custom [spans](https://docs.datadoghq.com/tracing/visualization/#spans) for various operations in your app.
- Send logs for each span individually.
- Use default and add custom attributes to each span.
- Leverage optimized network usage with automatic bulk posts.

{% alert level="info" %}
Datadog charges for **ingested and indexed** spans sent from your iOS applications, but does not charge for the underlying devices. Read more in the [APM billing documentation](https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/).
{% /alert %}

## Setup{% #setup %}

1. Declare the library as a dependency depending on your package manager. Swift Package Manager (SPM) is recommended.

{% tab title="Swift Package Manager (SPM)" %}
To integrate using Apple's Swift Package Manager, add the following as a dependency to your `Package.swift`:

```swift
.package(url: "https://github.com/Datadog/dd-sdk-ios.git", .upToNextMajor(from: "2.0.0"))
```

In your project, link the following libraries:

```
DatadogCore
DatadogTrace
```

{% /tab %}

{% tab title="CocoaPods" %}
You can use [CocoaPods](https://cocoapods.org/) to install `dd-sdk-ios`:

```
pod 'DatadogCore'
pod 'DatadogTrace'
```

{% /tab %}

{% tab title="Carthage" %}
You can use [Carthage](https://github.com/Carthage/Carthage) to install `dd-sdk-ios`:

```
github "DataDog/dd-sdk-ios"
```

In Xcode, link the following frameworks:

```
DatadogInternal.xcframework
DatadogCore.xcframework
DatadogTrace.xcframework
```

{% /tab %}
Initialize the library with your application context and your [Datadog client token](https://github.com/DataDog/dd-sdk-ios). For security reasons, you must use a client token: you cannot use [Datadog API keys](https://docs.datadoghq.com/tracing/visualization/#spans) to configure the `dd-sdk-ios` library as they would be exposed client-side in the iOS application IPA byte code.
For more information about setting up a client token, see the [client token documentation](https://github.com/DataDog/dd-sdk-ios).

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.com

{% tab title="Swift" %}

```swift
import DatadogCore

Datadog.initialize(
    with: Datadog.Configuration(
        clientToken: "<client token>",
        env: "<environment>",
        service: "<service name>"
    ),
    trackingConsent: trackingConsent
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDConfiguration *configuration = [[DDConfiguration alloc] initWithClientToken:@"<client token>" env:@"<environment>"];
configuration.service = @"<service name>";

[DDDatadog initializeWithConfiguration:configuration
                        trackingConsent:trackingConsent];
```

{% /tab %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.datadoghq.eu

{% tab title="Swift" %}

```swift
import DatadogCore

Datadog.initialize(
    with: Datadog.Configuration(
        clientToken: "<client token>",
        env: "<environment>",
        site: .eu1,
        service: "<service name>"
    ),
    trackingConsent: trackingConsent
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDConfiguration *configuration = [[DDConfiguration alloc] initWithClientToken:@"<client token>" env:@"<environment>"];
configuration.service = @"<service name>";
configuration.site = [DDSite eu1];

[DDDatadog initializeWithConfiguration:configuration
                        trackingConsent:trackingConsent];
```

{% /tab %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: us3.datadoghq.com

{% tab title="Swift" %}

```swift
import DatadogCore

Datadog.initialize(
    with: Datadog.Configuration(
        clientToken: "<client token>",
        env: "<environment>",
        site: .us3,
        service: "<service name>"
    ),
    trackingConsent: trackingConsent
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDConfiguration *configuration = [[DDConfiguration alloc] initWithClientToken:@"<client token>" env:@"<environment>"];
configuration.service = @"<service name>";
configuration.site = [DDSite us3];

[DDDatadog initializeWithConfiguration:configuration
                        trackingConsent:trackingConsent];
```

{% /tab %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: us5.datadoghq.com

{% tab title="Swift" %}

```swift
import DatadogCore

Datadog.initialize(
    with: Datadog.Configuration(
        clientToken: "<client token>",
        env: "<environment>",
        site: .us5,
        service: "<service name>"
    ),
    trackingConsent: trackingConsent
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDConfiguration *configuration = [[DDConfiguration alloc] initWithClientToken:@"<client token>" env:@"<environment>"];
configuration.service = @"<service name>";
configuration.site = [DDSite us5];

[DDDatadog initializeWithConfiguration:configuration
                        trackingConsent:trackingConsent];
```

{% /tab %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% tab title="Swift" %}

```swift
import DatadogCore

Datadog.initialize(
    with: Datadog.Configuration(
        clientToken: "<client token>",
        env: "<environment>",
        site: .us1_fed,
        service: "<service name>"
    ),
    trackingConsent: trackingConsent
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDConfiguration *configuration = [[DDConfiguration alloc] initWithClientToken:@"<client token>" env:@"<environment>"];
configuration.service = @"<service name>";
configuration.site = [DDSite us1_fed];

[DDDatadog initializeWithConfiguration:configuration
                        trackingConsent:trackingConsent];
```

{% /tab %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: ap1.datadoghq.com

{% tab title="Swift" %}

```swift
import DatadogCore

Datadog.initialize(
    with: Datadog.Configuration(
        clientToken: "<client token>",
        env: "<environment>",
        site: .ap1,
        service: "<service name>"
    ),
    trackingConsent: trackingConsent
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDConfiguration *configuration = [[DDConfiguration alloc] initWithClientToken:@"<client token>" env:@"<environment>"];
configuration.service = @"<service name>";
configuration.site = [DDSite ap1];

[DDDatadog initializeWithConfiguration:configuration
                        trackingConsent:trackingConsent];
```

{% /tab %}

{% /callout %}

{% callout %}
# Important note for users on the following Datadog sites: ap2.datadoghq.com

{% tab title="Swift" %}

```swift
import DatadogCore

Datadog.initialize(
    with: Datadog.Configuration(
        clientToken: "<client token>",
        env: "<environment>",
        site: .ap2,
        service: "<service name>"
    ),
    trackingConsent: trackingConsent
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDConfiguration *configuration = [[DDConfiguration alloc] initWithClientToken:@"<client token>" env:@"<environment>"];
configuration.service = @"<service name>";
configuration.site = [DDSite ap2];

[DDDatadog initializeWithConfiguration:configuration
                        trackingConsent:trackingConsent];
```

{% /tab %}

{% /callout %}

To be compliant with the GDPR regulation, the SDK requires the `trackingConsent` value at initialization. The `trackingConsent` can be one of the following values:

- `.pending`: The SDK starts collecting and batching the data but does not send it to Datadog. The SDK waits for the new tracking consent value to decide what to do with the batched data.
- `.granted`: The SDK starts collecting the data and sends it to Datadog.
- `.notGranted`: The SDK does not collect any data: logs, traces, and RUM events are not sent to Datadog.

To change the tracking consent value after the SDK is initialized, use the `Datadog.set(trackingConsent:)` API call.

The SDK changes its behavior according to the new value. For example, if the current tracking consent is `.pending`:

- If changed to `.granted`, the SDK send all current and future data to Datadog;
- If changed to `.notGranted`, the SDK wipe all current data and stop collecting any future data.

Before data is uploaded to Datadog, it is stored in cleartext in the cache directory (`Library/Caches`) of your [application sandbox](https://docs.datadoghq.com/account_management/api-app-keys/#client-tokens). The cache directory cannot be read by any other app installed on the device.

When writing your application, enable development logs to log to console all internal messages in the SDK with a priority equal to or higher than the provided level.

{% tab title="Swift" %}

```swift
Datadog.verbosityLevel = .debug
```

{% /tab %}

{% tab title="Objective-C" %}

```
DDDatadog.verbosityLevel = DDSDKVerbosityLevelDebug;
```

{% /tab %}
Datadog tracer implements both [OpenTracing](https://opentracing.io) and [OpenTelemetry](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/ios/otel) standards. Configure and enable the shared an OpenTracing `Tracer` as `Tracer.shared()`:
{% tab title="Swift" %}

```swift
import DatadogTrace

Trace.enable(
    with: Trace.Configuration(
        networkInfoEnabled: true
    )
)

let tracer = Tracer.shared()
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
DDTraceConfiguration *configuration = [[DDTraceConfiguration alloc] init];
configuration.networkInfoEnabled = YES;

[DDTrace enableWith:configuration];

DDTracer *tracer = [Tracer shared];
```

{% /tab %}
Instrument your code using the following methods:
{% tab title="Swift" %}

```swift
let span = tracer.startSpan(operationName: "<span_name>")
// do something you want to measure ...
// ... then, when the operation is finished:
span.finish()
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
id<OTSpan> span = [tracer startSpan:@"<span_name>"];
// do something you want to measure ...
// ... then, when the operation is finished:
[span finish];
```

{% /tab %}
(Optional) - Set child-parent relationship between your spans:
{% tab title="Swift" %}

```swift
let responseDecodingSpan = tracer.startSpan(
    operationName: "response decoding",
    childOf: networkRequestSpan.context // make it a child of `networkRequestSpan`
)
// ... decode HTTP response data ...
responseDecodingSpan.finish()
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
id<OTSpan> responseDecodingSpan = [tracer startSpan:@"response decoding"
                                                            childOf:networkRequestSpan.context];
// ... decode HTTP response data ...
[responseDecodingSpan finish];
```

{% /tab %}
(Optional) - Provide additional tags alongside your span:
{% tab title="Swift" %}

```swift
span.setTag(key: "http.url", value: url)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
[span setTag:@"http.url" value:url];
```

{% /tab %}
(Optional) Attach an error to a span - you can do so by logging the error information using the [standard Open Tracing log fields](https://github.com/opentracing/specification/blob/master/semantic_conventions.md#log-fields-table):
{% tab title="Swift" %}

```swift
span.log(
    fields: [
        OTLogFields.event: "error",
        OTLogFields.errorKind: "I/O Exception",
        OTLogFields.message: "File not found",
        OTLogFields.stack: "FileReader.swift:42",
    ]
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
[span log:@{
    @"event": @"error",
    @"error.kind": @"I/O Exception",
    @"message": @"File not found",
    @"stack": @"FileReader.swift:42",
}];
```

{% /tab %}
(Optional) To distribute traces between your environments, for example frontend - backend, you can either do it manually or leverage our auto instrumentation. In both cases, you can opt to inject the trace context into all requests or only into the sampled ones. A sampling of 100% is applied by default.
- To manually propagate the trace, inject the span context into `URLRequest` headers:

{% tab title="Swift" %}

```swift
var request: URLRequest = ... // the request to your API

let span = tracer.startSpan(operationName: "network request")
let traceContextInjection = ... // either `.all` or `.sampled`

let headersWriter = HTTPHeadersWriter(traceContextInjection: traceContextInjection)
tracer.inject(spanContext: span.context, writer: headersWriter)

for (headerField, value) in headersWriter.traceHeaderFields {
    request.addValue(value, forHTTPHeaderField: headerField)
}
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
id<OTSpan> span = [tracer startSpan:@"network request"];
DDTraceContextInjection traceContextInjection = ...; // either `DDTraceContextInjectionAll` or `DDTraceContextInjectionSampled`
DDHTTPHeadersWriter *headersWriter = [[DDHTTPHeadersWriter alloc] initWithTraceContextInjection:traceContextInjection];

NSError *error = nil;
[tracer inject:span.context
        format:OT.formatTextMap
    carrier:headersWriter
        error:&error];

for (NSString *key in headersWriter.traceHeaderFields) {
    NSString *value = headersWriter.traceHeaderFields[key];
    [request addValue:value forHTTPHeaderField:key];
}
```

{% /tab %}

This sets additional tracing headers on your request so your backend can extract the request and continue distributed tracing. Once the request is done, call `span.finish()` within a completion handler. If your backend is also instrumented with [Datadog APM & Distributed Tracing](https://docs.datadoghq.com/tracing/), the entire front-to-back trace appears in the Datadog dashboard.

- In order for the SDK to automatically trace all network requests made to the given hosts, specify the `firstPartyHosts` array in the Datadog initialization, enable `URLSessionInstrumentation` for your delegate type and pass the delegate instance to the URLSession:

{% tab title="Swift" %}

```swift
import DatadogTrace

Trace.enable(
    with: Trace.Configuration(
        urlSessionTracking: Trace.Configuration.URLSessionTracking(
            firstPartyHostsTracing: .trace(hosts: ["example.com", "api.yourdomain.com"])
        )
    )
)

URLSessionInstrumentation.enable(
    with: .init(
        delegateClass: <YourSessionDelegate>.self,
    )
)

let session = URLSession(
    configuration: .default,
    delegate: <YourSessionDelegate>(),
    delegateQueue: nil
)
```

{% /tab %}

{% tab title="Objective-C" %}

```objective
@import DatadogObjc;

DDTraceFirstPartyHostsTracing *firstPartyHosts = [DDTraceFirstPartyHostsTracing alloc] initWithHosts:@[@"example.com", @"api.yourdomain.com"]
                                                                                            sampleRate: 20];

DDTraceURLSessionTracking *urlSessionTracking = [DDTraceURLSessionTracking alloc] initWithFirstPartyHostsTracing:firstPartyHosts];
DDTraceConfiguration *configuration = [[DDTraceConfiguration] alloc] init];
[configuration setURLSessionTracking:urlSessionTracking];

[DDTrace enableWith:configuration];

NSURLSession *session = [NSURLSession sessionWithConfiguration:[NSURLSessionConfiguration defaultSessionConfiguration]
                                                        delegate:[[DDNSURLSessionDelegate alloc] init]
                                                    delegateQueue:nil];
```

{% /tab %}

This traces all requests made with this `session` to `example.com` and `api.yourdomain.com` hosts (for example, `https://api.yourdomain.com/v2/users` or `https://subdomain.example.com/image.png`).

**Note**: Tracing auto-instrumentation uses `URLSession` swizzling and is opt-in. If you do not specify `firstPartyHosts`, swizzling is not applied.

## Batch collection{% #batch-collection %}

All the spans are first stored on the local device in batches. Each batch follows the intake specification. They are sent periodically if network is available, and the battery is high enough to ensure the Datadog SDK does not impact the end user's experience. If the network is not available while your application is in the foreground, or if an upload of data fails, the batch is kept until it can be sent successfully.

This means that even if users open your application while being offline, no data will be lost.

The data on disk will automatically be discarded if it gets too old to ensure the SDK doesn't use too much disk space.

## Initialization{% #initialization %}

The following attributes in `Trace.Configuration` can be used when creating the Tracer:

| Method                 | Description                                                                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bundleWithRumEnabled` | Set to `true` to enable spans to be enriched with the current RUM View information. This enables you to see all of the spans produced during a specific View lifespan in the RUM Explorer.                                         |
| `customEndpoint`       | Set the url to send traces for a custom server.                                                                                                                                                                                    |
| `eventMapper`          | Set the mapper to modify span events before they are sent.                                                                                                                                                                         |
| `networkInfoEnabled`   | Set to `true` to enrich traces with network connection info (reachability status, connection type, mobile carrier name, and more).                                                                                                 |
| `sampleRate`           | Set a value `0-100` to define the percentage of Traces to collect.                                                                                                                                                                 |
| `service`              | Set the value for the `service`.                                                                                                                                                                                                   |
| `tags`                 | Set a `<KEY>:<VALUE>` pair of tags to be added to spans created by the Tracer.                                                                                                                                                     |
| `urlSessionTracking`   | Set it to configure automatic tracing for network requests. It defines the first-party hosts, the sample rate, and the trace context injection strategy. Do not set this if it's already configured by another feature like `RUM`. |

## Further Reading{% #further-reading %}

- [dd-sdk-ios Source code](https://github.com/DataDog/dd-sdk-ios)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/visualization/)
