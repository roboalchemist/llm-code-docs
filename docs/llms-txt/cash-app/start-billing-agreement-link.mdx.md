# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/start-billing-agreement-link.mdx

# Start Grant Link Flow

POST https://global-api-sandbox.afterpay.com/v2/grants/start
Content-Type: application/json

Initiates the headless grant link flow process.


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/start-billing-agreement-link

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/grants/start:
    post:
      operationId: start-billing-agreement-link
      summary: Start Grant Link Flow
      description: |
        Initiates the headless grant link flow process.
      tags:
        - ''
      parameters:
        - name: Authorization
          in: header
          description: Basic authentication
          required: true
          schema:
            type: string
        - name: Accept
          in: header
          required: false
          schema:
            type: string
            default: application/json
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GrantStartResponse'
        '404':
          description: |
            | errorCode | Description |
            | --- | --- |
            | not_found | Afterpay consumer account does not exist |
          content:
            application/json:
              schema:
                description: Any type
        '412':
          description: |
            | errorCode | Description |
            | --- | --- |
            | invalid_state | Failed to send code |
          content:
            application/json:
              schema:
                description: Any type
        '429':
          description: |
            | errorCode | Description |
            | --- | --- |
            | too_many_requests | Too many requests |
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GrantStartRequest'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    GrantStartRequest:
      type: object
      properties:
        alias:
          type: string
          description: Email or phone number associated with the consumer's account
        requestId:
          type: string
          description: A unique identifier for this request
      required:
        - alias
        - requestId
      title: GrantStartRequest
    GrantStartResponseDeliveryType:
      type: string
      enum:
        - SMS
        - EMAIL
      description: How the verification code was delivered to the consumer
      title: GrantStartResponseDeliveryType
    GrantStartResponse:
      type: object
      properties:
        token:
          type: string
          description: Token identifying the grant to be created
        requestId:
          type: string
          description: The unique identifier from the request
        expiresAt:
          type: string
          format: date-time
          description: When this link attempt will expire
        deliveryType:
          $ref: '#/components/schemas/GrantStartResponseDeliveryType'
          description: How the verification code was delivered to the consumer
      required:
        - token
        - requestId
        - expiresAt
        - deliveryType
      title: GrantStartResponse
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/grants/start"

payload = {
    "alias": "my-afterpay-email@gmail.com",
    "requestId": "123e4567-e89b-12d3-a456-426614174000"
}
headers = {
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/grants/start';
const options = {
  method: 'POST',
  headers: {
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"alias":"my-afterpay-email@gmail.com","requestId":"123e4567-e89b-12d3-a456-426614174000"}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/grants/start"

	payload := strings.NewReader("{\n  \"alias\": \"my-afterpay-email@gmail.com\",\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Basic <username>:<password>")
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

url = URI("https://global-api-sandbox.afterpay.com/v2/grants/start")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"alias\": \"my-afterpay-email@gmail.com\",\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/grants/start")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"alias\": \"my-afterpay-email@gmail.com\",\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/grants/start', [
  'body' => '{
  "alias": "my-afterpay-email@gmail.com",
  "requestId": "123e4567-e89b-12d3-a456-426614174000"
}',
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/grants/start");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"alias\": \"my-afterpay-email@gmail.com\",\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [
  "alias": "my-afterpay-email@gmail.com",
  "requestId": "123e4567-e89b-12d3-a456-426614174000"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/grants/start")! as URL,
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