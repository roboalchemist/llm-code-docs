# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-payment.mdx

# Create payment

POST https://api.cash.app/network/v1/payments
Content-Type: application/json

Creates a payment from a customer to a merchant.


<Note>
  Creating a payment requires a grant that is associated with the `ON_FILE_PAYMENT` or `ONE_TIME_PAYMENT` actions. To generate a grant, use the Customer Request API.
</Note>

**This endpoint is not rate limited.**

Scopes: `PAYMENTS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-payment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /payments:
    post:
      operationId: create-payment
      summary: Create payment
      description: |-
        Creates a payment from a customer to a merchant.


        <Note>
          Creating a payment requires a grant that is associated with the `ON_FILE_PAYMENT` or `ONE_TIME_PAYMENT` actions. To generate a grant, use the Customer Request API.
        </Note>

        **This endpoint is not rate limited.**

        Scopes: `PAYMENTS_WRITE`
      tags:
        - subpackage_payments
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
                $ref: '#/components/schemas/Payments_create-payment_Response_201'
        '400':
          description: >-
            Bad Request


            If a `PAYMENT_DECLINE_*` error is returned, the payment will still
            be created, but with a `DECLINED` status. This payment will then
            appear in the response payload.


            <Note> 

            **`PAYMENT_DECLINE_*` errors consume one-time use grants.**
             This means you must repeat the Customer Request flow to get a new grant if you want to try taking the payment again. All other errors will not consume grants.
            </Note>
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-paymentRequestBadRequestError'
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                idempotency_key:
                  $ref: '#/components/schemas/IdempotencyKey'
                payment:
                  $ref: >-
                    #/components/schemas/PaymentsPostRequestBodyContentApplicationJsonSchemaPayment
                  description: Data about the payment to create.
              required:
                - idempotency_key
                - payment
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
    PaymentEnrichmentsInitiationActor:
      type: string
      enum:
        - CUSTOMER
        - MERCHANT
      description: |-
        The party who initiated the payment.

        - `CUSTOMER`
        - `MERCHANT`
      title: PaymentEnrichmentsInitiationActor
    PaymentEnrichmentsInitiation:
      type: object
      properties:
        actor:
          $ref: '#/components/schemas/PaymentEnrichmentsInitiationActor'
          description: |-
            The party who initiated the payment.

            - `CUSTOMER`
            - `MERCHANT`
      required:
        - actor
      description: If present, provides information about transaction initiation.
      title: PaymentEnrichmentsInitiation
    PaymentEnrichmentsRestrictedCategoriesItems:
      type: string
      enum:
        - ALCOHOL
        - FINANCIAL_SERVICES
        - CANNABIS
      title: PaymentEnrichmentsRestrictedCategoriesItems
    PaymentEnrichments:
      type: object
      properties:
        initiation:
          $ref: '#/components/schemas/PaymentEnrichmentsInitiation'
          description: If present, provides information about transaction initiation.
        recurring_series_id:
          type: string
          description: >-
            If present, indicates that this payment is part of a recurring
            series of payments, such as a subscription.


            The value should contain a unique identifier for the recurring
            series that is constant across all of its payments, so it can be
            used to group them together.


            Min length: `1`

            Max length: `1024`
        statement_descriptor:
          type: string
          description: >-
            If present, adds the descriptor as line item on to a customer's
            payment receipt in their in-app Activity page.

            The descriptor will be present under the header "On statement as".


            Statement descriptor requirements vary by platform. If the input for
            this field exceeds the character limit, it will be truncated to the
            limit, then suffixed with an ellipsis (...).


            Min length: `1`

            Max length: `22`
        restricted_categories:
          type: array
          items:
            $ref: '#/components/schemas/PaymentEnrichmentsRestrictedCategoriesItems'
          description: >-
            If present, indicates that this payment is associated with one or
            more restricted categories. Contact the Cash App Pay support team to
            use this field.
      description: >-
        Describes optional fields beyond core payment information to supplement
        payment processing.


        Enrichments provide additional context about a payment, which can
        improve the overall payment experience including, but not limited to: 
          - Increased approval rates
          - Enhanced transaction insights
          - Better payment flows in Cash App
      title: PaymentEnrichments
    PaymentsPostRequestBodyContentApplicationJsonSchemaPayment:
      type: object
      properties:
        amount:
          type: integer
          description: >-
            The amount of money to charge the customer, in the lowest
            denomination of currency for the payment.


            Min value: `1`
        currency:
          $ref: '#/components/schemas/Currency'
        merchant_id:
          type: string
          description: |-
            ID of the merchant to make the payment to.

            Min length: `1`
            Max length: `128`
        grant_id:
          type: string
          description: >-
            A grant ID from the Customer Request API that indicates permission
            to take the payment.


            Min length: `1`

            Max length: `256`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this payment, typically used to
            associate the payment with a record in an external system.


            Min length: `1`

            Max length: `1024`
        capture:
          type: boolean
          default: true
          description: >-
            Whether or not to automatically capture the payment once it's
            created.


            Default: `true`
        metadata:
          $ref: '#/components/schemas/Metadata'
        enrichments:
          $ref: '#/components/schemas/PaymentEnrichments'
      required:
        - amount
        - currency
        - merchant_id
        - grant_id
      description: Data about the payment to create.
      title: PaymentsPostRequestBodyContentApplicationJsonSchemaPayment
    PaymentStatus:
      type: string
      enum:
        - AUTHORIZED
        - CAPTURED
        - VOIDED
        - DECLINED
      description: >-
        The step of the payment processing lifecycle that this payment is
        currently at.


        - `AUTHORIZED`

        - `CAPTURED`

        - `VOIDED`

        - `DECLINED`
      title: PaymentStatus
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
    FeeRate:
      type: object
      properties:
        basis_points:
          type: integer
          description: >-
            The variable fee charged for processing the payment expressed as
            1/100th of a percentage.
        fixed_amount:
          type: integer
          description: >-
            The amount charged for processing the payment, in the lowest
            denomination of currency on the payment.
             **Note: The currency for the fee is found on the fee plan.**
      description: >-
        A fee rate contains the components of a fee charged by Cash App to
        partners for a given payment.
      title: FeeRate
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
    Payment:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this payment issued by Cash App.

            Min length: `1`
            Max length: `128`
        amount:
          type: integer
          description: >-
            The amount of money to collect, in the lowest denomination of
            currency on the payment. This is the _original_ amount authorized
            when the payment was created.


            Min value: `1`
        net_amount:
          type: integer
          description: >-
            The amount remaining after refunds and voided payments are deducted
            from the amount field. The amount will be in the lowest denomination
            of the currency on the payment.

            This is the amount that will be shown to the customer in their Cash
            App account.



            Min value: `0`
        captured_amount:
          type: integer
          description: >-
            The amount of money on this payment that has been allocated for
            settlement. The amount will be in the lowest denomination of the
            currency on the payment.


            Min value: `0`
        voided_amount:
          type: integer
          description: >-
            The amount of money on this payment that is no longer authorized and
            has been released back to the customer. The amount will be in the
            lowest denomination of the currency on the payment.


            Min value: `0`
        refunded_amount:
          type: integer
          description: >-
            Sum of captured refunds in the lowest denomination of currency on
            the payment.


            Min value: `0`
        currency:
          $ref: '#/components/schemas/Currency'
        customer_id:
          type: string
          description: |-
            ID of the customer that sent this payment.

            Min length: `1`
            Max length: `128`
        merchant_id:
          type: string
          description: |-
            ID of the merchant that received this payment.

            Min length: `1`
            Max length: `128`
        grant_id:
          type: string
          description: |-
            ID of the grant to used to create this payment.

            Min length: `1`
            Max length: `256`
        status:
          $ref: '#/components/schemas/PaymentStatus'
          description: >-
            The step of the payment processing lifecycle that this payment is
            currently at.


            - `AUTHORIZED`

            - `CAPTURED`

            - `VOIDED`

            - `DECLINED`
        created_at:
          type: string
          format: date-time
          description: >-
            When this payment was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this payment was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        capture_before:
          type: string
          format: date-time
          description: >-
            When this payment should be captured by, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        refund_ids:
          type: array
          items:
            type: string
          description: >-
            A list of one or more IDs associated with refunds issued for this
            payment.


            Min array length: `1`

            Min length of IDs: `1`

            Max length of IDs: `128`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this payment, typically used to
            associate the payment with a record in an external system.


            Min length: `1`

            Max length: `1024`
        metadata:
          $ref: '#/components/schemas/Metadata'
        enrichments:
          $ref: '#/components/schemas/PaymentEnrichments'
        decline_errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: >-
            If the payment was declined, contains a list of the reasons why it
            was declined.


            Min number of items: `1`
        fee_amount:
          type: number
          format: double
          description: >-
            The total fee amount that was charged to the merchant for processing
            this payment.
        fee_rate:
          $ref: '#/components/schemas/FeeRate'
          description: >-
            The breakdown of the fee that was charged to the merchant for
            processing this payment.
        authorization_updates:
          type: array
          items:
            $ref: '#/components/schemas/Authorization'
          description: >-
            A list of authorization update attempts associated with this
            payment, sorted in chronological order.


            Note: This field contains only the authorization update attempts, so
            this field will be empty when 

            the payment is first created (even though the amount is authorized
            in this flow, it is not an update).
      required:
        - id
        - amount
        - net_amount
        - captured_amount
        - voided_amount
        - refunded_amount
        - currency
        - customer_id
        - merchant_id
        - grant_id
        - status
        - created_at
        - updated_at
      title: Payment
    Payments_create-payment_Response_201:
      type: object
      properties:
        payment:
          $ref: '#/components/schemas/Payment'
      title: Payments_create-payment_Response_201
    Create-paymentRequestBadRequestError:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: |-
            A list of errors indicating why the request failed.

            Min number of items: `1`
        payment:
          $ref: '#/components/schemas/Payment'
      required:
        - errors
      title: Create-paymentRequestBadRequestError

```

