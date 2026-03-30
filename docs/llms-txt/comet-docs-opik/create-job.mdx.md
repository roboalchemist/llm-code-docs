# Source: https://www.comet.com/docs/opik/reference/rest-api/runners/create-job.mdx

# Create local runner job

POST http://localhost:5173/api/v1/private/local-runners/jobs
Content-Type: application/json

Create a local runner job and enqueue it for execution

Reference: https://www.comet.com/docs/opik/reference/rest-api/runners/create-job

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/local-runners/jobs:
    post:
      operationId: create-job
      summary: Create local runner job
      description: Create a local runner job and enqueue it for execution
      tags:
        - subpackage_runners
      responses:
        '201':
          description: Job created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Runners_createJob_Response_201'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateLocalRunnerJobRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    LocalRunnerJobMetadata:
      type: object
      properties:
        dataset_id:
          type: string
          format: uuid
        dataset_version_id:
          type: string
          format: uuid
        dataset_item_version_id:
          type: string
          format: uuid
        dataset_item_id:
          type: string
          format: uuid
      title: LocalRunnerJobMetadata
    CreateLocalRunnerJobRequest:
      type: object
      properties:
        agent_name:
          type: string
        inputs:
          $ref: '#/components/schemas/JsonNode'
        project:
          type: string
        runner_id:
          type: string
          format: uuid
        mask_id:
          type: string
          format: uuid
        metadata:
          $ref: '#/components/schemas/LocalRunnerJobMetadata'
      required:
        - agent_name
      title: CreateLocalRunnerJobRequest
    Runners_createJob_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Runners_createJob_Response_201
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

url = "http://localhost:5173/api/v1/private/local-runners/jobs"

payload = { "agent_name": "local-runner-agent-01" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/local-runners/jobs';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"agent_name":"local-runner-agent-01"}'
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

	url := "http://localhost:5173/api/v1/private/local-runners/jobs"

	payload := strings.NewReader("{\n  \"agent_name\": \"local-runner-agent-01\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/local-runners/jobs")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"agent_name\": \"local-runner-agent-01\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/local-runners/jobs")
  .header("Content-Type", "application/json")
  .body("{\n  \"agent_name\": \"local-runner-agent-01\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/local-runners/jobs', [
  'body' => '{
  "agent_name": "local-runner-agent-01"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/local-runners/jobs");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"agent_name\": \"local-runner-agent-01\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["agent_name": "local-runner-agent-01"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/local-runners/jobs")! as URL,
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