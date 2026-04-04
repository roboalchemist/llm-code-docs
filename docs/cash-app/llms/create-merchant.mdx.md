# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-merchant.mdx

# Create merchant

POST https://api.cash.app/network/v1/merchants
Content-Type: application/json

Creates a new merchant. Merchants must have an `address` or `site_url` set.

**This endpoint is not rate limited.**

Scopes: `MERCHANTS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-merchant

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /merchants:
    post:
      operationId: create-merchant
      summary: Create merchant
      description: >-
        Creates a new merchant. Merchants must have an `address` or `site_url`
        set.


        **This endpoint is not rate limited.**


        Scopes: `MERCHANTS_WRITE`
      tags:
        - subpackage_merchants
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
                $ref: '#/components/schemas/Merchants_create-merchant_Response_201'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '409':
          description: Conflict
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
                merchant:
                  $ref: >-
                    #/components/schemas/MerchantsPostRequestBodyContentApplicationJsonSchemaMerchant
                  description: Details about the merchant to create.
              required:
                - idempotency_key
                - merchant
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
    Country:
      type: string
      enum:
        - US
      description: >-
        Indicates the country associated with an entity. Values are from the
        [ISO-3166 Alpha-2](https://www.iso.org/iso-3166-country-codes.html)
        specification.


        Current values:


        - `US`: United States of America
      title: Country
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
    Category:
      type: string
      description: >-
        The merchant category code associated with the entity. Values are from
        the [ISO-18245 specification](https://www.iso.org/standard/33365.html).
      title: Category
    Address:
      type: object
      properties:
        address_line_1:
          type: string
          description: >-
            First line of the street address, typically including street number,
            street name, and / or building name.


            Min length: `1`

            Max length: `1024`
        address_line_2:
          type: string
          description: |-
            Second line of the address, if any.

            Min length: `1`
            Max length: `1024`
        locality:
          type: string
          description: |-
            City or township where the entity is located.

            Min length: `1`
            Max length: `1024`
        country:
          $ref: '#/components/schemas/Country'
        postal_code:
          type: string
          description: |-
            ZIP or postal code.

            Min length: `1`
            Max length: `128`
        administrative_district_level_1:
          type: string
          description: |-
            State or province.

            Min length: `1`
            Max length: `1024`
      required:
        - country
      description: Where this entity is located
      title: Address
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
    MerchantFeePlans:
      type: object
      properties:
        in_app_fee_plan_id:
          type: string
          description: >-
            The fee plan ID identifying the fee plan that will be used for all
            in-app payments.
        in_person_fee_plan_id:
          type: string
          description: >-
            The fee plan ID identifying the fee plan that will be used for all
            in-person payments.
        online_fee_plan_id:
          type: string
          description: >-
            The fee plan ID identifying the fee plan that will be used for all
            online payments.
      description: >-
        Merchant fee plans contains the IDs of the different fee plans for a
        merchant. These IDs represent the processing fees that merchants will be
        charged for processing payments for each channel. You can use the Fee
        Plans API to get all the fee information for each fee plan.
      title: MerchantFeePlans
    MerchantsPostRequestBodyContentApplicationJsonSchemaMerchant:
      type: object
      properties:
        name:
          type: string
          description: >-
            The name of the individual or business entity associated with the
            merchant.


            Min length: `1`

            Max length: `1024`
        brand_id:
          type: string
          description: |
            ID of the brand associated with this merchant.

            Min length: `1`
            Max length: `128`
        country:
          $ref: '#/components/schemas/Country'
        currency:
          $ref: '#/components/schemas/Currency'
        category:
          $ref: '#/components/schemas/Category'
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this merchant, typically used to
            associate the merchant with a record in an external system.


            **Must be unique across all merchants. Independent from the [brand
            reference_id](https://developers.cash.app/docs/api/network-api/operations/create-a-brand#request-body)**


            Min length: `1`

            Max length: `1024`
        address:
          $ref: '#/components/schemas/Address'
        site_url:
          type: string
          format: uri
          description: |-
            The URL of the website, if this merchant is for an eCommerce site.

            Min length: `8`
            Max length: `8000`
        metadata:
          $ref: '#/components/schemas/Metadata'
        default_fee_plans:
          $ref: '#/components/schemas/MerchantFeePlans'
      required:
        - name
        - brand_id
        - country
        - currency
        - category
        - reference_id
        - address
      description: Details about the merchant to create.
      title: MerchantsPostRequestBodyContentApplicationJsonSchemaMerchant
    MerchantStatus:
      type: string
      enum:
        - ACTIVE
        - RISK_DISABLED
        - COMPLIANCE_DISABLED
        - CLIENT_DISABLED
        - PENDING
      description: >-
        Whether or not this merchant can be used to accept payments or issue
        refunds.


        - `ACTIVE`: The merchant can accept payments or issue refunds.

        - `RISK_DISABLED`: Cash App Pay blocked this merchant due to them being
        high risk. There is no way to re-enable them programmaticaly.

        - `COMPLIANCE_DISABLED`: Cash App Pay blocked this merchant due to them
        not following the terms of service, Program Rules, or local laws. There
        is no way to re-enable them programmaticaly.

        - `CLIENT_DISABLED`: The client called the
        [UpdateMerchant](Network-API.v1.yaml/paths/~1merchants~1{merchant_id}/patch)
        endpoint and disabled this merchant, preventing it from being able to
        handle payments or refunds. To reverse this, call the endpoint again
        with the status field set to `ACTIVE`.

        - `PENDING`: The merchant is not ready to accept payments or refunds
        yet; the registration process is still running.
      title: MerchantStatus
    Merchant:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the merchant issued by Cash App.

            Min length: `1`
            Max length: `128`
        brand_id:
          type: string
          description: |-
            ID of the brand associated with this merchant.

            Min length: `1`
            Max length: `128`
        name:
          type: string
          description: >-
            The name of the individual or business entity associated with the
            merchant.


            Min length: `1`

            Max length: `1024`
        country:
          $ref: '#/components/schemas/Country'
        currency:
          $ref: '#/components/schemas/Currency'
        category:
          $ref: '#/components/schemas/Category'
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this merchant, typically used to
            associate the merchant with a record in an external system.
            Independent from the [brand
            reference_id](https://developers.cash.app/docs/api/network-api/operations/create-a-brand#request-body).


            Min length: `1`

            Max length: `1024`
        status:
          $ref: '#/components/schemas/MerchantStatus'
          description: >-
            Whether or not this merchant can be used to accept payments or issue
            refunds.


            - `ACTIVE`: The merchant can accept payments or issue refunds.

            - `RISK_DISABLED`: Cash App Pay blocked this merchant due to them
            being high risk. There is no way to re-enable them programmaticaly.

            - `COMPLIANCE_DISABLED`: Cash App Pay blocked this merchant due to
            them not following the terms of service, Program Rules, or local
            laws. There is no way to re-enable them programmaticaly.

            - `CLIENT_DISABLED`: The client called the
            [UpdateMerchant](Network-API.v1.yaml/paths/~1merchants~1{merchant_id}/patch)
            endpoint and disabled this merchant, preventing it from being able
            to handle payments or refunds. To reverse this, call the endpoint
            again with the status field set to `ACTIVE`.

            - `PENDING`: The merchant is not ready to accept payments or refunds
            yet; the registration process is still running.
        created_at:
          type: string
          format: date-time
          description: >-
            When this merchant was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this merchant was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        address:
          $ref: '#/components/schemas/Address'
        site_url:
          type: string
          format: uri
          description: |-
            The URL of the website, if this merchant is for an eCommerce site.

            Min length: `8`
            Max length: `8000`
        metadata:
          $ref: '#/components/schemas/Metadata'
        default_fee_plans:
          $ref: '#/components/schemas/MerchantFeePlans'
      required:
        - id
        - brand_id
        - name
        - country
        - currency
        - category
        - reference_id
        - status
        - created_at
        - updated_at
        - address
      description: >-
        A merchant represents a depository account when processing payments from
        Cash App customers. Merchants do not have direct access to Cash App, so
        processed payments are stored in this account until they are ready for
        settlement.
      title: Merchant
    Merchants_create-merchant_Response_201:
      type: object
      properties:
        merchant:
          $ref: '#/components/schemas/Merchant'
      required:
        - merchant
      title: Merchants_create-merchant_Response_201
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

url = "https://api.cash.app/network/v1/merchants"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "merchant": {
        "name": "merchant name",
        "brand_id": "brand ID",
        "country": "US",
        "currency": "USD",
        "category": "5432",
        "reference_id": "reference ID",
        "address": {
            "country": "US",
            "address_line_1": "1215 4th Ave",
            "address_line_2": "Suite 2300",
            "locality": "Seattle",
            "postal_code": "98161-1001",
            "administrative_district_level_1": "Washington"
        },
        "site_url": "https://example.com",
        "default_fee_plans": {
            "in_app_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
            "in_person_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
            "online_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me"
        }
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
const url = 'https://api.cash.app/network/v1/merchants';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","merchant":{"name":"merchant name","brand_id":"brand ID","country":"US","currency":"USD","category":"5432","reference_id":"reference ID","address":{"country":"US","address_line_1":"1215 4th Ave","address_line_2":"Suite 2300","locality":"Seattle","postal_code":"98161-1001","administrative_district_level_1":"Washington"},"site_url":"https://example.com","default_fee_plans":{"in_app_fee_plan_id":"FEE_kewjsmjt35t8qhzyjeqcst5me","in_person_fee_plan_id":"FEE_kewjsmjt35t8qhzyjeqcst5me","online_fee_plan_id":"FEE_kewjsmjt35t8qhzyjeqcst5me"}}}'
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

	url := "https://api.cash.app/network/v1/merchants"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}")

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

url = URI("https://api.cash.app/network/v1/merchants")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/merchants")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/merchants', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "merchant": {
    "name": "merchant name",
    "brand_id": "brand ID",
    "country": "US",
    "currency": "USD",
    "category": "5432",
    "reference_id": "reference ID",
    "address": {
      "country": "US",
      "address_line_1": "1215 4th Ave",
      "address_line_2": "Suite 2300",
      "locality": "Seattle",
      "postal_code": "98161-1001",
      "administrative_district_level_1": "Washington"
    },
    "site_url": "https://example.com",
    "default_fee_plans": {
      "in_app_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "in_person_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "online_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me"
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

var client = new RestClient("https://api.cash.app/network/v1/merchants");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}", ParameterType.RequestBody);
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
  "merchant": [
    "name": "merchant name",
    "brand_id": "brand ID",
    "country": "US",
    "currency": "USD",
    "category": "5432",
    "reference_id": "reference ID",
    "address": [
      "country": "US",
      "address_line_1": "1215 4th Ave",
      "address_line_2": "Suite 2300",
      "locality": "Seattle",
      "postal_code": "98161-1001",
      "administrative_district_level_1": "Washington"
    ],
    "site_url": "https://example.com",
    "default_fee_plans": [
      "in_app_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "in_person_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "online_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/merchants")! as URL,
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

url = "https://api.cash.app/network/v1/merchants"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "merchant": {
        "name": "merchant name",
        "brand_id": "brand ID",
        "country": "US",
        "currency": "USD",
        "category": "5432",
        "reference_id": "reference ID",
        "address": {
            "country": "US",
            "address_line_1": "1215 4th Ave",
            "address_line_2": "Suite 2300",
            "locality": "Seattle",
            "postal_code": "98161-1001",
            "administrative_district_level_1": "Washington"
        },
        "site_url": "https://example.com",
        "metadata": { "key": "value" },
        "default_fee_plans": {
            "in_app_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
            "in_person_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
            "online_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me"
        }
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
const url = 'https://api.cash.app/network/v1/merchants';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","merchant":{"name":"merchant name","brand_id":"brand ID","country":"US","currency":"USD","category":"5432","reference_id":"reference ID","address":{"country":"US","address_line_1":"1215 4th Ave","address_line_2":"Suite 2300","locality":"Seattle","postal_code":"98161-1001","administrative_district_level_1":"Washington"},"site_url":"https://example.com","metadata":{"key":"value"},"default_fee_plans":{"in_app_fee_plan_id":"FEE_kewjsmjt35t8qhzyjeqcst5me","in_person_fee_plan_id":"FEE_kewjsmjt35t8qhzyjeqcst5me","online_fee_plan_id":"FEE_kewjsmjt35t8qhzyjeqcst5me"}}}'
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

	url := "https://api.cash.app/network/v1/merchants"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}")

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

url = URI("https://api.cash.app/network/v1/merchants")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/merchants")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/merchants', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "merchant": {
    "name": "merchant name",
    "brand_id": "brand ID",
    "country": "US",
    "currency": "USD",
    "category": "5432",
    "reference_id": "reference ID",
    "address": {
      "country": "US",
      "address_line_1": "1215 4th Ave",
      "address_line_2": "Suite 2300",
      "locality": "Seattle",
      "postal_code": "98161-1001",
      "administrative_district_level_1": "Washington"
    },
    "site_url": "https://example.com",
    "metadata": {
      "key": "value"
    },
    "default_fee_plans": {
      "in_app_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "in_person_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "online_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me"
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

var client = new RestClient("https://api.cash.app/network/v1/merchants");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"merchant\": {\n    \"name\": \"merchant name\",\n    \"brand_id\": \"brand ID\",\n    \"country\": \"US\",\n    \"currency\": \"USD\",\n    \"category\": \"5432\",\n    \"reference_id\": \"reference ID\",\n    \"address\": {\n      \"country\": \"US\",\n      \"address_line_1\": \"1215 4th Ave\",\n      \"address_line_2\": \"Suite 2300\",\n      \"locality\": \"Seattle\",\n      \"postal_code\": \"98161-1001\",\n      \"administrative_district_level_1\": \"Washington\"\n    },\n    \"site_url\": \"https://example.com\",\n    \"metadata\": {\n      \"key\": \"value\"\n    },\n    \"default_fee_plans\": {\n      \"in_app_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"in_person_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\",\n      \"online_fee_plan_id\": \"FEE_kewjsmjt35t8qhzyjeqcst5me\"\n    }\n  }\n}", ParameterType.RequestBody);
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
  "merchant": [
    "name": "merchant name",
    "brand_id": "brand ID",
    "country": "US",
    "currency": "USD",
    "category": "5432",
    "reference_id": "reference ID",
    "address": [
      "country": "US",
      "address_line_1": "1215 4th Ave",
      "address_line_2": "Suite 2300",
      "locality": "Seattle",
      "postal_code": "98161-1001",
      "administrative_district_level_1": "Washington"
    ],
    "site_url": "https://example.com",
    "metadata": ["key": "value"],
    "default_fee_plans": [
      "in_app_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "in_person_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me",
      "online_fee_plan_id": "FEE_kewjsmjt35t8qhzyjeqcst5me"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/merchants")! as URL,
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