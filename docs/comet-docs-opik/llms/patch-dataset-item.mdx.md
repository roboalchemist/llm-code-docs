# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/patch-dataset-item.mdx

# Partially update dataset item by id

PATCH http://localhost:5173/api/v1/private/datasets/items/{itemId}
Content-Type: application/json

Partially update dataset item by id. Only provided fields will be updated.

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/patch-dataset-item

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/items/{itemId}:
    patch:
      operationId: patch-dataset-item
      summary: Partially update dataset item by id
      description: >-
        Partially update dataset item by id. Only provided fields will be
        updated.
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
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Datasets_patchDatasetItem_Response_204'
        '404':
          description: Dataset item not found
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetItem_Write'
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
    Datasets_patchDatasetItem_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_patchDatasetItem_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/items/itemId"

payload = { "source": "manual" }
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/items/itemId';
const options = {
  method: 'PATCH',
  headers: {'Content-Type': 'application/json'},
  body: '{"source":"manual"}'
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

	url := "http://localhost:5173/api/v1/private/datasets/items/itemId"

	payload := strings.NewReader("{\n  \"source\": \"manual\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/items/itemId")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"source\": \"manual\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/datasets/items/itemId")
  .header("Content-Type", "application/json")
  .body("{\n  \"source\": \"manual\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/datasets/items/itemId', [
  'body' => '{
  "source": "manual"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/items/itemId");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"source\": \"manual\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["source": "manual"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/items/itemId")! as URL,
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