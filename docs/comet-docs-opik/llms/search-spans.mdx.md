# Source: https://www.comet.com/docs/opik/reference/rest-api/spans/search-spans.mdx

# Search spans

POST http://localhost:5173/api/v1/private/spans/search
Content-Type: application/json

Search spans

Reference: https://www.comet.com/docs/opik/reference/rest-api/spans/search-spans

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/spans/search:
    post:
      operationId: search-spans
      summary: Search spans
      description: Search spans
      tags:
        - subpackage_spans
      responses:
        '200':
          description: Spans stream or error during process
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Spans_searchSpans_Response_200'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SpanSearchStreamRequest_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    SpanSearchStreamRequestPublicType:
      type: string
      enum:
        - general
        - tool
        - llm
        - guardrail
      title: SpanSearchStreamRequestPublicType
    SpanFilterPublicOperator:
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
      title: SpanFilterPublicOperator
    SpanFilter_Public:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/SpanFilterPublicOperator'
        key:
          type: string
        value:
          type: string
      title: SpanFilter_Public
    SpanSearchStreamRequest_Public:
      type: object
      properties:
        trace_id:
          type: string
          format: uuid
        project_name:
          type: string
        project_id:
          type: string
          format: uuid
        type:
          $ref: '#/components/schemas/SpanSearchStreamRequestPublicType'
        filters:
          type: array
          items:
            $ref: '#/components/schemas/SpanFilter_Public'
        limit:
          type: integer
          default: 500
          description: Max number of spans to be streamed
        last_retrieved_id:
          type: string
          format: uuid
        truncate:
          type: boolean
          default: true
          description: Truncate image included in either input, output or metadata
        from_time:
          type: string
          format: date-time
          description: Filter spans created from this time (ISO-8601 format).
        to_time:
          type: string
          format: date-time
          description: >-
            Filter spans created up to this time (ISO-8601 format). If not
            provided, defaults to current time. Must be after 'from_time'.
      title: SpanSearchStreamRequest_Public
    Spans_searchSpans_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: Spans_searchSpans_Response_200

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/spans/search"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/spans/search';
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

	url := "http://localhost:5173/api/v1/private/spans/search"

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

url = URI("http://localhost:5173/api/v1/private/spans/search")

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

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/spans/search")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/spans/search', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/spans/search");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/spans/search")! as URL,
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