# Source: https://www.comet.com/docs/opik/reference/rest-api/guardrails/create-guardrails.mdx

# Create guardrails for traces in a batch

POST http://localhost:5173/api/v1/private/guardrails
Content-Type: application/json

Batch guardrails for traces

Reference: https://www.comet.com/docs/opik/reference/rest-api/guardrails/create-guardrails

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/guardrails:
    post:
      operationId: create-guardrails
      summary: Create guardrails for traces in a batch
      description: Batch guardrails for traces
      tags:
        - subpackage_guardrails
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Guardrails_createGuardrails_Response_204'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GuardrailBatch_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    GuardrailWriteName:
      type: string
      enum:
        - TOPIC
        - PII
      title: GuardrailWriteName
    GuardrailWriteResult:
      type: string
      enum:
        - passed
        - failed
      title: GuardrailWriteResult
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    Guardrail_Write:
      type: object
      properties:
        entity_id:
          type: string
          format: uuid
        secondary_id:
          type: string
          format: uuid
        project_name:
          type: string
          description: If null, the default project is used
        project_id:
          type: string
          format: uuid
        name:
          $ref: '#/components/schemas/GuardrailWriteName'
        result:
          $ref: '#/components/schemas/GuardrailWriteResult'
        config:
          $ref: '#/components/schemas/JsonNode'
        details:
          $ref: '#/components/schemas/JsonNode'
      required:
        - entity_id
        - secondary_id
        - name
        - result
        - config
        - details
      title: Guardrail_Write
    GuardrailBatch_Write:
      type: object
      properties:
        guardrails:
          type: array
          items:
            $ref: '#/components/schemas/Guardrail_Write'
      required:
        - guardrails
      title: GuardrailBatch_Write
    Guardrails_createGuardrails_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Guardrails_createGuardrails_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/guardrails"

payload = { "guardrails": [
        {
            "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "secondary_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
            "name": "TOPIC",
            "result": "passed",
            "config": {},
            "details": {}
        }
    ] }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/guardrails';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"guardrails":[{"entity_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","secondary_id":"7c9e6679-7425-40de-944b-e07fc1f90ae7","name":"TOPIC","result":"passed","config":{},"details":{}}]}'
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

	url := "http://localhost:5173/api/v1/private/guardrails"

	payload := strings.NewReader("{\n  \"guardrails\": [\n    {\n      \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"secondary_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"name\": \"TOPIC\",\n      \"result\": \"passed\",\n      \"config\": {},\n      \"details\": {}\n    }\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/guardrails")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"guardrails\": [\n    {\n      \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"secondary_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"name\": \"TOPIC\",\n      \"result\": \"passed\",\n      \"config\": {},\n      \"details\": {}\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/guardrails")
  .header("Content-Type", "application/json")
  .body("{\n  \"guardrails\": [\n    {\n      \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"secondary_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"name\": \"TOPIC\",\n      \"result\": \"passed\",\n      \"config\": {},\n      \"details\": {}\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/guardrails', [
  'body' => '{
  "guardrails": [
    {
      "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "secondary_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "name": "TOPIC",
      "result": "passed",
      "config": {},
      "details": {}
    }
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/guardrails");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"guardrails\": [\n    {\n      \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"secondary_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"name\": \"TOPIC\",\n      \"result\": \"passed\",\n      \"config\": {},\n      \"details\": {}\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["guardrails": [
    [
      "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "secondary_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "name": "TOPIC",
      "result": "passed",
      "config": [],
      "details": []
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/guardrails")! as URL,
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