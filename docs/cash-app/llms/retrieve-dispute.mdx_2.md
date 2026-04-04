# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/retrieve-dispute.mdx

# Retrieve dispute

GET https://api.cash.app/network/v1/disputes/{dispute_id}

Retrieves a dispute by its ID.

**This endpoint is not rate limited.**

Scopes: `DISPUTES_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/retrieve-dispute

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /disputes/{dispute_id}:
    get:
      operationId: retrieve-dispute
      summary: Retrieve dispute
      description: |-
        Retrieves a dispute by its ID.

        **This endpoint is not rate limited.**

        Scopes: `DISPUTES_READ`
      tags:
        - subpackage_disputes
      parameters:
        - name: dispute_id
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
                $ref: '#/components/schemas/Disputes_retrieve-dispute_Response_200'
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
    DisputeReason:
      type: string
      enum:
        - FR10
        - FR11
        - PE10
        - PE11
        - PE12
        - CD10
        - CD11
        - CD13
      description: >-
        4-digit code consisting of 2 letters followed by 2 numbers that
        indicates why the dispute was created, at a high level.


        Current values:


        - `FR10`: Customer has no knowledge of the payment.

        - `FR11`: Customer has no knowledge of the payment and liability has
        shifted to the merchant due to collusion, fraud monitoring program
        thresholds, or any other reason.

        - `PE10`: Payment was processed twice.

        - `PE11`: Payment amount differs from agreed amount.

        - `PE12`: Payment was paid for by another means.

        - `CD10`: Cancelled services.

        - `CD11`: Goods or services differ from what was agreed upon for the
        payment.

        - `CD12`: The goods or services were not received.

        - `CD13`: The purchase was cancelled or returned, but the refund has not
        been processed.
      title: DisputeReason
    DisputeSettlementWithholding:
      type: string
      enum:
        - NOT_WITHHELD
        - WITHHELD_ALREADY
      description: >-
        Indicates if the disputed amount has already been withheld from a
        settlement or not.


        Current values:


        - `NOT_WITHHELD`: The disputed amount has not yet been withheld in a
        settlement. It may impact future settlements if the dispute is "lost" by
        the merchant.


        - `WITHHELD_ALREADY`: The disputed amount was withheld in a prior
        settlement. This dispute will not impact future settlements.
      title: DisputeSettlementWithholding
    DisputeState:
      type: string
      enum:
        - RESPONSE_REQUIRED
        - NO_RESPONSE_REQUIRED
        - PROCESSING
        - ACCEPTED
        - WON
        - PARTIALLY_WON
        - LOST
      description: |-
        The step in the dispute lifecycle that this dispute is currently at:

        - `RESPONSE_REQUIRED`
        - `NO_RESPONSE_REQUIRED`
        - `PROCESSING`
        - `ACCEPTED`
        - `WON`
        - `PARTIALLY_WON`
        - `LOST`
      title: DisputeState
    Dispute:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the dispute issued by Cash App.

            Min length: `1`
            Max length: `128`
        payment_id:
          type: string
          description: |-
            ID of the disputed payment.

            Min length: `1`
            Max length: `128`
        amount:
          type: integer
          description: >-
            Amount of disputed money, in the lowest denomination of currency on
            the associated payment.


            Min value: `1`
        customer_credited_amount:
          type:
            - integer
            - 'null'
          description: >-
            The amount credited to the Customer after resolving the dispute. 


            Note: The amount will be in the lowest denomination of the currency
            used on the associated payment.


            Min value: `0`
        reason:
          $ref: '#/components/schemas/DisputeReason'
          description: >-
            4-digit code consisting of 2 letters followed by 2 numbers that
            indicates why the dispute was created, at a high level.


            Current values:


            - `FR10`: Customer has no knowledge of the payment.

            - `FR11`: Customer has no knowledge of the payment and liability has
            shifted to the merchant due to collusion, fraud monitoring program
            thresholds, or any other reason.

            - `PE10`: Payment was processed twice.

            - `PE11`: Payment amount differs from agreed amount.

            - `PE12`: Payment was paid for by another means.

            - `CD10`: Cancelled services.

            - `CD11`: Goods or services differ from what was agreed upon for the
            payment.

            - `CD12`: The goods or services were not received.

            - `CD13`: The purchase was cancelled or returned, but the refund has
            not been processed.
        settlement_withholding:
          $ref: '#/components/schemas/DisputeSettlementWithholding'
          description: >-
            Indicates if the disputed amount has already been withheld from a
            settlement or not.


            Current values:


            - `NOT_WITHHELD`: The disputed amount has not yet been withheld in a
            settlement. It may impact future settlements if the dispute is
            "lost" by the merchant.


            - `WITHHELD_ALREADY`: The disputed amount was withheld in a prior
            settlement. This dispute will not impact future settlements.
        state:
          $ref: '#/components/schemas/DisputeState'
          description: |-
            The step in the dispute lifecycle that this dispute is currently at:

            - `RESPONSE_REQUIRED`
            - `NO_RESPONSE_REQUIRED`
            - `PROCESSING`
            - `ACCEPTED`
            - `WON`
            - `PARTIALLY_WON`
            - `LOST`
        created_at:
          type: string
          format: date-time
          description: >-
            When this dispute was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        response_due_at:
          type:
            - string
            - 'null'
          format: date-time
          description: >-
            When the dispute must be challenged by, after which it will be
            automatically accepted, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this dispute was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        merchant_id:
          type: string
          description: |-
            ID of the merchant that collected the disputed payment.

            Min length: `1`
            Max length: `128`
      required:
        - id
        - payment_id
        - amount
        - reason
        - settlement_withholding
        - state
        - created_at
        - updated_at
        - merchant_id
      description: >-
        Represents a dispute initiated by a customer within Cash App or the
        customer's linked bank
      title: Dispute
    Disputes_retrieve-dispute_Response_200:
      type: object
      properties:
        dispute:
          $ref: '#/components/schemas/Dispute'
      required:
        - dispute
      title: Disputes_retrieve-dispute_Response_200
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

url = "https://api.cash.app/network/v1/disputes/dispute_id"

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
const url = 'https://api.cash.app/network/v1/disputes/dispute_id';
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

	url := "https://api.cash.app/network/v1/disputes/dispute_id"

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

url = URI("https://api.cash.app/network/v1/disputes/dispute_id")

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

HttpResponse<String> response = Unirest.get("https://api.cash.app/network/v1/disputes/dispute_id")
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

$response = $client->request('GET', 'https://api.cash.app/network/v1/disputes/dispute_id', [
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

var client = new RestClient("https://api.cash.app/network/v1/disputes/dispute_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/disputes/dispute_id")! as URL,
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