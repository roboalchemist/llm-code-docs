# Source: https://www.comet.com/docs/opik/reference/rest-api/runners/append-job-logs.mdx

# Append local runner job logs

POST http://localhost:5173/api/v1/private/local-runners/jobs/{jobId}/logs
Content-Type: application/json

Append log entries for a running local runner job

Reference: https://www.comet.com/docs/opik/reference/rest-api/runners/append-job-logs

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/local-runners/jobs/{jobId}/logs:
    post:
      operationId: append-job-logs
      summary: Append local runner job logs
      description: Append log entries for a running local runner job
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
                $ref: '#/components/schemas/Runners_appendJobLogs_Response_204'
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
              type: array
              items:
                $ref: '#/components/schemas/LocalRunnerLogEntry'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    LocalRunnerLogEntry:
      type: object
      properties:
        stream:
          type: string
        text:
          type: string
      required:
        - stream
        - text
      title: LocalRunnerLogEntry
    Runners_appendJobLogs_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Runners_appendJobLogs_Response_204
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

url = "http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs"

payload = [
    {
        "stream": "stdout",
        "text": "Job started successfully. Initializing environment variables."
    }
]
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '[{"stream":"stdout","text":"Job started successfully. Initializing environment variables."}]'
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

	url := "http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs"

	payload := strings.NewReader("[\n  {\n    \"stream\": \"stdout\",\n    \"text\": \"Job started successfully. Initializing environment variables.\"\n  }\n]")

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

url = URI("http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "[\n  {\n    \"stream\": \"stdout\",\n    \"text\": \"Job started successfully. Initializing environment variables.\"\n  }\n]"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs")
  .header("Content-Type", "application/json")
  .body("[\n  {\n    \"stream\": \"stdout\",\n    \"text\": \"Job started successfully. Initializing environment variables.\"\n  }\n]")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs', [
  'body' => '[
  {
    "stream": "stdout",
    "text": "Job started successfully. Initializing environment variables."
  }
]',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "[\n  {\n    \"stream\": \"stdout\",\n    \"text\": \"Job started successfully. Initializing environment variables.\"\n  }\n]", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  [
    "stream": "stdout",
    "text": "Job started successfully. Initializing environment variables."
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/local-runners/jobs/jobId/logs")! as URL,
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