# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/delete-webhook-endpoint.mdx

# Delete webhook endpoint

DELETE https://api.cash.app/management/v1/webhook-endpoints/{webhook_endpoint_id}

Deletes the webhook endpoint matching the `webhook_endpoint_id` provided. Note: Events that are created before the webhook endpoint was deleted will still be delivered after the webhook endpoint gets deleted.

Scopes: `WEBHOOK_CONFIG_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/delete-webhook-endpoint

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /webhook-endpoints/{webhook_endpoint_id}:
    delete:
      operationId: delete-webhook-endpoint
      summary: Delete webhook endpoint
      description: >-
        Deletes the webhook endpoint matching the `webhook_endpoint_id`
        provided. Note: Events that are created before the webhook endpoint was
        deleted will still be delivered after the webhook endpoint gets deleted.


        Scopes: `WEBHOOK_CONFIG_WRITE`
      tags:
        - subpackage_webhooks
      parameters:
        - name: webhook_endpoint_id
          in: path
          required: true
          schema:
            type: string
        - name: Accept
          in: header
          required: true
          schema:
            type: string
        - name: X-Region
          in: header
          required: true
          schema:
            type: string
        - name: X-Signature
          in: header
          required: true
          schema:
            type: string
        - name: User-Agent
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/webhooks_delete-webhook-endpoint_Response_200
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
    webhooks_delete-webhook-endpoint_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: webhooks_delete-webhook-endpoint_Response_200
    ErrorCategory:
      type: string
      enum:
        - API_ERROR
        - AUTHENTICATION_ERROR
        - BRAND_ERROR
        - DISPUTE_ERROR
        - MERCHANT_ERROR
        - INVALID_REQUEST_ERROR
        - PAYMENT_PROCESSING_ERROR
        - RATE_LIMIT_ERROR
        - WEBHOOK_ERROR
        - API_KEY_ERROR
        - GRANT_ERROR
      description: The high-level reason the error occurred
      title: ErrorCategory
    Error:
      type: object
      properties:
        category:
          $ref: '#/components/schemas/ErrorCategory'
          description: The high-level reason the error occurred
        code:
          type: string
          description: >-
            A unique identifier for the specific type of error that occurred.
            See the Error Code Reference for more information.


            Min length: `1`
        detail:
          type: string
          description: >-
            Human-readable description of why the error occurred and how to
            resolve it.


            Min length: `1`
        field:
          type: string
          description: >-
            The field in the request that caused the error, using array and
            object dot notation.


            Min length: `1`
      required:
        - category
        - code
      description: Represents an error encountered during a request to the API.
      title: Error
    ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: |-
            A list of errors that occurred while processing the request.

            Min number of items: `1`
      required:
        - errors
      title: ErrorResponse

```

## SDK Code Examples

```python
import requests

url = "https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id"

headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.delete(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id';
const options = {
  method: 'DELETE',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent'
  }
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("X-Region", "X-Region")
	req.Header.Add("X-Signature", "X-Signature")
	req.Header.Add("User-Agent", "User-Agent")

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

url = URI("https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id', [
  'headers' => [
    'Accept' => 'Accept',
    'User-Agent' => 'User-Agent',
    'X-Region' => 'X-Region',
    'X-Signature' => 'X-Signature',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/webhook-endpoints/webhook_endpoint_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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