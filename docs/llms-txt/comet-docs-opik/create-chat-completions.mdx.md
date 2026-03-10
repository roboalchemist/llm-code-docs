# Source: https://www.comet.com/docs/opik/reference/rest-api/chat-completions/create-chat-completions.mdx

# Create chat completions

POST http://localhost:5173/api/v1/private/chat/completions
Content-Type: application/json

Create chat completions

Reference: https://www.comet.com/docs/opik/reference/rest-api/chat-completions/create-chat-completions

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/chat/completions:
    post:
      operationId: create-chat-completions
      summary: Create chat completions
      description: Create chat completions
      tags:
        - subpackage_chatCompletions
      responses:
        '200':
          description: Chat completions response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatCompletionResponse'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatCompletionRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    Message:
      type: object
      properties: {}
      title: Message
    StreamOptions:
      type: object
      properties:
        include_usage:
          type: boolean
      title: StreamOptions
    ResponseFormatType:
      type: string
      enum:
        - text
        - json_object
        - json_schema
      title: ResponseFormatType
    JsonSchemaSchema:
      type: object
      properties: {}
      title: JsonSchemaSchema
    JsonSchema:
      type: object
      properties:
        name:
          type: string
        strict:
          type: boolean
        schema:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/JsonSchemaSchema'
      title: JsonSchema
    ResponseFormat:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ResponseFormatType'
        json_schema:
          $ref: '#/components/schemas/JsonSchema'
      title: ResponseFormat
    ToolType:
      type: string
      enum:
        - function
      title: ToolType
    FunctionParameters:
      type: object
      properties: {}
      title: FunctionParameters
    Function:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        strict:
          type: boolean
        parameters:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/FunctionParameters'
      title: Function
    Tool:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/ToolType'
        function:
          $ref: '#/components/schemas/Function'
      title: Tool
    ChatCompletionRequestToolChoice:
      type: object
      properties: {}
      title: ChatCompletionRequestToolChoice
    FunctionCall:
      type: object
      properties:
        name:
          type: string
        arguments:
          type: string
      title: FunctionCall
    ChatCompletionRequest:
      type: object
      properties:
        model:
          type: string
        messages:
          type: array
          items:
            $ref: '#/components/schemas/Message'
        temperature:
          type: number
          format: double
        top_p:
          type: number
          format: double
        'n':
          type: integer
        stream:
          type: boolean
        stream_options:
          $ref: '#/components/schemas/StreamOptions'
        stop:
          type: array
          items:
            type: string
        max_tokens:
          type: integer
        max_completion_tokens:
          type: integer
        presence_penalty:
          type: number
          format: double
        frequency_penalty:
          type: number
          format: double
        logit_bias:
          type: object
          additionalProperties:
            type: integer
        user:
          type: string
        response_format:
          $ref: '#/components/schemas/ResponseFormat'
        seed:
          type: integer
        tools:
          type: array
          items:
            $ref: '#/components/schemas/Tool'
        tool_choice:
          $ref: '#/components/schemas/ChatCompletionRequestToolChoice'
        parallel_tool_calls:
          type: boolean
        store:
          type: boolean
        metadata:
          type: object
          additionalProperties:
            type: string
        reasoning_effort:
          type: string
        service_tier:
          type: string
        functions:
          type: array
          items:
            $ref: '#/components/schemas/Function'
        function_call:
          $ref: '#/components/schemas/FunctionCall'
      title: ChatCompletionRequest
    AssistantMessageRole:
      type: string
      enum:
        - system
        - user
        - assistant
        - tool
        - function
      title: AssistantMessageRole
    ToolCallType:
      type: string
      enum:
        - function
      title: ToolCallType
    ToolCall:
      type: object
      properties:
        id:
          type: string
        index:
          type: integer
        type:
          $ref: '#/components/schemas/ToolCallType'
        function:
          $ref: '#/components/schemas/FunctionCall'
      title: ToolCall
    AssistantMessage:
      type: object
      properties:
        role:
          $ref: '#/components/schemas/AssistantMessageRole'
        content:
          type: string
        reasoning_content:
          type: string
        name:
          type: string
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ToolCall'
        refusal:
          type: string
        function_call:
          $ref: '#/components/schemas/FunctionCall'
      title: AssistantMessage
    Delta:
      type: object
      properties:
        role:
          type: string
        content:
          type: string
        reasoning_content:
          type: string
        tool_calls:
          type: array
          items:
            $ref: '#/components/schemas/ToolCall'
        function_call:
          $ref: '#/components/schemas/FunctionCall'
      title: Delta
    ChatCompletionChoice:
      type: object
      properties:
        index:
          type: integer
        message:
          $ref: '#/components/schemas/AssistantMessage'
        delta:
          $ref: '#/components/schemas/Delta'
        finish_reason:
          type: string
      title: ChatCompletionChoice
    PromptTokensDetails:
      type: object
      properties:
        cached_tokens:
          type: integer
      title: PromptTokensDetails
    CompletionTokensDetails:
      type: object
      properties:
        reasoning_tokens:
          type: integer
      title: CompletionTokensDetails
    Usage:
      type: object
      properties:
        total_tokens:
          type: integer
        prompt_tokens:
          type: integer
        prompt_tokens_details:
          $ref: '#/components/schemas/PromptTokensDetails'
        completion_tokens:
          type: integer
        completion_tokens_details:
          $ref: '#/components/schemas/CompletionTokensDetails'
      title: Usage
    ChatCompletionResponse:
      type: object
      properties:
        id:
          type: string
        created:
          type: integer
          format: int64
        model:
          type: string
        choices:
          type: array
          items:
            $ref: '#/components/schemas/ChatCompletionChoice'
        usage:
          $ref: '#/components/schemas/Usage'
        system_fingerprint:
          type: string
        service_tier:
          type: string
      title: ChatCompletionResponse

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/chat/completions"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/chat/completions';
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

	url := "http://localhost:5173/api/v1/private/chat/completions"

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

url = URI("http://localhost:5173/api/v1/private/chat/completions")

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

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/chat/completions")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/chat/completions', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/chat/completions");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/chat/completions")! as URL,
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