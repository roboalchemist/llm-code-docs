# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/retrieve-brand.mdx

# Retrieve brand

GET https://api.cash.app/network/v1/brands/{brand_id}

Returns a brand matching the given `brand_id`.

**This endpoint is not rate limited.**

Scopes: `BRANDS_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/retrieve-brand

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /brands/{brand_id}:
    get:
      operationId: retrieve-brand
      summary: Retrieve brand
      description: |-
        Returns a brand matching the given `brand_id`.

        **This endpoint is not rate limited.**

        Scopes: `BRANDS_READ`
      tags:
        - subpackage_brands
      parameters:
        - name: brand_id
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
                $ref: '#/components/schemas/Brands_retrieve-brand_Response_200'
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
    Brand:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the brand issued by Cash App.

            Min length: `1`
            Max length: `128`
        name:
          type: string
          description: |-
            Name of the brand to be shown in Cash App next to payments.

            Min length: `1`
            Max length: `1024`
        created_at:
          type: string
          format: date-time
          description: >-
            When this brand was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this brand was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this brand, typically used to
            associate the brand with a record in an external system. 
            Independent from the [merchant
            reference_id](https://developers.cash.app/docs/api/network-api/operations/create-a-merchant#request-body).


            Min length: `1`

            Max length: `1024`
        color:
          type: string
          description: >-
            Primary color associated with this brand and its logo, in 6-digit
            hex code format (`#f0f0f0`).


            Min length: `7`

            Max length: `7`
        profile_image_url:
          type: string
          format: uri
          default: >-
            https://franklin-assets.s3.amazonaws.com/merchants/assets/v3/generic/m_category_business.png
          description: >-
            URL to the image that should be shown in Cash App next to payments
            made to this brand, typically the brand's logo.


            The image should be square and be at least 256x256. It must be less
            than 2MB in filesize.


            Acceptable file formats:

            - `.png`

            - `.jpg`

            - `.jpeg`


            Min length: `8`

            Max length: `8000`
        metadata:
          $ref: '#/components/schemas/Metadata'
      required:
        - id
        - name
        - created_at
        - updated_at
        - reference_id
      description: >-
        A brand is the entity a customer perceives that they are transacting
        with.
      title: Brand
    Brands_retrieve-brand_Response_200:
      type: object
      properties:
        brand:
          $ref: '#/components/schemas/Brand'
      required:
        - brand
      title: Brands_retrieve-brand_Response_200
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

url = "https://api.cash.app/network/v1/brands/brand_id"

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
const url = 'https://api.cash.app/network/v1/brands/brand_id';
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

	url := "https://api.cash.app/network/v1/brands/brand_id"

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

url = URI("https://api.cash.app/network/v1/brands/brand_id")

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

HttpResponse<String> response = Unirest.get("https://api.cash.app/network/v1/brands/brand_id")
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

$response = $client->request('GET', 'https://api.cash.app/network/v1/brands/brand_id', [
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

var client = new RestClient("https://api.cash.app/network/v1/brands/brand_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/brands/brand_id")! as URL,
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