## SDK Code Examples

```python
import requests

url = "https://api.cash.app/network/v1/payments"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "payment": {
        "amount": 100,
        "currency": "USD",
        "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
        "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
        "reference_id": "external-id",
        "capture": True,
        "enrichments": { "recurring_series_id": "string" }
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
const url = 'https://api.cash.app/network/v1/payments';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","payment":{"amount":100,"currency":"USD","merchant_id":"MMI_4vxs5egfk7hmta3qx2h6rp91x","grant_id":"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50","reference_id":"external-id","capture":true,"enrichments":{"recurring_series_id":"string"}}}'
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

	url := "https://api.cash.app/network/v1/payments"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}")

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

url = URI("https://api.cash.app/network/v1/payments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/payments")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/payments', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "payment": {
    "amount": 100,
    "currency": "USD",
    "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
    "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
    "reference_id": "external-id",
    "capture": true,
    "enrichments": {
      "recurring_series_id": "string"
    }
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

var client = new RestClient("https://api.cash.app/network/v1/payments");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}", ParameterType.RequestBody);
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
  "payment": [
    "amount": 100,
    "currency": "USD",
    "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
    "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
    "reference_id": "external-id",
    "capture": true,
    "enrichments": ["recurring_series_id": "string"]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/payments")! as URL,
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

```python
import requests

