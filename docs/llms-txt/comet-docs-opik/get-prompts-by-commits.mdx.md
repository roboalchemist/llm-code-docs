# Source: https://www.comet.com/docs/opik/reference/rest-api/prompts/get-prompts-by-commits.mdx

# Get prompts by commits

POST http://localhost:5173/api/v1/private/prompts/retrieve-by-commits
Content-Type: application/json

Get prompts by prompt version commits

Reference: https://www.comet.com/docs/opik/reference/rest-api/prompts/get-prompts-by-commits

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/prompts/retrieve-by-commits:
    post:
      operationId: get-prompts-by-commits
      summary: Get prompts by commits
      description: Get prompts by prompt version commits
      tags:
        - subpackage_prompts
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/PromptVersionLink_Public'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PromptVersionCommitsRequest_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    PromptVersionCommitsRequest_Public:
      type: object
      properties:
        commits:
          type: array
          items:
            type: string
      required:
        - commits
      title: PromptVersionCommitsRequest_Public
    PromptVersionLink_Public:
      type: object
      properties:
        prompt_version_id:
          type: string
          format: uuid
        commit:
          type: string
        prompt_id:
          type: string
          format: uuid
        prompt_name:
          type: string
      title: PromptVersionLink_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/prompts/retrieve-by-commits"

payload = { "commits": ["a1b2c3d4e5f67890123456789abcdef123456789"] }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/prompts/retrieve-by-commits';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"commits":["a1b2c3d4e5f67890123456789abcdef123456789"]}'
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

	url := "http://localhost:5173/api/v1/private/prompts/retrieve-by-commits"

	payload := strings.NewReader("{\n  \"commits\": [\n    \"a1b2c3d4e5f67890123456789abcdef123456789\"\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/prompts/retrieve-by-commits")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"commits\": [\n    \"a1b2c3d4e5f67890123456789abcdef123456789\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/prompts/retrieve-by-commits")
  .header("Content-Type", "application/json")
  .body("{\n  \"commits\": [\n    \"a1b2c3d4e5f67890123456789abcdef123456789\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/prompts/retrieve-by-commits', [
  'body' => '{
  "commits": [
    "a1b2c3d4e5f67890123456789abcdef123456789"
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

var client = new RestClient("http://localhost:5173/api/v1/private/prompts/retrieve-by-commits");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"commits\": [\n    \"a1b2c3d4e5f67890123456789abcdef123456789\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["commits": ["a1b2c3d4e5f67890123456789abcdef123456789"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/prompts/retrieve-by-commits")! as URL,
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