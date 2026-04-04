# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/score-batch-of-traces.mdx

# Batch feedback scoring for traces

PUT http://localhost:5173/api/v1/private/traces/feedback-scores
Content-Type: application/json

Batch feedback scoring for traces

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/score-batch-of-traces

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/feedback-scores:
    put:
      operationId: score-batch-of-traces
      summary: Batch feedback scoring for traces
      description: Batch feedback scoring for traces
      tags:
        - subpackage_traces
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Traces_scoreBatchOfTraces_Response_204'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FeedbackScoreBatch'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    FeedbackScoreBatchItemSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScoreBatchItemSource
    FeedbackScoreBatchItem:
      type: object
      properties:
        project_name:
          type: string
          description: If null, the default project is used
        project_id:
          type: string
          format: uuid
        name:
          type: string
        category_name:
          type: string
        value:
          type: number
          format: double
        reason:
          type: string
        source:
          $ref: '#/components/schemas/FeedbackScoreBatchItemSource'
        author:
          type: string
        id:
          type: string
          format: uuid
      required:
        - name
        - value
        - source
        - id
      title: FeedbackScoreBatchItem
    FeedbackScoreBatch:
      type: object
      properties:
        scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreBatchItem'
      required:
        - scores
      title: FeedbackScoreBatch
    Traces_scoreBatchOfTraces_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Traces_scoreBatchOfTraces_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/feedback-scores"

payload = { "scores": [
        {
            "name": "Latency Improvement",
            "value": 0.85,
            "source": "ui",
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
    ] }
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/feedback-scores';
const options = {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: '{"scores":[{"name":"Latency Improvement","value":0.85,"source":"ui","id":"3fa85f64-5717-4562-b3fc-2c963f66afa6"}]}'
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

	url := "http://localhost:5173/api/v1/private/traces/feedback-scores"

	payload := strings.NewReader("{\n  \"scores\": [\n    {\n      \"name\": \"Latency Improvement\",\n      \"value\": 0.85,\n      \"source\": \"ui\",\n      \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/traces/feedback-scores")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"scores\": [\n    {\n      \"name\": \"Latency Improvement\",\n      \"value\": 0.85,\n      \"source\": \"ui\",\n      \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/traces/feedback-scores")
  .header("Content-Type", "application/json")
  .body("{\n  \"scores\": [\n    {\n      \"name\": \"Latency Improvement\",\n      \"value\": 0.85,\n      \"source\": \"ui\",\n      \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/traces/feedback-scores', [
  'body' => '{
  "scores": [
    {
      "name": "Latency Improvement",
      "value": 0.85,
      "source": "ui",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
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

var client = new RestClient("http://localhost:5173/api/v1/private/traces/feedback-scores");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"scores\": [\n    {\n      \"name\": \"Latency Improvement\",\n      \"value\": 0.85,\n      \"source\": \"ui\",\n      \"id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["scores": [
    [
      "name": "Latency Improvement",
      "value": 0.85,
      "source": "ui",
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/feedback-scores")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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