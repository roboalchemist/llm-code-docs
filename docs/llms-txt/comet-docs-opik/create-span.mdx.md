# Source: https://www.comet.com/docs/opik/reference/rest-api/spans/create-span.mdx

# Create span

POST http://localhost:5173/api/v1/private/spans
Content-Type: application/json

Create span

Reference: https://www.comet.com/docs/opik/reference/rest-api/spans/create-span

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/spans:
    post:
      operationId: create-span
      summary: Create span
      description: Create span
      tags:
        - subpackage_spans
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Spans_createSpan_Response_201'
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Span_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    SpanWriteType:
      type: string
      enum:
        - general
        - tool
        - llm
        - guardrail
      title: SpanWriteType
    JsonListStringWriteOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringWriteOneOf1Items
    JsonListStringWrite1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringWriteOneOf1Items'
      title: JsonListStringWrite1
    JsonListString_Write:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListStringWrite1'
        - type: string
      title: JsonListString_Write
    ErrorInfo_Write:
      type: object
      properties:
        exception_type:
          type: string
        message:
          type: string
        traceback:
          type: string
      required:
        - exception_type
        - traceback
      title: ErrorInfo_Write
    Span_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_name:
          type: string
          description: If null, the default project is used
        trace_id:
          type: string
          format: uuid
        parent_span_id:
          type: string
          format: uuid
        name:
          type: string
        type:
          $ref: '#/components/schemas/SpanWriteType'
        start_time:
          type: string
          format: date-time
        end_time:
          type: string
          format: date-time
        input:
          $ref: '#/components/schemas/JsonListString_Write'
        output:
          $ref: '#/components/schemas/JsonListString_Write'
        metadata:
          $ref: '#/components/schemas/JsonListString_Write'
        model:
          type: string
        provider:
          type: string
        tags:
          type: array
          items:
            type: string
        usage:
          type: object
          additionalProperties:
            type: integer
        error_info:
          $ref: '#/components/schemas/ErrorInfo_Write'
        last_updated_at:
          type: string
          format: date-time
        total_estimated_cost:
          type: number
          format: double
        total_estimated_cost_version:
          type: string
        ttft:
          type: number
          format: double
          description: Time to first token in milliseconds
      required:
        - start_time
      title: Span_Write
    Spans_createSpan_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Spans_createSpan_Response_201
    ErrorMessage:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/spans"

payload = { "start_time": "2024-01-15T09:30:00Z" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/spans';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"start_time":"2024-01-15T09:30:00Z"}'
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

	url := "http://localhost:5173/api/v1/private/spans"

	payload := strings.NewReader("{\n  \"start_time\": \"2024-01-15T09:30:00Z\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/spans")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"start_time\": \"2024-01-15T09:30:00Z\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/spans")
  .header("Content-Type", "application/json")
  .body("{\n  \"start_time\": \"2024-01-15T09:30:00Z\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/spans', [
  'body' => '{
  "start_time": "2024-01-15T09:30:00Z"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/spans");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"start_time\": \"2024-01-15T09:30:00Z\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["start_time": "2024-01-15T09:30:00Z"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/spans")! as URL,
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