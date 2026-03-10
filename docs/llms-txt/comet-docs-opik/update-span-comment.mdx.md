# Source: https://www.comet.com/docs/opik/reference/rest-api/spans/update-span-comment.mdx

# Update span comment by id

PATCH http://localhost:5173/api/v1/private/spans/comments/{commentId}
Content-Type: application/json

Update span comment by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/spans/update-span-comment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/spans/comments/{commentId}:
    patch:
      operationId: update-span-comment
      summary: Update span comment by id
      description: Update span comment by id
      tags:
        - subpackage_spans
      parameters:
        - name: commentId
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
                $ref: '#/components/schemas/Spans_updateSpanComment_Response_204'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                description: Any type
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
    Spans_updateSpanComment_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Spans_updateSpanComment_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/spans/comments/commentId"

payload = { "text": "Updated comment text to clarify span timing and context." }
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/spans/comments/commentId';
const options = {
  method: 'PATCH',
  headers: {'Content-Type': 'application/json'},
  body: '{"text":"Updated comment text to clarify span timing and context."}'
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

	url := "http://localhost:5173/api/v1/private/spans/comments/commentId"

	payload := strings.NewReader("{\n  \"text\": \"Updated comment text to clarify span timing and context.\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/spans/comments/commentId")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Updated comment text to clarify span timing and context.\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/spans/comments/commentId")
  .header("Content-Type", "application/json")
  .body("{\n  \"text\": \"Updated comment text to clarify span timing and context.\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/spans/comments/commentId', [
  'body' => '{
  "text": "Updated comment text to clarify span timing and context."
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/spans/comments/commentId");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Updated comment text to clarify span timing and context.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["text": "Updated comment text to clarify span timing and context."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/spans/comments/commentId")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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