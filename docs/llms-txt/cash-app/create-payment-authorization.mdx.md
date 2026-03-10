# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-payment-authorization.mdx

# Create incremental authorization

POST https://api.cash.app/network/v1/payments/{payment_id}/authorizations
Content-Type: application/json

Creates an authorization update for a payment. The authorization amount must be greater than or equal to the current authorized amount.

Use this endpoint for incremental authorization instead of overcapturing using the Capture payment endpoint. By creating additional payment authorizations exceeding the current authorized amount, you can request additional funds without risking the original amount being declined.

**This endpoint is not rate limited.** 

Scopes: `PAYMENTS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-payment-authorization

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /payments/{payment_id}/authorizations:
    post:
      operationId: create-payment-authorization
      summary: Create incremental authorization
      description: >-
        Creates an authorization update for a payment. The authorization amount
        must be greater than or equal to the current authorized amount.


        Use this endpoint for incremental authorization instead of overcapturing
        using the Capture payment endpoint. By creating additional payment
        authorizations exceeding the current authorized amount, you can request
        additional funds without risking the original amount being declined.


        **This endpoint is not rate limited.** 


        Scopes: `PAYMENTS_WRITE`
      tags:
        - subpackage_payments
      parameters:
        - name: payment_id
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
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Payments_create-payment-authorization_Response_201
        '400':
          description: >-
            Bad Request


            If a AUTHORIZATION_DECLINE_* error is returned, the authorization
            will still be created, but with a DECLINED status. This
            authorization will then appear in the response payload.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-payment-authorizationRequestBadRequestError
        '404':
          description: Not Found
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
                authorization:
                  $ref: >-
                    #/components/schemas/PaymentsPaymentIdAuthorizationsPostRequestBodyContentApplicationJsonSchemaAuthorization
                  description: Details about the authorization to create.
              required:
                - idempotency_key
                - authorization
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
    PaymentsPaymentIdAuthorizationsPostRequestBodyContentApplicationJsonSchemaAuthorization:
      type: object
      properties:
        amount:
          type: integer
          description: >-
            The updated total amount of money to collect from the customer, in
            the lowest denomination of currency for the payment.

            This value must be greater than or equal to the current authorized
            amount
        currency:
          $ref: '#/components/schemas/Currency'
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this authorization, typically used to
            associate the authorization with a record in an external system.


            Min length: `1`

            Max length: `1024`
        metadata:
          $ref: '#/components/schemas/Metadata'
      required:
        - amount
        - currency
      description: Details about the authorization to create.
      title: >-
        PaymentsPaymentIdAuthorizationsPostRequestBodyContentApplicationJsonSchemaAuthorization
    AuthorizationStatus:
      type: string
      enum:
        - AUTHORIZED
        - DECLINED
      description: >-
        The step of the authorization processing lifecycle that this
        authorization is currently at.


        Allowed values:

        - AUTHORIZED

        - DECLINED
      title: AuthorizationStatus
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
    Authorization:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this authorization issued by Cash App.

            Min length: 1 character
            Max length: 128 characters
        amount:
          type: integer
          description: >-
            Total authorized amount after this authorization was processed, in
            the lowest denomination of currency on the payment.
        currency:
          $ref: '#/components/schemas/Currency'
        status:
          $ref: '#/components/schemas/AuthorizationStatus'
          description: >-
            The step of the authorization processing lifecycle that this
            authorization is currently at.


            Allowed values:

            - AUTHORIZED

            - DECLINED
        created_at:
          type: string
          format: date-time
          description: When this authorization was created, in RFC 3339 format (UTC).
        payment_id:
          type: string
          description: ID of the payment associated with this authorization
        previous_amount:
          type: integer
          description: Total authorized amount before this authorization was requested
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this authorization, typically used to
            associate the authorization with a record in an external system.


            Min length: 1

            Max length: 1024
        metadata:
          $ref: '#/components/schemas/Metadata'
        decline_errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: >-
            If the authorization was declined, it contains a list of the reasons
            why it was declined.


            Min number of items: 1
      required:
        - id
        - amount
        - currency
        - status
        - created_at
        - payment_id
        - previous_amount
      description: Represents an authorization update for a payment
      title: Authorization
    Payments_create-payment-authorization_Response_201:
      type: object
      properties:
        authorization:
          $ref: '#/components/schemas/Authorization'
      required:
        - authorization
      title: Payments_create-payment-authorization_Response_201
    Create-payment-authorizationRequestBadRequestError:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: |-
            A list of errors indicating why the request failed.
             
            Min number of items: `1`
        authorization:
          $ref: '#/components/schemas/Authorization'
      required:
        - errors
      title: Create-payment-authorizationRequestBadRequestError
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

url = "https://api.cash.app/network/v1/payments/payment_id/authorizations"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "authorization": {
        "amount": 100,
        "currency": "USD"
    }
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
const url = 'https://api.cash.app/network/v1/payments/payment_id/authorizations';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","authorization":{"amount":100,"currency":"USD"}}'
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

	url := "https://api.cash.app/network/v1/payments/payment_id/authorizations"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"authorization\": {\n    \"amount\": 100,\n    \"currency\": \"USD\"\n  }\n}")

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

url = URI("https://api.cash.app/network/v1/payments/payment_id/authorizations")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"authorization\": {\n    \"amount\": 100,\n    \"currency\": \"USD\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/payments/payment_id/authorizations")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"authorization\": {\n    \"amount\": 100,\n    \"currency\": \"USD\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/payments/payment_id/authorizations', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "authorization": {
    "amount": 100,
    "currency": "USD"
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

var client = new RestClient("https://api.cash.app/network/v1/payments/payment_id/authorizations");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"authorization\": {\n    \"amount\": 100,\n    \"currency\": \"USD\"\n  }\n}", ParameterType.RequestBody);
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
  "authorization": [
    "amount": 100,
    "currency": "USD"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/payments/payment_id/authorizations")! as URL,
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