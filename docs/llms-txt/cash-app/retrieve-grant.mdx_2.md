# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/retrieve-grant.mdx

# Retrieve Grant

POST https://global-api-sandbox.afterpay.com/v2/grants/retrieve
Content-Type: application/json

Retrieves a Cash App Pay customer grant by the ID of the customer that approved it and its own ID.

Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/retrieve-grant

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/grants/retrieve:
    post:
      operationId: retrieve-grant
      summary: Retrieve Grant
      description: >-
        Retrieves a Cash App Pay customer grant by the ID of the customer that
        approved it and its own ID.
      tags:
        - ''
      parameters:
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
          description: Accept
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
                $ref: '#/components/schemas/retrieve-grant_Response_200'
        '401':
          description: Unauthenticated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Retrieve-grantRequestUnauthorizedError'
        '403':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Retrieve-grantRequestForbiddenError'
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RetrieveGrantRequest'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    RetrieveGrantRequest:
      type: object
      properties:
        customerId:
          type: string
          description: ID of the customer that approved the customer grant.
        grantId:
          type: string
          description: ID of the customer grant to retrieve.
      required:
        - customerId
        - grantId
      title: RetrieveGrantRequest
    CashGrantIntent:
      type: string
      enum:
        - ON_FILE
        - ONE_TIME
      description: Either ON_FILE or ONE_TIME
      title: CashGrantIntent
    CashGrantType:
      type: string
      enum:
        - CASHAPP
      description: CASHAPP for all Cash App Pay transactions
      title: CashGrantType
    CashGrantDetailsStatus:
      type: string
      enum:
        - ACTIVE
        - EXPIRED
        - CONSUMED
        - REVOKED
      description: >
        Describes whether or not this grant can be used to perform the action
        associated with it.


        If `ACTIVE`, it can be used to perform the action.


        If `EXPIRED`, it may no longer be used to perform the action due to the
        current time being past the "expires_at" time.


        If `CONSUMED`, it was already redeemed to perform the action and cannot
        be used again.


        If `REVOKED`, the customer or merchant explicitly unauthorized the
        grant, preventing it from being used to perform the action.
      title: CashGrantDetailsStatus
    CashGrantDetailsCashapp:
      type: object
      properties:
        customerId:
          type: string
        cashtag:
          type: string
          description: >-
            A publicly-accessible, unique identifier (username) for individuals
            and businesses using Cash App.
      required:
        - customerId
        - cashtag
      title: CashGrantDetailsCashapp
    CashGrantDetails:
      type: object
      properties:
        status:
          $ref: '#/components/schemas/CashGrantDetailsStatus'
          description: >
            Describes whether or not this grant can be used to perform the
            action associated with it.


            If `ACTIVE`, it can be used to perform the action.


            If `EXPIRED`, it may no longer be used to perform the action due to
            the current time being past the "expires_at" time.


            If `CONSUMED`, it was already redeemed to perform the action and
            cannot be used again.


            If `REVOKED`, the customer or merchant explicitly unauthorized the
            grant, preventing it from being used to perform the action.
        cashapp:
          $ref: '#/components/schemas/CashGrantDetailsCashapp'
        createdAt:
          type: string
          description: >-
            When this grant was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updatedAt:
          type: string
          description: >-
            When this grant was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        expiresAt:
          type: string
          description: >
            If present, indicates when the grant's status will become EXPIRED,
            preventing a client from using it to create payments or refunds.


            The timestamp is in the [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
      required:
        - status
        - cashapp
        - createdAt
        - updatedAt
        - expiresAt
      title: CashGrantDetails
    CashGrant:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for this grant issued by Cash App.
        intent:
          $ref: '#/components/schemas/CashGrantIntent'
          description: Either ON_FILE or ONE_TIME
        type:
          $ref: '#/components/schemas/CashGrantType'
          description: CASHAPP for all Cash App Pay transactions
        details:
          $ref: '#/components/schemas/CashGrantDetails'
      required:
        - id
        - intent
        - type
        - details
      description: Describes a grant provided by Cash App.
      title: CashGrant
    retrieve-grant_Response_200:
      type: object
      properties:
        grant:
          $ref: '#/components/schemas/CashGrant'
      required:
        - grant
      title: retrieve-grant_Response_200
    Retrieve-grantRequestUnauthorizedError:
      type: object
      properties:
        errorCode:
          type: string
        errorId:
          type: string
        message:
          type: string
        httpStatusCode:
          type: integer
      title: Retrieve-grantRequestUnauthorizedError
    Retrieve-grantRequestForbiddenError:
      type: object
      properties:
        errorCode:
          type: string
        errorId:
          type: string
        message:
          type: string
        httpStatusCode:
          type: integer
      title: Retrieve-grantRequestForbiddenError
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/grants/retrieve"

payload = {
    "customerId": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
    "grantId": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50"
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
const url = 'https://global-api-sandbox.afterpay.com/v2/grants/retrieve';
const options = {
  method: 'POST',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"customerId":"CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY","grantId":"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50"}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/grants/retrieve"

	payload := strings.NewReader("{\n  \"customerId\": \"CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY\",\n  \"grantId\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\"\n}")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/grants/retrieve")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"customerId\": \"CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY\",\n  \"grantId\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/grants/retrieve")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"customerId\": \"CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY\",\n  \"grantId\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/grants/retrieve', [
  'body' => '{
  "customerId": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
  "grantId": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50"
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/grants/retrieve");
var request = new RestRequest(Method.POST);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"customerId\": \"CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY\",\n  \"grantId\": \"GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50\"\n}", ParameterType.RequestBody);
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
  "customerId": "CST_AQmxh4y_QGoNNIG5NUw0jttqyYedL1LklACQdyJ3H-Vs6WmLtP6A_C7XjQNohvY",
  "grantId": "GRG_221243dc6985a6819ff6950c1a21332f7bc4a46ebd49b5a7002908ab768e8e5ff7831e084d0d2c9d8d939793b55eff50"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/grants/retrieve")! as URL,
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