# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/delete-trace-feedback-score.mdx

# Delete trace feedback score

POST http://localhost:5173/api/v1/private/traces/{id}/feedback-scores/delete
Content-Type: application/json

Delete trace feedback score

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/delete-trace-feedback-score

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/{id}/feedback-scores/delete:
    post:
      operationId: delete-trace-feedback-score
      summary: Delete trace feedback score
      description: Delete trace feedback score
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
                $ref: >-
                  #/components/schemas/Traces_deleteTraceFeedbackScore_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeleteFeedbackScore'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DeleteFeedbackScore:
      type: object
      properties:
        name:
          type: string
        author:
          type: string
      required:
        - name
      title: DeleteFeedbackScore
    Traces_deleteTraceFeedbackScore_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Traces_deleteTraceFeedbackScore_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete"

payload = { "name": "AccuracyScoreFeedback" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"AccuracyScoreFeedback"}'
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

	url := "http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete"

	payload := strings.NewReader("{\n  \"name\": \"AccuracyScoreFeedback\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"AccuracyScoreFeedback\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"AccuracyScoreFeedback\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete', [
  'body' => '{
  "name": "AccuracyScoreFeedback"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"AccuracyScoreFeedback\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "AccuracyScoreFeedback"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/id/feedback-scores/delete")! as URL,
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