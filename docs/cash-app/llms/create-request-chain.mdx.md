# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/create-request-chain.mdx

# Create request chain

POST https://api.cash.app/management/v1/request-chains
Content-Type: application/json

Executes multiple requests, grouped into "chains", in a single call. The API Client (Client) can use multiple chains and specify sub-requests within each chain to run sequentially or in parallel. However the chains, themselves, will only run sequentially.

### Accessing a previous response's value

Clients can access a previous response's value by using the format: `$[previous request's uid]:[key path]`. Clients can use this in the value fields of:
- `requests[].body`
- `requests[].path_params`
- `requests[].query_params`

The request's path `requests[].path` has an extra step to access a previous response's value. In the request's path, the Client will first refer to a key in the `requests[].path_params` field using the format: `{[path_params key name]}`. From there `requests[].path_params` can use the pattern described in **Accessing a previous response's value** to obtain a previous response's value.

<Warning>
The initial security headers will be passed to all requests.

Scopes are not required for this endpoint. However, the API key must contain the appropriate scopes required by the individual requests to execute.
</Warning>

For FAQs and performance improvement details, visit [Optimizing Performance with Request Chaining](../docs/partner-onboarding/optimizing-performance-with-request-chaining.md).


Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/create-request-chain

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /request-chains:
    post:
      operationId: create-request-chain
      summary: Create request chain
      description: >
        Executes multiple requests, grouped into "chains", in a single call. The
        API Client (Client) can use multiple chains and specify sub-requests
        within each chain to run sequentially or in parallel. However the
        chains, themselves, will only run sequentially.


        ### Accessing a previous response's value


        Clients can access a previous response's value by using the format:
        `$[previous request's uid]:[key path]`. Clients can use this in the
        value fields of:

        - `requests[].body`

        - `requests[].path_params`

        - `requests[].query_params`


        The request's path `requests[].path` has an extra step to access a
        previous response's value. In the request's path, the Client will first
        refer to a key in the `requests[].path_params` field using the format:
        `{[path_params key name]}`. From there `requests[].path_params` can use
        the pattern described in **Accessing a previous response's value** to
        obtain a previous response's value.


        <Warning>

        The initial security headers will be passed to all requests.


        Scopes are not required for this endpoint. However, the API key must
        contain the appropriate scopes required by the individual requests to
        execute.

        </Warning>


        For FAQs and performance improvement details, visit [Optimizing
        Performance with Request
        Chaining](../docs/partner-onboarding/optimizing-performance-with-request-chaining.md).
      tags:
        - subpackage_requestChains
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
                $ref: >-
                  #/components/schemas/requestChains_create-request-chain_Response_201
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
                requests:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItems
                  description: Requests to execute
                chains:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItems
                  description: Chains control the order and execution modes of requests
              required:
                - requests
                - chains
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
    RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsMethod:
      type: string
      enum:
        - GET
        - POST
        - PATCH
        - PUT
        - DELETE
      description: HTTP method of the request
      title: >-
        RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsMethod
    RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsPathParams:
      type: object
      properties: {}
      description: >-
        A map of path parameters. The keys represent variables from the `path`.
        The value fields allow for **Accessing a previous response's value**.
      title: >-
        RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsPathParams
    RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsQueryParams:
      type: object
      properties: {}
      description: >-
        A map of query parameters. The value fields allow for **Accessing a
        previous response's value**.
      title: >-
        RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsQueryParams
    RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsBody:
      type: object
      properties: {}
      description: >-
        The body that is required for the requested endpoint. The value fields
        allow for **Accessing a previous response's value**.
      title: >-
        RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsBody
    RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItems:
      type: object
      properties:
        uid:
          type: string
          description: Unique identifier for the request
        method:
          $ref: >-
            #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsMethod
          description: HTTP method of the request
        path:
          type: string
          description: >-
            URL path to call. Use format `{path_params key name}` to add
            variable path parameters.
        path_params:
          $ref: >-
            #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsPathParams
          description: >-
            A map of path parameters. The keys represent variables from the
            `path`. The value fields allow for **Accessing a previous response's
            value**.
        query_params:
          $ref: >-
            #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsQueryParams
          description: >-
            A map of query parameters. The value fields allow for **Accessing a
            previous response's value**.
        body:
          $ref: >-
            #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItemsBody
          description: >-
            The body that is required for the requested endpoint. The value
            fields allow for **Accessing a previous response's value**.
      required:
        - uid
        - method
        - path
      title: RequestChainsPostRequestBodyContentApplicationJsonSchemaRequestsItems
    RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItemsRequestsItems:
      type: object
      properties:
        uid:
          type: string
          description: Unique identifier for the request to execute
      required:
        - uid
      title: >-
        RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItemsRequestsItems
    RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItemsExecutionMode:
      type: string
      enum:
        - SEQUENTIAL
        - PARALLEL
      description: Execution mode of the requests in a chain
      title: >-
        RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItemsExecutionMode
    RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItems:
      type: object
      properties:
        requests:
          type: array
          items:
            $ref: >-
              #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItemsRequestsItems
        execution_mode:
          $ref: >-
            #/components/schemas/RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItemsExecutionMode
          description: Execution mode of the requests in a chain
      required:
        - requests
        - execution_mode
      title: RequestChainsPostRequestBodyContentApplicationJsonSchemaChainsItems
    ResponseExecutionStatus:
      type: string
      enum:
        - EXECUTED
        - NOT_STARTED
      description: Execution status of the request
      title: ResponseExecutionStatus
    ResponseMethod:
      type: string
      enum:
        - GET
        - POST
        - PATCH
        - PUT
        - DELETE
      description: HTTP method of the request
      title: ResponseMethod
    ResponseBody:
      type: object
      properties: {}
      description: Response body of the requested endpoint
      title: ResponseBody
    Response:
      type: object
      properties:
        request_uid:
          type: string
          description: Unique identifier for the request
        execution_status:
          $ref: '#/components/schemas/ResponseExecutionStatus'
          description: Execution status of the request
        path:
          type: string
          description: URL path that was called
        method:
          $ref: '#/components/schemas/ResponseMethod'
          description: HTTP method of the request
        status_code:
          type: integer
          description: Status code of the request
        body:
          $ref: '#/components/schemas/ResponseBody'
          description: Response body of the requested endpoint
        completed_at:
          type: string
          format: date-time
          description: >-
            When the request was completed, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
      required:
        - request_uid
        - execution_status
        - path
        - method
      title: Response
    requestChains_create-request-chain_Response_201:
      type: object
      properties:
        responses:
          type: array
          items:
            $ref: '#/components/schemas/Response'
      required:
        - responses
      title: requestChains_create-request-chain_Response_201
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

```python Create brand -> create merchant -> retrieve brand -> list brands
import requests

url = "https://api.cash.app/management/v1/request-chains"

payload = {
    "requests": [
        {
            "uid": "request_1",
            "method": "POST",
            "path": "/network/v1/brands",
            "body": {
                "idempotency_key": "idempotency_key",
                "brand": {
                    "name": "Brand Name",
                    "reference_id": "reference_id"
                }
            }
        },
        {
            "uid": "request_2",
            "method": "POST",
            "path": "/network/v1/merchants",
            "body": {
                "idempotency_key": "idempotency_key",
                "merchant": {
                    "name": "Merchant Name",
                    "brand_id": "$request_1:brand.id",
                    "country": "US",
                    "currency": "USD",
                    "category": "5432",
                    "reference_id": "reference_id",
                    "address": { "country": "US" }
                }
            }
        },
        {
            "uid": "request_3",
            "method": "GET",
            "path": "/network/v1/brands/{brandId}",
            "path_params": { "brandId": "$request_1:brand.id" }
        },
        {
            "uid": "request_4",
            "method": "GET",
            "path": "/network/v1/brands",
            "query_params": { "limit": "1" }
        }
    ],
    "chains": [
        {
            "requests": [{ "uid": "request_1" }, { "uid": "request_2" }, { "uid": "request_3" }, { "uid": "request_4" }],
            "execution_mode": "SEQUENTIAL"
        }
    ]
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

```javascript Create brand -> create merchant -> retrieve brand -> list brands
const url = 'https://api.cash.app/management/v1/request-chains';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"requests":[{"uid":"request_1","method":"POST","path":"/network/v1/brands","body":{"idempotency_key":"idempotency_key","brand":{"name":"Brand Name","reference_id":"reference_id"}}},{"uid":"request_2","method":"POST","path":"/network/v1/merchants","body":{"idempotency_key":"idempotency_key","merchant":{"name":"Merchant Name","brand_id":"$request_1:brand.id","country":"US","currency":"USD","category":"5432","reference_id":"reference_id","address":{"country":"US"}}}},{"uid":"request_3","method":"GET","path":"/network/v1/brands/{brandId}","path_params":{"brandId":"$request_1:brand.id"}},{"uid":"request_4","method":"GET","path":"/network/v1/brands","query_params":{"limit":"1"}}],"chains":[{"requests":[{"uid":"request_1"},{"uid":"request_2"},{"uid":"request_3"},{"uid":"request_4"}],"execution_mode":"SEQUENTIAL"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Create brand -> create merchant -> retrieve brand -> list brands
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/request-chains"

	payload := strings.NewReader("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands/{brandId}\",\n      \"path_params\": {\n        \"brandId\": \"$request_1:brand.id\"\n      }\n    },\n    {\n      \"uid\": \"request_4\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands\",\n      \"query_params\": {\n        \"limit\": \"1\"\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        },\n        {\n          \"uid\": \"request_4\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")

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

```ruby Create brand -> create merchant -> retrieve brand -> list brands
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/management/v1/request-chains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands/{brandId}\",\n      \"path_params\": {\n        \"brandId\": \"$request_1:brand.id\"\n      }\n    },\n    {\n      \"uid\": \"request_4\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands\",\n      \"query_params\": {\n        \"limit\": \"1\"\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        },\n        {\n          \"uid\": \"request_4\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java Create brand -> create merchant -> retrieve brand -> list brands
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/management/v1/request-chains")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands/{brandId}\",\n      \"path_params\": {\n        \"brandId\": \"$request_1:brand.id\"\n      }\n    },\n    {\n      \"uid\": \"request_4\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands\",\n      \"query_params\": {\n        \"limit\": \"1\"\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        },\n        {\n          \"uid\": \"request_4\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")
  .asString();
```

```php Create brand -> create merchant -> retrieve brand -> list brands
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/management/v1/request-chains', [
  'body' => '{
  "requests": [
    {
      "uid": "request_1",
      "method": "POST",
      "path": "/network/v1/brands",
      "body": {
        "idempotency_key": "idempotency_key",
        "brand": {
          "name": "Brand Name",
          "reference_id": "reference_id"
        }
      }
    },
    {
      "uid": "request_2",
      "method": "POST",
      "path": "/network/v1/merchants",
      "body": {
        "idempotency_key": "idempotency_key",
        "merchant": {
          "name": "Merchant Name",
          "brand_id": "$request_1:brand.id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference_id",
          "address": {
            "country": "US"
          }
        }
      }
    },
    {
      "uid": "request_3",
      "method": "GET",
      "path": "/network/v1/brands/{brandId}",
      "path_params": {
        "brandId": "$request_1:brand.id"
      }
    },
    {
      "uid": "request_4",
      "method": "GET",
      "path": "/network/v1/brands",
      "query_params": {
        "limit": "1"
      }
    }
  ],
  "chains": [
    {
      "requests": [
        {
          "uid": "request_1"
        },
        {
          "uid": "request_2"
        },
        {
          "uid": "request_3"
        },
        {
          "uid": "request_4"
        }
      ],
      "execution_mode": "SEQUENTIAL"
    }
  ]
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

```csharp Create brand -> create merchant -> retrieve brand -> list brands
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/request-chains");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands/{brandId}\",\n      \"path_params\": {\n        \"brandId\": \"$request_1:brand.id\"\n      }\n    },\n    {\n      \"uid\": \"request_4\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/brands\",\n      \"query_params\": {\n        \"limit\": \"1\"\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        },\n        {\n          \"uid\": \"request_4\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Create brand -> create merchant -> retrieve brand -> list brands
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = [
  "requests": [
    [
      "uid": "request_1",
      "method": "POST",
      "path": "/network/v1/brands",
      "body": [
        "idempotency_key": "idempotency_key",
        "brand": [
          "name": "Brand Name",
          "reference_id": "reference_id"
        ]
      ]
    ],
    [
      "uid": "request_2",
      "method": "POST",
      "path": "/network/v1/merchants",
      "body": [
        "idempotency_key": "idempotency_key",
        "merchant": [
          "name": "Merchant Name",
          "brand_id": "$request_1:brand.id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference_id",
          "address": ["country": "US"]
        ]
      ]
    ],
    [
      "uid": "request_3",
      "method": "GET",
      "path": "/network/v1/brands/{brandId}",
      "path_params": ["brandId": "$request_1:brand.id"]
    ],
    [
      "uid": "request_4",
      "method": "GET",
      "path": "/network/v1/brands",
      "query_params": ["limit": "1"]
    ]
  ],
  "chains": [
    [
      "requests": [["uid": "request_1"], ["uid": "request_2"], ["uid": "request_3"], ["uid": "request_4"]],
      "execution_mode": "SEQUENTIAL"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/request-chains")! as URL,
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

```python Create brand -> create merchant -> create customer request
import requests

url = "https://api.cash.app/management/v1/request-chains"

payload = {
    "requests": [
        {
            "uid": "request_1",
            "method": "POST",
            "path": "/network/v1/brands",
            "body": {
                "idempotency_key": "idempotency_key",
                "brand": {
                    "name": "Brand Name",
                    "reference_id": "reference_id"
                }
            }
        },
        {
            "uid": "request_2",
            "method": "POST",
            "path": "/network/v1/merchants",
            "body": {
                "idempotency_key": "idempotency_key",
                "merchant": {
                    "name": "Merchant Name",
                    "brand_id": "$request_1:brand.id",
                    "country": "US",
                    "currency": "USD",
                    "category": "5432",
                    "reference_id": "reference_id",
                    "address": { "country": "US" }
                }
            }
        },
        {
            "uid": "request_3",
            "method": "POST",
            "path": "/customer-request/v1/requests",
            "body": {
                "idempotency_key": "idempotency_key",
                "request": {
                    "actions": [
                        {
                            "amount": 2500,
                            "currency": "USD",
                            "scope_id": "$request_2:merchant.id",
                            "type": "ONE_TIME_PAYMENT"
                        }
                    ],
                    "channel": "IN_PERSON",
                    "redirect_url": "https://example.com",
                    "reference_id": "string",
                    "metadata": { "key": "value" },
                    "customer_metadata": { "reference_id": "string" }
                }
            }
        }
    ],
    "chains": [
        {
            "requests": [{ "uid": "request_1" }, { "uid": "request_2" }, { "uid": "request_3" }],
            "execution_mode": "SEQUENTIAL"
        }
    ]
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

```javascript Create brand -> create merchant -> create customer request
const url = 'https://api.cash.app/management/v1/request-chains';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"requests":[{"uid":"request_1","method":"POST","path":"/network/v1/brands","body":{"idempotency_key":"idempotency_key","brand":{"name":"Brand Name","reference_id":"reference_id"}}},{"uid":"request_2","method":"POST","path":"/network/v1/merchants","body":{"idempotency_key":"idempotency_key","merchant":{"name":"Merchant Name","brand_id":"$request_1:brand.id","country":"US","currency":"USD","category":"5432","reference_id":"reference_id","address":{"country":"US"}}}},{"uid":"request_3","method":"POST","path":"/customer-request/v1/requests","body":{"idempotency_key":"idempotency_key","request":{"actions":[{"amount":2500,"currency":"USD","scope_id":"$request_2:merchant.id","type":"ONE_TIME_PAYMENT"}],"channel":"IN_PERSON","redirect_url":"https://example.com","reference_id":"string","metadata":{"key":"value"},"customer_metadata":{"reference_id":"string"}}}}],"chains":[{"requests":[{"uid":"request_1"},{"uid":"request_2"},{"uid":"request_3"}],"execution_mode":"SEQUENTIAL"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Create brand -> create merchant -> create customer request
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/request-chains"

	payload := strings.NewReader("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/customer-request/v1/requests\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"request\": {\n          \"actions\": [\n            {\n              \"amount\": 2500,\n              \"currency\": \"USD\",\n              \"scope_id\": \"$request_2:merchant.id\",\n              \"type\": \"ONE_TIME_PAYMENT\"\n            }\n          ],\n          \"channel\": \"IN_PERSON\",\n          \"redirect_url\": \"https://example.com\",\n          \"reference_id\": \"string\",\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"customer_metadata\": {\n            \"reference_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")

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

```ruby Create brand -> create merchant -> create customer request
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/management/v1/request-chains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/customer-request/v1/requests\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"request\": {\n          \"actions\": [\n            {\n              \"amount\": 2500,\n              \"currency\": \"USD\",\n              \"scope_id\": \"$request_2:merchant.id\",\n              \"type\": \"ONE_TIME_PAYMENT\"\n            }\n          ],\n          \"channel\": \"IN_PERSON\",\n          \"redirect_url\": \"https://example.com\",\n          \"reference_id\": \"string\",\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"customer_metadata\": {\n            \"reference_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java Create brand -> create merchant -> create customer request
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/management/v1/request-chains")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/customer-request/v1/requests\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"request\": {\n          \"actions\": [\n            {\n              \"amount\": 2500,\n              \"currency\": \"USD\",\n              \"scope_id\": \"$request_2:merchant.id\",\n              \"type\": \"ONE_TIME_PAYMENT\"\n            }\n          ],\n          \"channel\": \"IN_PERSON\",\n          \"redirect_url\": \"https://example.com\",\n          \"reference_id\": \"string\",\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"customer_metadata\": {\n            \"reference_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")
  .asString();
```

```php Create brand -> create merchant -> create customer request
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/management/v1/request-chains', [
  'body' => '{
  "requests": [
    {
      "uid": "request_1",
      "method": "POST",
      "path": "/network/v1/brands",
      "body": {
        "idempotency_key": "idempotency_key",
        "brand": {
          "name": "Brand Name",
          "reference_id": "reference_id"
        }
      }
    },
    {
      "uid": "request_2",
      "method": "POST",
      "path": "/network/v1/merchants",
      "body": {
        "idempotency_key": "idempotency_key",
        "merchant": {
          "name": "Merchant Name",
          "brand_id": "$request_1:brand.id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference_id",
          "address": {
            "country": "US"
          }
        }
      }
    },
    {
      "uid": "request_3",
      "method": "POST",
      "path": "/customer-request/v1/requests",
      "body": {
        "idempotency_key": "idempotency_key",
        "request": {
          "actions": [
            {
              "amount": 2500,
              "currency": "USD",
              "scope_id": "$request_2:merchant.id",
              "type": "ONE_TIME_PAYMENT"
            }
          ],
          "channel": "IN_PERSON",
          "redirect_url": "https://example.com",
          "reference_id": "string",
          "metadata": {
            "key": "value"
          },
          "customer_metadata": {
            "reference_id": "string"
          }
        }
      }
    }
  ],
  "chains": [
    {
      "requests": [
        {
          "uid": "request_1"
        },
        {
          "uid": "request_2"
        },
        {
          "uid": "request_3"
        }
      ],
      "execution_mode": "SEQUENTIAL"
    }
  ]
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

```csharp Create brand -> create merchant -> create customer request
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/request-chains");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"brand\": {\n          \"name\": \"Brand Name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"merchant\": {\n          \"name\": \"Merchant Name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference_id\",\n          \"address\": {\n            \"country\": \"US\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/customer-request/v1/requests\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"request\": {\n          \"actions\": [\n            {\n              \"amount\": 2500,\n              \"currency\": \"USD\",\n              \"scope_id\": \"$request_2:merchant.id\",\n              \"type\": \"ONE_TIME_PAYMENT\"\n            }\n          ],\n          \"channel\": \"IN_PERSON\",\n          \"redirect_url\": \"https://example.com\",\n          \"reference_id\": \"string\",\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"customer_metadata\": {\n            \"reference_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Create brand -> create merchant -> create customer request
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = [
  "requests": [
    [
      "uid": "request_1",
      "method": "POST",
      "path": "/network/v1/brands",
      "body": [
        "idempotency_key": "idempotency_key",
        "brand": [
          "name": "Brand Name",
          "reference_id": "reference_id"
        ]
      ]
    ],
    [
      "uid": "request_2",
      "method": "POST",
      "path": "/network/v1/merchants",
      "body": [
        "idempotency_key": "idempotency_key",
        "merchant": [
          "name": "Merchant Name",
          "brand_id": "$request_1:brand.id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference_id",
          "address": ["country": "US"]
        ]
      ]
    ],
    [
      "uid": "request_3",
      "method": "POST",
      "path": "/customer-request/v1/requests",
      "body": [
        "idempotency_key": "idempotency_key",
        "request": [
          "actions": [
            [
              "amount": 2500,
              "currency": "USD",
              "scope_id": "$request_2:merchant.id",
              "type": "ONE_TIME_PAYMENT"
            ]
          ],
          "channel": "IN_PERSON",
          "redirect_url": "https://example.com",
          "reference_id": "string",
          "metadata": ["key": "value"],
          "customer_metadata": ["reference_id": "string"]
        ]
      ]
    ]
  ],
  "chains": [
    [
      "requests": [["uid": "request_1"], ["uid": "request_2"], ["uid": "request_3"]],
      "execution_mode": "SEQUENTIAL"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/request-chains")! as URL,
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

```python Upsert brand -> upsert merchant -> create payment
import requests

url = "https://api.cash.app/management/v1/request-chains"

payload = {
    "requests": [
        {
            "uid": "request_1",
            "method": "PUT",
            "path": "/network/v1/brands",
            "body": { "brand": {
                    "name": "brand name",
                    "reference_id": "reference_id"
                } }
        },
        {
            "uid": "request_2",
            "method": "PUT",
            "path": "/network/v1/merchants",
            "body": { "merchant": {
                    "name": "merchant name",
                    "brand_id": "$request_1:brand.id",
                    "country": "US",
                    "currency": "USD",
                    "category": "5432",
                    "reference_id": "reference ID",
                    "address": {
                        "address_line_1": "1215 4th Ave",
                        "address_line_2": "Suite 2300",
                        "locality": "Seattle",
                        "country": "US",
                        "postal_code": "98161-1001",
                        "administrative_district_level_1": "Washington"
                    }
                } }
        },
        {
            "uid": "request_3",
            "method": "POST",
            "path": "/network/v1/payments",
            "body": {
                "idempotency_key": "idempotency_key",
                "payment": {
                    "amount": 100,
                    "currency": "USD",
                    "merchant_id": "$request_2:merchant.id",
                    "grant_id": "GRG_grant-id",
                    "reference_id": "external-id",
                    "capture": True,
                    "metadata": { "key": "value" },
                    "enrichments": { "recurring_series_id": "string" }
                }
            }
        }
    ],
    "chains": [
        {
            "requests": [{ "uid": "request_1" }, { "uid": "request_2" }, { "uid": "request_3" }],
            "execution_mode": "SEQUENTIAL"
        }
    ]
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

```javascript Upsert brand -> upsert merchant -> create payment
const url = 'https://api.cash.app/management/v1/request-chains';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"requests":[{"uid":"request_1","method":"PUT","path":"/network/v1/brands","body":{"brand":{"name":"brand name","reference_id":"reference_id"}}},{"uid":"request_2","method":"PUT","path":"/network/v1/merchants","body":{"merchant":{"name":"merchant name","brand_id":"$request_1:brand.id","country":"US","currency":"USD","category":"5432","reference_id":"reference ID","address":{"address_line_1":"1215 4th Ave","address_line_2":"Suite 2300","locality":"Seattle","country":"US","postal_code":"98161-1001","administrative_district_level_1":"Washington"}}}},{"uid":"request_3","method":"POST","path":"/network/v1/payments","body":{"idempotency_key":"idempotency_key","payment":{"amount":100,"currency":"USD","merchant_id":"$request_2:merchant.id","grant_id":"GRG_grant-id","reference_id":"external-id","capture":true,"metadata":{"key":"value"},"enrichments":{"recurring_series_id":"string"}}}}],"chains":[{"requests":[{"uid":"request_1"},{"uid":"request_2"},{"uid":"request_3"}],"execution_mode":"SEQUENTIAL"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Upsert brand -> upsert merchant -> create payment
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/request-chains"

	payload := strings.NewReader("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"brand\": {\n          \"name\": \"brand name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/payments\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"payment\": {\n          \"amount\": 100,\n          \"currency\": \"USD\",\n          \"merchant_id\": \"$request_2:merchant.id\",\n          \"grant_id\": \"GRG_grant-id\",\n          \"reference_id\": \"external-id\",\n          \"capture\": true,\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"enrichments\": {\n            \"recurring_series_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")

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

```ruby Upsert brand -> upsert merchant -> create payment
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/management/v1/request-chains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"brand\": {\n          \"name\": \"brand name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/payments\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"payment\": {\n          \"amount\": 100,\n          \"currency\": \"USD\",\n          \"merchant_id\": \"$request_2:merchant.id\",\n          \"grant_id\": \"GRG_grant-id\",\n          \"reference_id\": \"external-id\",\n          \"capture\": true,\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"enrichments\": {\n            \"recurring_series_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java Upsert brand -> upsert merchant -> create payment
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/management/v1/request-chains")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"brand\": {\n          \"name\": \"brand name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/payments\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"payment\": {\n          \"amount\": 100,\n          \"currency\": \"USD\",\n          \"merchant_id\": \"$request_2:merchant.id\",\n          \"grant_id\": \"GRG_grant-id\",\n          \"reference_id\": \"external-id\",\n          \"capture\": true,\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"enrichments\": {\n            \"recurring_series_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")
  .asString();
```

```php Upsert brand -> upsert merchant -> create payment
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/management/v1/request-chains', [
  'body' => '{
  "requests": [
    {
      "uid": "request_1",
      "method": "PUT",
      "path": "/network/v1/brands",
      "body": {
        "brand": {
          "name": "brand name",
          "reference_id": "reference_id"
        }
      }
    },
    {
      "uid": "request_2",
      "method": "PUT",
      "path": "/network/v1/merchants",
      "body": {
        "merchant": {
          "name": "merchant name",
          "brand_id": "$request_1:brand.id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference ID",
          "address": {
            "address_line_1": "1215 4th Ave",
            "address_line_2": "Suite 2300",
            "locality": "Seattle",
            "country": "US",
            "postal_code": "98161-1001",
            "administrative_district_level_1": "Washington"
          }
        }
      }
    },
    {
      "uid": "request_3",
      "method": "POST",
      "path": "/network/v1/payments",
      "body": {
        "idempotency_key": "idempotency_key",
        "payment": {
          "amount": 100,
          "currency": "USD",
          "merchant_id": "$request_2:merchant.id",
          "grant_id": "GRG_grant-id",
          "reference_id": "external-id",
          "capture": true,
          "metadata": {
            "key": "value"
          },
          "enrichments": {
            "recurring_series_id": "string"
          }
        }
      }
    }
  ],
  "chains": [
    {
      "requests": [
        {
          "uid": "request_1"
        },
        {
          "uid": "request_2"
        },
        {
          "uid": "request_3"
        }
      ],
      "execution_mode": "SEQUENTIAL"
    }
  ]
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

```csharp Upsert brand -> upsert merchant -> create payment
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/request-chains");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/brands\",\n      \"body\": {\n        \"brand\": {\n          \"name\": \"brand name\",\n          \"reference_id\": \"reference_id\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"$request_1:brand.id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          }\n        }\n      }\n    },\n    {\n      \"uid\": \"request_3\",\n      \"method\": \"POST\",\n      \"path\": \"/network/v1/payments\",\n      \"body\": {\n        \"idempotency_key\": \"idempotency_key\",\n        \"payment\": {\n          \"amount\": 100,\n          \"currency\": \"USD\",\n          \"merchant_id\": \"$request_2:merchant.id\",\n          \"grant_id\": \"GRG_grant-id\",\n          \"reference_id\": \"external-id\",\n          \"capture\": true,\n          \"metadata\": {\n            \"key\": \"value\"\n          },\n          \"enrichments\": {\n            \"recurring_series_id\": \"string\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        },\n        {\n          \"uid\": \"request_3\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Upsert brand -> upsert merchant -> create payment
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = [
  "requests": [
    [
      "uid": "request_1",
      "method": "PUT",
      "path": "/network/v1/brands",
      "body": ["brand": [
          "name": "brand name",
          "reference_id": "reference_id"
        ]]
    ],
    [
      "uid": "request_2",
      "method": "PUT",
      "path": "/network/v1/merchants",
      "body": ["merchant": [
          "name": "merchant name",
          "brand_id": "$request_1:brand.id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference ID",
          "address": [
            "address_line_1": "1215 4th Ave",
            "address_line_2": "Suite 2300",
            "locality": "Seattle",
            "country": "US",
            "postal_code": "98161-1001",
            "administrative_district_level_1": "Washington"
          ]
        ]]
    ],
    [
      "uid": "request_3",
      "method": "POST",
      "path": "/network/v1/payments",
      "body": [
        "idempotency_key": "idempotency_key",
        "payment": [
          "amount": 100,
          "currency": "USD",
          "merchant_id": "$request_2:merchant.id",
          "grant_id": "GRG_grant-id",
          "reference_id": "external-id",
          "capture": true,
          "metadata": ["key": "value"],
          "enrichments": ["recurring_series_id": "string"]
        ]
      ]
    ]
  ],
  "chains": [
    [
      "requests": [["uid": "request_1"], ["uid": "request_2"], ["uid": "request_3"]],
      "execution_mode": "SEQUENTIAL"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/request-chains")! as URL,
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

```python Retrieve fee plan -> upsert merchant
import requests

url = "https://api.cash.app/management/v1/request-chains"

payload = {
    "requests": [
        {
            "uid": "request_1",
            "method": "GET",
            "path": "/network/v1/fee-plans/FEE_fee-plan-id"
        },
        {
            "uid": "request_2",
            "method": "PUT",
            "path": "/network/v1/merchants",
            "body": { "merchant": {
                    "name": "merchant name",
                    "brand_id": "BRAND_brand-id",
                    "country": "US",
                    "currency": "USD",
                    "category": "5432",
                    "reference_id": "reference ID",
                    "address": {
                        "address_line_1": "1215 4th Ave",
                        "address_line_2": "Suite 2300",
                        "locality": "Seattle",
                        "country": "US",
                        "postal_code": "98161-1001",
                        "administrative_district_level_1": "Washington"
                    },
                    "default_fee_plans": { "in_app_fee_plan_id": "$request_1:fee_plan.id" }
                } }
        }
    ],
    "chains": [
        {
            "requests": [{ "uid": "request_1" }, { "uid": "request_2" }],
            "execution_mode": "SEQUENTIAL"
        }
    ]
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

```javascript Retrieve fee plan -> upsert merchant
const url = 'https://api.cash.app/management/v1/request-chains';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"requests":[{"uid":"request_1","method":"GET","path":"/network/v1/fee-plans/FEE_fee-plan-id"},{"uid":"request_2","method":"PUT","path":"/network/v1/merchants","body":{"merchant":{"name":"merchant name","brand_id":"BRAND_brand-id","country":"US","currency":"USD","category":"5432","reference_id":"reference ID","address":{"address_line_1":"1215 4th Ave","address_line_2":"Suite 2300","locality":"Seattle","country":"US","postal_code":"98161-1001","administrative_district_level_1":"Washington"},"default_fee_plans":{"in_app_fee_plan_id":"$request_1:fee_plan.id"}}}}],"chains":[{"requests":[{"uid":"request_1"},{"uid":"request_2"}],"execution_mode":"SEQUENTIAL"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Retrieve fee plan -> upsert merchant
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/request-chains"

	payload := strings.NewReader("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/fee-plans/FEE_fee-plan-id\"\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"BRAND_brand-id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          },\n          \"default_fee_plans\": {\n            \"in_app_fee_plan_id\": \"$request_1:fee_plan.id\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")

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

```ruby Retrieve fee plan -> upsert merchant
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/management/v1/request-chains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/fee-plans/FEE_fee-plan-id\"\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"BRAND_brand-id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          },\n          \"default_fee_plans\": {\n            \"in_app_fee_plan_id\": \"$request_1:fee_plan.id\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java Retrieve fee plan -> upsert merchant
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/management/v1/request-chains")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/fee-plans/FEE_fee-plan-id\"\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"BRAND_brand-id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          },\n          \"default_fee_plans\": {\n            \"in_app_fee_plan_id\": \"$request_1:fee_plan.id\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")
  .asString();
```

```php Retrieve fee plan -> upsert merchant
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/management/v1/request-chains', [
  'body' => '{
  "requests": [
    {
      "uid": "request_1",
      "method": "GET",
      "path": "/network/v1/fee-plans/FEE_fee-plan-id"
    },
    {
      "uid": "request_2",
      "method": "PUT",
      "path": "/network/v1/merchants",
      "body": {
        "merchant": {
          "name": "merchant name",
          "brand_id": "BRAND_brand-id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference ID",
          "address": {
            "address_line_1": "1215 4th Ave",
            "address_line_2": "Suite 2300",
            "locality": "Seattle",
            "country": "US",
            "postal_code": "98161-1001",
            "administrative_district_level_1": "Washington"
          },
          "default_fee_plans": {
            "in_app_fee_plan_id": "$request_1:fee_plan.id"
          }
        }
      }
    }
  ],
  "chains": [
    {
      "requests": [
        {
          "uid": "request_1"
        },
        {
          "uid": "request_2"
        }
      ],
      "execution_mode": "SEQUENTIAL"
    }
  ]
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

```csharp Retrieve fee plan -> upsert merchant
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/request-chains");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"GET\",\n      \"path\": \"/network/v1/fee-plans/FEE_fee-plan-id\"\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PUT\",\n      \"path\": \"/network/v1/merchants\",\n      \"body\": {\n        \"merchant\": {\n          \"name\": \"merchant name\",\n          \"brand_id\": \"BRAND_brand-id\",\n          \"country\": \"US\",\n          \"currency\": \"USD\",\n          \"category\": \"5432\",\n          \"reference_id\": \"reference ID\",\n          \"address\": {\n            \"address_line_1\": \"1215 4th Ave\",\n            \"address_line_2\": \"Suite 2300\",\n            \"locality\": \"Seattle\",\n            \"country\": \"US\",\n            \"postal_code\": \"98161-1001\",\n            \"administrative_district_level_1\": \"Washington\"\n          },\n          \"default_fee_plans\": {\n            \"in_app_fee_plan_id\": \"$request_1:fee_plan.id\"\n          }\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Retrieve fee plan -> upsert merchant
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = [
  "requests": [
    [
      "uid": "request_1",
      "method": "GET",
      "path": "/network/v1/fee-plans/FEE_fee-plan-id"
    ],
    [
      "uid": "request_2",
      "method": "PUT",
      "path": "/network/v1/merchants",
      "body": ["merchant": [
          "name": "merchant name",
          "brand_id": "BRAND_brand-id",
          "country": "US",
          "currency": "USD",
          "category": "5432",
          "reference_id": "reference ID",
          "address": [
            "address_line_1": "1215 4th Ave",
            "address_line_2": "Suite 2300",
            "locality": "Seattle",
            "country": "US",
            "postal_code": "98161-1001",
            "administrative_district_level_1": "Washington"
          ],
          "default_fee_plans": ["in_app_fee_plan_id": "$request_1:fee_plan.id"]
        ]]
    ]
  ],
  "chains": [
    [
      "requests": [["uid": "request_1"], ["uid": "request_2"]],
      "execution_mode": "SEQUENTIAL"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/request-chains")! as URL,
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

```python Create API key -> update webhook endpoint
import requests

url = "https://api.cash.app/management/v1/request-chains"

payload = {
    "requests": [
        {
            "uid": "request_1",
            "method": "POST",
            "path": "/management/v1/api-keys",
            "body": {
                "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
                "api_key": {
                    "scopes": ["PAYMENTS_READ"],
                    "reference_id": "string"
                }
            }
        },
        {
            "uid": "request_2",
            "method": "PATCH",
            "path": "/management/v1/webhook-endpoints/WC_webhook-configuration-id",
            "body": { "webhook_endpoint": { "api_key_id": "$request_1:api_key.id" } }
        }
    ],
    "chains": [
        {
            "requests": [{ "uid": "request_1" }, { "uid": "request_2" }],
            "execution_mode": "SEQUENTIAL"
        }
    ]
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

```javascript Create API key -> update webhook endpoint
const url = 'https://api.cash.app/management/v1/request-chains';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"requests":[{"uid":"request_1","method":"POST","path":"/management/v1/api-keys","body":{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","api_key":{"scopes":["PAYMENTS_READ"],"reference_id":"string"}}},{"uid":"request_2","method":"PATCH","path":"/management/v1/webhook-endpoints/WC_webhook-configuration-id","body":{"webhook_endpoint":{"api_key_id":"$request_1:api_key.id"}}}],"chains":[{"requests":[{"uid":"request_1"},{"uid":"request_2"}],"execution_mode":"SEQUENTIAL"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Create API key -> update webhook endpoint
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/request-chains"

	payload := strings.NewReader("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/management/v1/api-keys\",\n      \"body\": {\n        \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n        \"api_key\": {\n          \"scopes\": [\n            \"PAYMENTS_READ\"\n          ],\n          \"reference_id\": \"string\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PATCH\",\n      \"path\": \"/management/v1/webhook-endpoints/WC_webhook-configuration-id\",\n      \"body\": {\n        \"webhook_endpoint\": {\n          \"api_key_id\": \"$request_1:api_key.id\"\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")

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

```ruby Create API key -> update webhook endpoint
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/management/v1/request-chains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/management/v1/api-keys\",\n      \"body\": {\n        \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n        \"api_key\": {\n          \"scopes\": [\n            \"PAYMENTS_READ\"\n          ],\n          \"reference_id\": \"string\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PATCH\",\n      \"path\": \"/management/v1/webhook-endpoints/WC_webhook-configuration-id\",\n      \"body\": {\n        \"webhook_endpoint\": {\n          \"api_key_id\": \"$request_1:api_key.id\"\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java Create API key -> update webhook endpoint
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/management/v1/request-chains")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/management/v1/api-keys\",\n      \"body\": {\n        \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n        \"api_key\": {\n          \"scopes\": [\n            \"PAYMENTS_READ\"\n          ],\n          \"reference_id\": \"string\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PATCH\",\n      \"path\": \"/management/v1/webhook-endpoints/WC_webhook-configuration-id\",\n      \"body\": {\n        \"webhook_endpoint\": {\n          \"api_key_id\": \"$request_1:api_key.id\"\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}")
  .asString();
```

```php Create API key -> update webhook endpoint
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/management/v1/request-chains', [
  'body' => '{
  "requests": [
    {
      "uid": "request_1",
      "method": "POST",
      "path": "/management/v1/api-keys",
      "body": {
        "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
        "api_key": {
          "scopes": [
            "PAYMENTS_READ"
          ],
          "reference_id": "string"
        }
      }
    },
    {
      "uid": "request_2",
      "method": "PATCH",
      "path": "/management/v1/webhook-endpoints/WC_webhook-configuration-id",
      "body": {
        "webhook_endpoint": {
          "api_key_id": "$request_1:api_key.id"
        }
      }
    }
  ],
  "chains": [
    {
      "requests": [
        {
          "uid": "request_1"
        },
        {
          "uid": "request_2"
        }
      ],
      "execution_mode": "SEQUENTIAL"
    }
  ]
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

```csharp Create API key -> update webhook endpoint
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/request-chains");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requests\": [\n    {\n      \"uid\": \"request_1\",\n      \"method\": \"POST\",\n      \"path\": \"/management/v1/api-keys\",\n      \"body\": {\n        \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n        \"api_key\": {\n          \"scopes\": [\n            \"PAYMENTS_READ\"\n          ],\n          \"reference_id\": \"string\"\n        }\n      }\n    },\n    {\n      \"uid\": \"request_2\",\n      \"method\": \"PATCH\",\n      \"path\": \"/management/v1/webhook-endpoints/WC_webhook-configuration-id\",\n      \"body\": {\n        \"webhook_endpoint\": {\n          \"api_key_id\": \"$request_1:api_key.id\"\n        }\n      }\n    }\n  ],\n  \"chains\": [\n    {\n      \"requests\": [\n        {\n          \"uid\": \"request_1\"\n        },\n        {\n          \"uid\": \"request_2\"\n        }\n      ],\n      \"execution_mode\": \"SEQUENTIAL\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Create API key -> update webhook endpoint
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = [
  "requests": [
    [
      "uid": "request_1",
      "method": "POST",
      "path": "/management/v1/api-keys",
      "body": [
        "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
        "api_key": [
          "scopes": ["PAYMENTS_READ"],
          "reference_id": "string"
        ]
      ]
    ],
    [
      "uid": "request_2",
      "method": "PATCH",
      "path": "/management/v1/webhook-endpoints/WC_webhook-configuration-id",
      "body": ["webhook_endpoint": ["api_key_id": "$request_1:api_key.id"]]
    ]
  ],
  "chains": [
    [
      "requests": [["uid": "request_1"], ["uid": "request_2"]],
      "execution_mode": "SEQUENTIAL"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/request-chains")! as URL,
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