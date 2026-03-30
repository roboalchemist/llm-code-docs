# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/start-grant-approval.mdx

# Create Grant Approval

POST https://global-api-sandbox.afterpay.com/v2/grants/approvals
Content-Type: application/json

Initiates the approval process for a new grant.


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/start-grant-approval

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/grants/approvals:
    post:
      operationId: start-grant-approval
      summary: Create Grant Approval
      description: |
        Initiates the approval process for a new grant.
      tags:
        - ''
      parameters:
        - name: Authorization
          in: header
          description: Basic authentication
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
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GrantApprovalResponse'
        '401':
          description: >
            Authentication failed or insufficient permissions.


            | errorCode | Description |

            | --- | --- |

            | unauthorized | The API credentials are invalid or missing. |

            | insufficient_permissions | The merchant lacks the required
            'merchant_api_v2/initiate' permission. |
          content:
            application/json:
              schema:
                description: Any type
        '403':
          description: >
            | errorCode | Description |

            | --- | --- |

            | feature_not_enabled | On file payments are not enabled for this
            merchant. |
          content:
            application/json:
              schema:
                description: Any type
        '415':
          description: Unsupported Media Type - Content-Type header is missing or invalid
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: >
            | errorCode | Description |

            | --- | --- |

            | invalid_object | One or more required fields in the request body
            were missing or invalid. |
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GrantApprovalRequest'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    GrantApprovalTypeType:
      type: string
      enum:
        - ON_FILE
      description: Grant Type for approval.
      title: GrantApprovalTypeType
    GrantApprovalType:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/GrantApprovalTypeType'
          description: Grant Type for approval.
        merchantReference:
          type:
            - string
            - 'null'
          description: A merchant-provided reference for the grant.
      required:
        - type
      description: Details about the grant to be created.
      title: GrantApprovalType
    GrantApprovalRequestMerchant:
      type: object
      properties:
        redirectConfirmUrl:
          type: string
        redirectCancelUrl:
          type: string
        popupOriginUrl:
          type: string
          description: This property is optional when a `redirectConfirmURL` is provided.
        name:
          type: string
          description: The merchant name displayed in the Afterpay approval flow.
      required:
        - redirectConfirmUrl
        - redirectCancelUrl
      title: GrantApprovalRequestMerchant
    Consumer:
      type: object
      properties:
        email:
          type: string
          format: email
        givenNames:
          type: string
          description: The consumer's first name
        surname:
          type: string
          description: The consumer's last name
        phoneNumber:
          type: string
      required:
        - email
      description: >-
        The consumer data model is used for gathering essential user
        information. It captures details such as the individual's first name,
        represented by `givenNames`, and their last name, captured under
        `surname`. In addition, it stores the user's contact number under
        `phoneNumber` and their email address under `email`. These fields
        collectively provide contact and identification details for a user.
      title: Consumer
    GrantApprovalRequest:
      type: object
      properties:
        grants:
          type: array
          items:
            $ref: '#/components/schemas/GrantApprovalType'
          description: Grant type for approval (only single grant is supported)
        merchant:
          $ref: '#/components/schemas/GrantApprovalRequestMerchant'
        consumer:
          $ref: '#/components/schemas/Consumer'
          description: Consumer details for the grant
      required:
        - grants
        - merchant
      title: GrantApprovalRequest
    GrantApprovalResponse:
      type: object
      properties:
        token:
          type: string
          description: Token identifying this grant approval request
        expires:
          type: string
          format: date-time
          description: When this approval request expires
        redirectCheckoutUrl:
          type: string
          format: uri
          description: URL where the consumer should be redirected to complete approval
      required:
        - token
        - expires
        - redirectCheckoutUrl
      title: GrantApprovalResponse
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/grants/approvals"

payload = {
    "grants": [{ "type": "ON_FILE" }],
    "merchant": {
        "redirectConfirmUrl": "https://example.com/approval/confirm",
        "redirectCancelUrl": "https://example.com/approval/cancel"
    }
}
headers = {
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/grants/approvals';
const options = {
  method: 'POST',
  headers: {
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"grants":[{"type":"ON_FILE"}],"merchant":{"redirectConfirmUrl":"https://example.com/approval/confirm","redirectCancelUrl":"https://example.com/approval/cancel"}}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/grants/approvals"

	payload := strings.NewReader("{\n  \"grants\": [\n    {\n      \"type\": \"ON_FILE\"\n    }\n  ],\n  \"merchant\": {\n    \"redirectConfirmUrl\": \"https://example.com/approval/confirm\",\n    \"redirectCancelUrl\": \"https://example.com/approval/cancel\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://global-api-sandbox.afterpay.com/v2/grants/approvals")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"grants\": [\n    {\n      \"type\": \"ON_FILE\"\n    }\n  ],\n  \"merchant\": {\n    \"redirectConfirmUrl\": \"https://example.com/approval/confirm\",\n    \"redirectCancelUrl\": \"https://example.com/approval/cancel\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/grants/approvals")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"grants\": [\n    {\n      \"type\": \"ON_FILE\"\n    }\n  ],\n  \"merchant\": {\n    \"redirectConfirmUrl\": \"https://example.com/approval/confirm\",\n    \"redirectCancelUrl\": \"https://example.com/approval/cancel\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/grants/approvals', [
  'body' => '{
  "grants": [
    {
      "type": "ON_FILE"
    }
  ],
  "merchant": {
    "redirectConfirmUrl": "https://example.com/approval/confirm",
    "redirectCancelUrl": "https://example.com/approval/cancel"
  }
}',
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/grants/approvals");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"grants\": [\n    {\n      \"type\": \"ON_FILE\"\n    }\n  ],\n  \"merchant\": {\n    \"redirectConfirmUrl\": \"https://example.com/approval/confirm\",\n    \"redirectCancelUrl\": \"https://example.com/approval/cancel\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [
  "grants": [["type": "ON_FILE"]],
  "merchant": [
    "redirectConfirmUrl": "https://example.com/approval/confirm",
    "redirectCancelUrl": "https://example.com/approval/cancel"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/grants/approvals")! as URL,
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