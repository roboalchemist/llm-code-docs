# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/create-refund.mdx

# Create Refund

POST https://global-api-sandbox.afterpay.com/v2/payments/{orderId}/refund
Content-Type: application/json

This endpoint performs a full or partial refund. The refund operation is idempotent if a unique `requestId` and `merchantReference` are provided.

If using the Deferred Payment Flow, be aware that only captured funds can be refunded. Do not create refunds after 120 days from the date of purchase.

**Connection Timeouts**
| Timeout | Time (Seconds) |
|---------|----------------|
| Open    | 10             |
| Read    | 70             |


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/create-refund

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/payments/{orderId}/refund:
    post:
      operationId: create-refund
      summary: Create Refund
      description: >
        This endpoint performs a full or partial refund. The refund operation is
        idempotent if a unique `requestId` and `merchantReference` are provided.


        If using the Deferred Payment Flow, be aware that only captured funds
        can be refunded. Do not create refunds after 120 days from the date of
        purchase.


        **Connection Timeouts**

        | Timeout | Time (Seconds) |

        |---------|----------------|

        | Open    | 10             |

        | Read    | 70             |
      tags:
        - ''
      parameters:
        - name: orderId
          in: path
          description: The unique Cash App Afterpay Order ID to apply the refund to.
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
          description: >
            Returns a Refund object in response. All request parameters are
            echoed in the response. In addition, the response includes the
            following:

            | Attribute | Type | Description |

            | --- | --- | --- |

            | `refundId` | string | The unique, permanent, Cash App
            Afterpay-generated Refund ID. |

            | `refundedAt` | string | The UTC timestamp of when the refund was
            completed, in [ISO
            8601](https://www.iso.org/iso-8601-date-and-time-format.html)
            format. |
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Refund'
        '412':
          description: >-
            The `orderId` is invalid, does not exist, or is not eligible for a
            refund. For example, the order was declined. Error code
            `precondition_failed`.
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: >
            | errorCode | Description |

            | --- | --- |

            | invalid_object | The `refundMerchantReference` exceeded 128
            characters. |

            | invalid_amount | The `amount` requested exceeded the amount
            available. |

            | invalid_object | The currency of the refund does not match the
            currency of the order (and the Merchant account). |

            | refund_timelimit_exceeded | The refund exceeds the time limit of
            120 days. |
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateRefund'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    MoneyCurrency:
      type: string
      enum:
        - AUD
        - NZD
        - USD
        - CAD
        - GBP
      title: MoneyCurrency
    Money:
      type: object
      properties:
        amount:
          type: string
          description: >-
            The amount as a string representation of a decimal number, rounded
            to 2 decimal places.
        currency:
          $ref: '#/components/schemas/MoneyCurrency'
      required:
        - amount
        - currency
      description: Object containing amount and currency
      title: Money
    CreateRefund:
      type: object
      properties:
        requestId:
          type: string
          description: Unique ID required for safe retries. Max length 64 (varchar).
        amount:
          $ref: '#/components/schemas/Money'
        merchantReference:
          type: string
          description: >-
            The merchant’s internal refund id/reference. This must be included
            along with the `requestId` to utilise idempotency. Max length 85
            (varchar).
        refundMerchantReference:
          type: string
          description: >-
            A unique reference for the individual refund event. Max length 128
            (varchar).
      description: >
        To guarantee safe retries, the merchant should offer their refund ID or
        reference, aligning with their internal records


        Unique values for the `requestID`  and `merchantReference` are required
        to guarantee safe retries. It is recommended that the merchant generates
        a UUID for each unique refund request. 


        The `refundMerchantReference` is a unique reference that when provided,
        will appear in the daily settlement file as "Payment Event Id". In most
        cases, this would hold the same value as the `merchantReference`.
      title: CreateRefund
    Refund:
      type: object
      properties:
        requestId:
          type: string
          description: Unique ID required for safe retries. Max length 64 (varchar).
        amount:
          $ref: '#/components/schemas/Money'
        merchantReference:
          type: string
          description: >-
            The merchant’s internal refund id/reference. This must be included
            along with the `requestId` to utilise idempotency. Max length 85
            (varchar).
        refundMerchantReference:
          type: string
          description: >-
            A unique reference for the individual refund event. Max length 128
            (varchar).
        refundId:
          type: string
          description: The unique, permanent, Cash App Afterpay-generated Refund ID.
        refundedAt:
          type: string
      description: >
        To guarantee safe retries, the merchant should offer their refund ID or
        reference, aligning with their internal records


        Unique values for the `requestID`  and `merchantReference` are required
        to guarantee safe retries. It is recommended that the merchant generates
        a UUID for each unique refund request. 


        The `refundMerchantReference` is a unique reference that when provided,
        will appear in the daily settlement file as "Payment Event Id". In most
        cases, this would hold the same value as the `merchantReference`.
      title: Refund
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund"

payload = {
    "requestId": "49efce77-4bf2-4e41-86e8-c2b92f493c2a",
    "amount": {
        "amount": "10.00",
        "currency": "AUD"
    },
    "merchantReference": "merchantRefundId-1234",
    "refundMerchantReference": "merchantRefundId-1234",
    "refundId": "67890123",
    "refundedAt": "2023-01-01T00:00:00.000Z"
}
headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund';
const options = {
  method: 'POST',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"requestId":"49efce77-4bf2-4e41-86e8-c2b92f493c2a","amount":{"amount":"10.00","currency":"AUD"},"merchantReference":"merchantRefundId-1234","refundMerchantReference":"merchantRefundId-1234","refundId":"67890123","refundedAt":"2023-01-01T00:00:00.000Z"}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund"

	payload := strings.NewReader("{\n  \"requestId\": \"49efce77-4bf2-4e41-86e8-c2b92f493c2a\",\n  \"amount\": {\n    \"amount\": \"10.00\",\n    \"currency\": \"AUD\"\n  },\n  \"merchantReference\": \"merchantRefundId-1234\",\n  \"refundMerchantReference\": \"merchantRefundId-1234\",\n  \"refundId\": \"67890123\",\n  \"refundedAt\": \"2023-01-01T00:00:00.000Z\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requestId\": \"49efce77-4bf2-4e41-86e8-c2b92f493c2a\",\n  \"amount\": {\n    \"amount\": \"10.00\",\n    \"currency\": \"AUD\"\n  },\n  \"merchantReference\": \"merchantRefundId-1234\",\n  \"refundMerchantReference\": \"merchantRefundId-1234\",\n  \"refundId\": \"67890123\",\n  \"refundedAt\": \"2023-01-01T00:00:00.000Z\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"requestId\": \"49efce77-4bf2-4e41-86e8-c2b92f493c2a\",\n  \"amount\": {\n    \"amount\": \"10.00\",\n    \"currency\": \"AUD\"\n  },\n  \"merchantReference\": \"merchantRefundId-1234\",\n  \"refundMerchantReference\": \"merchantRefundId-1234\",\n  \"refundId\": \"67890123\",\n  \"refundedAt\": \"2023-01-01T00:00:00.000Z\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund', [
  'body' => '{
  "requestId": "49efce77-4bf2-4e41-86e8-c2b92f493c2a",
  "amount": {
    "amount": "10.00",
    "currency": "AUD"
  },
  "merchantReference": "merchantRefundId-1234",
  "refundMerchantReference": "merchantRefundId-1234",
  "refundId": "67890123",
  "refundedAt": "2023-01-01T00:00:00.000Z"
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund");
var request = new RestRequest(Method.POST);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requestId\": \"49efce77-4bf2-4e41-86e8-c2b92f493c2a\",\n  \"amount\": {\n    \"amount\": \"10.00\",\n    \"currency\": \"AUD\"\n  },\n  \"merchantReference\": \"merchantRefundId-1234\",\n  \"refundMerchantReference\": \"merchantRefundId-1234\",\n  \"refundId\": \"67890123\",\n  \"refundedAt\": \"2023-01-01T00:00:00.000Z\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [
  "requestId": "49efce77-4bf2-4e41-86e8-c2b92f493c2a",
  "amount": [
    "amount": "10.00",
    "currency": "AUD"
  ],
  "merchantReference": "merchantRefundId-1234",
  "refundMerchantReference": "merchantRefundId-1234",
  "refundId": "67890123",
  "refundedAt": "2023-01-01T00:00:00.000Z"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/orderId/refund")! as URL,
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