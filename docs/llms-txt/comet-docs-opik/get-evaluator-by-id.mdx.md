# Source: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/get-evaluator-by-id.mdx

# Get automation rule evaluator by id

GET http://localhost:5173/api/v1/private/automations/evaluators/{id}

Get automation rule by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/get-evaluator-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/automations/evaluators/{id}:
    get:
      operationId: get-evaluator-by-id
      summary: Get automation rule evaluator by id
      description: Get automation rule by id
      tags:
        - subpackage_automationRuleEvaluators
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: project_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Automation Rule resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AutomationRuleEvaluator_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ProjectReference_Public:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
          description: Project ID
        project_name:
          type: string
          description: Project name
      required:
        - project_id
        - project_name
      description: Project reference with ID and name
      title: ProjectReference_Public
    AutomationRuleEvaluatorLlmAsJudgePublicType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorLlmAsJudgePublicType
    AutomationRuleEvaluatorLlmAsJudgePublicAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorLlmAsJudgePublicAction
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
    JsonNode_Public:
      type: object
      properties: {}
      title: JsonNode_Public
    LlmAsJudgeModelParameters_Public:
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
          $ref: '#/components/schemas/JsonNode_Public'
      required:
        - name
        - temperature
      title: LlmAsJudgeModelParameters_Public
    LlmAsJudgeMessagePublicRole:
      type: string
      enum:
        - SYSTEM
        - USER
        - AI
        - TOOL_EXECUTION_RESULT
        - CUSTOM
      title: LlmAsJudgeMessagePublicRole
    ImageUrl_Public:
      type: object
      properties:
        url:
          type: string
        detail:
          type: string
      required:
        - url
      title: ImageUrl_Public
    VideoUrl_Public:
      type: object
      properties:
        url:
          type: string
      required:
        - url
      title: VideoUrl_Public
    AudioUrl_Public:
      type: object
      properties:
        url:
          type: string
      required:
        - url
      title: AudioUrl_Public
    LlmAsJudgeMessageContent_Public:
      type: object
      properties:
        type:
          type: string
        text:
          type: string
        image_url:
          $ref: '#/components/schemas/ImageUrl_Public'
        video_url:
          $ref: '#/components/schemas/VideoUrl_Public'
        audio_url:
          $ref: '#/components/schemas/AudioUrl_Public'
      required:
        - type
      title: LlmAsJudgeMessageContent_Public
    LlmAsJudgeMessage_Public:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/LlmAsJudgeMessagePublicRole'
        content:
          type: string
        content_array:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessageContent_Public'
        string_content:
          type: boolean
        structured_content:
          type: boolean
      required:
        - role
      title: LlmAsJudgeMessage_Public
    LlmAsJudgeOutputSchemaPublicType:
      type: string
      enum:
        - BOOLEAN
        - INTEGER
        - DOUBLE
      title: LlmAsJudgeOutputSchemaPublicType
    LlmAsJudgeOutputSchema_Public:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/LlmAsJudgeOutputSchemaPublicType'
        description:
          type: string
      required:
        - name
        - type
        - description
      title: LlmAsJudgeOutputSchema_Public
    LlmAsJudgeCode_Public:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters_Public'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage_Public'
        variables:
          type: object
          additionalProperties:
            type: string
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema_Public'
      required:
        - model
        - messages
        - variables
        - schema
      title: LlmAsJudgeCode_Public
    AutomationRuleEvaluatorPublicType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorPublicType
    AutomationRuleEvaluatorPublicAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorPublicAction
    AutomationRuleEvaluatorUserDefinedMetricPythonPublicType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorUserDefinedMetricPythonPublicType
    AutomationRuleEvaluatorUserDefinedMetricPythonPublicAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorUserDefinedMetricPythonPublicAction
    UserDefinedMetricPythonCode_Public:
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
      title: UserDefinedMetricPythonCode_Public
    AutomationRuleEvaluatorTraceThreadLlmAsJudgePublicType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorTraceThreadLlmAsJudgePublicType
    AutomationRuleEvaluatorTraceThreadLlmAsJudgePublicAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorTraceThreadLlmAsJudgePublicAction
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
    TraceThreadLlmAsJudgeCode_Public:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters_Public'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage_Public'
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema_Public'
      required:
        - model
        - messages
        - schema
      title: TraceThreadLlmAsJudgeCode_Public
    AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonPublicType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonPublicType
    AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonPublicAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorTraceThreadUserDefinedMetricPythonPublicAction
    TraceThreadUserDefinedMetricPythonCode_Public:
      type: object
      properties:
        metric:
          type: string
      required:
        - metric
      title: TraceThreadUserDefinedMetricPythonCode_Public
    AutomationRuleEvaluatorSpanLlmAsJudgePublicType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorSpanLlmAsJudgePublicType
    AutomationRuleEvaluatorSpanLlmAsJudgePublicAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorSpanLlmAsJudgePublicAction
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
    SpanLlmAsJudgeCode_Public:
      type: object
      properties:
        model:
          $ref: '#/components/schemas/LlmAsJudgeModelParameters_Public'
        messages:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeMessage_Public'
        variables:
          type: object
          additionalProperties:
            type: string
        schema:
          type: array
          items:
            $ref: '#/components/schemas/LlmAsJudgeOutputSchema_Public'
      required:
        - model
        - messages
        - variables
        - schema
      title: SpanLlmAsJudgeCode_Public
    AutomationRuleEvaluatorSpanUserDefinedMetricPythonPublicType:
      type: string
      enum:
        - llm_as_judge
        - user_defined_metric_python
        - trace_thread_llm_as_judge
        - trace_thread_user_defined_metric_python
        - span_llm_as_judge
        - span_user_defined_metric_python
      title: AutomationRuleEvaluatorSpanUserDefinedMetricPythonPublicType
    AutomationRuleEvaluatorSpanUserDefinedMetricPythonPublicAction:
      type: string
      enum:
        - evaluator
      title: AutomationRuleEvaluatorSpanUserDefinedMetricPythonPublicAction
    SpanUserDefinedMetricPythonCode_Public:
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
      title: SpanUserDefinedMetricPythonCode_Public
    AutomationRuleEvaluator_Public:
      oneOf:
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicType'
            id:
              type: string
              format: uuid
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_name:
              type: string
              description: Primary project name (legacy field for backwards compatibility)
            projects:
              type: array
              items:
                $ref: '#/components/schemas/ProjectReference_Public'
              description: >-
                Projects assigned to this rule (unique, sorted alphabetically by
                name)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceFilter_Public'
            code:
              $ref: '#/components/schemas/LlmAsJudgeCode_Public'
          required:
            - type
            - name
            - action
            - code
          description: llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicType'
            id:
              type: string
              format: uuid
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_name:
              type: string
              description: Primary project name (legacy field for backwards compatibility)
            projects:
              type: array
              items:
                $ref: '#/components/schemas/ProjectReference_Public'
              description: >-
                Projects assigned to this rule (unique, sorted alphabetically by
                name)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceFilter_Public'
            code:
              $ref: '#/components/schemas/UserDefinedMetricPythonCode_Public'
          required:
            - type
            - name
            - action
            - code
          description: user_defined_metric_python variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicType'
            id:
              type: string
              format: uuid
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_name:
              type: string
              description: Primary project name (legacy field for backwards compatibility)
            projects:
              type: array
              items:
                $ref: '#/components/schemas/ProjectReference_Public'
              description: >-
                Projects assigned to this rule (unique, sorted alphabetically by
                name)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceThreadFilter_Public'
            code:
              $ref: '#/components/schemas/TraceThreadLlmAsJudgeCode_Public'
          required:
            - type
            - name
            - action
            - code
          description: trace_thread_llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicType'
            id:
              type: string
              format: uuid
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_name:
              type: string
              description: Primary project name (legacy field for backwards compatibility)
            projects:
              type: array
              items:
                $ref: '#/components/schemas/ProjectReference_Public'
              description: >-
                Projects assigned to this rule (unique, sorted alphabetically by
                name)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/TraceThreadFilter_Public'
            code:
              $ref: >-
                #/components/schemas/TraceThreadUserDefinedMetricPythonCode_Public
          required:
            - type
            - name
            - action
            - code
          description: trace_thread_user_defined_metric_python variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicType'
            id:
              type: string
              format: uuid
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_name:
              type: string
              description: Primary project name (legacy field for backwards compatibility)
            projects:
              type: array
              items:
                $ref: '#/components/schemas/ProjectReference_Public'
              description: >-
                Projects assigned to this rule (unique, sorted alphabetically by
                name)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/SpanFilter_Public'
            code:
              $ref: '#/components/schemas/SpanLlmAsJudgeCode_Public'
          required:
            - type
            - name
            - action
            - code
          description: span_llm_as_judge variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicType'
            id:
              type: string
              format: uuid
            project_id:
              type: string
              format: uuid
              description: Primary project ID (legacy field for backwards compatibility)
            project_name:
              type: string
              description: Primary project name (legacy field for backwards compatibility)
            projects:
              type: array
              items:
                $ref: '#/components/schemas/ProjectReference_Public'
              description: >-
                Projects assigned to this rule (unique, sorted alphabetically by
                name)
            name:
              type: string
            sampling_rate:
              type: number
              format: double
            enabled:
              type: boolean
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
            action:
              $ref: '#/components/schemas/AutomationRuleEvaluatorPublicAction'
            filters:
              type: array
              items:
                $ref: '#/components/schemas/SpanFilter_Public'
            code:
              $ref: '#/components/schemas/SpanUserDefinedMetricPythonCode_Public'
          required:
            - type
            - name
            - action
            - code
          description: span_user_defined_metric_python variant
      discriminator:
        propertyName: type
      title: AutomationRuleEvaluator_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/automations/evaluators/id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/automations/evaluators/id';
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

	url := "http://localhost:5173/api/v1/private/automations/evaluators/id"

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

url = URI("http://localhost:5173/api/v1/private/automations/evaluators/id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/automations/evaluators/id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/automations/evaluators/id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/automations/evaluators/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/automations/evaluators/id")! as URL,
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