# Source: https://www.comet.com/docs/opik/reference/rest-api/prompts/get-prompt-by-id.mdx

# Get prompt by id

GET http://localhost:5173/api/v1/private/prompts/{id}

Get prompt by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/prompts/get-prompt-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/prompts/{id}:
    get:
      operationId: get-prompt-by-id
      summary: Get prompt by id
      description: Get prompt by id
      tags:
        - subpackage_prompts
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Prompt resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Prompt_Detail'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Detail'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    PromptDetailTemplateStructure:
      type: string
      enum:
        - text
        - chat
      default: text
      description: 'Template structure type: ''text'' or ''chat''. Immutable after creation.'
      title: PromptDetailTemplateStructure
    JsonNode_Detail:
      type: object
      properties: {}
      title: JsonNode_Detail
    PromptVersionDetailType:
      type: string
      enum:
        - mustache
        - jinja2
      title: PromptVersionDetailType
    PromptVersionDetailTemplateStructure:
      type: string
      enum:
        - text
        - chat
      title: PromptVersionDetailTemplateStructure
    PromptVersion_Detail:
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
          $ref: '#/components/schemas/JsonNode_Detail'
        type:
          $ref: '#/components/schemas/PromptVersionDetailType'
        change_description:
          type: string
        tags:
          type: array
          items:
            type: string
        variables:
          type: array
          items:
            type: string
        template_structure:
          $ref: '#/components/schemas/PromptVersionDetailTemplateStructure'
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
      required:
        - template
      title: PromptVersion_Detail
    Prompt_Detail:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        template_structure:
          $ref: '#/components/schemas/PromptDetailTemplateStructure'
          description: 'Template structure type: ''text'' or ''chat''. Immutable after creation.'
        tags:
          type: array
          items:
            type: string
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_at:
          type: string
          format: date-time
        last_updated_by:
          type: string
        version_count:
          type: integer
          format: int64
        latest_version:
          $ref: '#/components/schemas/PromptVersion_Detail'
        requested_version:
          $ref: '#/components/schemas/PromptVersion_Detail'
      required:
        - name
      title: Prompt_Detail
    ErrorMessage_Detail:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage_Detail

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/prompts/id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/prompts/id';
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

	url := "http://localhost:5173/api/v1/private/prompts/id"

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

url = URI("http://localhost:5173/api/v1/private/prompts/id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/prompts/id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/prompts/id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/prompts/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/prompts/id")! as URL,
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