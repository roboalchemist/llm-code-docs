# Source: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/update-automation-rule-evaluator.mdx

# Update Automation Rule Evaluator by id

PATCH http://localhost:5173/api/v1/private/automations/evaluators/{id}
Content-Type: application/json

Update Automation Rule Evaluator by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/update-automation-rule-evaluator

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/automations/evaluators/{id}:
    patch:
      operationId: update-automation-rule-evaluator
      summary: Update Automation Rule Evaluator by id
      description: Update Automation Rule Evaluator by id
      tags:
        - subpackage_automationRuleEvaluators
      parameters:
        - name: id
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
                $ref: >-
                  #/components/schemas/Automation rule
                  evaluators_updateAutomationRuleEvaluator_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AutomationRuleEvaluatorUpdateLlmAsJudgeType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUpdateLlmAsJudgeType
    AutomationRuleEvaluatorUpdateLlmAsJudgeAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUpdateLlmAsJudgeAction
    TraceFilterOperator:
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
      title: TraceFilterOperator
    TraceFilter:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/TraceFilterOperator'
        key:
          type: string
        value:
          type: string
      title: TraceFilter
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    LlmAsJudgeModelParameters:
      type: object
      properties:
        name:
          type: string
        temperature:
          type: number
          format: double
        seed:
          type: integer
        custom_parameters:
          $ref: '#/components/schemas/JsonNode'
      required:
        - name
        - temperature
      title: LlmAsJudgeModelParameters
    LlmAsJudgeMessageRole:
      type: string
      enum:
        - SYSTEM
        - USER
        - AI
        - TOOL_EXECUTION_RESULT
        - CUSTOM
      title: LlmAsJudgeMessageRole
    ImageUrl:
      type: object
      properties:
        url:
          type: string
        detail:
          type: string
      required:
        - url
      title: ImageUrl
    VideoUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
      title: VideoUrl
    AudioUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
      title: AudioUrl
    LlmAsJudgeMessageContent:
      type: object
      properties:
        type:
          type: string
        text:
          type: string
        image_url:
          $ref: '#/components/schemas/ImageUrl'
        video_url:
          $ref: '#/components/schemas/VideoUrl'
        audio_url:
          $ref: '#/components/schemas/AudioUrl'
      required:
        - type
      title: LlmAsJudgeMessageContent
    LlmAsJudgeMessage:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/LlmAsJudgeMessageRole'
        content:
          type: string
        content_array:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessageContent'
        string_content:
          type: boolean
        structured_content:
          type: boolean
      required:
        - role
      title: LlmAsJudgeMessage
    LlmAsJudgeOutputSchemaType:
      type: string
      enum:
        - BOOLEAN
        - INTEGER
        - DOUBLE
      title: LlmAsJudgeOutputSchemaType
    LlmAsJudgeOutputSchema:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/LlmAsJudgeOutputSchemaType'
        description:
          type: string
      required:
        - name
        - type
        - description
      title: LlmAsJudgeOutputSchema
    LlmAsJudgeCode:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage'
        variables:
          type: object
          additionalProperties:
            type: string
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema'
      required:
        - model
        - messages
        - variables
        - schema
      title: LlmAsJudgeCode
    AutomationRuleEvaluatorUpdateType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUpdateType
    AutomationRuleEvaluatorUpdateAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUpdateAction
    AutomationRuleEvaluatorUpdateUserDefinedMetricPythonType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUpdateUserDefinedMetricPythonType
    AutomationRuleEvaluatorUpdateUserDefinedMetricPythonAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUpdateUserDefinedMetricPythonAction
    UserDefinedMetricPythonCode:
      type: object
      properties:
        metric:
          type: string
        arguments:
          type: object
          additionalProperties:
            type: string
      required:
        - metric
        - arguments
      title: UserDefinedMetricPythonCode
    AutomationRuleEvaluatorUpdateTraceThreadLlmAsJudgeType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUpdateTraceThreadLlmAsJudgeType
    AutomationRuleEvaluatorUpdateTraceThreadLlmAsJudgeAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUpdateTraceThreadLlmAsJudgeAction
    TraceThreadFilterOperator:
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
      title: TraceThreadFilterOperator
    TraceThreadFilter:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/TraceThreadFilterOperator'
        key:
          type: string
        value:
          type: string
      title: TraceThreadFilter
    TraceThreadLlmAsJudgeCode:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage'
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema'
      required:
        - model
        - messages
        - schema
      title: TraceThreadLlmAsJudgeCode
    AutomationRuleEvaluatorUpdateTraceThreadUserDefinedMetricPythonType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUpdateTraceThreadUserDefinedMetricPythonType
    AutomationRuleEvaluatorUpdateTraceThreadUserDefinedMetricPythonAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUpdateTraceThreadUserDefinedMetricPythonAction
    TraceThreadUserDefinedMetricPythonCode:
      type: object
      properties:
        metric:
          type: string
      required:
        - metric
      title: TraceThreadUserDefinedMetricPythonCode
    AutomationRuleEvaluatorUpdateSpanLlmAsJudgeType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUpdateSpanLlmAsJudgeType
    AutomationRuleEvaluatorUpdateSpanLlmAsJudgeAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUpdateSpanLlmAsJudgeAction
    SpanFilterOperator:
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
      title: SpanFilterOperator
    SpanFilter:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/SpanFilterOperator'
        key:
          type: string
        value:
          type: string
      title: SpanFilter
    SpanLlmAsJudgeCode:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage'
        variables:
          type: object
          additionalProperties:
            type: string
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema'
      required:
        - model
        - messages
        - variables
        - schema
      title: SpanLlmAsJudgeCode
    AutomationRuleEvaluatorUpdateSpanUserDefinedMetricPythonType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUpdateSpanUserDefinedMetricPythonType
    AutomationRuleEvaluatorUpdateSpanUserDefinedMetricPythonAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUpdateSpanUserDefinedMetricPythonAction
    SpanUserDefinedMetricPythonCode:
      type: object
      properties:
        metric:
          type: string
        arguments:
          type: object
          additionalProperties:
            type: string
      required:
        - metric
        - arguments
      title: SpanUserDefinedMetricPythonCode
    AutomationRuleEvaluatorUpdate:
      oneOf:
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateType'
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            project_id:
              type: string
              format: uuid
              description: >-
                Primary project ID (legacy field, maintained for backwards
                compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: Multiple project IDs (new field for multi-project support)
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceFilter'
            code:
              $ref: '#/components/schemas/LlmAsJudgeCode'
          required:
            - type
            - name
            - action
            - code
          description: llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateType'
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            project_id:
              type: string
              format: uuid
              description: >-
                Primary project ID (legacy field, maintained for backwards
                compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: Multiple project IDs (new field for multi-project support)
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceFilter'
            code:
              $ref: '#/components/schemas/UserDefinedMetricPythonCode'
          required:
            - type
            - name
            - action
            - code
          description: user_defined_metric_python variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateType'
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            project_id:
              type: string
              format: uuid
              description: >-
                Primary project ID (legacy field, maintained for backwards
                compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: Multiple project IDs (new field for multi-project support)
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceThreadFilter'
            code:
              $ref: '#/components/schemas/TraceThreadLlmAsJudgeCode'
          required:
            - type
            - name
            - action
            - code
          description: trace_thread_llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateType'
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            project_id:
              type: string
              format: uuid
              description: >-
                Primary project ID (legacy field, maintained for backwards
                compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: Multiple project IDs (new field for multi-project support)
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceThreadFilter'
            code:
              $ref: '#/components/schemas/TraceThreadUserDefinedMetricPythonCode'
          required:
            - type
            - name
            - action
            - code
          description: trace_thread_user_defined_metric_python variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateType'
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            project_id:
              type: string
              format: uuid
              description: >-
                Primary project ID (legacy field, maintained for backwards
                compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: Multiple project IDs (new field for multi-project support)
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/SpanFilter'
            code:
              $ref: '#/components/schemas/SpanLlmAsJudgeCode'
          required:
            - type
            - name
            - action
            - code
          description: span_llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateType'
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            project_id:
              type: string
              format: uuid
              description: >-
                Primary project ID (legacy field, maintained for backwards
                compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: Multiple project IDs (new field for multi-project support)
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorUpdateAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/SpanFilter'
            code:
              $ref: '#/components/schemas/SpanUserDefinedMetricPythonCode'
          required:
            - type
            - name
            - action
            - code
          description: span_user_defined_metric_python variant
      discriminator:
        propertyName: type
      title: AutomationRuleEvaluatorUpdate
    Automation rule evaluators_updateAutomationRuleEvaluator_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Automation rule evaluators_updateAutomationRuleEvaluator_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/automations/evaluators/id"

payload = {
    "name": "Latency Threshold Evaluator",
    "action": "evaluator"
}
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/automations/evaluators/id';
const options = {
  method: 'PATCH',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"Latency Threshold Evaluator","action":"evaluator"}'
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

	url := "http://localhost:5173/api/v1/private/automations/evaluators/id"

	payload := strings.NewReader("{\n  \"name\": \"Latency Threshold Evaluator\",\n  \"action\": \"evaluator\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/automations/evaluators/id")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Latency Threshold Evaluator\",\n  \"action\": \"evaluator\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/automations/evaluators/id")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Latency Threshold Evaluator\",\n  \"action\": \"evaluator\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/automations/evaluators/id', [
  'body' => '{
  "name": "Latency Threshold Evaluator",
  "action": "evaluator"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/automations/evaluators/id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Latency Threshold Evaluator\",\n  \"action\": \"evaluator\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "name": "Latency Threshold Evaluator",
  "action": "evaluator"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/automations/evaluators/id")! as URL,
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