# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/retrieve-refund.mdx

# Retrieve refund

GET https://api.cash.app/network/v1/refunds/{refund_id}

Retrieves a refund by its ID.

**This endpoint is not rate limited.**

Scopes: `REFUNDS_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/retrieve-refund

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /refunds/{refund_id}:
    get:
      operationId: retrieve-refund
      summary: Retrieve refund
      description: |-
        Retrieves a refund by its ID.

        **This endpoint is not rate limited.**

        Scopes: `REFUNDS_READ`
      tags:
        - subpackage_refunds
      parameters:
        - name: refund_id
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
                $ref: '#/components/schemas/Refunds_retrieve-refund_Response_200'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.cash.app/network/v1
  - url: https://sandbox.api.cash.app/network/v1
components:
  schemas:
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
    Refunds_retrieve-refund_Response_200:
      type: object
      properties:
        refund:
          $ref: '#/components/schemas/Refund'
      required:
        - refund
      title: Refunds_retrieve-refund_Response_200
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

url = "https://api.cash.app/network/v1/refunds/refund_id"

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
const url = 'https://api.cash.app/network/v1/refunds/refund_id';
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

	url := "https://api.cash.app/network/v1/refunds/refund_id"

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

url = URI("https://api.cash.app/network/v1/refunds/refund_id")

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

HttpResponse<String> response = Unirest.get("https://api.cash.app/network/v1/refunds/refund_id")
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

$response = $client->request('GET', 'https://api.cash.app/network/v1/refunds/refund_id', [
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

var client = new RestClient("https://api.cash.app/network/v1/refunds/refund_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/refunds/refund_id")! as URL,
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