# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/add-trace-feedback-score.mdx

# Add trace feedback score

PUT http://localhost:5173/api/v1/private/traces/{id}/feedback-scores
Content-Type: application/json

Add trace feedback score

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/add-trace-feedback-score

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/{id}/feedback-scores:
    put:
      operationId: add-trace-feedback-score
      summary: Add trace feedback score
      description: Add trace feedback score
      tags:
        - subpackage_traces
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Traces_addTraceFeedbackScore_Response_204'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FeedbackScore'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    FeedbackScoreSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScoreSource
    ValueEntrySource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: ValueEntrySource
    ValueEntry:
      type: object
      properties:
        value:
          type: number
          format: double
        reason:
          type: string
        category_name:
          type: string
        source:
          $ref: '#/components/schemas/ValueEntrySource'
        last_updated_at:
          type: string
          format: date-time
        span_type:
          type: string
        span_id:
          type: string
      title: ValueEntry
    FeedbackScore:
      type: object
      properties:
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
          $ref: '#/components/schemas/FeedbackScoreSource'
        created_at:
          type: string
          format: date-time
        last_updated_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_by:
          type: string
        value_by_author:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ValueEntry'
      required:
        - name
        - value
        - source
      title: FeedbackScore
    Traces_addTraceFeedbackScore_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Traces_addTraceFeedbackScore_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/id/feedback-scores"

payload = {
    "name": "LatencyScore",
    "value": 250.5,
    "source": "ui"
}
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/id/feedback-scores';
const options = {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"LatencyScore","value":250.5,"source":"ui"}'
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

	url := "http://localhost:5173/api/v1/private/traces/id/feedback-scores"

	payload := strings.NewReader("{\n  \"name\": \"LatencyScore\",\n  \"value\": 250.5,\n  \"source\": \"ui\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/traces/id/feedback-scores")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"LatencyScore\",\n  \"value\": 250.5,\n  \"source\": \"ui\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/traces/id/feedback-scores")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"LatencyScore\",\n  \"value\": 250.5,\n  \"source\": \"ui\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/traces/id/feedback-scores', [
  'body' => '{
  "name": "LatencyScore",
  "value": 250.5,
  "source": "ui"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/id/feedback-scores");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"LatencyScore\",\n  \"value\": 250.5,\n  \"source\": \"ui\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "name": "LatencyScore",
  "value": 250.5,
  "source": "ui"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/id/feedback-scores")! as URL,
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