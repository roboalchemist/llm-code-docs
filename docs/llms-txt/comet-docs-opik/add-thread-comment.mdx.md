# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/add-thread-comment.mdx

# Add thread comment

POST http://localhost:5173/api/v1/private/traces/threads/{id}/comments
Content-Type: application/json

Add thread comment

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/add-thread-comment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/threads/{id}/comments:
    post:
      operationId: add-thread-comment
      summary: Add thread comment
      description: Add thread comment
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
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Traces_addThreadComment_Response_201'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Comment'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    Comment:
      type: object
      properties:
        id:
          type: string
          format: uuid
        text:
          type: string
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
      required:
        - text
      title: Comment
    Traces_addThreadComment_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Traces_addThreadComment_Response_201

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/threads/id/comments"

payload = { "text": "I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes." }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/threads/id/comments';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"text":"I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes."}'
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

	url := "http://localhost:5173/api/v1/private/traces/threads/id/comments"

	payload := strings.NewReader("{\n  \"text\": \"I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes.\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/traces/threads/id/comments")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/traces/threads/id/comments")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/traces/threads/id/comments', [
  'body' => '{
  "text": "I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/threads/id/comments");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["text": "I believe the root cause of this issue is related to the recent database migration. We should verify the schema changes."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/threads/id/comments")! as URL,
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