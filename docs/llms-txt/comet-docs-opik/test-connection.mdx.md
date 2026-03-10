# Source: https://www.comet.com/docs/opik/reference/rest-api/ollama/test-connection.mdx

# Test connection to Ollama instance

POST http://localhost:5173/api/v1/private/ollama/test-connection
Content-Type: application/json

Validates that the provided Ollama URL is reachable. URL may be provided with or without /v1 suffix (e.g., http://localhost:11434 or http://localhost:11434/v1). The /v1 suffix will be automatically removed for connection testing. For inference, use the URL with /v1 suffix.

Reference: https://www.comet.com/docs/opik/reference/rest-api/ollama/test-connection

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/ollama/test-connection:
    post:
      operationId: test-connection
      summary: Test connection to Ollama instance
      description: >-
        Validates that the provided Ollama URL is reachable. URL may be provided
        with or without /v1 suffix (e.g., http://localhost:11434 or
        http://localhost:11434/v1). The /v1 suffix will be automatically removed
        for connection testing. For inference, use the URL with /v1 suffix.
      tags:
        - subpackage_ollama
      responses:
        '200':
          description: Connection test successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OllamaConnectionTestResponse'
        '422':
          description: Unprocessable Content - Invalid URL format
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '502':
          description: Connection test failed - Ollama instance unreachable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OllamaConnectionTestResponse'
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
    OllamaConnectionTestResponse:
      type: object
      properties:
        connected:
          type: boolean
          description: Whether the connection was successful
        version:
          type: string
          description: >-
            Server version (returned even if connection failed or version is
            incompatible)
        error_message:
          type: string
          description: Error message if connection failed
      description: Response from Ollama connection test.
      title: OllamaConnectionTestResponse
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

url = "http://localhost:5173/api/v1/private/ollama/test-connection"

payload = { "base_url": "http://localhost:11434/v1" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/ollama/test-connection';
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

	url := "http://localhost:5173/api/v1/private/ollama/test-connection"

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

url = URI("http://localhost:5173/api/v1/private/ollama/test-connection")

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

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/ollama/test-connection")
  .header("Content-Type", "application/json")
  .body("{\n  \"base_url\": \"http://localhost:11434/v1\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/ollama/test-connection', [
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

var client = new RestClient("http://localhost:5173/api/v1/private/ollama/test-connection");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/ollama/test-connection")! as URL,
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