# Source: https://www.comet.com/docs/opik/reference/rest-api/llm-provider-key/update-llm-provider-api-key.mdx

# Update LLM Provider's ApiKey

PATCH http://localhost:5173/api/v1/private/llm-provider-key/{id}
Content-Type: application/json

Update LLM Provider's ApiKey

Reference: https://www.comet.com/docs/opik/reference/rest-api/llm-provider-key/update-llm-provider-api-key

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/llm-provider-key/{id}:
    patch:
      operationId: update-llm-provider-api-key
      summary: Update LLM Provider's ApiKey
      description: Update LLM Provider's ApiKey
      tags:
        - subpackage_llmProviderKey
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
                  #/components/schemas/LlmProviderKey_updateLlmProviderApiKey_Response_204
        '401':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '403':
          description: Access forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProviderApiKeyUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ProviderApiKeyUpdate:
      type: object
      properties:
        api_key:
          type: string
        name:
          type: string
        provider_name:
          type: string
          description: >-
            Provider name - can be set to migrate legacy custom LLM or Bedrock
            providers to the new multi-provider format. Once set, it cannot be
            changed. Should only be set for custom LLM and Bedrock providers.
        headers:
          type: object
          additionalProperties:
            type: string
        configuration:
          type: object
          additionalProperties:
            type: string
        base_url:
          type: string
      title: ProviderApiKeyUpdate
    LlmProviderKey_updateLlmProviderApiKey_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: LlmProviderKey_updateLlmProviderApiKey_Response_204
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

url = "http://localhost:5173/api/v1/private/llm-provider-key/id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/llm-provider-key/id';
const options = {method: 'PATCH', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/llm-provider-key/id"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/llm-provider-key/id")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/llm-provider-key/id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/llm-provider-key/id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/llm-provider-key/id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/llm-provider-key/id")! as URL,
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