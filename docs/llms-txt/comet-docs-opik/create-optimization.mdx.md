# Source: https://www.comet.com/docs/opik/reference/rest-api/optimizations/create-optimization.mdx

# Create optimization

POST http://localhost:5173/api/v1/private/optimizations
Content-Type: application/json

Create optimization

Reference: https://www.comet.com/docs/opik/reference/rest-api/optimizations/create-optimization

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/optimizations:
    post:
      operationId: create-optimization
      summary: Create optimization
      description: Create optimization
      tags:
        - subpackage_optimizations
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Optimizations_createOptimization_Response_201
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Optimization_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    OptimizationWriteStatus:
      type: string
      enum:
        - running
        - completed
        - cancelled
        - initialized
        - error
      title: OptimizationWriteStatus
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
    StudioMessage_Write:
      type: object
      properties:
        role:
          type: string
        content:
          type: string
      required:
        - role
        - content
      title: StudioMessage_Write
    StudioPrompt_Write:
      type: object
      properties:
        messages:
          type: array
          items:
            $ref: '#/components/schemas/StudioMessage_Write'
      required:
        - messages
      title: StudioPrompt_Write
    JsonNode_Write:
      type: object
      properties: {}
      title: JsonNode_Write
    StudioLlmModel_Write:
      type: object
      properties:
        model:
          type: string
        parameters:
          $ref: '#/components/schemas/JsonNode_Write'
      required:
        - model
      title: StudioLlmModel_Write
    StudioMetric_Write:
      type: object
      properties:
        type:
          type: string
        parameters:
          $ref: '#/components/schemas/JsonNode_Write'
      required:
        - type
      title: StudioMetric_Write
    StudioEvaluation_Write:
      type: object
      properties:
        metrics:
          type: array
          items:
            $ref: '#/components/schemas/StudioMetric_Write'
      required:
        - metrics
      title: StudioEvaluation_Write
    StudioOptimizer_Write:
      type: object
      properties:
        type:
          type: string
        parameters:
          $ref: '#/components/schemas/JsonNode_Write'
      required:
        - type
      title: StudioOptimizer_Write
    OptimizationStudioConfig_Write:
      type: object
      properties:
        dataset_name:
          type: string
        prompt:
          $ref: '#/components/schemas/StudioPrompt_Write'
        llm_model:
          $ref: '#/components/schemas/StudioLlmModel_Write'
        evaluation:
          $ref: '#/components/schemas/StudioEvaluation_Write'
        optimizer:
          $ref: '#/components/schemas/StudioOptimizer_Write'
      required:
        - dataset_name
        - prompt
        - llm_model
        - evaluation
        - optimizer
      title: OptimizationStudioConfig_Write
    Optimization_Write:
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
          $ref: '#/components/schemas/OptimizationWriteStatus'
        metadata:
          $ref: '#/components/schemas/JsonListString_Write'
        studio_config:
          $ref: '#/components/schemas/OptimizationStudioConfig_Write'
        last_updated_at:
          type: string
          format: date-time
      required:
        - dataset_name
        - objective_name
        - status
      title: Optimization_Write
    Optimizations_createOptimization_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Optimizations_createOptimization_Response_201

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/optimizations"

payload = {
    "dataset_name": "customer_churn_data",
    "objective_name": "maximize_accuracy",
    "status": "running"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/optimizations';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"dataset_name":"customer_churn_data","objective_name":"maximize_accuracy","status":"running"}'
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

	url := "http://localhost:5173/api/v1/private/optimizations"

	payload := strings.NewReader("{\n  \"dataset_name\": \"customer_churn_data\",\n  \"objective_name\": \"maximize_accuracy\",\n  \"status\": \"running\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/optimizations")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"dataset_name\": \"customer_churn_data\",\n  \"objective_name\": \"maximize_accuracy\",\n  \"status\": \"running\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/optimizations")
  .header("Content-Type", "application/json")
  .body("{\n  \"dataset_name\": \"customer_churn_data\",\n  \"objective_name\": \"maximize_accuracy\",\n  \"status\": \"running\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/optimizations', [
  'body' => '{
  "dataset_name": "customer_churn_data",
  "objective_name": "maximize_accuracy",
  "status": "running"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/optimizations");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"dataset_name\": \"customer_churn_data\",\n  \"objective_name\": \"maximize_accuracy\",\n  \"status\": \"running\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "dataset_name": "customer_churn_data",
  "objective_name": "maximize_accuracy",
  "status": "running"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/optimizations")! as URL,
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