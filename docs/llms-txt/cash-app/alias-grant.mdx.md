# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/alias-grant.mdx

# Create Grant Alias

POST https://global-api-sandbox.afterpay.com/v2/grants/alias
Content-Type: application/json

Creates an alias for an existing grant to help load the payment schedule widget.


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/alias-grant

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/grants/alias:
    post:
      operationId: alias-grant
      summary: Create Grant Alias
      description: >
        Creates an alias for an existing grant to help load the payment schedule
        widget.
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
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GrantAliasResponse'
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
              $ref: '#/components/schemas/GrantAliasRequest'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    GrantAliasRequest:
      type: object
      properties:
        token:
          type: string
          description: Token of the grant to create an alias for
        duration:
          type:
            - string
            - 'null'
          format: duration
          description: Duration of the grant in ISO-8601 period format
      required:
        - token
      title: GrantAliasRequest
    GrantAliasResponse:
      type: object
      properties:
        token:
          type: string
          description: Token representing the grant alias
        expiry:
          type: string
          format: date-time
          description: Timestamp when the alias token expires
      required:
        - token
        - expiry
      title: GrantAliasResponse
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/grants/alias"

payload = { "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2" }
headers = {
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/grants/alias';
const options = {
  method: 'POST',
  headers: {
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"token":"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2"}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/grants/alias"

	payload := strings.NewReader("{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/grants/alias")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/grants/alias")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/grants/alias', [
  'body' => '{
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/grants/alias");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = ["token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/grants/alias")! as URL,
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