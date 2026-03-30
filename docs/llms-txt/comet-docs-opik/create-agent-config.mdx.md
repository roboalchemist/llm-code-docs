# Source: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/create-agent-config.mdx

# Create optimizer config or add blueprint

POST http://localhost:5173/api/v1/private/agent-configs/blueprints
Content-Type: application/json

Creates a new optimizer config with initial blueprint, or adds a new blueprint to existing config

Reference: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/create-agent-config

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/agent-configs/blueprints:
    post:
      operationId: create-agent-config
      summary: Create optimizer config or add blueprint
      description: >-
        Creates a new optimizer config with initial blueprint, or adds a new
        blueprint to existing config
      tags:
        - subpackage_agentConfigs
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Agent
                  Configs_createAgentConfig_Response_201
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Write'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Write'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AgentConfigCreate_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AgentBlueprintWriteType:
      type: string
      enum:
        - blueprint
        - mask
      title: AgentBlueprintWriteType
    AgentConfigValueWriteType:
      type: string
      enum:
        - string
        - integer
        - float
        - boolean
        - prompt
        - prompt_commit
      title: AgentConfigValueWriteType
    AgentConfigValue_Write:
      type: object
      properties:
        key:
          type: string
        value:
          type: string
        type:
          $ref: '#/components/schemas/AgentConfigValueWriteType'
        description:
          type: string
      required:
        - key
        - value
        - type
      title: AgentConfigValue_Write
    AgentBlueprint_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        type:
          $ref: '#/components/schemas/AgentBlueprintWriteType'
        description:
          type: string
        values:
          type: array
          items:
            $ref: '#/components/schemas/AgentConfigValue_Write'
      required:
        - type
        - values
      title: AgentBlueprint_Write
    AgentConfigCreate_Write:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
          description: Project ID. Either project_id or project_name must be provided
        project_name:
          type: string
          description: Project name. Either project_id or project_name must be provided
        id:
          type: string
          format: uuid
          description: Agent config ID. Generated automatically if not provided
        blueprint:
          $ref: '#/components/schemas/AgentBlueprint_Write'
      required:
        - blueprint
      title: AgentConfigCreate_Write
    Agent Configs_createAgentConfig_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Agent Configs_createAgentConfig_Response_201
    ErrorMessage_Write:
      type: object
      properties:
        errors:
          type: array
          items:
            type: string
      title: ErrorMessage_Write

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/agent-configs/blueprints"

payload = { "blueprint": {
        "type": "blueprint",
        "values": [
            {
                "key": "max_iterations",
                "value": "1000",
                "type": "integer"
            }
        ]
    } }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/agent-configs/blueprints';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"blueprint":{"type":"blueprint","values":[{"key":"max_iterations","value":"1000","type":"integer"}]}}'
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

	url := "http://localhost:5173/api/v1/private/agent-configs/blueprints"

	payload := strings.NewReader("{\n  \"blueprint\": {\n    \"type\": \"blueprint\",\n    \"values\": [\n      {\n        \"key\": \"max_iterations\",\n        \"value\": \"1000\",\n        \"type\": \"integer\"\n      }\n    ]\n  }\n}")

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

url = URI("http://localhost:5173/api/v1/private/agent-configs/blueprints")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"blueprint\": {\n    \"type\": \"blueprint\",\n    \"values\": [\n      {\n        \"key\": \"max_iterations\",\n        \"value\": \"1000\",\n        \"type\": \"integer\"\n      }\n    ]\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/agent-configs/blueprints")
  .header("Content-Type", "application/json")
  .body("{\n  \"blueprint\": {\n    \"type\": \"blueprint\",\n    \"values\": [\n      {\n        \"key\": \"max_iterations\",\n        \"value\": \"1000\",\n        \"type\": \"integer\"\n      }\n    ]\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/agent-configs/blueprints', [
  'body' => '{
  "blueprint": {
    "type": "blueprint",
    "values": [
      {
        "key": "max_iterations",
        "value": "1000",
        "type": "integer"
      }
    ]
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/agent-configs/blueprints");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"blueprint\": {\n    \"type\": \"blueprint\",\n    \"values\": [\n      {\n        \"key\": \"max_iterations\",\n        \"value\": \"1000\",\n        \"type\": \"integer\"\n      }\n    ]\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["blueprint": [
    "type": "blueprint",
    "values": [
      [
        "key": "max_iterations",
        "value": "1000",
        "type": "integer"
      ]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/agent-configs/blueprints")! as URL,
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