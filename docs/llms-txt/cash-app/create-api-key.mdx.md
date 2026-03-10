# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/create-api-key.mdx

# Create API key

POST https://api.cash.app/management/v1/api-keys
Content-Type: application/json

Creates a new API key and secret to use in the `Authorization` and `X-Signature` headers for requests to the Cash App Pay API. This key will automatically expire at the date and time specified in the `expires_at` field in the response payload.

<Note title="Note">
 The `secret` returned in the response payload is what you use to calculate the `X-Signature` header. The API key ID is only used to keep track of which API keys are active, and isn't considered secret.
 Keep in mind that the `secret` can never be retrieved in subsequent requests to the API, so make sure to store it immediately!
</Note>
**This endpoint is rate limited to 5 QPS.**

Scopes: `API_KEYS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/create-api-key

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /api-keys:
    post:
      operationId: create-api-key
      summary: Create API key
      description: >-
        Creates a new API key and secret to use in the `Authorization` and
        `X-Signature` headers for requests to the Cash App Pay API. This key
        will automatically expire at the date and time specified in the
        `expires_at` field in the response payload.


        <Note title="Note">
         The `secret` returned in the response payload is what you use to calculate the `X-Signature` header. The API key ID is only used to keep track of which API keys are active, and isn't considered secret.
         Keep in mind that the `secret` can never be retrieved in subsequent requests to the API, so make sure to store it immediately!
        </Note>

        **This endpoint is rate limited to 5 QPS.**


        Scopes: `API_KEYS_WRITE`
      tags:
        - subpackage_apiKeys
      parameters:
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
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/apiKeys_create-api-key_Response_201'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                idempotency_key:
                  $ref: '#/components/schemas/IdempotencyKey'
                api_key:
                  $ref: >-
                    #/components/schemas/ApiKeysPostRequestBodyContentApplicationJsonSchemaApiKey
                  description: Details about the API key to create.
              required:
                - idempotency_key
                - api_key
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
    IdempotencyKey:
      type: string
      description: >-
        A unique identifier which can be used by Cash App to de-duplicate
        retries of this request, making it idempotent. Learn more about
        [idempotency](../docs/api/technical-documentation/api-fundamentals/idempotency)
        in the API.
      title: IdempotencyKey
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
    ApiKeysPostRequestBodyContentApplicationJsonSchemaApiKey:
      type: object
      properties:
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
        - scopes
      description: Details about the API key to create.
      title: ApiKeysPostRequestBodyContentApplicationJsonSchemaApiKey
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
    apiKeys_create-api-key_Response_201:
      type: object
      properties:
        api_key:
          $ref: '#/components/schemas/ApiKey'
        secret:
          type: string
          description: >-
            Secret value to use when calculating the `X-Signature` header of
            requests.


            This value is not returned when retrieving an API key, so make sure
            to store it immediately.


            Min length: `32`

            Max length: `256`
      required:
        - api_key
        - secret
      title: apiKeys_create-api-key_Response_201
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

url = "https://api.cash.app/management/v1/api-keys"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "api_key": { "scopes": ["PAYMENTS_READ"] }
}
headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/management/v1/api-keys';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","api_key":{"scopes":["PAYMENTS_READ"]}}'
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

	url := "https://api.cash.app/management/v1/api-keys"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"api_key\": {\n    \"scopes\": [\n      \"PAYMENTS_READ\"\n    ]\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("X-Region", "X-Region")
	req.Header.Add("X-Signature", "X-Signature")
	req.Header.Add("User-Agent", "User-Agent")
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

url = URI("https://api.cash.app/management/v1/api-keys")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"api_key\": {\n    \"scopes\": [\n      \"PAYMENTS_READ\"\n    ]\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/management/v1/api-keys")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"api_key\": {\n    \"scopes\": [\n      \"PAYMENTS_READ\"\n    ]\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/management/v1/api-keys', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "api_key": {
    "scopes": [
      "PAYMENTS_READ"
    ]
  }
}',
  'headers' => [
    'Accept' => 'Accept',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
    'X-Region' => 'X-Region',
    'X-Signature' => 'X-Signature',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/api-keys");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"api_key\": {\n    \"scopes\": [\n      \"PAYMENTS_READ\"\n    ]\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = [
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "api_key": ["scopes": ["PAYMENTS_READ"]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/api-keys")! as URL,
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