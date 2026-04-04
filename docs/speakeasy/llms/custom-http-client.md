# Source: https://www.speakeasy.com/md/docs/sdks/customize/runtime/custom-http-client.md

# Use Custom HTTP Clients

SDK users can provide a custom HTTP client when initializing SDKs. This is useful for modifying or debugging requests and responses in flight.

See below for per-language examples:

Go:
```go
/* The Go SDK will accept a client that implements a 
     `Do(*http.Request) (*http.Response, error)` method similar 
     to the standard library's `http.Client`. */

  // A custom HTTP client that implements caching
  c := NewCachedClient(&http.Client{}, cache)

  opts := []sdk.SDKOption{
      sdk.WithClient(c),
  }

  s := sdk.New(opts)
```

Python:
```python
# The Python SDK will accept any client that implements the 
  # `HttpClient` interface from the SDK. Here's an example using the 
  # [`requests`](https://requests.readthedocs.io/en/latest/) library:

  import requests
  from sdk import SDK, HttpClient

  # Define a custom HTTP client using Requests
  class RequestsHttpClient(HttpClient):
      def __init__(self):
          self.session = requests.Session()

      def send(self, request, **kwargs):
          return self.session.send(request.prepare())

      def build_request(
          self,
          method,
          url,
          *,
          content = None,
          headers = None,
          **kwargs,
      ):
          return requests.Request(
              method=method,
              url=url,
              data=content,
              headers=headers,
          )

  # Initialize the custom client
  client = RequestsHttpClient()

  # Initialize the SDK with the custom client
  sdk = SDK(client=client)

  # Use the SDK client
  res = sdk.method_name()
```

TypeScript:
```typescript
/* The TypeScript SDK makes API calls using an `HTTPClient`
  that wraps the native [Fetch API]
  (https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).
  This client is a thin wrapper around `fetch` and provides the ability 
  to attach hooks around the request lifecycle that can be used to modify 
  the request or handleerrors and response. */

import { SDK } from "openapi";
import { HTTPClient } from "openapi/dist/commonjs/lib/http";

// Create an HTTPClient instance with the default fetcher
const httpClient = new HTTPClient({
  // fetcher takes a function that has the same signature as native `fetch`.
  fetcher: async (request) => fetch(request),
});

httpClient.addHook("requestError", (err) => {
  console.log(`Request failed: ${err}`);
});

// Initialize the SDK with the custom HTTP client
const sdk = new SDK({ httpClient });
```

Java:
```java
/* The Java SDK will accept a client that implements the 
  `HTTPClient` interface in the `utils` package. This will wrap 
  a `java.net.http.HttpClient` instance and the call to `send`. */

  // Custom HTTP client
  YouHttpClient client = new YourHttpClient();

  SDK.Builder builder = SDK.builder();

  builder.setClient(client);

  SDK sdk = builder.build();
```

C#:
```csharp
/* YourHttpClient must implement the ISpeakeasyHttpClient interface */

var httpClient = new YourHttpClient();
// Initialize the SDK with the custom HTTP client
var sdk = new SDK(client: httpClient);
```
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
