# Source: https://www.comet.com/docs/opik/reference/rest-api/manual-evaluation/evaluate-threads.mdx

# Manually evaluate threads

POST http://localhost:5173/api/v1/private/manual-evaluation/threads
Content-Type: application/json

Manually trigger evaluation rules on selected threads. Bypasses sampling and enqueues all specified threads for evaluation.

Reference: https://www.comet.com/docs/opik/reference/rest-api/manual-evaluation/evaluate-threads

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/manual-evaluation/threads:
    post:
      operationId: evaluate-threads
      summary: Manually evaluate threads
      description: >-
        Manually trigger evaluation rules on selected threads. Bypasses sampling
        and enqueues all specified threads for evaluation.
      tags:
        - subpackage_manualEvaluation
      responses:
        '202':
          description: Accepted - Evaluation request queued successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ManualEvaluationResponse'
        '400':
          description: Bad Request - Invalid request or missing automation rules
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '404':
          description: Not Found - Project not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ManualEvaluationRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ManualEvaluationRequestEntityType:
      type: string
      enum:
        - trace
        - thread
        - span
      description: Type of entity to evaluate (trace or thread)
      title: ManualEvaluationRequestEntityType
    ManualEvaluationRequest:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
          description: Project ID
        entity_ids:
          type: array
          items:
            type: string
            format: uuid
          description: List of entity IDs (trace IDs or thread IDs) to evaluate
        rule_ids:
          type: array
          items:
            type: string
            format: uuid
          description: List of automation rule IDs to apply
        entity_type:
          $ref: '#/components/schemas/ManualEvaluationRequestEntityType'
          description: Type of entity to evaluate (trace or thread)
      required:
        - project_id
        - entity_ids
        - rule_ids
        - entity_type
      title: ManualEvaluationRequest
    ManualEvaluationResponse:
      type: object
      properties:
        entities_queued:
          type: integer
          description: Number of entities queued for evaluation
        rules_applied:
          type: integer
          description: Number of rules that will be applied
      title: ManualEvaluationResponse
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

url = "http://localhost:5173/api/v1/private/manual-evaluation/threads"

payload = {
    "project_id": "550e8400-e29b-41d4-a716-446655440000",
    "entity_ids": ["550e8400-e29b-41d4-a716-446655440000", "550e8400-e29b-41d4-a716-446655440001"],
    "rule_ids": ["660e8400-e29b-41d4-a716-446655440000"],
    "entity_type": "trace"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/manual-evaluation/threads';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"project_id":"550e8400-e29b-41d4-a716-446655440000","entity_ids":["550e8400-e29b-41d4-a716-446655440000","550e8400-e29b-41d4-a716-446655440001"],"rule_ids":["660e8400-e29b-41d4-a716-446655440000"],"entity_type":"trace"}'
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

	url := "http://localhost:5173/api/v1/private/manual-evaluation/threads"

	payload := strings.NewReader("{\n  \"project_id\": \"550e8400-e29b-41d4-a716-446655440000\",\n  \"entity_ids\": [\n    \"550e8400-e29b-41d4-a716-446655440000\",\n    \"550e8400-e29b-41d4-a716-446655440001\"\n  ],\n  \"rule_ids\": [\n    \"660e8400-e29b-41d4-a716-446655440000\"\n  ],\n  \"entity_type\": \"trace\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/manual-evaluation/threads")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"project_id\": \"550e8400-e29b-41d4-a716-446655440000\",\n  \"entity_ids\": [\n    \"550e8400-e29b-41d4-a716-446655440000\",\n    \"550e8400-e29b-41d4-a716-446655440001\"\n  ],\n  \"rule_ids\": [\n    \"660e8400-e29b-41d4-a716-446655440000\"\n  ],\n  \"entity_type\": \"trace\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/manual-evaluation/threads")
  .header("Content-Type", "application/json")
  .body("{\n  \"project_id\": \"550e8400-e29b-41d4-a716-446655440000\",\n  \"entity_ids\": [\n    \"550e8400-e29b-41d4-a716-446655440000\",\n    \"550e8400-e29b-41d4-a716-446655440001\"\n  ],\n  \"rule_ids\": [\n    \"660e8400-e29b-41d4-a716-446655440000\"\n  ],\n  \"entity_type\": \"trace\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/manual-evaluation/threads', [
  'body' => '{
  "project_id": "550e8400-e29b-41d4-a716-446655440000",
  "entity_ids": [
    "550e8400-e29b-41d4-a716-446655440000",
    "550e8400-e29b-41d4-a716-446655440001"
  ],
  "rule_ids": [
    "660e8400-e29b-41d4-a716-446655440000"
  ],
  "entity_type": "trace"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/manual-evaluation/threads");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"project_id\": \"550e8400-e29b-41d4-a716-446655440000\",\n  \"entity_ids\": [\n    \"550e8400-e29b-41d4-a716-446655440000\",\n    \"550e8400-e29b-41d4-a716-446655440001\"\n  ],\n  \"rule_ids\": [\n    \"660e8400-e29b-41d4-a716-446655440000\"\n  ],\n  \"entity_type\": \"trace\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "project_id": "550e8400-e29b-41d4-a716-446655440000",
  "entity_ids": ["550e8400-e29b-41d4-a716-446655440000", "550e8400-e29b-41d4-a716-446655440001"],
  "rule_ids": ["660e8400-e29b-41d4-a716-446655440000"],
  "entity_type": "trace"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/manual-evaluation/threads")! as URL,
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