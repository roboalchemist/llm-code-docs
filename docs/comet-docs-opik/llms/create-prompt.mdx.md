# Source: https://www.comet.com/docs/opik/reference/rest-api/prompts/create-prompt.mdx

# Create prompt

POST http://localhost:5173/api/v1/private/prompts
Content-Type: application/json

Create prompt

Reference: https://www.comet.com/docs/opik/reference/rest-api/prompts/create-prompt

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/prompts:
    post:
      operationId: create-prompt
      summary: Create prompt
      description: Create prompt
      tags:
        - subpackage_prompts
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Prompts_createPrompt_Response_201'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '422':
          description: Unprocessable Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Prompt_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonNode_Write:
      type: object
      properties: {}
      title: JsonNode_Write
    PromptWriteType:
      type: string
      enum:
        - mustache
        - jinja2
      title: PromptWriteType
    PromptWriteTemplateStructure:
      type: string
      enum:
        - text
        - chat
      default: text
      description: 'Template structure type: ''text'' or ''chat''. Immutable after creation.'
      title: PromptWriteTemplateStructure
    Prompt_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        template:
          type: string
        metadata:
          $ref: '#/components/schemas/JsonNode_Write'
        change_description:
          type: string
        type:
          $ref: '#/components/schemas/PromptWriteType'
        template_structure:
          $ref: '#/components/schemas/PromptWriteTemplateStructure'
          description: 'Template structure type: ''text'' or ''chat''. Immutable after creation.'
        tags:
          type: array
          items:
            type: string
      required:
        - name
      title: Prompt_Write
    Prompts_createPrompt_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Prompts_createPrompt_Response_201
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

url = "http://localhost:5173/api/v1/private/prompts"

payload = { "name": "Customer Support Greeting Prompt" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/prompts';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"Customer Support Greeting Prompt"}'
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

	url := "http://localhost:5173/api/v1/private/prompts"

	payload := strings.NewReader("{\n  \"name\": \"Customer Support Greeting Prompt\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/prompts")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Customer Support Greeting Prompt\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/prompts")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Customer Support Greeting Prompt\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/prompts', [
  'body' => '{
  "name": "Customer Support Greeting Prompt"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/prompts");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Customer Support Greeting Prompt\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "Customer Support Greeting Prompt"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/prompts")! as URL,
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