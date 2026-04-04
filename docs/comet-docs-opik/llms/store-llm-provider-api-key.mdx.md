# Source: https://www.comet.com/docs/opik/reference/rest-api/llm-provider-key/store-llm-provider-api-key.mdx

# Store LLM Provider's ApiKey

POST http://localhost:5173/api/v1/private/llm-provider-key
Content-Type: application/json

Store LLM Provider's ApiKey

Reference: https://www.comet.com/docs/opik/reference/rest-api/llm-provider-key/store-llm-provider-api-key

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/llm-provider-key:
    post:
      operationId: store-llm-provider-api-key
      summary: Store LLM Provider's ApiKey
      description: Store LLM Provider's ApiKey
      tags:
        - subpackage_llmProviderKey
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/LlmProviderKey_storeLlmProviderApiKey_Response_201
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProviderApiKey_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ProviderApiKeyWriteProvider:
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
      title: ProviderApiKeyWriteProvider
    ProviderApiKey_Write:
      type: object
      properties:
        provider:
          $ref: '#/components/schemas/ProviderApiKeyWriteProvider'
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
      required:
        - provider
      title: ProviderApiKey_Write
    LlmProviderKey_storeLlmProviderApiKey_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: LlmProviderKey_storeLlmProviderApiKey_Response_201
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

url = "http://localhost:5173/api/v1/private/llm-provider-key"

payload = { "provider": "openai" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/llm-provider-key';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"provider":"openai"}'
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

	url := "http://localhost:5173/api/v1/private/llm-provider-key"

	payload := strings.NewReader("{\n  \"provider\": \"openai\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/llm-provider-key")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"provider\": \"openai\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/llm-provider-key")
  .header("Content-Type", "application/json")
  .body("{\n  \"provider\": \"openai\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/llm-provider-key', [
  'body' => '{
  "provider": "openai"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/llm-provider-key");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"provider\": \"openai\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["provider": "openai"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/llm-provider-key")! as URL,
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