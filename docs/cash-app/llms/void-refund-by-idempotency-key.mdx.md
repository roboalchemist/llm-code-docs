# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/void-refund-by-idempotency-key.mdx

# Void refund by idempotency key

POST https://api.cash.app/network/v1/refunds/void-by-idempotency-key
Content-Type: application/json

Moves an authorized refund to the voided state using the idempotency key specified while creating the refund.

<Note> 
You can only void an authorized refund. If a refund is captured, there is no way to reverse it.
</Note>

In rare cases, an issue with an integration, network connectivity, or the Cash App Pay API may cause an API client to end up in a state where a refund is created in Cash App Pay, but the API client doesn't know the ID of the refund. This endpoint allows an API client to void a refund using _only_ the idempotency key to recover from these situations.

If you don't have the idempotency key or ID of the refund you want to void, you can use the [list refunds](Network-API.v1.yaml/paths/~1refunds/get) endpoint to try to search for the refund you're looking for.

**This endpoint is not rate limited.**

Scopes: `REFUNDS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/void-refund-by-idempotency-key

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /refunds/void-by-idempotency-key:
    post:
      operationId: void-refund-by-idempotency-key
      summary: Void refund by idempotency key
      description: >-
        Moves an authorized refund to the voided state using the idempotency key
        specified while creating the refund.


        <Note> 

        You can only void an authorized refund. If a refund is captured, there
        is no way to reverse it.

        </Note>


        In rare cases, an issue with an integration, network connectivity, or
        the Cash App Pay API may cause an API client to end up in a state where
        a refund is created in Cash App Pay, but the API client doesn't know the
        ID of the refund. This endpoint allows an API client to void a refund
        using _only_ the idempotency key to recover from these situations.


        If you don't have the idempotency key or ID of the refund you want to
        void, you can use the [list
        refunds](Network-API.v1.yaml/paths/~1refunds/get) endpoint to try to
        search for the refund you're looking for.


        **This endpoint is not rate limited.**


        Scopes: `REFUNDS_WRITE`
      tags:
        - subpackage_refunds
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
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Refunds_void-refund-by-idempotency-key_Response_200
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                idempotency_key:
                  $ref: '#/components/schemas/IdempotencyKey'
              required:
                - idempotency_key
servers:
  - url: https://api.cash.app/network/v1
  - url: https://sandbox.api.cash.app/network/v1
components:
  schemas:
    IdempotencyKey:
      type: string
      description: >-
        A unique identifier which can be used by Cash App to de-duplicate
        retries of this request, making it idempotent. Learn more about
        idempotency in the API.
      title: IdempotencyKey
    Currency:
      type: string
      enum:
        - USD
      description: >-
        Indicates the country associated with an entity. Values are from the
        [ISO-4217 Alpha-3](https://www.iso.org/iso-4217-currency-codes.html)
        specification.


        Current values:


        - `USD`: United States Dollar
      title: Currency
    RefundStatus:
      type: string
      enum:
        - AUTHORIZED
        - CAPTURED
        - VOIDED
        - DECLINED
      description: >-
        The step of the refund processing lifecycle that this refund is
        currently at.


        - `AUTHORIZED`

        - `CAPTURED`

        - `VOIDED`

        - `DECLINED`
      title: RefundStatus
    Metadata:
      type: object
      additionalProperties:
        type: string
      description: >-
        Freeform key-value pairs of arbitrary data associated with this
        resource.


        Keys and values must be passed as strings and not contain any personally
        identifiable information (PII).


        Min keys: `0`

        Max keys: `50`



        > Note: Nested keys are not supported.
      title: Metadata
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
    Refund:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this refund issued by Cash App.

            Min length: `1`
            Max length: `128`
        amount:
          type: integer
          description: >-
            Amount of money to refund, in the lowest denomination of currency on
            the refund.


            Min value: `1`
        currency:
          $ref: '#/components/schemas/Currency'
        customer_id:
          type: string
          description: |-
            ID of the customer that received this refund.

            Min length: `1`
            Max length: `128`
        merchant_id:
          type: string
          description: |-
            ID of the merchant that issued this refund.

            Min length: `1`
            Max length: `128`
        status:
          $ref: '#/components/schemas/RefundStatus'
          description: >-
            The step of the refund processing lifecycle that this refund is
            currently at.


            - `AUTHORIZED`

            - `CAPTURED`

            - `VOIDED`

            - `DECLINED`
        created_at:
          type: string
          format: date-time
          description: >-
            When this refund was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this refund was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        grant_id:
          type: string
          description: |-
            This is currently unused and empty.

            Min length: `1`
            Max length: `256`
        payment_id:
          type: string
          description: |-
            This is currently unused and empty.

            Min length: `1`
            Max length: `128`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this refund, typically used to
            associate the refund with a record in an external system.


            Min length: `1`

            Max length: `1024`
        metadata:
          $ref: '#/components/schemas/Metadata'
        decline_errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: >-
            If the refund was declined, contains a list of the reasons why it
            was declined.


            Min number of items: `1`
      required:
        - id
        - amount
        - currency
        - customer_id
        - merchant_id
        - status
        - created_at
        - updated_at
      title: Refund
    Refunds_void-refund-by-idempotency-key_Response_200:
      type: object
      properties:
        refund:
          $ref: '#/components/schemas/Refund'
      required:
        - refund
      title: Refunds_void-refund-by-idempotency-key_Response_200
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

url = "https://api.cash.app/network/v1/refunds/void-by-idempotency-key"

payload = { "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19" }
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
const url = 'https://api.cash.app/network/v1/refunds/void-by-idempotency-key';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19"}'
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

	url := "https://api.cash.app/network/v1/refunds/void-by-idempotency-key"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\"\n}")

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

url = URI("https://api.cash.app/network/v1/refunds/void-by-idempotency-key")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/refunds/void-by-idempotency-key")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/refunds/void-by-idempotency-key', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19"
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

var client = new RestClient("https://api.cash.app/network/v1/refunds/void-by-idempotency-key");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\"\n}", ParameterType.RequestBody);
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
let parameters = ["idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/refunds/void-by-idempotency-key")! as URL,
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