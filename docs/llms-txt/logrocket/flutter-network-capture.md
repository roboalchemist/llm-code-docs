# Source: https://docs.logrocket.com/reference/flutter-network-capture.md

# Capture and Sanitize Network Data

Capture Flutter network data in LogRocket

## Automatic Network Capture

The LogRocket Flutter SDK automatically captures Network Requests in your application when your app is [wrapped](https://docs.logrocket.com/reference/initialize-flutter#/initializing-the-sdk) with LogRocket. Any network requests that are made using `dart:io`'s http internals will automatically be recorded.

### Disable Automatic Network Capture

To disable automatically recording network traffic, set LogRocket SDK wrap option `networkCaptureEnabled` to false.

```dart Flutter
LogRocket.wrapAndInitialize(
  LogRocketWrapConfiguration(
    networkCaptureEnabled: false,
  ),
  LogRocketInitConfiguration(appID: 'YOUR_APP_ID'),
  () => runApp(MyApp()),
);
```

## Manual Network Capture

> 🚧 If Automatic and Manual network capture are both in use, network requests may be duplicated in session replay.

An [http](https://pub.dev/packages/http) client has been provided to allow manually recording network requests into LogRocket. This can be used to capture specific network requests even when `networkCaptureEnabled` is set to false. It can also be used to capture some network requests that don't make use of `dart:io`'s http internals, such as those made through the `cupertino_http` library, which are not recorded by automatic network capture.

```dart Flutter
var httpClient = LogRocketHttpClient();

await httpClient.get(Uri.https('example.com')));

await httpClient.post(
  Uri.https('example.com', 'whatsit/create'),
  body: jsonEncode({
    'key': 'value',
    'uid': 1234,
    'isTrue': true,
    'nested': {
      'child': 'value'
    },
  }),
  headers: {'Content-Type': 'application/json'}
);
```

The `LogRocketHttpClient` supports all [BaseClient](https://pub.dev/documentation/http/latest/http/BaseClient-class.html) methods. The client will only capture bodies for [Request](https://pub.dev/documentation/http/latest/http/Request-class.html) types requests in the session, which is the default for most methods. `MultipartRequests` and `StreamedRequests` sent directly through the `send` method will not include request bodies in replay.

The `LogRocketHttpClient` can also be used to wrap other `http` clients. Network request and response details will be captured in LogRocket, but the requests will be executed by the underlying `httpClient`.

```dart Flutter
var customLrClient = LogRocketHttpClient(httpClient: CustomClient());
```

## Sanitize Network Data

The `LogRocketWrapConfiguration` and `LogRocketHttpClient` both include 2 optional parameters to sanitize request and response data. When defining network sanitizers, we recommend thoroughly testing your implementations and confirming the data appears in session replay as you'd expect before releasing them to production.

```dart Flutter
// Automatic capture config
LogRocketWrapConfiguration(
  networkCaptureEnabled: true,
  requestSanitizer: myRequestSanitizerFunction,
  responseSanitizer: myResponseSanitizerFunction,
)

// Manual capture config
var httpClient = LogRocketHttpClient(
  requestSanitizer: myRequestSanitizerFunction,
  responseSanitizer: myResponseSanitizerFunction,
)
```

### requestSanitizer

The `requestSanitizer` can be used to modify the request's `url`, `headers`, `method`, and `body` values as they are captured and displayed in LogRocket. Changing these values in the request sanitizer has no effect on the actual request.

Returning `null` from the request sanitizer will cause the LogRocket SDK to completely ignore that request. It will not appear in any form within LogRocket.

#### Example:

```dart Flutter
var excludedDomains = ['https://example.com', 'https://test.com'];

LogRocketNetworkRequest? myRequestSanitizer (LogRocketNetworkRequest request) {
  if (excludedDomains.any(url => request.url.startsWith(excludedDomain))) {
    // exclude the request from the LogRocket session
    return null;
  } else if (request.url.contains('sensitive')) {
    // capture the request without the request headers or the request bodies
    request.headers = null;
    request.body = "";
  } else {
    try {
      // remove a field from the captured request body
      Map<String, dynamic> bodyMap = jsonDecode(response.body);
      bodyMap.remove('sensitiveField');
      response.body = jsonEncode(bodyMap);
    } catch (e) {}
  }
  return request;
}

// In automatic capture config
LogRocketWrapConfiguration(
  requestSanitizer: myRequestSanitizer,
)

// In manual capture config
var httpClient = LogRocketHttpClient(
  requestSanitizer: myRequestSanitizer,
)
```

### responseSanitizer

The `responseSanitizer` can be used to modify a response's  `headers`, `status`, and `body` values as they are captured and displayed in LogRocket. Changing these values in the response sanitizer has no effect on the actual response.

See  [requestSanitizer](#requestsanitizer) for details on how to completely exclude a request/response pair.

#### Example

```dart Flutter
LogRocketNetworkResponse myResponseSanitizer (LogRocketNetworkResponse response) {
  // always remove a certain header
  response.headers.remove('x-api-key`)
  try {
    // remove a field from the captured response body
    Map<String, dynamic> bodyMap = jsonDecode(response.body);
    bodyMap.remove('sensitiveField');
    response.body = jsonEncode(bodyMap);
  } catch (e) {}
  return response;
}

// In automatic capture config
LogRocketWrapConfiguration(
  responseSanitizer: myResponseSanitizer,
)

// In manual capture config
var httpClient = LogRocketHttpClient(
  responseSanitizer: myResponseSanitizer,
)
```