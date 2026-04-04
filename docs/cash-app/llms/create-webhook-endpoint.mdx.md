# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint.mdx

# Create webhook endpoint

POST https://api.cash.app/management/v1/webhook-endpoints
Content-Type: application/json

Creates a new webhook endpoint which Cash App can send events to.

<Note title="Note">
 Webhook events will not be successfully delivered for new domains until the new domain is allow-listed. New domains must be manually reviewed and allow-listed. It will typically take 1 business day to allow-list new domains.
</Note>

Scopes: `WEBHOOK_CONFIG_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/create-webhook-endpoint

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /webhook-endpoints:
    post:
      operationId: create-webhook-endpoint
      summary: Create webhook endpoint
      description: |-
        Creates a new webhook endpoint which Cash App can send events to.

        <Note title="Note">
         Webhook events will not be successfully delivered for new domains until the new domain is allow-listed. New domains must be manually reviewed and allow-listed. It will typically take 1 business day to allow-list new domains.
        </Note>

        Scopes: `WEBHOOK_CONFIG_WRITE`
      tags:
        - subpackage_webhooks
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
                  #/components/schemas/webhooks_create-webhook-endpoint_Response_201
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
                webhook_endpoint:
                  $ref: >-
                    #/components/schemas/WebhookEndpointsPostRequestBodyContentApplicationJsonSchemaWebhookEndpoint
              required:
                - idempotency_key
                - webhook_endpoint
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
    IdempotencyKey:
      type: string
      description: >-
        A unique identifier which can be used by Cash App to de-duplicate
        retries of this request, making it idempotent. Learn more about
        [idempotency](../docs/api/technical-documentation/api-fundamentals/idempotency)
        in the API.
      title: IdempotencyKey
    EventType:
      type: string
      enum:
        - customer.created
        - customer.deleted
        - customer.updated
        - customer_request.state.updated
        - dispute.created
        - dispute.state.updated
        - grant.created
        - grant.status.updated
        - merchant.status.updated
        - payment.status.updated
        - refund.status.updated
      description: The type of event that will be sent to the webhook endpoint.
      title: EventType
    ApiVersion:
      type: string
      enum:
        - v1
      description: 'Represents the API version. '
      title: ApiVersion
    EventConfiguration:
      type: object
      properties:
        event_type:
          $ref: '#/components/schemas/EventType'
        api_version:
          $ref: '#/components/schemas/ApiVersion'
      required:
        - event_type
        - api_version
      description: >-
        Represents a supported event type and the API version that the event of
        this type should be serialized to.
      title: EventConfiguration
    WebhookEndpointsPostRequestBodyContentApplicationJsonSchemaWebhookEndpoint:
      type: object
      properties:
        api_key_id:
          type: string
          description: >-
            The API key ID which will be used to sign requests made to this
            webhook endpoint.
        event_configurations:
          type: array
          items:
            $ref: '#/components/schemas/EventConfiguration'
          description: >-
            The list of supported event types for this webhook endpoint. Events
            of a particular type will only be sent to endpoints that contain the
            type in this list.
        url:
          type:
            - string
            - 'null'
          description: >-
            The URL of the endpoint which events will be delivered to. If NULL
            is specified, events will be not be delivered to an endpoint but
            will still be persisted and accessible via the List Webhook Events
            API.
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this webhook endpoint, typically used
            to associate the webhook endpoint with a record in an external
            system.
        delivery_timeout:
          type: number
          format: double
          default: 5000
          description: >-
            The duration, in milliseconds, that Cash App will take to deliver an
            event to this endpoint before timing out.
        max_delivery_frequency:
          type: number
          format: double
          description: >-
            The maximum number of events per second that will be delivered to
            this endpoint before rate limiting kicks in. The default for this
            field is unset (NULL) which means no rate limiting. However, if you
            enable rate limiting, the values can range from 1 to 100000.
      required:
        - api_key_id
        - event_configurations
        - url
      title: >-
        WebhookEndpointsPostRequestBodyContentApplicationJsonSchemaWebhookEndpoint
    WebhookEndpointStatus:
      type: string
      enum:
        - APPROVED
        - ENDPOINT_URL_UNDER_REVIEW
      description: >-
        The approval status of a webhook endpoint. Once a webhook endpoint is
        approved, Cash App will deliver events to that webhook endpoint.
      title: WebhookEndpointStatus
    WebhookEndpoint:
      type: object
      properties:
        id:
          type: string
          description: The unique ID for a webhook endpoint issued by Cash App.
        api_key_id:
          type: string
          description: >-
            The API key ID which will be used to sign requests made to this
            webhook endpoint.
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this webhook endpoint, typically used
            to associate the webhook endpoint with a record in an external
            system.
        url:
          type:
            - string
            - 'null'
          format: uri
          description: >-
            The events are delivered to this endpoint URL. If NULL, events will
            be not be delivered to an endpoint but will still be persisted and
            accessible via the List Webhook Events API.
        event_configurations:
          type: array
          items:
            $ref: '#/components/schemas/EventConfiguration'
          description: >-
            The list of supported event types for this webhook endpoint. Events
            of a particular type will only be sent to endpoints that contain the
            type in this list.
        created_at:
          type: string
          format: date-time
          description: The timestamp of when this webhook endpoint was created.
        updated_at:
          type: string
          format: date-time
          description: The timestamp of when this endpoint was last updated.
        delivery_timeout:
          type: number
          format: double
          default: 5000
          description: >-
            The duration, in milliseconds, that Cash App will take to deliver an
            event to this endpoint before timing out.
        max_delivery_frequency:
          type:
            - number
            - 'null'
          format: double
          description: >-
            The maximum number of events per second that will be delivered to
            this endpoint before rate limiting kicks in. The default for this
            field is unset (NULL) which means no rate limiting. However, if you
            enable rate limiting, the values can range from 1 to 100000.
        status:
          $ref: '#/components/schemas/WebhookEndpointStatus'
      required:
        - id
        - api_key_id
        - url
        - event_configurations
        - created_at
        - updated_at
        - delivery_timeout
        - status
      description: The events will be sent to this webhook endpoint.
      title: WebhookEndpoint
    webhooks_create-webhook-endpoint_Response_201:
      type: object
      properties:
        webhook_endpoint:
          $ref: '#/components/schemas/WebhookEndpoint'
      required:
        - webhook_endpoint
      title: webhooks_create-webhook-endpoint_Response_201
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

url = "https://api.cash.app/management/v1/webhook-endpoints"

payload = {
    "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
    "webhook_endpoint": {
        "api_key_id": "KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
        "event_configurations": [
            {
                "event_type": "customer.created",
                "api_version": "v1"
            }
        ],
        "url": "string"
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
const url = 'https://api.cash.app/management/v1/webhook-endpoints';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"idempotency_key":"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19","webhook_endpoint":{"api_key_id":"KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30","event_configurations":[{"event_type":"customer.created","api_version":"v1"}],"url":"string"}}'
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

	url := "https://api.cash.app/management/v1/webhook-endpoints"

	payload := strings.NewReader("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"webhook_endpoint\": {\n    \"api_key_id\": \"KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30\",\n    \"event_configurations\": [\n      {\n        \"event_type\": \"customer.created\",\n        \"api_version\": \"v1\"\n      }\n    ],\n    \"url\": \"string\"\n  }\n}")

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

url = URI("https://api.cash.app/management/v1/webhook-endpoints")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"webhook_endpoint\": {\n    \"api_key_id\": \"KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30\",\n    \"event_configurations\": [\n      {\n        \"event_type\": \"customer.created\",\n        \"api_version\": \"v1\"\n      }\n    ],\n    \"url\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/management/v1/webhook-endpoints")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"webhook_endpoint\": {\n    \"api_key_id\": \"KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30\",\n    \"event_configurations\": [\n      {\n        \"event_type\": \"customer.created\",\n        \"api_version\": \"v1\"\n      }\n    ],\n    \"url\": \"string\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/management/v1/webhook-endpoints', [
  'body' => '{
  "idempotency_key": "e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19",
  "webhook_endpoint": {
    "api_key_id": "KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
    "event_configurations": [
      {
        "event_type": "customer.created",
        "api_version": "v1"
      }
    ],
    "url": "string"
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

var client = new RestClient("https://api.cash.app/management/v1/webhook-endpoints");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"idempotency_key\": \"e345c3fb-1caa-46fd-b0d3-aa6c7b00ab19\",\n  \"webhook_endpoint\": {\n    \"api_key_id\": \"KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30\",\n    \"event_configurations\": [\n      {\n        \"event_type\": \"customer.created\",\n        \"api_version\": \"v1\"\n      }\n    ],\n    \"url\": \"string\"\n  }\n}", ParameterType.RequestBody);
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
  "webhook_endpoint": [
    "api_key_id": "KEY_2f6cd0d5cc26b34ac8785026b149797ecc0758be3dc3a857d405f2f62074ef30",
    "event_configurations": [
      [
        "event_type": "customer.created",
        "api_version": "v1"
      ]
    ],
    "url": "string"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/webhook-endpoints")! as URL,
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