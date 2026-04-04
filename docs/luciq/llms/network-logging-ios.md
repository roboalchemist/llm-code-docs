# Source: https://docs.luciq.ai/references/report-data/logging/network-logging-ios.md

# Network Logging - iOS

Network logs are automatically collected by Luciq when possible. There are many way to configure and manipulate these logs from the code.

Note: The maximum number of network logs sent with each report is 100.

### Disable and Enable Request Logging

By default, request logging is enabled. It can be disabled using the API to the right.

**Enable and Disable**

{% tabs %}
{% tab title="Swift" %}

```swift
NetworkLogger.enabled = false
```

{% endtab %}

{% tab title="Objective-C" %}

```objective-c
LCQNetworkLogger.enabled = NO;
```

{% endtab %}
{% endtabs %}

### Omitting Requests from Logs

You can omit requests from being logged based on either their request or response details. `[Luciq setNetworkLoggingRequestFilterPredicate:responseFilterPredicate:]` allows you to specify two predicates that are going to be evaluated against every request and response to determine if the request should be included in logs or not.

The example code to the right will exclude all requests made to URLs that have /products path. It will also exclude all responses that has a success and redirection status code, thus only including requests with 4xx and 5xx responses.

`requestFilterPredicate` is evaluated against an `NSURLRequest`, while `responseFilterPredicate` is evaluated against an `NSHTTPURLResponse`.

**Omit Request**

{% tabs %}
{% tab title="Swift" %}

```swift
let path = \"/products\"
let requestPredicate = NSPredicate(format: \"URL.path MATCHES %@\", path)
let responsePredicate = NSPredicate(format: \"statusCode >= %d AND statusCode <= %d\", 200, 399)
NetworkLogger.setNetworkLoggingRequestFilterPredicate(requestPredicate, responseFilterPredicate: responsePredicate)
```

{% endtab %}

{% tab title="Objective-C" %}

```objective-c
NSString *path = @"/products";
NSPredicate *requestPredicate = [NSPredicate predicateWithFormat:@"URL.path MATCHES %@", path];
NSPredicate *responsePredicate = [NSPredicate predicateWithFormat:@"statusCode >= %d AND statusCode <= %d", 200, 399];
[LCQNetworkLogger setNetworkLoggingRequestFilterPredicate:requestPredicate responseFilterPredicate:responsePredicate];
```

{% endtab %}
{% endtabs %}

### Manual Network Logging

Manual network logging gives you precise control over what data is sent to Luciq. It's ideal for advanced scenarios like instrumenting a highly custom networking layer, or for selective logging in performance-sensitive apps where you only want to capture specific, high-importance requests.

You can log network requests manually using the following API:

{% tabs %}
{% tab title="Swift" %}

```swift
NetworkLogger.addNetworkLog(
            withUrl: "https://api.example.com/user",
            method: "POST",
            requestBody: requestBodyAsString,
            requestBodySize: 1024, // in bytes
            responseBody: responseBodyAsString,
            responseBodySize: 1024, // in bytes
            responseCode: 200,
            requestHeaders: ["example":"example"],
            responseHeaders: ["example":"example"],
            contentType: "application/json",
            errorDomain: nil, // If available when a request fails, otherwise `nil`
            errorCode: 422,     // If available when a request fails, otherwise 0
            startTime: 1664625600000000,    // Unix timestamp in microseconds
            duration: 500000,           // Duration in microseconds
            gqlQueryName: "query",      // If available, otherwise `nil`
            serverErrorMessage: "error") // If available when request is gql, otherwise `nil`
```

{% endtab %}

{% tab title="Objective-C" %}

