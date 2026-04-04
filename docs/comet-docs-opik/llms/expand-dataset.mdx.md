# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/expand-dataset.mdx

# Expand dataset with synthetic samples

POST http://localhost:5173/api/v1/private/datasets/{id}/expansions
Content-Type: application/json

Generate synthetic dataset samples using LLM based on existing data patterns

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/expand-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{id}/expansions:
    post:
      operationId: expand-dataset
      summary: Expand dataset with synthetic samples
      description: >-
        Generate synthetic dataset samples using LLM based on existing data
        patterns
      tags:
        - subpackage_datasets
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Generated synthetic samples
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetExpansionResponse'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetExpansion_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetExpansion_Write:
      type: object
      properties:
        model:
          type: string
          description: The model to use for synthetic data generation
        sample_count:
          type: integer
          description: Number of synthetic samples to generate
        preserve_fields:
          type: array
          items:
            type: string
          description: Fields to preserve patterns from original data
        variation_instructions:
          type: string
          description: Additional instructions for data variation
        custom_prompt:
          type: string
          description: Custom prompt to use for generation instead of auto-generated one
      required:
        - model
      title: DatasetExpansion_Write
    DatasetItemSource:
      type: string
      enum:
        - manual
        - trace
        - span
        - sdk
      title: DatasetItemSource
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
    DatasetItem:
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
          $ref: '#/components/schemas/DatasetItemSource'
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
            $ref: '#/components/schemas/EvaluatorItem'
        execution_policy:
          $ref: '#/components/schemas/ExecutionPolicy'
        experiment_items:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentItem'
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
      title: DatasetItem
    DatasetExpansionResponse:
      type: object
      properties:
        generated_samples:
          type: array
          items:
            $ref: '#/components/schemas/DatasetItem'
          description: List of generated synthetic dataset items
        model:
          type: string
          description: Model used for generation
        total_generated:
          type: integer
          description: Total number of samples generated
        generation_time:
          type: string
          format: date-time
          description: Generation timestamp
      title: DatasetExpansionResponse

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/id/expansions"

payload = { "model": "gpt-4" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/id/expansions';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"model":"gpt-4"}'
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

	url := "http://localhost:5173/api/v1/private/datasets/id/expansions"

	payload := strings.NewReader("{\n  \"model\": \"gpt-4\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/id/expansions")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"gpt-4\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/id/expansions")
  .header("Content-Type", "application/json")
  .body("{\n  \"model\": \"gpt-4\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/id/expansions', [
  'body' => '{
  "model": "gpt-4"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/id/expansions");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"gpt-4\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["model": "gpt-4"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/id/expansions")! as URL,
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