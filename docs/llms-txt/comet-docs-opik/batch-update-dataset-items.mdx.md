# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/batch-update-dataset-items.mdx

# Batch update dataset items

PATCH http://localhost:5173/api/v1/private/datasets/items/batch
Content-Type: application/json

Update multiple dataset items

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/batch-update-dataset-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/items/batch:
    patch:
      operationId: batch-update-dataset-items
      summary: Batch update dataset items
      description: Update multiple dataset items
      tags:
        - subpackage_datasets
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Datasets_batchUpdateDatasetItems_Response_204
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetItemBatchUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetItemFilterOperator:
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
      title: DatasetItemFilterOperator
    DatasetItemFilter:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/DatasetItemFilterOperator'
        key:
          type: string
        value:
          type: string
      description: >-
        Filters to select dataset items to delete within the specified dataset.
        Must be used with 'dataset_id'. Mutually exclusive with 'item_ids'.
        Empty array means 'delete all items in the dataset'.
      title: DatasetItemFilter
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    EvaluatorItemType:
      type: string
      enum:
        - llm_judge
        - code_metric
      title: EvaluatorItemType
    EvaluatorItem:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/EvaluatorItemType'
        config:
          $ref: '#/components/schemas/JsonNode'
      required:
        - name
        - type
        - config
      title: EvaluatorItem
    ExecutionPolicy:
      type: object
      properties:
        runs_per_item:
          type: integer
        pass_threshold:
          type: integer
      title: ExecutionPolicy
    DatasetItemUpdate:
      type: object
      properties:
        input:
          type: string
          description: Dataset item input
        expected_output:
          type: string
          description: Dataset item expected output
        metadata:
          $ref: '#/components/schemas/JsonNode'
        data:
          $ref: '#/components/schemas/JsonNode'
        description:
          type: string
          description: Dataset item description
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
        evaluators:
          type: array
          items:
            $ref: '#/components/schemas/EvaluatorItem'
          description: Evaluators
        execution_policy:
          $ref: '#/components/schemas/ExecutionPolicy'
        clear_execution_policy:
          type: boolean
          description: >-
            When true, clears the item-level execution policy (falls back to
            dataset-level)
      description: Dataset item update request
      title: DatasetItemUpdate
    DatasetItemBatchUpdate:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            List of dataset item IDs to update (max 1000). Mutually exclusive
            with 'filters'.
        filters:
          type: array
          items:
            $ref: '#/components/schemas/DatasetItemFilter'
        dataset_id:
          type: string
          format: uuid
          description: >-
            Dataset ID. Required when using 'filters', optional when using
            'ids'.
        update:
          $ref: '#/components/schemas/DatasetItemUpdate'
        merge_tags:
          type: boolean
          description: >-
            If true, merge tags with existing tags instead of replacing them.
            Default: false. When using 'filters', this is automatically set to
            true.
      required:
        - update
      description: Request to batch update multiple dataset items
      title: DatasetItemBatchUpdate
    Datasets_batchUpdateDatasetItems_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_batchUpdateDatasetItems_Response_204
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

url = "http://localhost:5173/api/v1/private/datasets/items/batch"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/items/batch';
const options = {method: 'PATCH', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/datasets/items/batch"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/items/batch")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/datasets/items/batch")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/datasets/items/batch', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/items/batch");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/items/batch")! as URL,
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