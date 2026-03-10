# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/update-payment-by-order-id.mdx

# Update Payment by Order ID

PUT https://global-api-sandbox.afterpay.com/v2/payments/{orderId}
Content-Type: application/json

This endpoint is to create merchant side order ID's following the Cash App Afterpay order ID creation. Call the endpoint immediately after the Cash App Afterpay order is created.

Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/update-payment-by-order-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/payments/{orderId}:
    put:
      operationId: update-payment-by-order-id
      summary: Update Payment by Order ID
      description: >-
        This endpoint is to create merchant side order ID's following the Cash
        App Afterpay order ID creation. Call the endpoint immediately after the
        Cash App Afterpay order is created.
      tags:
        - ''
      parameters:
        - name: orderId
          in: path
          description: The Order ID to update
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Basic authentication
          required: true
          schema:
            type: string
        - name: User-Agent
          in: header
          required: true
          schema:
            type: string
        - name: Accept
          in: header
          required: false
          schema:
            type: string
            default: application/json
      responses:
        '201':
          description: Returns object containing the following attributes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/update-payment-by-order-id_Response_201'
        '404':
          description: >-
            The Cash App Afterpay payment ID to update was not found. Error code
            `not_found`.
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                merchantReference:
                  type: string
                  default: new_merchant_order_id_1234
                  description: The merchant’s new order ID to replace with
              required:
                - merchantReference
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOriginalAmount:
      type: object
      properties: {}
      description: Total amount for the order. See Money.
      title: V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOriginalAmount
    V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOpenToCaptureAmount:
      type: object
      properties: {}
      description: Total amount that can be captured for order. See Money.
      title: >-
        V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOpenToCaptureAmount
    V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaRefunds:
      type: object
      properties: {}
      description: The refund details for merchant's order. See Refund.
      title: V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaRefunds
    V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOrderDetails:
      type: object
      properties: {}
      description: The order bound to the payment. See Order Details.
      title: V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOrderDetails
    V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaEvents:
      type: object
      properties: {}
      description: Event list for for merchant's order. See Events.
      title: V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaEvents
    update-payment-by-order-id_Response_201:
      type: object
      properties:
        id:
          type: string
          description: The unique Cash App Afterpay (merchant payment) payment ID.
        token:
          type: string
          description: Checkout token to be used to complete customer checkout and payment.
        status:
          type: string
          description: \"APPROVED" (update is only valid for successful orders)
        created:
          description: >-
            The payment creation time [ISO 8601 UTC/Zulu
            time](https://www.iso.org/iso-8601-date-and-time-format.html).
        originalAmount:
          $ref: >-
            #/components/schemas/V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOriginalAmount
          description: Total amount for the order. See Money.
        openToCaptureAmount:
          $ref: >-
            #/components/schemas/V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOpenToCaptureAmount
          description: Total amount that can be captured for order. See Money.
        paymentState:
          type: string
          description: >-
            Available states: "AUTH_APPROVED", "CAPTURED", "VOIDED", "EXPIRED",
            "AUTH_DECLINED", "PARTIALLY_CAPTURED", "CAPTURE_DECLINED""
        merchantReference:
          description: Any type
        refunds:
          $ref: >-
            #/components/schemas/V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaRefunds
          description: The refund details for merchant's order. See Refund.
        orderDetails:
          $ref: >-
            #/components/schemas/V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaOrderDetails
          description: The order bound to the payment. See Order Details.
        events:
          $ref: >-
            #/components/schemas/V2PaymentsOrderIdPutResponsesContentApplicationJsonSchemaEvents
          description: Event list for for merchant's order. See Events.
      title: update-payment-by-order-id_Response_201
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/payments/orderId"

payload = { "merchantReference": "new_merchant_order_id_1234" }
headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/orderId';
const options = {
  method: 'PUT',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"merchantReference":"new_merchant_order_id_1234"}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/payments/orderId"

	payload := strings.NewReader("{\n  \"merchantReference\": \"new_merchant_order_id_1234\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")
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

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/orderId")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"merchantReference\": \"new_merchant_order_id_1234\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://global-api-sandbox.afterpay.com/v2/payments/orderId")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"merchantReference\": \"new_merchant_order_id_1234\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://global-api-sandbox.afterpay.com/v2/payments/orderId', [
  'body' => '{
  "merchantReference": "new_merchant_order_id_1234"
}',
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/orderId");
var request = new RestRequest(Method.PUT);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"merchantReference\": \"new_merchant_order_id_1234\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = ["merchantReference": "new_merchant_order_id_1234"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/orderId")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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