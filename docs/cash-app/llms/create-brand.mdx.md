# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-brand.mdx

# Create brand

POST https://api.cash.app/network/v1/brands
Content-Type: application/json

Creates a new brand with the given attributes.

**This endpoint is not rate limited.**

Scopes: `BRANDS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/create-brand

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /brands:
    post:
      operationId: create-brand
      summary: Create brand
      description: |-
        Creates a new brand with the given attributes.

        **This endpoint is not rate limited.**

        Scopes: `BRANDS_WRITE`
      tags:
        - subpackage_brands
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
                $ref: '#/components/schemas/Brands_create-brand_Response_201'
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
                brand:
                  $ref: >-
                    #/components/schemas/BrandsPostRequestBodyContentApplicationJsonSchemaBrand
                  description: Details about the brand to create.
              required:
                - idempotency_key
                - brand
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
    BrandsPostRequestBodyContentApplicationJsonSchemaBrand:
      type: object
      properties:
        name:
          type: string
          description: |-
            Name of the brand to be shown in Cash App next to payments.

            Min length: `1`
            Max length: `1024`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this brand, typically used to
            associate the brand with a record in an external system.


            **Must be unique across all brands. Independent from the [merchant
            reference_id](https://developers.cash.app/docs/api/network-api/operations/create-a-merchant#request-body)**


            Min length: `1`

            Max length: `1024`
        profile_image_url:
          type: string
          format: uri
          description: >-
            URL to the image that should be shown in Cash App next to payments
            made to this brand, typically the brand's logo.


            The image should be square and be at least 256x256. It must be less
            than 2MB in filesize.


            Acceptable image formats:

            - `png`

            - `jpg`

            - `jpeg`


            Min length: `8`

            Max length: `8000`
        color:
          type: string
          description: >-
            Primary color associated with this brand and its logo, in 6-digit
            hex code format.


            Pattern: `^#[a-fA-F0-9]{6}$`

            Min length: `7`

            Max length: `7`
        metadata:
          $ref: '#/components/schemas/Metadata'
      required:
        - name
        - reference_id
      description: Details about the brand to create.
      title: BrandsPostRequestBodyContentApplicationJsonSchemaBrand
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
    Brands_create-brand_Response_201:
      type: object
      properties:
        brand:
          $ref: '#/components/schemas/Brand'
      title: Brands_create-brand_Response_201
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

url = "https://api.cash.app/network/v1/brands"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "brand": {
        "name": "brand name",
        "reference_id": "reference ID",
        "profile_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg",
        "color": "#ffffff",
        "metadata": { "key": "value" }
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
const url = 'https://api.cash.app/network/v1/brands';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","brand":{"name":"brand name","reference_id":"reference ID","profile_image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg","color":"#ffffff","metadata":{"key":"value"}}}'
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

	url := "https://api.cash.app/network/v1/brands"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}")

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

url = URI("https://api.cash.app/network/v1/brands")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/brands")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/brands', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "brand": {
    "name": "brand name",
    "reference_id": "reference ID",
    "profile_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg",
    "color": "#ffffff",
    "metadata": {
      "key": "value"
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

var client = new RestClient("https://api.cash.app/network/v1/brands");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}", ParameterType.RequestBody);
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
  "brand": [
    "name": "brand name",
    "reference_id": "reference ID",
    "profile_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg",
    "color": "#ffffff",
    "metadata": ["key": "value"]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/brands")! as URL,
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

url = "https://api.cash.app/network/v1/brands"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "brand": {
        "name": "brand name",
        "reference_id": "reference ID",
        "profile_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg",
        "color": "#ffffff",
        "metadata": { "key": "value" }
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
const url = 'https://api.cash.app/network/v1/brands';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","brand":{"name":"brand name","reference_id":"reference ID","profile_image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg","color":"#ffffff","metadata":{"key":"value"}}}'
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

	url := "https://api.cash.app/network/v1/brands"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}")

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

url = URI("https://api.cash.app/network/v1/brands")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/brands")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/brands', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "brand": {
    "name": "brand name",
    "reference_id": "reference ID",
    "profile_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg",
    "color": "#ffffff",
    "metadata": {
      "key": "value"
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

var client = new RestClient("https://api.cash.app/network/v1/brands");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"brand\": {\n    \"name\": \"brand name\",\n    \"reference_id\": \"reference ID\",\n    \"profile_image_url\": \"https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg\",\n    \"color\": \"#ffffff\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}", ParameterType.RequestBody);
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
  "brand": [
    "name": "brand name",
    "reference_id": "reference ID",
    "profile_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Earth_from_Space.jpg/480px-Earth_from_Space.jpg",
    "color": "#ffffff",
    "metadata": ["key": "value"]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/brands")! as URL,
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