# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/find-dataset-items-with-experiment-items.mdx

# Find dataset items with experiment items

GET http://localhost:5173/api/v1/private/datasets/{id}/items/experiments/items

Find dataset items with experiment items

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/find-dataset-items-with-experiment-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{id}/items/experiments/items:
    get:
      operationId: find-dataset-items-with-experiment-items
      summary: Find dataset items with experiment items
      description: Find dataset items with experiment items
      tags:
        - subpackage_datasets
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
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
        - name: experiment_ids
          in: query
          required: true
          schema:
            type: string
        - name: filters
          in: query
          required: false
          schema:
            type: string
        - name: sorting
          in: query
          required: false
          schema:
            type: string
        - name: search
          in: query
          required: false
          schema:
            type: string
        - name: truncate
          in: query
          required: false
          schema:
            type: boolean
      responses:
        '200':
          description: Dataset item resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetItemPage_Compare'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetItemCompareSource:
      type: string
      enum:
        - manual
        - trace
        - span
        - sdk
      title: DatasetItemCompareSource
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    EvaluatorItemCompareType:
      type: string
      enum:
        - llm_judge
        - code_metric
      title: EvaluatorItemCompareType
    JsonNode_Compare:
      type: object
      properties: {}
      title: JsonNode_Compare
    EvaluatorItem_Compare:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/EvaluatorItemCompareType'
        config:
          $ref: '#/components/schemas/JsonNode_Compare'
      required:
        - name
        - type
        - config
      title: EvaluatorItem_Compare
    ExecutionPolicy_Compare:
      type: object
      properties:
        runs_per_item:
          type: integer
        pass_threshold:
          type: integer
      title: ExecutionPolicy_Compare
    JsonListStringCompareOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringCompareOneOf1Items
    JsonListStringCompare1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringCompareOneOf1Items'
      title: JsonListStringCompare1
    JsonListString_Compare:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListStringCompare1'
        - type: string
      title: JsonListString_Compare
    FeedbackScoreCompareSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScoreCompareSource
    ValueEntryCompareSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: ValueEntryCompareSource
    ValueEntry_Compare:
      type: object
      properties:
        value:
          type: number
          format: double
        reason:
          type: string
        category_name:
          type: string
        source:
          $ref: '#/components/schemas/ValueEntryCompareSource'
        last_updated_at:
          type: string
          format: date-time
        span_type:
          type: string
        span_id:
          type: string
      title: ValueEntry_Compare
    FeedbackScore_Compare:
      type: object
      properties:
        name:
          type: string
        category_name:
          type: string
        value:
          type: number
          format: double
        reason:
          type: string
        source:
          $ref: '#/components/schemas/FeedbackScoreCompareSource'
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
        value_by_author:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ValueEntry_Compare'
      required:
        - name
        - value
        - source
      title: FeedbackScore_Compare
    Comment_Compare:
      type: object
      properties:
        id:
          type: string
          format: uuid
        text:
          type: string
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
        - text
      title: Comment_Compare
    ExperimentItemCompareTraceVisibilityMode:
      type: string
      enum:
        - default
        - hidden
      title: ExperimentItemCompareTraceVisibilityMode
    ExperimentItem_Compare:
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
        input:
          $ref: '#/components/schemas/JsonListString_Compare'
        output:
          $ref: '#/components/schemas/JsonListString_Compare'
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScore_Compare'
        comments:
          type: array
          items:
            $ref: '#/components/schemas/Comment_Compare'
        total_estimated_cost:
          type: number
          format: double
        duration:
          type: number
          format: double
        usage:
          type: object
          additionalProperties:
            type: integer
            format: int64
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
          $ref: '#/components/schemas/ExperimentItemCompareTraceVisibilityMode'
        description:
          type: string
      required:
        - experiment_id
        - dataset_item_id
        - trace_id
      title: ExperimentItem_Compare
    DatasetItem_Compare:
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
          $ref: '#/components/schemas/DatasetItemCompareSource'
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
            $ref: '#/components/schemas/EvaluatorItem_Compare'
        execution_policy:
          $ref: '#/components/schemas/ExecutionPolicy_Compare'
        experiment_items:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentItem_Compare'
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
      title: DatasetItem_Compare
    ColumnCompareTypesItems:
      type: string
      enum:
        - string
        - number
        - object
        - boolean
        - array
        - 'null'
      title: ColumnCompareTypesItems
    Column_Compare:
      type: object
      properties:
        name:
          type: string
        types:
          type: array
          items:
            $ref: '#/components/schemas/ColumnCompareTypesItems'
        filter_field_prefix:
          type: string
        filterField:
          type: string
          description: The field to use for filtering
      title: Column_Compare
    DatasetItemPage_Compare:
      type: object
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/DatasetItem_Compare'
        page:
          type: integer
        size:
          type: integer
        total:
          type: integer
          format: int64
        columns:
          type: array
          items:
            $ref: '#/components/schemas/Column_Compare'
        sortableBy:
          type: array
          items:
            type: string
      title: DatasetItemPage_Compare

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/id/items/experiments/items"

querystring = {"experiment_ids":"experiment_ids"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/id/items/experiments/items?experiment_ids=experiment_ids';
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

	url := "http://localhost:5173/api/v1/private/datasets/id/items/experiments/items?experiment_ids=experiment_ids"

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

url = URI("http://localhost:5173/api/v1/private/datasets/id/items/experiments/items?experiment_ids=experiment_ids")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/datasets/id/items/experiments/items?experiment_ids=experiment_ids")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/datasets/id/items/experiments/items?experiment_ids=experiment_ids', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/id/items/experiments/items?experiment_ids=experiment_ids");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/id/items/experiments/items?experiment_ids=experiment_ids")! as URL,
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