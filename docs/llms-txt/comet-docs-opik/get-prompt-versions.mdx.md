# Source: https://www.comet.com/docs/opik/reference/rest-api/prompts/get-prompt-versions.mdx

# Get prompt versions

GET http://localhost:5173/api/v1/private/prompts/{id}/versions

Get prompt versions

Reference: https://www.comet.com/docs/opik/reference/rest-api/prompts/get-prompt-versions

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/prompts/{id}/versions:
    get:
      operationId: get-prompt-versions
      summary: Get prompt versions
      description: Get prompt versions
      tags:
        - subpackage_prompts
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: page
          in: query
          required: false
          schema:
            type: integer
            default: 1
        - name: size
          in: query
          required: false
          schema:
            type: integer
            default: 10
        - name: search
          in: query
          description: Search text to find in template or change description fields
          required: false
          schema:
            type: string
        - name: sorting
          in: query
          required: false
          schema:
            type: string
        - name: filters
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptVersionPage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonNode_Public:
      type: object
      properties: {}
      title: JsonNode_Public
    PromptVersionPublicType:
      type: string
      enum:
        - mustache
        - jinja2
      title: PromptVersionPublicType
    PromptVersionPublicTemplateStructure:
      type: string
      enum:
        - text
        - chat
      title: PromptVersionPublicTemplateStructure
    PromptVersion_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: version unique identifier, generated if absent
        prompt_id:
          type: string
          format: uuid
        commit:
          type: string
          description: >-
            version short unique identifier, generated if absent. it must be 8
            characters long
        template:
          type: string
        metadata:
          $ref: '#/components/schemas/JsonNode_Public'
        type:
          $ref: '#/components/schemas/PromptVersionPublicType'
        change_description:
          type: string
        tags:
          type: array
          items:
            type: string
        template_structure:
          $ref: '#/components/schemas/PromptVersionPublicTemplateStructure'
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
      required:
        - template
      title: PromptVersion_Public
    PromptVersionPage_Public:
      type: object
      properties:
        page:
          type: integer
        size:
          type: integer
        total:
          type: integer
          format: int64
        content:
          type: array
          items:
            $ref: '#/components/schemas/PromptVersion_Public'
        sortableBy:
          type: array
          items:
            type: string
      title: PromptVersionPage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/prompts/id/versions"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/prompts/id/versions';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/prompts/id/versions"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/prompts/id/versions")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/prompts/id/versions")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/prompts/id/versions', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/prompts/id/versions");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/prompts/id/versions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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