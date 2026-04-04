# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/get-dataset-item-by-id.mdx

# Get dataset item by id

GET http://localhost:5173/api/v1/private/datasets/items/{itemId}

Get dataset item by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/get-dataset-item-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/items/{itemId}:
    get:
      operationId: get-dataset-item-by-id
      summary: Get dataset item by id
      description: Get dataset item by id
      tags:
        - subpackage_datasets
      parameters:
        - name: itemId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Dataset item resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetItem_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetItemPublicSource:
      type: string
      enum:
        - manual
        - trace
        - span
        - sdk
      title: DatasetItemPublicSource
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    EvaluatorItemPublicType:
      type: string
      enum:
        - llm_judge
        - code_metric
      title: EvaluatorItemPublicType
    JsonNode_Public:
      type: object
      properties: {}
      title: JsonNode_Public
    EvaluatorItem_Public:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/EvaluatorItemPublicType'
        config:
          $ref: '#/components/schemas/JsonNode_Public'
      required:
        - name
        - type
        - config
      description: Default evaluators for items in this version
      title: EvaluatorItem_Public
    ExecutionPolicy_Public:
      type: object
      properties:
        runs_per_item:
          type: integer
        pass_threshold:
          type: integer
      description: Default execution policy for items in this version
      title: ExecutionPolicy_Public
    ExperimentItemPublicTraceVisibilityMode:
      type: string
      enum:
        - default
        - hidden
      title: ExperimentItemPublicTraceVisibilityMode
    ExperimentItem_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        experiment_id:
          type: string
          format: uuid
        dataset_item_id:
          type: string
          format: uuid
        trace_id:
          type: string
          format: uuid
        project_id:
          type: string
          format: uuid
        created_at:
          type: string
          format: date-time
        last_updated_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_by:
          type: string
        trace_visibility_mode:
          $ref: '#/components/schemas/ExperimentItemPublicTraceVisibilityMode'
      required:
        - experiment_id
        - dataset_item_id
        - trace_id
      title: ExperimentItem_Public
    DatasetItem_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        dataset_item_id:
          type: string
          format: uuid
        trace_id:
          type: string
          format: uuid
        span_id:
          type: string
          format: uuid
        source:
          $ref: '#/components/schemas/DatasetItemPublicSource'
        data:
          $ref: '#/components/schemas/JsonNode'
        description:
          type: string
        tags:
          type: array
          items:
            type: string
        evaluators:
          type: array
          items:
            $ref: '#/components/schemas/EvaluatorItem_Public'
        execution_policy:
          $ref: '#/components/schemas/ExecutionPolicy_Public'
        experiment_items:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentItem_Public'
        dataset_id:
          type: string
          format: uuid
        created_at:
          type: string
          format: date-time
        last_updated_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_by:
          type: string
      required:
        - source
        - data
      title: DatasetItem_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/items/itemId"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/items/itemId';
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

	url := "http://localhost:5173/api/v1/private/datasets/items/itemId"

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

url = URI("http://localhost:5173/api/v1/private/datasets/items/itemId")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/datasets/items/itemId")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/datasets/items/itemId', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/items/itemId");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/items/itemId")! as URL,
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