url = "https://api.cash.app/network/v1/payments"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "payment": {
        "amount": 100,
        "currency": "USD",
        "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
        "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
        "reference_id": "external-id",
        "capture": True,
        "metadata": { "key": "value" },
        "enrichments": { "recurring_series_id": "string" }
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
const url = 'https://api.cash.app/network/v1/payments';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","payment":{"amount":100,"currency":"USD","merchant_id":"MMI_4vxs5egfk7hmta3qx2h6rp91x","grant_id":"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50","reference_id":"external-id","capture":true,"metadata":{"key":"value"},"enrichments":{"recurring_series_id":"string"}}}'
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

	url := "https://api.cash.app/network/v1/payments"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}")

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

url = URI("https://api.cash.app/network/v1/payments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/payments")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/payments', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "payment": {
    "amount": 100,
    "currency": "USD",
    "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
    "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
    "reference_id": "external-id",
    "capture": true,
    "metadata": {
      "key": "value"
    },
    "enrichments": {
      "recurring_series_id": "string"
    }
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

var client = new RestClient("https://api.cash.app/network/v1/payments");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"payment\": {\n    \"amount\": 100,\n    \"currency\": \"USD\",\n    \"merchant_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n    \"grant_id\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\",\n    \"reference_id\": \"external-id\",\n    \"capture\": true,\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"enrichments\": {\n      \"recurring_series_id\": \"string\"\n    }\n  }\n}", ParameterType.RequestBody);
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
  "payment": [
    "amount": 100,
    "currency": "USD",
    "merchant_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
    "grant_id": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50",
    "reference_id": "external-id",
    "capture": true,
    "metadata": ["key": "value"],
    "enrichments": ["recurring_series_id": "string"]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/payments")! as URL,
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