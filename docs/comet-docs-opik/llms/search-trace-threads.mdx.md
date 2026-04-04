# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/search-trace-threads.mdx

# Search trace threads

POST http://localhost:5173/api/v1/private/traces/threads/search
Content-Type: application/json

Search trace threads

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/search-trace-threads

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/threads/search:
    post:
      operationId: search-trace-threads
      summary: Search trace threads
      description: Search trace threads
      tags:
        - subpackage_traces
      responses:
        '200':
          description: Trace threads stream or error during process
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Traces_searchTraceThreads_Response_200'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TraceThreadSearchStreamRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    TraceThreadFilterOperator:
      type: string
      enum:
        - contains
        - not_contains
        - starts_with
        - ends_with
        - '='
        - '!='
        - '>'
        - '>='
        - <
        - <=
        - is_empty
        - is_not_empty
      title: TraceThreadFilterOperator
    TraceThreadFilter:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/TraceThreadFilterOperator'
        key:
          type: string
        value:
          type: string
      title: TraceThreadFilter
    TraceThreadSearchStreamRequest:
      type: object
      properties:
        project_name:
          type: string
        project_id:
          type: string
          format: uuid
        filters:
          type: array
          items:
            $ref: '#/components/schemas/TraceThreadFilter'
        last_retrieved_thread_model_id:
          type: string
          format: uuid
        limit:
          type: integer
          default: 500
          description: Max number of trace thread to be streamed
        truncate:
          type: boolean
          default: true
          description: Truncate input, output and metadata to slim payloads
        strip_attachments:
          type: boolean
          default: false
          description: >-
            If true, returns attachment references like [file.png]; if false,
            downloads and reinjects stripped attachments
        from_time:
          type: string
          format: date-time
          description: Filter trace threads created from this time (ISO-8601 format).
        to_time:
          type: string
          format: date-time
          description: >-
            Filter trace threads created up to this time (ISO-8601 format). If
            not provided, defaults to current time. Must be after 'from_time'.
      title: TraceThreadSearchStreamRequest
    Traces_searchTraceThreads_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: Traces_searchTraceThreads_Response_200

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/threads/search"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/threads/search';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/traces/threads/search"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/traces/threads/search")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/traces/threads/search")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/traces/threads/search', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/threads/search");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/threads/search")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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