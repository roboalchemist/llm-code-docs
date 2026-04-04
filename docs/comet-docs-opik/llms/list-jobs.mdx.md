# Source: https://www.comet.com/docs/opik/reference/rest-api/runners/list-jobs.mdx

# List local runner jobs

GET http://localhost:5173/api/v1/private/local-runners/{runnerId}/jobs

List jobs for a local runner

Reference: https://www.comet.com/docs/opik/reference/rest-api/runners/list-jobs

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/local-runners/{runnerId}/jobs:
    get:
      operationId: list-jobs
      summary: List local runner jobs
      description: List jobs for a local runner
      tags:
        - subpackage_runners
      parameters:
        - name: runnerId
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: project
          in: query
          required: false
          schema:
            type: string
        - name: page
          in: query
          required: false
          schema:
            type: integer
            default: 0
        - name: size
          in: query
          required: false
          schema:
            type: integer
            default: 25
      responses:
        '200':
          description: Jobs list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LocalRunnerJobPage'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    LocalRunnerJobStatus:
      type: string
      enum:
        - pending
        - running
        - completed
        - failed
        - cancelled
      title: LocalRunnerJobStatus
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
    LocalRunnerJob:
      type: object
      properties:
        id:
          type: string
          format: uuid
        runner_id:
          type: string
          format: uuid
        agent_name:
          type: string
        status:
          $ref: '#/components/schemas/LocalRunnerJobStatus'
        inputs:
          $ref: '#/components/schemas/JsonNode'
        result:
          $ref: '#/components/schemas/JsonNode'
        error:
          type: string
        project:
          type: string
        trace_id:
          type: string
          format: uuid
        mask_id:
          type: string
          format: uuid
        metadata:
          $ref: '#/components/schemas/LocalRunnerJobMetadata'
        timeout:
          type: integer
        created_at:
          type: string
          format: date-time
        started_at:
          type: string
          format: date-time
        completed_at:
          type: string
          format: date-time
      title: LocalRunnerJob
    LocalRunnerJobPage:
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
            $ref: '#/components/schemas/LocalRunnerJob'
      title: LocalRunnerJobPage
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

url = "http://localhost:5173/api/v1/private/local-runners/runnerId/jobs"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/local-runners/runnerId/jobs';
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

	url := "http://localhost:5173/api/v1/private/local-runners/runnerId/jobs"

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

url = URI("http://localhost:5173/api/v1/private/local-runners/runnerId/jobs")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/local-runners/runnerId/jobs")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/local-runners/runnerId/jobs', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/local-runners/runnerId/jobs");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/local-runners/runnerId/jobs")! as URL,
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