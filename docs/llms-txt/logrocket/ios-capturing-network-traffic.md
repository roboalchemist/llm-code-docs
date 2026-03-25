# Source: https://docs.logrocket.com/reference/ios-capturing-network-traffic.md

# Sanitize Network Data (iOS)

Sanitize Network Requests and Responses

### Redacting Sensitive Information

The SDK accepts a `requestSanitizer` and `responseSanitizer` at initialization. The values provided must conform to the `RequestSanitizer` protocol (`LRORequestSanitizer` in Objective-C) and the `ResponseSanitizer` protocol (`LROResponseSanitizer` in Objective-C) respectively.

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

// Add to configuration
let sanitizer = ExampleSanitizer()
let configuration = Configuration(appID: "<APP_SLUG>", requestSanitizer: sanitizer, responseSanitizer: sanitizer)
SDK.initialize(configuration: configuration)
```

For more information on general network capture, including disabling network capture entirely or by domain, and manual network capture, see [Capture Network Data](ios-capture-network-data#).