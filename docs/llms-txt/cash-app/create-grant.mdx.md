# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/create-grant.mdx

# Create Grant

POST https://global-api-sandbox.afterpay.com/v2/grants
Content-Type: application/json

Creates a new grant from a grant approval token. 


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/create-grant

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/grants:
    post:
      operationId: create-grant
      summary: Create Grant
      description: |
        Creates a new grant from a grant approval token. 
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
                $ref: '#/components/schemas/GrantResponse'
        '403':
          description: >
            | errorCode | Description |

            | --- | --- |

            | feature_not_enabled | On file payments are not enabled for this
            merchant. |
          content:
            application/json:
              schema:
                description: Any type
        '412':
          description: |
            | errorCode | Description |
            | --- | --- |
            | consumer_ineligible | Consumer not eligible |
          content:
            application/json:
              schema:
                description: Any type
        '415':
          description: Unsupported Media Type - Content-Type header is missing or invalid
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateGrantRequest'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    CreateGrantRequest:
      type: object
      properties:
        requestId:
          type: string
          description: >-
            A unique request ID, required for idempotent retries. It is
            recommended that the merchant generate a UUID for each unique
            request.
        token:
          type: string
          description: The token returned from the create approval request.
        code:
          type: string
          description: |-
            The one-time code received from the consumer.
            Note: The code will only be sent with the headless integration.
      required:
        - requestId
        - token
      title: CreateGrantRequest
    GrantType:
      type: string
      enum:
        - ON_FILE
      description: Type of grant
      title: GrantType
    GrantStatus:
      type: string
      enum:
        - ACTIVE
        - CANCELLED
      description: Current status of the grant
      title: GrantStatus
    Grant:
      type: object
      properties:
        id:
          type: string
          description: Unique id identifying the grant
        type:
          $ref: '#/components/schemas/GrantType'
          description: Type of grant
        status:
          $ref: '#/components/schemas/GrantStatus'
          description: Current status of the grant
        created:
          type: string
          format: date-time
          description: Timestamp when the grant was created
        merchantReference:
          type:
            - string
            - 'null'
          description: Merchant's reference for this grant
        cancelled:
          type: string
          format: date-time
          description: If present, indicates when the grant was cancelled
        expires:
          type: string
          format: date-time
          description: >-
            If present, indicates when the grant's status will become EXPIRED,
            preventing a client from using it to create payments
        consumerReference:
          type:
            - string
            - 'null'
          description: Reference identifier for the consumer
        email:
          type:
            - string
            - 'null'
          description: Masked email address of the consumer
        requestId:
          type:
            - string
            - 'null'
          description: If present, unique identifier for the request
      required:
        - id
        - type
        - status
        - created
      title: Grant
    GrantResponse:
      type: object
      properties:
        grant:
          $ref: '#/components/schemas/Grant'
      required:
        - grant
      title: GrantResponse
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/grants"

payload = {
    "requestId": "123e4567-e89b-12d3-a456-426614174000",
    "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2"
}
headers = {
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/grants';
const options = {
  method: 'POST',
  headers: {
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"requestId":"123e4567-e89b-12d3-a456-426614174000","token":"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2"}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/grants"

	payload := strings.NewReader("{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/grants")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/grants")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/grants', [
  'body' => '{
  "requestId": "123e4567-e89b-12d3-a456-426614174000",
  "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2"
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/grants");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [
  "requestId": "123e4567-e89b-12d3-a456-426614174000",
  "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/grants")! as URL,
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