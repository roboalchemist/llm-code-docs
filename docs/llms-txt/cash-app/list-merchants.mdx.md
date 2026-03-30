# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/list-merchants.mdx

# List merchants

GET https://api.cash.app/network/v1/merchants

Returns a list of merchants matching the given query parameters.

**This endpoint is rate limited to 50 QPS.**

Scopes: `MERCHANTS_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/list-merchants

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /merchants:
    get:
      operationId: list-merchants
      summary: List merchants
      description: |-
        Returns a list of merchants matching the given query parameters.

        **This endpoint is rate limited to 50 QPS.**

        Scopes: `MERCHANTS_READ`
      tags:
        - subpackage_merchants
      parameters:
        - name: reference_id
          in: query
          description: >-
            Filters results to only include merchants with a `reference_id`
            matching the given value.
          required: false
          schema:
            type: string
        - name: cursor
          in: query
          description: >-
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the
            original query.
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: Maximum number of merchants to return.
          required: false
          schema:
            type: integer
            default: 50
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
                $ref: '#/components/schemas/Merchants_list-merchants_Response_200'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-merchantsRequestBadRequestError'
servers:
  - url: https://api.cash.app/network/v1
  - url: https://sandbox.api.cash.app/network/v1
components:
  schemas:
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
    Merchants_list-merchants_Response_200:
      type: object
      properties:
        merchants:
          type: array
          items:
            $ref: '#/components/schemas/Merchant'
          description: List of merchants matching the given query parameters.
        cursor:
          type: string
          description: >-
            The pagination cursor to be used in a subsequent request. If empty,
            this is the final response.
      required:
        - merchants
      title: Merchants_list-merchants_Response_200
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
    List-merchantsRequestBadRequestError:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
      required:
        - errors
      title: List-merchantsRequestBadRequestError

```

## SDK Code Examples

```python
import requests

url = "https://api.cash.app/network/v1/merchants"

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
const url = 'https://api.cash.app/network/v1/merchants';
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

	url := "https://api.cash.app/network/v1/merchants"

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

url = URI("https://api.cash.app/network/v1/merchants")

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

HttpResponse<String> response = Unirest.get("https://api.cash.app/network/v1/merchants")
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

$response = $client->request('GET', 'https://api.cash.app/network/v1/merchants', [
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

var client = new RestClient("https://api.cash.app/network/v1/merchants");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/merchants")! as URL,
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