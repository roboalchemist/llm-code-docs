# Source: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/create-automation-rule-evaluator.mdx

# Create automation rule evaluator

POST http://localhost:5173/api/v1/private/automations/evaluators
Content-Type: application/json

Create automation rule evaluator

Reference: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/create-automation-rule-evaluator

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/automations/evaluators:
    post:
      operationId: create-automation-rule-evaluator
      summary: Create automation rule evaluator
      description: Create automation rule evaluator
      tags:
        - subpackage_automationRuleEvaluators
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Automation rule
                  evaluators_createAutomationRuleEvaluator_Response_201
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AutomationRuleEvaluator_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AutomationRuleEvaluatorLlmAsJudgeWriteType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorLlmAsJudgeWriteType
    AutomationRuleEvaluatorLlmAsJudgeWriteAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorLlmAsJudgeWriteAction
    TraceFilterWriteOperator:
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
      title: TraceFilterWriteOperator
    TraceFilter_Write:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/TraceFilterWriteOperator'
        key:
          type: string
        value:
          type: string
      title: TraceFilter_Write
    JsonNode_Write:
      type: object
      properties: {}
      title: JsonNode_Write
    LlmAsJudgeModelParameters_Write:
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
          $ref: '#/components/schemas/JsonNode_Write'
      required:
        - name
        - temperature
      title: LlmAsJudgeModelParameters_Write
    LlmAsJudgeMessageWriteRole:
      type: string
      enum:
        - SYSTEM
        - USER
        - AI
        - TOOL_EXECUTION_RESULT
        - CUSTOM
      title: LlmAsJudgeMessageWriteRole
    ImageUrl_Write:
      type: object
      properties:
        url:
          type: string
        detail:
          type: string
      required:
        - url
      title: ImageUrl_Write
    VideoUrl_Write:
      type: object
      properties:
        url:
          type: string
      required:
        - url
      title: VideoUrl_Write
    AudioUrl_Write:
      type: object
      properties:
        url:
          type: string
      required:
        - url
      title: AudioUrl_Write
    LlmAsJudgeMessageContent_Write:
      type: object
      properties:
        type:
          type: string
        text:
          type: string
        image_url:
          $ref: '#/components/schemas/ImageUrl_Write'
        video_url:
          $ref: '#/components/schemas/VideoUrl_Write'
        audio_url:
          $ref: '#/components/schemas/AudioUrl_Write'
      required:
        - type
      title: LlmAsJudgeMessageContent_Write
    LlmAsJudgeMessage_Write:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/LlmAsJudgeMessageWriteRole'
        content:
          type: string
        content_array:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessageContent_Write'
        string_content:
          type: boolean
        structured_content:
          type: boolean
      required:
        - role
      title: LlmAsJudgeMessage_Write
    LlmAsJudgeOutputSchemaWriteType:
      type: string
      enum:
        - BOOLEAN
        - INTEGER
        - DOUBLE
      title: LlmAsJudgeOutputSchemaWriteType
    LlmAsJudgeOutputSchema_Write:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/LlmAsJudgeOutputSchemaWriteType'
        description:
          type: string
      required:
        - name
        - type
        - description
      title: LlmAsJudgeOutputSchema_Write
    LlmAsJudgeCode_Write:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters_Write'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage_Write'
        variables:
          type: object
          additionalProperties:
            type: string
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema_Write'
      required:
        - model
        - messages
        - variables
        - schema
      title: LlmAsJudgeCode_Write
    AutomationRuleEvaluatorWriteType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorWriteType
    AutomationRuleEvaluatorWriteAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorWriteAction
    AutomationRuleEvaluatorUserDefinedMetricPythonWriteType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUserDefinedMetricPythonWriteType
    AutomationRuleEvaluatorUserDefinedMetricPythonWriteAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUserDefinedMetricPythonWriteAction
    UserDefinedMetricPythonCode_Write:
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
      title: UserDefinedMetricPythonCode_Write
    AutomationRuleEvaluatorTraceThreadLlmAsJudgeWriteType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorTraceThreadLlmAsJudgeWriteType
    AutomationRuleEvaluatorTraceThreadLlmAsJudgeWriteAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorTraceThreadLlmAsJudgeWriteAction
    TraceThreadFilterWriteOperator:
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
      title: TraceThreadFilterWriteOperator
    TraceThreadFilter_Write:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/TraceThreadFilterWriteOperator'
        key:
          type: string
        value:
          type: string
      title: TraceThreadFilter_Write
    TraceThreadLlmAsJudgeCode_Write:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters_Write'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage_Write'
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema_Write'
      required:
        - model
        - messages
        - schema
      title: TraceThreadLlmAsJudgeCode_Write
    AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonWriteType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonWriteType
    AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonWriteAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonWriteAction
    TraceThreadUserDefinedMetricPythonCode_Write:
      type: object
      properties:
        metric:
          type: string
      required:
        - metric
      title: TraceThreadUserDefinedMetricPythonCode_Write
    AutomationRuleEvaluatorSpanLlmAsJudgeWriteType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorSpanLlmAsJudgeWriteType
    AutomationRuleEvaluatorSpanLlmAsJudgeWriteAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorSpanLlmAsJudgeWriteAction
    SpanFilterWriteOperator:
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
      title: SpanFilterWriteOperator
    SpanFilter_Write:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/SpanFilterWriteOperator'
        key:
          type: string
        value:
          type: string
      title: SpanFilter_Write
    SpanLlmAsJudgeCode_Write:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters_Write'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage_Write'
        variables:
          type: object
          additionalProperties:
            type: string
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema_Write'
      required:
        - model
        - messages
        - variables
        - schema
      title: SpanLlmAsJudgeCode_Write
    AutomationRuleEvaluatorSpanUserDefinedMetricPythonWriteType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorSpanUserDefinedMetricPythonWriteType
    AutomationRuleEvaluatorSpanUserDefinedMetricPythonWriteAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorSpanUserDefinedMetricPythonWriteAction
    SpanUserDefinedMetricPythonCode_Write:
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
      title: SpanUserDefinedMetricPythonCode_Write
    AutomationRuleEvaluator_Write:
      oneOf:
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteType'
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: >-
                Project IDs for write operations (used when creating/updating
                rules)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceFilter_Write'
            code:
              $ref: '#/components/schemas/LlmAsJudgeCode_Write'
          required:
            - type
            - name
            - action
            - code
          description: llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteType'
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: >-
                Project IDs for write operations (used when creating/updating
                rules)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceFilter_Write'
            code:
              $ref: '#/components/schemas/UserDefinedMetricPythonCode_Write'
          required:
            - type
            - name
            - action
            - code
          description: user_defined_metric_python variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteType'
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: >-
                Project IDs for write operations (used when creating/updating
                rules)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceThreadFilter_Write'
            code:
              $ref: '#/components/schemas/TraceThreadLlmAsJudgeCode_Write'
          required:
            - type
            - name
            - action
            - code
          description: trace_thread_llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteType'
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: >-
                Project IDs for write operations (used when creating/updating
                rules)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceThreadFilter_Write'
            code:
              $ref: >-
                #/components/schemas/TraceThreadUserDefinedMetricPythonCode_Write
          required:
            - type
            - name
            - action
            - code
          description: trace_thread_user_defined_metric_python variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteType'
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: >-
                Project IDs for write operations (used when creating/updating
                rules)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/SpanFilter_Write'
            code:
              $ref: '#/components/schemas/SpanLlmAsJudgeCode_Write'
          required:
            - type
            - name
            - action
            - code
          description: span_llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteType'
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_ids:
              type: array
              items:
                type: string
                format: uuid
              description: >-
                Project IDs for write operations (used when creating/updating
                rules)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorWriteAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/SpanFilter_Write'
            code:
              $ref: '#/components/schemas/SpanUserDefinedMetricPythonCode_Write'
          required:
            - type
            - name
            - action
            - code
          description: span_user_defined_metric_python variant
      discriminator:
        propertyName: type
      title: AutomationRuleEvaluator_Write
    Automation rule evaluators_createAutomationRuleEvaluator_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Automation rule evaluators_createAutomationRuleEvaluator_Response_201

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/automations/evaluators"

payload = {
    "type": "llm_as_judge",
    "action": "evaluator",
    "name": "Quality Assessment Evaluator"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/automations/evaluators';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"type":"llm_as_judge","action":"evaluator","name":"Quality Assessment Evaluator"}'
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

	url := "http://localhost:5173/api/v1/private/automations/evaluators"

	payload := strings.NewReader("{\n  \"type\": \"llm_as_judge\",\n  \"action\": \"evaluator\",\n  \"name\": \"Quality Assessment Evaluator\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/automations/evaluators")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"llm_as_judge\",\n  \"action\": \"evaluator\",\n  \"name\": \"Quality Assessment Evaluator\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/automations/evaluators")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"llm_as_judge\",\n  \"action\": \"evaluator\",\n  \"name\": \"Quality Assessment Evaluator\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/automations/evaluators', [
  'body' => '{
  "type": "llm_as_judge",
  "action": "evaluator",
  "name": "Quality Assessment Evaluator"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/automations/evaluators");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"llm_as_judge\",\n  \"action\": \"evaluator\",\n  \"name\": \"Quality Assessment Evaluator\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "type": "llm_as_judge",
  "action": "evaluator",
  "name": "Quality Assessment Evaluator"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/automations/evaluators")! as URL,
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