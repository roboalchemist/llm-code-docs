# Source: https://www.comet.com/docs/opik/reference/rest-api/ollama/list-models.mdx

# List available Ollama models

POST http://localhost:5173/api/v1/private/ollama/models
Content-Type: application/json

Fetches the list of models available from the Ollama instance. URL may be provided with or without /v1 suffix (e.g., http://localhost:11434 or http://localhost:11434/v1). The /v1 suffix will be automatically removed for model discovery. For actual LLM inference, use the URL with /v1 suffix for OpenAI-compatible endpoints.

Reference: https://www.comet.com/docs/opik/reference/rest-api/ollama/list-models

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/ollama/models:
    post:
      operationId: list-models
      summary: List available Ollama models
      description: >-
        Fetches the list of models available from the Ollama instance. URL may
        be provided with or without /v1 suffix (e.g., http://localhost:11434 or
        http://localhost:11434/v1). The /v1 suffix will be automatically removed
        for model discovery. For actual LLM inference, use the URL with /v1
        suffix for OpenAI-compatible endpoints.
      tags:
        - subpackage_ollama
      responses:
        '200':
          description: Models retrieved successfully
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/OllamaModel'
        '422':
          description: Unprocessable Content - Invalid URL format
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '500':
          description: Failed to fetch models
          content:
            application/json:
              schema:
                description: Any type
        '503':
          description: Ollama provider is disabled
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OllamaInstanceBaseUrlRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    OllamaInstanceBaseUrlRequest:
      type: object
      properties:
        base_url:
          type: string
          description: >-
            Base URL of the Ollama instance. May include /v1 suffix which will
            be automatically removed for connection testing. For inference, use
            the URL with /v1 suffix for OpenAI-compatible endpoints.
        api_key:
          type: string
          description: >-
            Optional API key for authenticated Ollama instances. If provided,
            will be sent as Bearer token in Authorization header.
      required:
        - base_url
      description: >-
        Request with Ollama instance base URL for connection testing or model
        discovery.
      title: OllamaInstanceBaseUrlRequest
    OllamaModel:
      type: object
      properties:
        name:
          type: string
          description: Model name
        size:
          type: integer
          format: int64
          description: Model size in bytes
        digest:
          type: string
          description: Model digest/hash
        modified_at:
          type: string
          format: date-time
          description: Model modification date
      required:
        - name
      description: Ollama model information
      title: OllamaModel
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

url = "http://localhost:5173/api/v1/private/ollama/models"

payload = { "base_url": "http://localhost:11434/v1" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/ollama/models';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"base_url":"http://localhost:11434/v1"}'
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

	url := "http://localhost:5173/api/v1/private/ollama/models"

	payload := strings.NewReader("{\n  \"base_url\": \"http://localhost:11434/v1\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/ollama/models")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"base_url\": \"http://localhost:11434/v1\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/ollama/models")
  .header("Content-Type", "application/json")
  .body("{\n  \"base_url\": \"http://localhost:11434/v1\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/ollama/models', [
  'body' => '{
  "base_url": "http://localhost:11434/v1"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/ollama/models");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"base_url\": \"http://localhost:11434/v1\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["base_url": "http://localhost:11434/v1"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/ollama/models")! as URL,
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