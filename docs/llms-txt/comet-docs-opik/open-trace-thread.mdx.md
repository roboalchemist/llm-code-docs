# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/open-trace-thread.mdx

# Open trace thread

PUT http://localhost:5173/api/v1/private/traces/threads/open
Content-Type: application/json

Open trace thread

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/open-trace-thread

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/threads/open:
    put:
      operationId: open-trace-thread
      summary: Open trace thread
      description: Open trace thread
      tags:
        - subpackage_traces
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Traces_openTraceThread_Response_204'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TraceThreadIdentifier'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    TraceThreadIdentifier:
      type: object
      properties:
        project_name:
          type: string
        project_id:
          type: string
          format: uuid
        thread_id:
          type: string
        truncate:
          type: boolean
      required:
        - thread_id
      title: TraceThreadIdentifier
    Traces_openTraceThread_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Traces_openTraceThread_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/threads/open"

payload = { "thread_id": "thread-9f8b7c6d5e4a3b2c1d0e" }
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/threads/open';
const options = {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: '{"thread_id":"thread-9f8b7c6d5e4a3b2c1d0e"}'
};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "http://localhost:5173/api/v1/private/traces/threads/open"

	payload := strings.NewReader("{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Content-Type", "application/json")

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

url = URI("http://localhost:5173/api/v1/private/traces/threads/open")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/traces/threads/open")
  .header("Content-Type", "application/json")
  .body("{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/traces/threads/open', [
  'body' => '{
  "thread_id": "thread-9f8b7c6d5e4a3b2c1d0e"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/threads/open");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["thread_id": "thread-9f8b7c6d5e4a3b2c1d0e"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/threads/open")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

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