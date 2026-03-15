# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-application-performance-monitoring/setup-network.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-application-performance-monitoring/setup-network.md

# Setup Network

### Getting Started

Luciq App Performance Monitoring automatically captures your HTTP/S network requests when you're using the shared session. If some of your requests don't appear, you can follow the instructions below, depending on your setup: [Custom Session Configuration](#custom-session-configuration), [AFNetworking](#using-afnetworking), or [Alamofire](#using-alamofire).

#### Using Custom Session Configuration? <a href="#custom-session-configuration" id="custom-session-configuration"></a>

If you're using a custom `NSURLSession` or `NSURLSessionConfiguration`, add the following code snippet.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let configuration = URLSessionConfiguration.ephemeral
NetworkLogger.enableLogging(for: configuration)
let session = URLSession(configuration: configuration)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSURLSessionConfiguration *configuration = NSURLSessionConfiguration.ephemeralSessionConfiguration;
[LCQNetworkLogger enableLoggingForURLSessionConfiguration:configuration];
NSURLSession *session = [NSURLSession sessionWithConfiguration:configuration];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %} <mark style="color:blue;">Multiple NSURLSessions</mark>

Starting from SDK v11.0.3, Luciq supports multiple NSURLSession objects.
{% endhint %}

#### Using AFNetworking

To enable network monitoring for AFNetworking, create the following class. Then use LCQ`AFURLSessionManager` to create your requests.

