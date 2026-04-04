# Source: https://www.comet.com/docs/opik/reference/rest-api/projects/get-project-metrics.mdx

# Get Project Metrics

POST http://localhost:5173/api/v1/private/projects/{id}/metrics
Content-Type: application/json

Gets specified metrics for a project

Reference: https://www.comet.com/docs/opik/reference/rest-api/projects/get-project-metrics

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/projects/{id}/metrics:
    post:
      operationId: get-project-metrics
      summary: Get Project Metrics
      description: Gets specified metrics for a project
      tags:
        - subpackage_projects
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Project Metrics
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectMetricResponse_Public'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProjectMetricRequest_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ProjectMetricRequestPublicMetricType:
      type: string
      enum:
        - FEEDBACK_SCORES
        - TRACE_COUNT
        - TOKEN_USAGE
        - DURATION
        - COST
        - GUARDRAILS_FAILED_COUNT
        - THREAD_COUNT
        - THREAD_DURATION
        - THREAD_FEEDBACK_SCORES
        - SPAN_FEEDBACK_SCORES
        - SPAN_COUNT
        - SPAN_DURATION
        - SPAN_TOKEN_USAGE
      title: ProjectMetricRequestPublicMetricType
    ProjectMetricRequestPublicInterval:
      type: string
      enum:
        - HOURLY
        - DAILY
        - WEEKLY
        - TOTAL
      title: ProjectMetricRequestPublicInterval
    SpanFilterPublicOperator:
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
      title: SpanFilterPublicOperator
    SpanFilter_Public:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/SpanFilterPublicOperator'
        key:
          type: string
        value:
          type: string
      title: SpanFilter_Public
    TraceFilterPublicOperator:
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
      title: TraceFilterPublicOperator
    TraceFilter_Public:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/TraceFilterPublicOperator'
        key:
          type: string
        value:
          type: string
      title: TraceFilter_Public
    TraceThreadFilterPublicOperator:
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
      title: TraceThreadFilterPublicOperator
    TraceThreadFilter_Public:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/TraceThreadFilterPublicOperator'
        key:
          type: string
        value:
          type: string
      title: TraceThreadFilter_Public
    BreakdownConfigPublicField:
      type: string
      enum:
        - none
        - tags
        - metadata
        - name
        - error_info
        - error_type
        - model
        - provider
        - type
      title: BreakdownConfigPublicField
    BreakdownConfig_Public:
      type: object
      properties:
        field:
          $ref: '#/components/schemas/BreakdownConfigPublicField'
        metadata_key:
          type: string
        sub_metric:
          type: string
      title: BreakdownConfig_Public
    ProjectMetricRequest_Public:
      type: object
      properties:
        metric_type:
          $ref: '#/components/schemas/ProjectMetricRequestPublicMetricType'
        interval:
          $ref: '#/components/schemas/ProjectMetricRequestPublicInterval'
        interval_start:
          type: string
          format: date-time
        interval_end:
          type: string
          format: date-time
        span_filters:
          type: array
          items:
            $ref: '#/components/schemas/SpanFilter_Public'
        trace_filters:
          type: array
          items:
            $ref: '#/components/schemas/TraceFilter_Public'
        thread_filters:
          type: array
          items:
            $ref: '#/components/schemas/TraceThreadFilter_Public'
        breakdown:
          $ref: '#/components/schemas/BreakdownConfig_Public'
      title: ProjectMetricRequest_Public
    ProjectMetricResponsePublicMetricType:
      type: string
      enum:
        - FEEDBACK_SCORES
        - TRACE_COUNT
        - TOKEN_USAGE
        - DURATION
        - COST
        - GUARDRAILS_FAILED_COUNT
        - THREAD_COUNT
        - THREAD_DURATION
        - THREAD_FEEDBACK_SCORES
        - SPAN_FEEDBACK_SCORES
        - SPAN_COUNT
        - SPAN_DURATION
        - SPAN_TOKEN_USAGE
      title: ProjectMetricResponsePublicMetricType
    ProjectMetricResponsePublicInterval:
      type: string
      enum:
        - HOURLY
        - DAILY
        - WEEKLY
        - TOTAL
      title: ProjectMetricResponsePublicInterval
    DataPointNumber_Public:
      type: object
      properties:
        time:
          type: string
          format: date-time
        value:
          type: number
          format: double
      required:
        - time
      title: DataPointNumber_Public
    ResultsNumber_Public:
      type: object
      properties:
        name:
          type: string
        data:
          type: array
          items:
            $ref: '#/components/schemas/DataPointNumber_Public'
      title: ResultsNumber_Public
    ProjectMetricResponse_Public:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
        metric_type:
          $ref: '#/components/schemas/ProjectMetricResponsePublicMetricType'
        interval:
          $ref: '#/components/schemas/ProjectMetricResponsePublicInterval'
        results:
          type: array
          items:
            $ref: '#/components/schemas/ResultsNumber_Public'
      title: ProjectMetricResponse_Public
    ErrorMessage_Public:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/projects/id/metrics"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/projects/id/metrics';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/projects/id/metrics"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/projects/id/metrics")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/projects/id/metrics")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/projects/id/metrics', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/projects/id/metrics");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/projects/id/metrics")! as URL,
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