# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/revoke-grant.mdx

# Revoke Grant

POST https://global-api-sandbox.afterpay.com/v2/grants/{grantId}/revoke

Revokes a grant, rendering it unusable. Other endpoints will no longer be able to use the grant to perform its associated action.


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/revoke-grant

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/grants/{grantId}/revoke:
    post:
      operationId: revoke-grant
      summary: Revoke Grant
      description: >
        Revokes a grant, rendering it unusable. Other endpoints will no longer
        be able to use the grant to perform its associated action.
      tags:
        - ''
      parameters:
        - name: grantId
          in: path
          description: The unique identifier id of the grant to revoke
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Basic authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
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
        '404':
          description: |
            | errorCode | Description |
            | --- | --- |
            | grant_not_found | The specified grant was not found. |
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
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

url = "https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke"

headers = {"Authorization": "Basic <username>:<password>"}

response = requests.post(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke';
const options = {method: 'POST', headers: {Authorization: 'Basic <username>:<password>'}};

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
	"net/http"
	"io"
)

func main() {

	url := "https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke"

	req, _ := http.NewRequest("POST", url, nil)

	req.Header.Add("Authorization", "Basic <username>:<password>")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Basic <username>:<password>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Basic <username>:<password>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Basic <username>:<password>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/grants/grantId/revoke")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers

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