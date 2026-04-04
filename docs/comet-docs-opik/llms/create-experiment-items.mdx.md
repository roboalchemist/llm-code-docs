# Source: https://www.comet.com/docs/opik/reference/rest-api/experiments/create-experiment-items.mdx

# Create experiment items

POST http://localhost:5173/api/v1/private/experiments/items
Content-Type: application/json

Create experiment items

Reference: https://www.comet.com/docs/opik/reference/rest-api/experiments/create-experiment-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/experiments/items:
    post:
      operationId: create-experiment-items
      summary: Create experiment items
      description: Create experiment items
      tags:
        - subpackage_experiments
      responses:
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Experiments_createExperimentItems_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExperimentItemsBatch'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonListStringOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringOneOf1Items
    JsonListString1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringOneOf1Items'
      title: JsonListString1
    JsonListString:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListString1'
        - type: string
      title: JsonListString
    FeedbackScoreSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScoreSource
    ValueEntrySource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: ValueEntrySource
    ValueEntry:
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
          $ref: '#/components/schemas/ValueEntrySource'
        last_updated_at:
          type: string
          format: date-time
        span_type:
          type: string
        span_id:
          type: string
      title: ValueEntry
    FeedbackScore:
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
          $ref: '#/components/schemas/FeedbackScoreSource'
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
            $ref: '#/components/schemas/ValueEntry'
      required:
        - name
        - value
        - source
      title: FeedbackScore
    Comment:
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
      title: Comment
    ExperimentItemTraceVisibilityMode:
      type: string
      enum:
        - default
        - hidden
      title: ExperimentItemTraceVisibilityMode
    ExperimentItem:
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
        project_name:
          type: string
        input:
          $ref: '#/components/schemas/JsonListString'
        output:
          $ref: '#/components/schemas/JsonListString'
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScore'
        comments:
          type: array
          items:
            $ref: '#/components/schemas/Comment'
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
          $ref: '#/components/schemas/ExperimentItemTraceVisibilityMode'
        description:
          type: string
      required:
        - experiment_id
        - dataset_item_id
        - trace_id
      title: ExperimentItem
    ExperimentItemsBatch:
      type: object
      properties:
        experiment_items:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentItem'
      required:
        - experiment_items
      title: ExperimentItemsBatch
    Experiments_createExperimentItems_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Experiments_createExperimentItems_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/experiments/items"

payload = { "experiment_items": [
        {
            "experiment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "dataset_item_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
            "trace_id": "1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f"
        }
    ] }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/experiments/items';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"experiment_items":[{"experiment_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","dataset_item_id":"7c9e6679-7425-40de-944b-e07fc1f90ae7","trace_id":"1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f"}]}'
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

	url := "http://localhost:5173/api/v1/private/experiments/items"

	payload := strings.NewReader("{\n  \"experiment_items\": [\n    {\n      \"experiment_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"dataset_item_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"trace_id\": \"1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f\"\n    }\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/experiments/items")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"experiment_items\": [\n    {\n      \"experiment_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"dataset_item_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"trace_id\": \"1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/experiments/items")
  .header("Content-Type", "application/json")
  .body("{\n  \"experiment_items\": [\n    {\n      \"experiment_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"dataset_item_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"trace_id\": \"1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/experiments/items', [
  'body' => '{
  "experiment_items": [
    {
      "experiment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "dataset_item_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "trace_id": "1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f"
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

var client = new RestClient("http://localhost:5173/api/v1/private/experiments/items");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"experiment_items\": [\n    {\n      \"experiment_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n      \"dataset_item_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n      \"trace_id\": \"1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["experiment_items": [
    [
      "experiment_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "dataset_item_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "trace_id": "1c6b147e-8f3a-4d2a-9f3e-2a1b5d6c7e8f"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/experiments/items")! as URL,
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