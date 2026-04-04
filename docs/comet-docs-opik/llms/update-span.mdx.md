# Source: https://www.comet.com/docs/opik/reference/rest-api/spans/update-span.mdx

# Update span by id

PATCH http://localhost:5173/api/v1/private/spans/{id}
Content-Type: application/json

Update span by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/spans/update-span

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/spans/{id}:
    patch:
      operationId: update-span
      summary: Update span by id
      description: Update span by id
      tags:
        - subpackage_spans
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Spans_updateSpan_Response_204'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SpanUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    SpanUpdateType:
      type: string
      enum:
        - general
        - tool
        - llm
        - guardrail
      title: SpanUpdateType
    JsonListStringOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringOneOf1Items
    JsonListString1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringOneOf1Items'
      title: JsonListString1
    JsonListString:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListString1'
        - type: string
      title: JsonListString
    ErrorInfo:
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
      title: ErrorInfo
    SpanUpdate:
      type: object
      properties:
        project_name:
          type: string
          description: If null and project_id not specified, Default Project is assumed
        project_id:
          type: string
          format: uuid
          description: If null and project_name not specified, Default Project is assumed
        trace_id:
          type: string
          format: uuid
        parent_span_id:
          type: string
          format: uuid
        name:
          type: string
        type:
          $ref: '#/components/schemas/SpanUpdateType'
        end_time:
          type: string
          format: date-time
        input:
          $ref: '#/components/schemas/JsonListString'
        output:
          $ref: '#/components/schemas/JsonListString'
        metadata:
          $ref: '#/components/schemas/JsonListString'
        model:
          type: string
        provider:
          type: string
        tags:
          type: array
          items:
            type: string
          description: Tags
        tags_to_add:
          type: array
          items:
            type: string
          description: Tags to add
        tags_to_remove:
          type: array
          items:
            type: string
          description: Tags to remove
        usage:
          type: object
          additionalProperties:
            type: integer
        total_estimated_cost:
          type: number
          format: double
        error_info:
          $ref: '#/components/schemas/ErrorInfo'
        ttft:
          type: number
          format: double
      required:
        - trace_id
      title: SpanUpdate
    Spans_updateSpan_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Spans_updateSpan_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/spans/id"

payload = { "trace_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/spans/id';
const options = {
  method: 'PATCH',
  headers: {'Content-Type': 'application/json'},
  body: '{"trace_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6"}'
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

	url := "http://localhost:5173/api/v1/private/spans/id"

	payload := strings.NewReader("{\n  \"trace_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/spans/id")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"trace_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/spans/id")
  .header("Content-Type", "application/json")
  .body("{\n  \"trace_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/spans/id', [
  'body' => '{
  "trace_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/spans/id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"trace_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["trace_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/spans/id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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