{% tabs %}
{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
// LCQAFURLSessionManager.h

#import <AFNetworking/AFNetworking.h>

@interface LCQAFURLSessionManager : AFURLSessionManager

@end

// LCQAFURLSessionManager.m
  
#import "LCQAFURLSessionManager.h"
#import <Luciq/Luciq.h>

@implementation LCQAFURLSessionManager

- (instancetype)initWithSessionConfiguration:(nullable NSURLSessionConfiguration *)configuration {
		[LCQNetworkLogger enableLoggingForURLSessionConfiguration:configuration];
    
    return [super initWithSessionConfiguration:configuration];
}

@end
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Using Alamofire?

To enable logging for Alamofire, create the following class. Then use LCQ`SessionManager` to create your requests.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
import Alamofire
import Luciq

class LCQSessionManager: Alamofire.Session {
    static let sharedManager: LCQSessionManager = {
        let configuration = URLSessionConfiguration.default
        NetworkLogger.enableLogging(for: configuration)
        let manager = LCQSessionManager(configuration: configuration)
        return manager
    }()
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Using Apollo?

To enable logging for Apollo, pass your session configuration to our `NetworkLogger` and Apollo client

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
import Apollo
import Luciq

class LuciqApollo {
    static let shared = LuciqApollo()
    lazy var client: ApolloClient = {
        let url = URL(string: "https://example.com")!
        let configuration = URLSessionConfiguration.default
        NetworkLogger.enableLogging(for: configuration)
        let store = ApolloStore(cache: InMemoryNormalizedCache())
        let client = URLSessionClient(sessionConfiguration: configuration)
        let provider = LegacyInterceptorProvider(client: client, store: store)
        let transport = RequestChainNetworkTransport(interceptorProvider: provider,
                                                     endpointURL: url)
        return ApolloClient(networkTransport: transport, store: store)
    }()
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

### gRPC Support

Luciq supports the logging of gRPC requests. Depending on whether your codebase is Objective-C or Swift, a few different steps are required.

{% hint style="warning" %} <mark style="color:orange;">**iOS minimum version**</mark>

Logging gRPC requests is supported on iOS 10 and above.
{% endhint %}

#### gRPC Requests for Swift apps

To log gRPC requests in your Swift app, you'll need to add `pod Luciq-gRPC-Swift` to your `podfile`. Below you can find a few sample steps to assist with setting it up:

1. Import our destination: `import Luciq_gRPC_Swift`
2. Create an interceptor factory that confirms to the interceptor factory protocol that you have in your .grpc file
3. Make sure to return new instance of our interceptor `LuciqClientInterceptor()` in the methods that require being logged by Luciq
4. You can pass the port optionally in `LuciqClientInterceptor` as `LuciqClientInterceptor(port: <#T##Int?#>)` to see it on the dashboard
5. You can convert your model to Data by conforming to Encodable
6. You can pass the port optional in LuciqClientInterceptor as LuciqClientInterceptor(port: <#T##Int?#>) to see it on the dashboard

*Below is sample code for the interceptor factory:*

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
class ExampleClientInterceptorFactory: Echo_EchoClientInterceptorFactoryProtocol {
  // Returns an array of interceptors to use for the 'Get' RPC.
  func makeGetInterceptors() -> [ClientInterceptor<Echo_EchoRequest, Echo_EchoResponse>] {
    return [LuciqClientInterceptor()]
  }

  // Returns an array of interceptors to use for the 'Expand' RPC.
  func makeExpandInterceptors() -> [ClientInterceptor<Echo_EchoRequest, Echo_EchoResponse>] {
    return [LuciqClientInterceptor()]
  }

  // Returns an array of interceptors to use for the 'Collect' RPC.
  func makeCollectInterceptors() -> [ClientInterceptor<Echo_EchoRequest, Echo_EchoResponse>] {
    return [LuciqClientInterceptor()]
  }

  // Returns an array of interceptors to use for the 'Update' RPC.
  func makeUpdateInterceptors() -> [ClientInterceptor<Echo_EchoRequest, Echo_EchoResponse>] {
    return [LuciqClientInterceptor()]
  }
}

extension GrpcAutomation_RepeaterRequest: LuciqGRPCDataProtocol, Encodable {
    enum CodingKeys: String, CodingKey {
        case message, unknownFields
    }
    
    public func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(message, forKey: .message)
    }
    
    public var gRPCRequestData: Data? {
        let jsonEncoder = JSONEncoder()
        let data = try? jsonEncoder.encode(self)
        return data
    }
  
  //Finally
  let client = Echo_EchoClient(channel: channel, interceptors: ExampleClientInterceptorFactory())
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### gRPC requests for Objective-C apps

To log gRPC requests in your Swift app, you'll need to add `pod Luciq_gRPC_ObjC` to your `podfile`. Below you can find a few sample steps to assist with setting it up:

1. Create an array of `GRPCInterceptorFactory`
2. Create a class that conforms to GRPCInterceptorFactory protocol

{% tabs %}
{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
@interface GRPCFactory : NSObject <GRPCInterceptorFactory>
```

{% endcode %}
{% endtab %}
{% endtabs %}

3. Override `createInterceptorWithManager` in `GRPCFactory` and return `LuciqClientInterceptor`

{% tabs %}
{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
- (nonnull GRPCInterceptor *)createInterceptorWithManager:(nonnull GRPCInterceptorManager *)interceptorManager {
    LuciqClientInterceptor *interceptor = [[LuciqClientInterceptor alloc] initWithInterceptorManager:interceptorManager dispatchQueue:dispatch_get_main_queue()];
    return  interceptor;
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

4. Create a new instance of `GRPCFactory` and add it to the interceptors array
5. Create a new instance of `GRPCInterceptorManager` with the `interceptorFactories` array
6. Pass the manager to the factory instance
7. Finally pass `interceptorFactories` to `options.interceptorFactories`&#x20;

{% tabs %}
{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
GRPCMutableCallOptions *options = [[GRPCMutableCallOptions alloc] init];

NSMutableArray<id<GRPCInterceptorFactory>> *interceptorFactories = [NSMutableArray new];

GRPCFactory *factory = [GRPCFactory new];
[interceptorFactories addObject:factory];
GRPCInterceptorManager *manager = [[GRPCInterceptorManager alloc] initWithFactories:interceptorFactories
                                                                previousInterceptor:nil
                                                                        transportID:GRPCDefaultTransportImplList.core_insecure];

[factory createInterceptorWithManager:manager];
options.interceptorFactories = interceptorFactories;
```

{% endcode %}
{% endtab %}
{% endtabs %}

***

### Trace Attributes

Sometimes, you may need to add additional data or attributes to your network traces. This can be done using the API below.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let urlPattern = "*.example.com/*"
let urlPredicate = NSPredicate(format: "SELF LIKE[c] '\(urlPattern)'")
APM.addNetworkTraceAttributesForURL(matching: urlPredicate, owner: self) { trace in
    return [
        "trace": "example"
    ]
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[LCQAPM addNetworkTraceAttributesForURLMatchingPredicate:[NSPredicate predicateWithFormat:@"SELF LIKE[c] '%@'", @"*.example.com/*"]
                                                   owner:self
                                            usingHandler:^NSDictionary<NSString *,NSString *> * _Nullable(LCQNetworkTrace * _Nonnull networkTrace) {
    return @{
        @"type": @"example"
    };
}];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
You can add up to **20 unique trace attributes** per each trace.
{% endhint %}
