# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/delete-thread-feedback-scores.mdx

# Delete thread feedback scores

POST http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete
Content-Type: application/json

Delete thread feedback scores

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/delete-thread-feedback-scores

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/threads/feedback-scores/delete:
    post:
      operationId: delete-thread-feedback-scores
      summary: Delete thread feedback scores
      description: Delete thread feedback scores
      tags:
        - subpackage_traces
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Traces_deleteThreadFeedbackScores_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeleteThreadFeedbackScores'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DeleteThreadFeedbackScores:
      type: object
      properties:
        project_name:
          type: string
        thread_id:
          type: string
        names:
          type: array
          items:
            type: string
        author:
          type: string
      required:
        - project_name
        - thread_id
        - names
      title: DeleteThreadFeedbackScores
    Traces_deleteThreadFeedbackScores_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Traces_deleteThreadFeedbackScores_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete"

payload = {
    "project_name": "image-classification",
    "thread_id": "thread-987654321",
    "names": ["accuracy", "precision", "recall"]
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"project_name":"image-classification","thread_id":"thread-987654321","names":["accuracy","precision","recall"]}'
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

	url := "http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete"

	payload := strings.NewReader("{\n  \"project_name\": \"image-classification\",\n  \"thread_id\": \"thread-987654321\",\n  \"names\": [\n    \"accuracy\",\n    \"precision\",\n    \"recall\"\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"project_name\": \"image-classification\",\n  \"thread_id\": \"thread-987654321\",\n  \"names\": [\n    \"accuracy\",\n    \"precision\",\n    \"recall\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete")
  .header("Content-Type", "application/json")
  .body("{\n  \"project_name\": \"image-classification\",\n  \"thread_id\": \"thread-987654321\",\n  \"names\": [\n    \"accuracy\",\n    \"precision\",\n    \"recall\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete', [
  'body' => '{
  "project_name": "image-classification",
  "thread_id": "thread-987654321",
  "names": [
    "accuracy",
    "precision",
    "recall"
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

var client = new RestClient("http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"project_name\": \"image-classification\",\n  \"thread_id\": \"thread-987654321\",\n  \"names\": [\n    \"accuracy\",\n    \"precision\",\n    \"recall\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "project_name": "image-classification",
  "thread_id": "thread-987654321",
  "names": ["accuracy", "precision", "recall"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/threads/feedback-scores/delete")! as URL,
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