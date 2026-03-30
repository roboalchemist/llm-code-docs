# Source: https://www.comet.com/docs/opik/reference/rest-api/prompts/restore-prompt-version.mdx

# Restore prompt version

POST http://localhost:5173/api/v1/private/prompts/{promptId}/versions/{versionId}/restore

Restore a prompt version by creating a new version with the content from the specified version

Reference: https://www.comet.com/docs/opik/reference/rest-api/prompts/restore-prompt-version

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/prompts/{promptId}/versions/{versionId}/restore:
    post:
      operationId: restore-prompt-version
      summary: Restore prompt version
      description: >-
        Restore a prompt version by creating a new version with the content from
        the specified version
      tags:
        - subpackage_prompts
      parameters:
        - name: promptId
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: versionId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PromptVersion_Detail'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Detail'
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

url = "http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/prompts/promptId/versions/versionId/restore")! as URL,
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