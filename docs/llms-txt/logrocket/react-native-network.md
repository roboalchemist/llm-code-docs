# Source: https://docs.logrocket.com/reference/react-native-network.md

# Sanitize Network Data (React Native)

Control how data is passed in network requests or responses

By default, the LogRocket React Native SDK captures all network requests made through [XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) and the [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

### `network`

A collection of configuration options specific to network capture. This option is available for configuration, and should be provided in the second argument to `LogRocket.init`.

## Disable recording of network data

#### `isEnabled` - Boolean

##### optional (default - *true*)

```javascript Disable Network Logging
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    isEnabled: false,
  },
});
```

## Sanitize a network request

#### `requestSanitizer` - Function

##### optional

Use requestSanitizer to scrub sensitive data from JavaScript network requests, or to ignore request/response pairs entirely.

To ignore a request/response pair return `null` from the `requestSanitizer`. You can also redact fields on the `request` object by modifying the object. Make sure that you still return the modified request from the function:

```javascript Ignore Network Pair By URL
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    requestSanitizer: request => {
      // if the url contains 'ignore'
      if (request.url.toLowerCase().indexOf('ignore') !== -1) {
        // ignore the request response pair
        return null;
      }
      
      // otherwise log the request normally
      return request;
    },
  },
});
```

```javascript Remove Body From Request
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    requestSanitizer: request => {
      // if the url contains 'ignore'
      if (request.url.toLowerCase().indexOf('ignore') !== -1) {
        // scrub out the body
        return {
          ...request,
          body: null,
        };
      }
        
      return request;
    },
  },
});
```

```javascript Remove Header Value From Request
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
   network: {
     requestSanitizer: request => {
       return {
         ...request,
         headers: {
           ...request.headers,
           'x-auth-token': null,
         },
       };
     },
   },
});
```

```javascript Scrub Header Value From Request
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
  network: {
    requestSanitizer: request => {
      if (request.headers['x-auth-token']) {
        return {
          ...request,
          headers: {
            ...request.headers,
            'x-auth-token': '',
          },
       	};
      }
      
      return request;
    },
  },
});
```

## Sanitize a network response

#### `responseSanitizer` - Function

##### optional

Use the `responseSanitizer` to redact sensitive data from javascript network responses. Return `null` from the function to redact all response fields and only record timing data.

```javascript Remove Body From Responses
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
   network: {
     responseSanitizer: response => {
       return {
         ...response,
         body: null,
       };
     },
   },
});
```

```javascript Remove All Response Data
// Add this to your existing init call, do not call init twice!
LogRocket.init(YOUR_APP_ID, {
   network: {
     responseSanitizer: response => {
       return null;
     },
   },
});
```

> 📘 logrocket-fuzzy-search-sanitizer
>
> Joshua Bailey, a LogRocket user, contributed a plugin for more easily sanitizing data from network requests and responses. Check it out here: [https://github.com/LogRocket/logrocket-fuzzy-search-sanitizer](https://github.com/LogRocket/logrocket-fuzzy-search-sanitizer)

## Android Native network capture in React Native

Native Android network requests cannot be captured automatically. You must make use of the Android LogRocket SDK to capture network requests and configure sanitation. The LogRocket Android SDK can be made available to your native Android codebase via the [Gradle setup documented here](https://docs.logrocket.com/reference/android#/configure-gradle). From there, network capture can be configured following the [Android network setup guide here](https://docs.logrocket.com/reference/android-capturing-network-traffic#/).

## iOS Native network capture in React Native

Native iOS network capture is available as of React Native SDK version `1.57.1`.

By default, the LogRocket React Native SDK captures all network requests made through [JavaScript XMLHttpRequests](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) and the [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch). In order to capture requests made natively (i.e. in Swift or Objective-C code), you can configure the React Native SDK to capture network requests natively instead of through JavaScript.

Once native network capture is enabled, *all* network requests will be captured by native intercepts, including those made from JavaScript.

<Callout icon="❗️" theme="error">
  Setting `iosNetworkCaptureMode` to `'native' `will capture *all* network requests at the native iOS level, including those made in JavaScript app code. This setting **disables** the JavaScript 'requestSanitizer' and 'responseSanitizer' configured in the React Native SDK init. All network sanitation must be configured through the native SDK as described below.
</Callout>

```javascript
// Add this to your existing init call
LogRocket.init(YOUR_APP_ID, {
  network: {
    iosNetworkCaptureMode: 'native',
  },
});
```

### Manual iOS native network capture

Alternatively to the above configuration, you can keep React Native network requests captured in JavaScript, and import the LogRocket SDK into the Native portion of your React Native app to manually capture network requests. You can find [an example here](https://docs.logrocket.com/reference/ios-capture-network-data#/manual-network-capture).

### Disabling iOS Native network capture on Specific Domains

<Callout icon="📘" theme="info">
  We recommend using [request and response sanitizers](#sanitize-ios-native-network-data) for fine-grained redaction of request data. Domain redaction results in complete exclusion of all requests and request data to that domain from network capture.
</Callout>

The `iosNativeNetworkRedactedOrigins` configuration accepts an array of domains or subdomains to be excluded from network capture. Requests to resources on these domains will completely bypass LogRocket's network capture at runtime. These will be executed normally within the app, but will not appear in session replay. This is useful for running LogRocket alongside other third-party tools that could otherwise cause conflicts when intercepted by LogRocket.

If specifying a specific subdomain for network capture exclusion, supply the subdomain within the configuration array. Requests to other subdomains or higher-level domains (e.g. `example.com` of `redactedsubdomain.example.com`) will still be captured. Likewise, if `example.com` is redacted, its subdomains will still be captured unless specifically supplied within `iosNativeNetworkRedactedOrigins`.

```javascript
// Add this to your existing init call
LogRocket.init(YOUR_APP_ID, {
  network: {
    iosNetworkCaptureMode: 'native',
    iosNativeNetworkRedactedOrigins: ['redacted-domain.com', 'redactedsubdomain.example.com'],
  },
});
```

### Sanitize iOS native network data

Custom `requestSanitizer` and `responseSanitizer` functions can be written to sanitize network requests when using 'native' network capture mode. Because network data is intercepted in the native execution environment, network sanitizers must also be written and configured in native code.

First, set the following configuration in your React Native init to ensure that network requests aren't captured prior to sanitizers being configured

```javascript
// Add this to your existing init call
LogRocket.init(YOUR_APP_ID, {
  network: {
    iosNetworkCaptureMode: 'native',
    iosRequireNativeNetworkSanitizers: true,
  },
});
```

Then, in your native application code, add the following. Note that the LogRocket native iOS SDK should already be available for import after the React Native SDK's [iOS preparation step](https://docs.logrocket.com/reference/react-native#/preparing-ios). The `SDK.setReactNativeNetworkSanitizers` call can be made from anywhere, but the earlier the sanitizers are configured (such as in your `AppDelegate.application()`, the less likely it is that any network calls will be missed.

```swift
import Foundation
import LogRocket

class ExampleSanitizer: RequestSanitizer, ResponseSanitizer {
  public func sanitize(request: Request) -> Request? {
    if let url = request.url, url.contains("privateInformation") {
      // This will redact the entirety of the request
      // The matching response will be ignored as well
      return nil
    }
    
    // This will remove only privateHeader, but leave the rest of the headers in the recording
    request.headers?.removeValue(forKey: "privateHeader")

    return request
  }

  public func sanitize(response: Response) -> Response? {
    if response.status == 404 {
      // This will redact only the response body for responses with a 404 status code
      response.body = nil
    }

    return response
  }
}

// Add to native SDK
let sanitizer = ExampleSanitizer()
SDK.setReactNativeNetworkSanitizers(requestSanitizer: sanitizer, responseSanitizer: sanitizer)

```

<br />