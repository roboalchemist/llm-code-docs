# Source: https://www.comet.com/docs/opik/reference/rest-api/llm-provider-key/get-llm-provider-api-key-by-id.mdx

# Get LLM Provider's ApiKey by id

GET http://localhost:5173/api/v1/private/llm-provider-key/{id}

Get LLM Provider's ApiKey by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/llm-provider-key/get-llm-provider-api-key-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/llm-provider-key/{id}:
    get:
      operationId: get-llm-provider-api-key-by-id
      summary: Get LLM Provider's ApiKey by id
      description: Get LLM Provider's ApiKey by id
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
        '200':
          description: LLMProviderApiKey resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProviderApiKey_Public'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ProviderApiKeyPublicProvider:
      type: string
      enum:
        - openai
        - anthropic
        - gemini
        - openrouter
        - vertex-ai
        - bedrock
        - ollama
        - custom-llm
        - opik-free
      title: ProviderApiKeyPublicProvider
    ProviderApiKey_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        provider:
          $ref: '#/components/schemas/ProviderApiKeyPublicProvider'
        api_key:
          type: string
        name:
          type: string
        provider_name:
          type: string
          description: >-
            Provider name - required for custom LLM and Bedrock providers to
            uniquely identify them (e.g., 'ollama', 'vllm', 'Bedrock
            us-east-1'). Must not be blank for custom and Bedrock providers.
            Should not be set for standard providers (OpenAI, Anthropic, etc.).
            This requirement is conditional and validation is enforced
            programmatically.
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
        read_only:
          type: boolean
          description: >-
            If true, this provider is system-managed and cannot be edited or
            deleted
      required:
        - provider
      title: ProviderApiKey_Public
    ErrorMessage_Public:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/llm-provider-key/id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/llm-provider-key/id';
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

	url := "http://localhost:5173/api/v1/private/llm-provider-key/id"

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

url = URI("http://localhost:5173/api/v1/private/llm-provider-key/id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/llm-provider-key/id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/llm-provider-key/id', [
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/llm-provider-key/id")! as URL,
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