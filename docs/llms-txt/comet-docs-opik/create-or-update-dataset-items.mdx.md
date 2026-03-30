# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-or-update-dataset-items.mdx

# Create/update dataset items

PUT http://localhost:5173/api/v1/private/datasets/items
Content-Type: application/json

Create/update dataset items based on dataset item id

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-or-update-dataset-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/items:
    put:
      operationId: create-or-update-dataset-items
      summary: Create/update dataset items
      description: Create/update dataset items based on dataset item id
      tags:
        - subpackage_datasets
      responses:
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Datasets_createOrUpdateDatasetItems_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetItemBatch_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetItemWriteSource:
      type: string
      enum:
        - manual
        - trace
        - span
        - sdk
      title: DatasetItemWriteSource
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    EvaluatorItemWriteType:
      type: string
      enum:
        - llm_judge
        - code_metric
      title: EvaluatorItemWriteType
    JsonNode_Write:
      type: object
      properties: {}
      title: JsonNode_Write
    EvaluatorItem_Write:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/EvaluatorItemWriteType'
        config:
          $ref: '#/components/schemas/JsonNode_Write'
      required:
        - name
        - type
        - config
      title: EvaluatorItem_Write
    ExecutionPolicy_Write:
      type: object
      properties:
        runs_per_item:
          type: integer
        pass_threshold:
          type: integer
      title: ExecutionPolicy_Write
    DatasetItem_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        trace_id:
          type: string
          format: uuid
        span_id:
          type: string
          format: uuid
        source:
          $ref: '#/components/schemas/DatasetItemWriteSource'
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
            $ref: '#/components/schemas/EvaluatorItem_Write'
        execution_policy:
          $ref: '#/components/schemas/ExecutionPolicy_Write'
      required:
        - source
        - data
      title: DatasetItem_Write
    DatasetItemBatch_Write:
      type: object
      properties:
        dataset_name:
          type: string
          description: If null, dataset_id must be provided
        dataset_id:
          type: string
          format: uuid
          description: If null, dataset_name must be provided
        items:
          type: array
          items:
            $ref: '#/components/schemas/DatasetItem_Write'
        batch_group_id:
          type: string
          format: uuid
          description: >-
            Optional batch group ID to group multiple batches into a single
            dataset version. If null, mutates the latest version instead of
            creating a new one.
      required:
        - items
      title: DatasetItemBatch_Write
    Datasets_createOrUpdateDatasetItems_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_createOrUpdateDatasetItems_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/items"

payload = { "items": [
        {
            "source": "manual",
            "data": {}
        }
    ] }
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/items';
const options = {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: '{"items":[{"source":"manual","data":{}}]}'
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

	url := "http://localhost:5173/api/v1/private/datasets/items"

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"source\": \"manual\",\n      \"data\": {}\n    }\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/items")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"source\": \"manual\",\n      \"data\": {}\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/datasets/items")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"source\": \"manual\",\n      \"data\": {}\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/datasets/items', [
  'body' => '{
  "items": [
    {
      "source": "manual",
      "data": {}
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

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/items");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"source\": \"manual\",\n      \"data\": {}\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["items": [
    [
      "source": "manual",
      "data": []
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/items")! as URL,
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