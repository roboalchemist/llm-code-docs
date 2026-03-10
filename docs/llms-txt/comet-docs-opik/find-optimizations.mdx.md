# Source: https://www.comet.com/docs/opik/reference/rest-api/optimizations/find-optimizations.mdx

# Find optimizations

GET http://localhost:5173/api/v1/private/optimizations

Find optimizations

Reference: https://www.comet.com/docs/opik/reference/rest-api/optimizations/find-optimizations

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/optimizations:
    get:
      operationId: find-optimizations
      summary: Find optimizations
      description: Find optimizations
      tags:
        - subpackage_optimizations
      parameters:
        - name: page
          in: query
          required: false
          schema:
            type: integer
            default: 1
        - name: size
          in: query
          required: false
          schema:
            type: integer
            default: 10
        - name: dataset_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
        - name: name
          in: query
          required: false
          schema:
            type: string
        - name: dataset_deleted
          in: query
          required: false
          schema:
            type: boolean
        - name: filters
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Optimizations resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OptimizationPage_Public'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    OptimizationPublicStatus:
      type: string
      enum:
        - running
        - completed
        - cancelled
        - initialized
        - error
      title: OptimizationPublicStatus
    JsonListStringPublicOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringPublicOneOf1Items
    JsonListStringPublic1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringPublicOneOf1Items'
      title: JsonListStringPublic1
    JsonListString_Public:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListStringPublic1'
        - type: string
      title: JsonListString_Public
    StudioMessage_Public:
      type: object
      properties:
        role:
          type: string
        content:
          type: string
      required:
        - role
        - content
      title: StudioMessage_Public
    StudioPrompt_Public:
      type: object
      properties:
        messages:
          type: array
          items:
            $ref: '#/components/schemas/StudioMessage_Public'
      required:
        - messages
      title: StudioPrompt_Public
    JsonNode_Public:
      type: object
      properties: {}
      title: JsonNode_Public
    StudioLlmModel_Public:
      type: object
      properties:
        model:
          type: string
        parameters:
          $ref: '#/components/schemas/JsonNode_Public'
      required:
        - model
      title: StudioLlmModel_Public
    StudioMetric_Public:
      type: object
      properties:
        type:
          type: string
        parameters:
          $ref: '#/components/schemas/JsonNode_Public'
      required:
        - type
      title: StudioMetric_Public
    StudioEvaluation_Public:
      type: object
      properties:
        metrics:
          type: array
          items:
            $ref: '#/components/schemas/StudioMetric_Public'
      required:
        - metrics
      title: StudioEvaluation_Public
    StudioOptimizer_Public:
      type: object
      properties:
        type:
          type: string
        parameters:
          $ref: '#/components/schemas/JsonNode_Public'
      required:
        - type
      title: StudioOptimizer_Public
    OptimizationStudioConfig_Public:
      type: object
      properties:
        dataset_name:
          type: string
        prompt:
          $ref: '#/components/schemas/StudioPrompt_Public'
        llm_model:
          $ref: '#/components/schemas/StudioLlmModel_Public'
        evaluation:
          $ref: '#/components/schemas/StudioEvaluation_Public'
        optimizer:
          $ref: '#/components/schemas/StudioOptimizer_Public'
      required:
        - dataset_name
        - prompt
        - llm_model
        - evaluation
        - optimizer
      title: OptimizationStudioConfig_Public
    FeedbackScoreAverage_Public:
      type: object
      properties:
        name:
          type: string
        value:
          type: number
          format: double
      required:
        - name
        - value
      title: FeedbackScoreAverage_Public
    Optimization_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        dataset_name:
          type: string
        objective_name:
          type: string
        status:
          $ref: '#/components/schemas/OptimizationPublicStatus'
        metadata:
          $ref: '#/components/schemas/JsonListString_Public'
        studio_config:
          $ref: '#/components/schemas/OptimizationStudioConfig_Public'
        dataset_id:
          type: string
          format: uuid
        num_trials:
          type: integer
          format: int64
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreAverage_Public'
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_at:
          type: string
          format: date-time
        last_updated_by:
          type: string
      required:
        - dataset_name
        - objective_name
        - status
      title: Optimization_Public
    OptimizationPage_Public:
      type: object
      properties:
        page:
          type: integer
        size:
          type: integer
        total:
          type: integer
          format: int64
        content:
          type: array
          items:
            $ref: '#/components/schemas/Optimization_Public'
        sortableBy:
          type: array
          items:
            type: string
      title: OptimizationPage_Public
    ErrorMessage_Public:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/optimizations"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/optimizations';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/optimizations"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/optimizations")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/optimizations")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/optimizations', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/optimizations");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/optimizations")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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