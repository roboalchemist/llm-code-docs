# Source: https://www.comet.com/docs/opik/reference/rest-api/open-telemetry-ingestion/receive-protobuf-traces.mdx

# Receive Protobuf Traces

POST http://localhost:5173/api/v1/private/otel/v1/traces

Reference: https://www.comet.com/docs/opik/reference/rest-api/open-telemetry-ingestion/receive-protobuf-traces

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/otel/v1/traces:
    post:
      operationId: receive-protobuf-traces
      summary: Receive Protobuf Traces
      tags:
        - subpackage_openTelemetryIngestion
      responses:
        '200':
          description: Successful response
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/otel/v1/traces"

response = requests.post(url)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/otel/v1/traces';
const options = {method: 'POST'};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "http://localhost:5173/api/v1/private/otel/v1/traces"

	req, _ := http.NewRequest("POST", url, nil)

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("http://localhost:5173/api/v1/private/otel/v1/traces")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/otel/v1/traces")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/otel/v1/traces');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/otel/v1/traces");
var request = new RestRequest(Method.POST);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/otel/v1/traces")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```