```objective-c
 [LCQNetworkLogger addNetworkLogWithUrl: @"https://api.example.com/user"
                                    method: @"POST"
                               requestBody: requesteBodyAsString
                           requestBodySize: 1024 // in bytes
                              responseBody: responseBodyAsString
                          responseBodySize: 1024 // in bytes
                              responseCode: 200
                            requestHeaders: @{@"example": @"example"}
                           responseHeaders: @{@"example":@"example"}
                               contentType: @"application/json"
                               errorDomain: nil // If available when a request fails, otherwise `nil`
                                 errorCode: 422     // If available when a request fails, otherwise 0
                                 startTime: 1664625600000000    // Unix timestamp in microseconds
                                  duration: 500000           // Duration in microseconds
                              gqlQueryName: @"query"      // If available, otherwise `nil`
                        serverErrorMessage: @"error"]; // If available when request is gql, otherwise `nil`
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}

#### Timestamp Format

To ensure your network data is processed correctly, all time-based values (startTime, duration) must be passed in microseconds (µs), not milliseconds. Providing values in milliseconds will cause the requests to be dropped or processed incorrectly.
{% endhint %}

### Disable Automatic Network Capture

By default, the SDK automatically captures network requests. To use **manual logging only**, disable automatic capture **before starting the SDK**.

{% tabs %}
{% tab title="Swift" %}

```swift
NetworkLogger.disableAutomaticCapturingOfNetworkLogs()
```

{% endtab %}

{% tab title="Objective-C" %}

```objective-c
[LCQNetworkLogger disableAutomaticCapturingOfNetworkLogs];
```

{% endtab %}
{% endtabs %}

### Obfuscating Data

Both requests and responses can be obfuscated if required. You can obfuscate user sensitive data in requests, like authentication tokens for example, without filtering out the whole request. As with requests, the response object, as well as the response data, could be modified for obfuscation purposes before they are logged.

**Obfuscate Request**

{% tabs %}
{% tab title="Swift" %}

```swift
NetworkLogger.setRequestObfuscationHandler { (request) -> URLRequest in
    var myRequest:NSMutableURLRequest = request as! NSMutableURLRequest
    let urlString = request.url?.absoluteString
    urlString = obfuscateAuthenticationTokenInString()
    let obfuscatedURL = URL(string: urlString)
    myRequest.url = obfuscatedURL
    return myRequest.copy() as! URLRequest
}
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
LCQNetworkLogger.requestObfuscationHandler = ^NSURLRequest * _Nonnull(NSURLRequest * _Nonnull request) {
        NSMutableURLRequest *myRequest = [request mutableCopy];
        NSString *urlString = request.URL.absoluteString;
        urlString = [self obfuscateAuthenticationTokenInString:urlString];
        NSURL *obfuscatedURL = [NSURL URLWithString:urlString];
        myRequest.URL = obfuscatedURL;
        return myRequest;
    };
```

{% endtab %}
{% endtabs %}

**Obfuscate Response**

{% tabs %}
{% tab title="Swift" %}

```swift
NetworkLogger.setResponseObfuscationHandler { (data, response, completion) in
    if let data = data {
        let modifiedData = self.modify(data: data)
        let modifiedResponse = self.modify(response: response)
        
        completion(modifiedData, modifiedResponse)
    }
}
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
[LCQNetworkLogger setResponseObfuscationHandler:^(NSData * _Nullable responseData, NSURLResponse * _Nonnull response, NetworkObfuscationCompletionBlock  _Nonnull returnBlock) {
    NSData *modifiedData = [self obfuscateData:responseData];
    NSURLResponse *modifiedResponse = [self obfuscateResponse:response];
    
    returnBlock(modifiedData, modifiedResponse);
}];
```

{% endtab %}
{% endtabs %}

### Requests Not Appearing

If your network requests aren't being logged automatically because you're probably using a custom `NSURLSession` or `NSURLSessionConfiguration`, you would need to enable logging for your `NSURLSession` using this API.

{% tabs %}
{% tab title="Swift" %}

```swift
let configuration = URLSessionConfiguration.ephemeral
NetworkLogger.enableLogging(for: configuration)
let session = URLSession(configuration: configuration)
```

{% endtab %}

{% tab title="Objective-C" %}

```objectivec
NSURLSessionConfiguration *configuration = NSURLSessionConfiguration.ephemeralSessionConfiguration;
[LCQNetworkLogger enableLoggingForURLSessionConfiguration:configuration];
NSURLSession *session = [NSURLSession sessionWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}

#### If the requests still aren't appearing

You'll need to make sure that `enableLoggingForURLSessionConfiguration:` was called just before using the configuration to create the session.
{% endhint %}

### AFNetworking

To enable logging for AFNetworking, you may create this class, then use `LCQAFURLSessionManager` to create your requests.

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

### Alamofire

To enable logging for Alamofire, you may create this class, then use `LCQSessionManager` to create your requests.

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
