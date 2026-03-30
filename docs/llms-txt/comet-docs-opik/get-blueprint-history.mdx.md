# Source: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/get-blueprint-history.mdx

# Get blueprint history

GET http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/{project_id}

Retrieves paginated blueprint history for a project

Reference: https://www.comet.com/docs/opik/reference/rest-api/agent-configs/get-blueprint-history

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/agent-configs/blueprints/history/projects/{project_id}:
    get:
      operationId: get-blueprint-history
      summary: Get blueprint history
      description: Retrieves paginated blueprint history for a project
      tags:
        - subpackage_agentConfigs
      parameters:
        - name: project_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: page
          in: query
          required: false
          schema:
            type: integer
            default: 1
        - name: size
          in: query
          required: false
          schema:
            type: integer
            default: 10
      responses:
        '200':
          description: History retrieved
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BlueprintPage_History'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_History'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_History'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AgentBlueprintHistoryType:
      type: string
      enum:
        - blueprint
        - mask
      title: AgentBlueprintHistoryType
    AgentConfigValueHistoryType:
      type: string
      enum:
        - string
        - integer
        - float
        - boolean
        - prompt
        - prompt_commit
      title: AgentConfigValueHistoryType
    AgentConfigValue_History:
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
          $ref: '#/components/schemas/AgentConfigValueHistoryType'
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
      title: AgentConfigValue_History
    AgentBlueprint_History:
      type: object
      properties:
        id:
          type: string
          format: uuid
        type:
          $ref: '#/components/schemas/AgentBlueprintHistoryType'
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
            $ref: '#/components/schemas/AgentConfigValue_History'
      required:
        - type
        - values
      title: AgentBlueprint_History
    BlueprintPage_History:
      type: object
      properties:
        page:
          type: integer
        size:
          type: integer
        total:
          type: integer
          format: int64
        content:
          type: array
          items:
            $ref: '#/components/schemas/AgentBlueprint_History'
      title: BlueprintPage_History
    ErrorMessage_History:
      type: object
      properties:
        errors:
          type: array
          items:
            type: string
      title: ErrorMessage_History

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id';
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

	url := "http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id"

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

url = URI("http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/agent-configs/blueprints/history/projects/project_id")! as URL,
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