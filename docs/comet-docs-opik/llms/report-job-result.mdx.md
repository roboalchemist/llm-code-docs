# Source: https://www.comet.com/docs/opik/reference/rest-api/runners/report-job-result.mdx

# Report local runner job result

POST http://localhost:5173/api/v1/private/local-runners/jobs/{jobId}/results
Content-Type: application/json

Report local runner job completion or failure

Reference: https://www.comet.com/docs/opik/reference/rest-api/runners/report-job-result

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/local-runners/jobs/{jobId}/results:
    post:
      operationId: report-job-result
      summary: Report local runner job result
      description: Report local runner job completion or failure
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
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Runners_reportJobResult_Response_204'
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LocalRunnerJobResultRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    LocalRunnerJobResultRequestStatus:
      type: string
      enum:
        - pending
        - running
        - completed
        - failed
        - cancelled
      title: LocalRunnerJobResultRequestStatus
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    LocalRunnerJobResultRequest:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/LocalRunnerJobResultRequestStatus'
        result:
          $ref: '#/components/schemas/JsonNode'
        error:
          type: string
        trace_id:
          type: string
          format: uuid
      required:
        - status
      title: LocalRunnerJobResultRequest
    Runners_reportJobResult_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Runners_reportJobResult_Response_204
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

url = "http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results"

payload = { "status": "pending" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"status":"pending"}'
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

	url := "http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results"

	payload := strings.NewReader("{\n  \"status\": \"pending\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"status\": \"pending\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results")
  .header("Content-Type", "application/json")
  .body("{\n  \"status\": \"pending\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results', [
  'body' => '{
  "status": "pending"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"status\": \"pending\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["status": "pending"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/local-runners/jobs/jobId/results")! as URL,
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