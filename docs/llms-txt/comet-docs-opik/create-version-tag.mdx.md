# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-version-tag.mdx

# Create version tag

POST http://localhost:5173/api/v1/private/datasets/{id}/versions/hash/{versionHash}/tags
Content-Type: application/json

Add a tag to a specific dataset version for easy reference (e.g., 'baseline', 'v1.0', 'production')

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-version-tag

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{id}/versions/hash/{versionHash}/tags:
    post:
      operationId: create-version-tag
      summary: Create version tag
      description: >-
        Add a tag to a specific dataset version for easy reference (e.g.,
        'baseline', 'v1.0', 'production')
      tags:
        - subpackage_datasets
      parameters:
        - name: versionHash
          in: path
          required: true
          schema:
            type: string
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: Tag created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Datasets_createVersionTag_Response_204'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '404':
          description: Not Found - Version not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '409':
          description: Conflict - Tag already exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetVersionTag'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetVersionTag:
      type: object
      properties:
        tag:
          type: string
      required:
        - tag
      title: DatasetVersionTag
    Datasets_createVersionTag_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_createVersionTag_Response_204
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

url = "http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags"

payload = { "tag": "v1.0" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"tag":"v1.0"}'
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

	url := "http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags"

	payload := strings.NewReader("{\n  \"tag\": \"v1.0\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tag\": \"v1.0\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags")
  .header("Content-Type", "application/json")
  .body("{\n  \"tag\": \"v1.0\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags', [
  'body' => '{
  "tag": "v1.0"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tag\": \"v1.0\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["tag": "v1.0"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/id/versions/hash/versionHash/tags")! as URL,
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