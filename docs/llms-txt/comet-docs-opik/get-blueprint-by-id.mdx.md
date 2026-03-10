# Source: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/get-blueprint-by-id.mdx

# Retrieve blueprint by ID

GET http://localhost:5173/api/v1/private/agent-configs/blueprints/{blueprint_id}

Retrieves a specific blueprint by its ID

Reference: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/get-blueprint-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/agent-configs/blueprints/{blueprint_id}:
    get:
      operationId: get-blueprint-by-id
      summary: Retrieve blueprint by ID
      description: Retrieves a specific blueprint by its ID
      tags:
        - subpackage_agentConfigs
      parameters:
        - name: blueprint_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: mask_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Blueprint retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AgentBlueprint_Public'
        '401':
          description: Unauthorized
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
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AgentBlueprintPublicType:
      type: string
      enum:
        - blueprint
        - mask
      title: AgentBlueprintPublicType
    AgentConfigValuePublicType:
      type: string
      enum:
        - string
        - integer
        - float
        - boolean
        - prompt
        - prompt_commit
      title: AgentConfigValuePublicType
    AgentConfigValue_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_id:
          type: string
          format: uuid
        key:
          type: string
        value:
          type: string
        type:
          $ref: '#/components/schemas/AgentConfigValuePublicType'
        description:
          type: string
        valid_from_blueprint_id:
          type: string
          format: uuid
        valid_to_blueprint_id:
          type: string
          format: uuid
      required:
        - key
        - value
        - type
      title: AgentConfigValue_Public
    AgentBlueprint_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        type:
          $ref: '#/components/schemas/AgentBlueprintPublicType'
        description:
          type: string
        envs:
          type: array
          items:
            type: string
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
        values:
          type: array
          items:
            $ref: '#/components/schemas/AgentConfigValue_Public'
      required:
        - type
        - values
      title: AgentBlueprint_Public
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

url = "http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id';
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

	url := "http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id"

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

url = URI("http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/agent-configs/blueprints/blueprint_id")! as URL,
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