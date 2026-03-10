# Source: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/create-or-update-envs.mdx

# Create or update environments

POST http://localhost:5173/api/v1/private/agent-configs/blueprints/environments
Content-Type: application/json

Creates or updates environment-to-blueprint mappings

Reference: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/create-or-update-envs

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/agent-configs/blueprints/environments:
    post:
      operationId: create-or-update-envs
      summary: Create or update environments
      description: Creates or updates environment-to-blueprint mappings
      tags:
        - subpackage_agentConfigs
      responses:
        '204':
          description: Environments updated
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Agent
                  Configs_createOrUpdateEnvs_Response_204
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AgentConfigEnvUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AgentConfigEnv:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_id:
          type: string
          format: uuid
        env_name:
          type: string
        blueprint_id:
          type: string
          format: uuid
        created_by:
          type: string
        created_at:
          type: string
          format: date-time
        last_updated_by:
          type: string
        last_updated_at:
          type: string
          format: date-time
      required:
        - env_name
        - blueprint_id
      title: AgentConfigEnv
    AgentConfigEnvUpdate:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
        envs:
          type: array
          items:
            $ref: '#/components/schemas/AgentConfigEnv'
      required:
        - project_id
        - envs
      title: AgentConfigEnvUpdate
    Agent Configs_createOrUpdateEnvs_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Agent Configs_createOrUpdateEnvs_Response_204
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

url = "http://localhost:5173/api/v1/private/agent-configs/blueprints/environments"

payload = {
    "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "envs": [
        {
            "env_name": "production",
            "blueprint_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"
        }
    ]
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/agent-configs/blueprints/environments';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"project_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","envs":[{"env_name":"production","blueprint_id":"7c9e6679-7425-40de-944b-e07fc1f90ae7"}]}'
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

	url := "http://localhost:5173/api/v1/private/agent-configs/blueprints/environments"

	payload := strings.NewReader("{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"envs\": [\n    {\n      \"env_name\": \"production\",\n      \"blueprint_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n    }\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/agent-configs/blueprints/environments")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"envs\": [\n    {\n      \"env_name\": \"production\",\n      \"blueprint_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/agent-configs/blueprints/environments")
  .header("Content-Type", "application/json")
  .body("{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"envs\": [\n    {\n      \"env_name\": \"production\",\n      \"blueprint_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/agent-configs/blueprints/environments', [
  'body' => '{
  "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "envs": [
    {
      "env_name": "production",
      "blueprint_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"
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

var client = new RestClient("http://localhost:5173/api/v1/private/agent-configs/blueprints/environments");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"envs\": [\n    {\n      \"env_name\": \"production\",\n      \"blueprint_id\": \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "envs": [
    [
      "env_name": "production",
      "blueprint_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/agent-configs/blueprints/environments")! as URL,
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