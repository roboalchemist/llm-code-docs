# Source: https://www.comet.com/docs/opik/reference/rest-api/experiments/experiment-items-bulk.mdx

# Record experiment items in bulk

PUT http://localhost:5173/api/v1/private/experiments/items/bulk
Content-Type: application/json

Record experiment items in bulk with traces, spans, and feedback scores. Maximum request size is 4MB.

Reference: https://www.comet.com/docs/opik/reference/rest-api/experiments/experiment-items-bulk

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/experiments/items/bulk:
    put:
      operationId: experiment-items-bulk
      summary: Record experiment items in bulk
      description: >-
        Record experiment items in bulk with traces, spans, and feedback scores.
        Maximum request size is 4MB.
      tags:
        - subpackage_experiments
      responses:
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Experiments_experimentItemsBulk_Response_204
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '409':
          description: Experiment dataset mismatch
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '422':
          description: Unprocessable Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/ExperimentItemBulkUpload_ExperimentItemBulkWriteView
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonListStringExperimentItemBulkWriteViewOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringExperimentItemBulkWriteViewOneOf1Items
    JsonListStringExperimentItemBulkWriteView1:
      type: array
      items:
        $ref: >-
          #/components/schemas/JsonListStringExperimentItemBulkWriteViewOneOf1Items
      title: JsonListStringExperimentItemBulkWriteView1
    JsonListString_ExperimentItemBulkWriteView:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListStringExperimentItemBulkWriteView1'
        - type: string
      title: JsonListString_ExperimentItemBulkWriteView
    ErrorInfo_ExperimentItemBulkWriteView:
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
      title: ErrorInfo_ExperimentItemBulkWriteView
    Trace_ExperimentItemBulkWriteView:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_name:
          type: string
          description: If null, the default project is used
        name:
          type: string
        start_time:
          type: string
          format: date-time
        end_time:
          type: string
          format: date-time
        input:
          $ref: '#/components/schemas/JsonListString_ExperimentItemBulkWriteView'
        output:
          $ref: '#/components/schemas/JsonListString_ExperimentItemBulkWriteView'
        metadata:
          $ref: '#/components/schemas/JsonListString_ExperimentItemBulkWriteView'
        tags:
          type: array
          items:
            type: string
        error_info:
          $ref: '#/components/schemas/ErrorInfo_ExperimentItemBulkWriteView'
        last_updated_at:
          type: string
          format: date-time
        ttft:
          type: number
          format: double
          description: Time to first token in milliseconds
        thread_id:
          type: string
      required:
        - start_time
      description: >-
        Please provide either none, only one of evaluate_task_result or trace,
        but never both
      title: Trace_ExperimentItemBulkWriteView
    SpanExperimentItemBulkWriteViewType:
      type: string
      enum:
        - general
        - tool
        - llm
        - guardrail
      title: SpanExperimentItemBulkWriteViewType
    Span_ExperimentItemBulkWriteView:
      type: object
      properties:
        id:
          type: string
          format: uuid
        parent_span_id:
          type: string
          format: uuid
        name:
          type: string
        type:
          $ref: '#/components/schemas/SpanExperimentItemBulkWriteViewType'
        start_time:
          type: string
          format: date-time
        end_time:
          type: string
          format: date-time
        input:
          $ref: '#/components/schemas/JsonListString_ExperimentItemBulkWriteView'
        output:
          $ref: '#/components/schemas/JsonListString_ExperimentItemBulkWriteView'
        metadata:
          $ref: '#/components/schemas/JsonListString_ExperimentItemBulkWriteView'
        model:
          type: string
        provider:
          type: string
        tags:
          type: array
          items:
            type: string
        usage:
          type: object
          additionalProperties:
            type: integer
        error_info:
          $ref: '#/components/schemas/ErrorInfo_ExperimentItemBulkWriteView'
        last_updated_at:
          type: string
          format: date-time
        total_estimated_cost:
          type: number
          format: double
        total_estimated_cost_version:
          type: string
        ttft:
          type: number
          format: double
          description: Time to first token in milliseconds
      required:
        - start_time
      title: Span_ExperimentItemBulkWriteView
    FeedbackScoreExperimentItemBulkWriteViewSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScoreExperimentItemBulkWriteViewSource
    ValueEntryExperimentItemBulkWriteViewSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: ValueEntryExperimentItemBulkWriteViewSource
    ValueEntry_ExperimentItemBulkWriteView:
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
          $ref: '#/components/schemas/ValueEntryExperimentItemBulkWriteViewSource'
        last_updated_at:
          type: string
          format: date-time
        span_type:
          type: string
        span_id:
          type: string
      title: ValueEntry_ExperimentItemBulkWriteView
    FeedbackScore_ExperimentItemBulkWriteView:
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
          $ref: '#/components/schemas/FeedbackScoreExperimentItemBulkWriteViewSource'
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
            $ref: '#/components/schemas/ValueEntry_ExperimentItemBulkWriteView'
      required:
        - name
        - value
        - source
      title: FeedbackScore_ExperimentItemBulkWriteView
    ExperimentItemBulkRecord_ExperimentItemBulkWriteView:
      type: object
      properties:
        dataset_item_id:
          type: string
          format: uuid
        evaluate_task_result:
          $ref: '#/components/schemas/JsonListString_ExperimentItemBulkWriteView'
        trace:
          $ref: '#/components/schemas/Trace_ExperimentItemBulkWriteView'
        spans:
          type: array
          items:
            $ref: '#/components/schemas/Span_ExperimentItemBulkWriteView'
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScore_ExperimentItemBulkWriteView'
      required:
        - dataset_item_id
      title: ExperimentItemBulkRecord_ExperimentItemBulkWriteView
    ExperimentItemBulkUpload_ExperimentItemBulkWriteView:
      type: object
      properties:
        experiment_name:
          type: string
        dataset_name:
          type: string
        experiment_id:
          type: string
          format: uuid
          description: >-
            Optional experiment ID. If provided, items will be added to the
            existing experiment and experimentName will be ignored. If not
            provided or experiment with that ID doesn't exist, a new experiment
            will be created with the given experimentName
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/ExperimentItemBulkRecord_ExperimentItemBulkWriteView
      required:
        - experiment_name
        - dataset_name
        - items
      title: ExperimentItemBulkUpload_ExperimentItemBulkWriteView
    Experiments_experimentItemsBulk_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Experiments_experimentItemsBulk_Response_204
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

