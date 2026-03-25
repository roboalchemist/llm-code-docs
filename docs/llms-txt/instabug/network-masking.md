# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/custom-settings/privacy-settings/network-masking.md

# Network Masking

Luciq automatically logs all network requests performed by your app from the start of the session. Requests details, along with their responses, are sent with each report. Luciq will also show you an alert at the top of the bug report in your dashboard when network requests have timed-out or taken too long to complete. Note that the maximum number of network logs sent with each report is 1,000.

<figure><img src="https://828794017-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAM8wNfllcup3GnWJ1WtW%2Fuploads%2FnRTuJVXsbile4oZQJIzY%2Fimage.png?alt=media&#x26;token=3a94619b-e023-479f-bf77-675c817b8e47" alt=""><figcaption><p><em>An example of network request logs in the Luciq dashboard</em></p></figcaption></figure>

#### Logging `HttpUrlConnection` requests for Android

To log network requests, use Luciq`NetworkLog` then use the following method at the `HttpUrlConnection`, `requestBody` and `responseBody` referenced [here](https://docs.luciq.ai/ios/setup-luciq-for-ios/logs-and-profiling/report-logs#network-logs).

#### Auto-Masking Network Headers

Starting from SDK Version 14.2.0, our SDK will automatically mask the below keys from Network Headers and Query Parameters to ensure that no sensitive data reaches our servers.

The below keys will be displayed normally on the dashboard, but their corresponding values will be replaced with an asterisk (\*) to protect sensitive data.

{% tabs %}
{% tab title="Keys" %}
{% code overflow="wrap" %}

```
List of keys that will be automatically masked" 
 "authorization_token, auth_token, auth, access_token, token, oauth_token, bearer_token, refresh_token, jwt_token, jwt, Username, password, pwd, api_key, apikey, secret, client_secret, app_secret, consumer_secret"
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Adding New Keys

The list of masked keys is configurable on our side. This means you don't need to make any code changes to add new keys; they will be automatically reflected in the next session. If you need additional keys added, please reach out to support.

#### Disabling Network Header Auto-Masking

***This feature is enabled by default and we strongly recommend to keep it enabled*** to make sure PII data is not collected by our SDK. However, if you need to disable it for any reason, please use the below API.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
NetworkLogger.autoMaskingEnabled = false
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQNetworkLogger.autoMaskingEnabled = false;
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Omitting Requests

You can omit requests from being logged based on their request or response details. You can also specify an expression to be evaluated against every request and response to determine if the request should be included in logs or not.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let path = "/products"
let requestPredicate = NSPredicate(format: "URL.path MATCHES %@", path)
let responsePredicate = NSPredicate(format: "statusCode >= %d AND statusCode <= %d", 200, 399)
NetworkLogger.setNetworkLoggingRequestFilterPredicate(requestPredicate, responseFilterPredicate: responsePredicate)
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSString *path = @"/products";
NSPredicate *requestPredicate = [NSPredicate predicateWithFormat:@"URL.path MATCHES %@", path];
NSPredicate *responsePredicate = [NSPredicate predicateWithFormat:@"statusCode >= %d AND statusCode <= %d", 200, 399];
[LCQNetworkLogger setNetworkLoggingRequestFilterPredicate:requestPredicate 
                                responseFilterPredicate:responsePredicate];

// The code above excludes all requests made to URLs that have the /products path.
// It also excludes all responses with success and redirection status codes, 
// thus only including requests with 4xx and 5xx responses.
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Obsucating Data

#### Requests

You can obfuscate sensitive user data, such as authentication tokens, in requests without filtering out the whole request.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
NetworkLogger.setRequestObfuscationHandler { (request) -> URLRequest in
    var myRequest: NSMutableURLRequest = request as! NSMutableURLRequest
    let urlString = request.url?.absoluteString
    urlString = obfuscateAuthenticationTokenInString()
    let obfuscatedURL = URL(string: urlString)
    myRequest.url = obfuscatedURL
    return myRequest.copy() as! URLRequest
}

```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

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

{% endcode %}
{% endtab %}
{% endtabs %}

#### Responses

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
NetworkLogger.setResponseObfuscationHandler { (data, response, completion) in
    if let data = data {
        let modifiedData = self.modify(data: data)
        let modifiedResponse = self.modify(response: response)
        completion(modifiedData, modifiedResponse)
    }
}

```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[LCQNetworkLogger setResponseObfuscationHandler:^(NSData * _Nullable responseData,
                                                  NSURLResponse * _Nonnull response,
                                                  NetworkObfuscationCompletionBlock _Nonnull returnBlock) {
    NSData *modifiedData = [self obfuscateData:responseData];
    NSURLResponse *modifiedResponse = [self obfuscateResponse:response];
    returnBlock(modifiedData, modifiedResponse);
}];
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Note: Protecting sensitive information and respecting user privacy are vital. By following these steps, you'll create a secure and trustworthy environment for your users.
{% endhint %}
