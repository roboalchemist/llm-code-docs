# Source: https://www.comet.com/docs/opik/reference/rest-api/runners/get-job.mdx

# Get local runner job

GET http://localhost:5173/api/v1/private/local-runners/jobs/{jobId}

Get a single local runner job's status and results

Reference: https://www.comet.com/docs/opik/reference/rest-api/runners/get-job

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/local-runners/jobs/{jobId}:
    get:
      operationId: get-job
      summary: Get local runner job
      description: Get a single local runner job's status and results
      tags:
        - subpackage_runners
      parameters:
        - name: jobId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Job details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LocalRunnerJob'
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

url = "http://localhost:5173/api/v1/private/local-runners/jobs/jobId"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/local-runners/jobs/jobId';
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

	url := "http://localhost:5173/api/v1/private/local-runners/jobs/jobId"

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

url = URI("http://localhost:5173/api/v1/private/local-runners/jobs/jobId")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/local-runners/jobs/jobId")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/local-runners/jobs/jobId', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/local-runners/jobs/jobId");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/local-runners/jobs/jobId")! as URL,
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