url = "http://localhost:5173/api/v1/private/experiments/items/bulk"

payload = {
    "experiment_name": "Image Classification Experiment April 2024",
    "dataset_name": "CIFAR-10 Dataset",
    "items": [{ "dataset_item_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6" }]
}
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/experiments/items/bulk';
const options = {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: '{"experiment_name":"Image Classification Experiment April 2024","dataset_name":"CIFAR-10 Dataset","items":[{"dataset_item_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6"}]}'
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

	url := "http://localhost:5173/api/v1/private/experiments/items/bulk"

	payload := strings.NewReader("{\n  \"experiment_name\": \"Image Classification Experiment April 2024\",\n  \"dataset_name\": \"CIFAR-10 Dataset\",\n  \"items\": [\n    {\n      \"dataset_item_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/experiments/items/bulk")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"experiment_name\": \"Image Classification Experiment April 2024\",\n  \"dataset_name\": \"CIFAR-10 Dataset\",\n  \"items\": [\n    {\n      \"dataset_item_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/experiments/items/bulk")
  .header("Content-Type", "application/json")
  .body("{\n  \"experiment_name\": \"Image Classification Experiment April 2024\",\n  \"dataset_name\": \"CIFAR-10 Dataset\",\n  \"items\": [\n    {\n      \"dataset_item_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/experiments/items/bulk', [
  'body' => '{
  "experiment_name": "Image Classification Experiment April 2024",
  "dataset_name": "CIFAR-10 Dataset",
  "items": [
    {
      "dataset_item_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
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

var client = new RestClient("http://localhost:5173/api/v1/private/experiments/items/bulk");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"experiment_name\": \"Image Classification Experiment April 2024\",\n  \"dataset_name\": \"CIFAR-10 Dataset\",\n  \"items\": [\n    {\n      \"dataset_item_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "experiment_name": "Image Classification Experiment April 2024",
  "dataset_name": "CIFAR-10 Dataset",
  "items": [["dataset_item_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/experiments/items/bulk")! as URL,
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