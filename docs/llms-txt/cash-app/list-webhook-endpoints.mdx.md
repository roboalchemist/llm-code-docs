# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/list-webhook-endpoints.mdx

# List webhook endpoints

GET https://api.cash.app/management/v1/webhook-endpoints

Returns a list of webhook endpoints matching the query parameters provided.

Scopes: `WEBHOOK_CONFIG_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/list-webhook-endpoints

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /webhook-endpoints:
    get:
      operationId: list-webhook-endpoints
      summary: List webhook endpoints
      description: >-
        Returns a list of webhook endpoints matching the query parameters
        provided.


        Scopes: `WEBHOOK_CONFIG_READ`
      tags:
        - subpackage_webhooks
      parameters:
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
          description: Maximum number of webhook endpoints to return.
          required: false
          schema:
            type: integer
            default: 50
        - name: reference_id
          in: query
          description: >-
            A user-defined identifier for this webhook endpoint, typically used
            to associate the webhook endpoint with a record in an external
            system.
          required: false
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
                $ref: >-
                  #/components/schemas/webhooks_list-webhook-endpoints_Response_200
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
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
    webhooks_list-webhook-endpoints_Response_200:
      type: object
      properties:
        webhook_endpoints:
          type: array
          items:
            $ref: '#/components/schemas/WebhookEndpoint'
        cursor:
          type: string
          description: >-
            The pagination cursor to be used in a subsequent request. If empty,
            this is the final response.
      required:
        - webhook_endpoints
      title: webhooks_list-webhook-endpoints_Response_200
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
const url = 'https://api.cash.app/management/v1/webhook-endpoints';
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

	url := "https://api.cash.app/management/v1/webhook-endpoints"

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

url = URI("https://api.cash.app/management/v1/webhook-endpoints")

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

HttpResponse<String> response = Unirest.get("https://api.cash.app/management/v1/webhook-endpoints")
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

$response = $client->request('GET', 'https://api.cash.app/management/v1/webhook-endpoints', [
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

var client = new RestClient("https://api.cash.app/management/v1/webhook-endpoints");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/webhook-endpoints")! as URL,
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