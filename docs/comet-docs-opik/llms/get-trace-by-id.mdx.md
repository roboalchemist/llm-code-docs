# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/get-trace-by-id.mdx

# Get trace by id

GET http://localhost:5173/api/v1/private/traces/{id}

Get trace by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/get-trace-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/{id}:
    get:
      operationId: get-trace-by-id
      summary: Get trace by id
      description: Get trace by id
      tags:
        - subpackage_traces
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: strip_attachments
          in: query
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Trace resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Trace_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
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
    ErrorInfo_Public:
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
      title: ErrorInfo_Public
    FeedbackScorePublicSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScorePublicSource
    ValueEntryPublicSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: ValueEntryPublicSource
    ValueEntry_Public:
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
          $ref: '#/components/schemas/ValueEntryPublicSource'
        last_updated_at:
          type: string
          format: date-time
        span_type:
          type: string
        span_id:
          type: string
      title: ValueEntry_Public
    FeedbackScore_Public:
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
          $ref: '#/components/schemas/FeedbackScorePublicSource'
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
            $ref: '#/components/schemas/ValueEntry_Public'
      required:
        - name
        - value
        - source
      description: >-
        Aggregated feedback scores from all spans in this trace, averaged by
        score name
      title: FeedbackScore_Public
    Comment_Public:
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
      title: Comment_Public
    CheckPublicName:
      type: string
      enum:
        - TOPIC
        - PII
      title: CheckPublicName
    CheckPublicResult:
      type: string
      enum:
        - passed
        - failed
      title: CheckPublicResult
    Check_Public:
      type: object
      properties:
        name:
          $ref: '#/components/schemas/CheckPublicName'
        result:
          $ref: '#/components/schemas/CheckPublicResult'
      title: Check_Public
    GuardrailsValidation_Public:
      type: object
      properties:
        span_id:
          type: string
          format: uuid
        checks:
          type: array
          items:
            $ref: '#/components/schemas/Check_Public'
      title: GuardrailsValidation_Public
    TracePublicVisibilityMode:
      type: string
      enum:
        - default
        - hidden
      title: TracePublicVisibilityMode
    ExperimentItemReference_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Experiment ID
        name:
          type: string
          description: Experiment name
        dataset_id:
          type: string
          format: uuid
          description: Dataset ID
        dataset_item_id:
          type: string
          format: uuid
          description: Dataset Item ID
      required:
        - id
        - name
        - dataset_id
        - dataset_item_id
      description: Experiment reference with ID, name, dataset ID, and dataset item ID
      title: ExperimentItemReference_Public
    Trace_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_id:
          type: string
          format: uuid
        name:
          type: string
        start_time:
          type: string
          format: date-time
        end_time:
          type: string
          format: date-time
        input:
          $ref: '#/components/schemas/JsonListString_Public'
        output:
          $ref: '#/components/schemas/JsonListString_Public'
        metadata:
          $ref: '#/components/schemas/JsonListString_Public'
        tags:
          type: array
          items:
            type: string
        error_info:
          $ref: '#/components/schemas/ErrorInfo_Public'
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
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScore_Public'
        span_feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScore_Public'
          description: >-
            Aggregated feedback scores from all spans in this trace, averaged by
            score name
        comments:
          type: array
          items:
            $ref: '#/components/schemas/Comment_Public'
        guardrails_validations:
          type: array
          items:
            $ref: '#/components/schemas/GuardrailsValidation_Public'
        total_estimated_cost:
          type: number
          format: double
        span_count:
          type: integer
        duration:
          type: number
          format: double
          description: >-
            Duration in milliseconds as a decimal number to support
            sub-millisecond precision
        ttft:
          type: number
          format: double
          description: Time to first token in milliseconds
        thread_id:
          type: string
        visibility_mode:
          $ref: '#/components/schemas/TracePublicVisibilityMode'
        llm_span_count:
          type: integer
        has_tool_spans:
          type: boolean
        providers:
          type: array
          items:
            type: string
          description: >-
            List of unique provider names from all spans in this trace, sorted
            alphabetically
        experiment:
          $ref: '#/components/schemas/ExperimentItemReference_Public'
      required:
        - start_time
      title: Trace_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/id';
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

	url := "http://localhost:5173/api/v1/private/traces/id"

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

url = URI("http://localhost:5173/api/v1/private/traces/id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/traces/id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/traces/id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/id")! as URL,
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