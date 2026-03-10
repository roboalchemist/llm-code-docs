# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/retrieve-api-key.mdx

# Retrieve API key

GET https://api.cash.app/management/v1/api-keys/{api_key_id}

Retrieves an API key by ID.

**This endpoint is rate limited to 10 QPS.**

Scopes: `API_KEYS_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/retrieve-api-key

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /api-keys/{api_key_id}:
    get:
      operationId: retrieve-api-key
      summary: Retrieve API key
      description: |-
        Retrieves an API key by ID.

        **This endpoint is rate limited to 10 QPS.**

        Scopes: `API_KEYS_READ`
      tags:
        - subpackage_apiKeys
      parameters:
        - name: api_key_id
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
                $ref: '#/components/schemas/apiKeys_retrieve-api-key_Response_200'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
    ScopesItems:
      type: string
      enum:
        - PAYMENTS_READ
        - PAYMENTS_WRITE
        - REFUNDS_READ
        - REFUNDS_WRITE
        - DISPUTES_READ
        - DISPUTES_WRITE
        - CUSTOMERS_READ
        - FEE_PLANS_READ
        - GRANTS_READ
        - GRANTS_WRITE
        - API_KEYS_READ
        - API_KEYS_WRITE
        - BRANDS_READ
        - BRANDS_WRITE
        - MERCHANTS_READ
        - MERCHANTS_WRITE
        - WEBHOOK_CONFIG_READ
        - WEBHOOK_CONFIG_WRITE
        - WEBHOOK_EVENTS_READ
      title: ScopesItems
    Scopes:
      type: array
      items:
        $ref: '#/components/schemas/ScopesItems'
      description: >-
        An array of permissions granted to the API key.


        Current values:


        - `API_KEYS_READ`: Permits listing API keys and retrieving individual
        keys.

        - `API_KEYS_WRITE`: Permits creating and deleting API keys.

        - `BRANDS_READ`: Permits listing brands and retrieving individual
        brands.

        - `BRANDS_WRITE`: Permits creating, upserting, and updating brands.

        - `CUSTOMERS_READ`: Permits listing customers and retrieving individual
        customers.

        - `DISPUTES_READ`: Permits listing disputes / dispute evidence and
        retrieving details about individual disputes / dispute evidence.

        - `DISPUTES_WRITE`: Permits uploading dispute evidence, accepting
        disputes, and challenging disputes.

        - `FEE_PLANS_READ`: Permits listing fee plans and retrieving individual
        fee plans.

        - `GRANTS_READ`: Permits listing grants for a customer and retrieving
        individual grants.

        - `GRANTS_WRITE`: Permits revoking a grant.

        - `MERCHANTS_READ`: Permits listing merchants and retrieving individual
        merchants.

        - `MERCHANTS_WRITE`: Permits creating, upserting, and updating
        merchants.

        - `PAYMENTS_READ`: Permits listing payments and retrieving individual
        payments.

        - `PAYMENTS_WRITE`: Permits taking payments, capturing payments, and
        voiding payments.

        - `REFUNDS_READ`: Permits listing refunds and retrieving individual
        refunds.

        - `REFUNDS_WRITE`: Permits issuing refunds, capturing refunds, and
        voiding refunds.

        - `WEBHOOK_CONFIG_READ`: Permits listing webhook delivery settings and
        retrieving individual configurations.

        - `WEBHOOK_CONFIG_WRITE`: Permits creating and updating webhook delivery
        settings.

        - `WEBHOOK_EVENTS_READ`: Permits listing webhook events and retrieving
        individual events.


        Min number of items: `1`
      title: Scopes
    ApiKey:
      type: object
      properties:
        id:
          type: string
          description: >-
            Unique identifier for this API key issued by Cash App. This is the
            API key value that is passed in the `Authorization` header.
        created_at:
          type: string
          format: date-time
          description: >-
            When this API key was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        expires_at:
          type: string
          format: date-time
          description: >-
            When this API key will be automatically deleted and become unusable,
            in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format
            (UTC).
        scopes:
          $ref: '#/components/schemas/Scopes'
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this API key, typically used to
            associate the API key with a record in an external system.


            Min length: `1`

            Max length: `1024`
      required:
        - id
        - created_at
        - expires_at
        - scopes
      title: ApiKey
    apiKeys_retrieve-api-key_Response_200:
      type: object
      properties:
        api_key:
          $ref: '#/components/schemas/ApiKey'
      required:
        - api_key
      title: apiKeys_retrieve-api-key_Response_200
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

url = "https://api.cash.app/management/v1/api-keys/api_key_id"

headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/management/v1/api-keys/api_key_id';
const options = {
  method: 'GET',
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

	url := "https://api.cash.app/management/v1/api-keys/api_key_id"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.cash.app/management/v1/api-keys/api_key_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
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

HttpResponse<String> response = Unirest.get("https://api.cash.app/management/v1/api-keys/api_key_id")
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

$response = $client->request('GET', 'https://api.cash.app/management/v1/api-keys/api_key_id', [
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

var client = new RestClient("https://api.cash.app/management/v1/api-keys/api_key_id");
var request = new RestRequest(Method.GET);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/api-keys/api_key_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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