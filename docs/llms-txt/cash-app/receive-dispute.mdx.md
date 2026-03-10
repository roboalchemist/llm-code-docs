# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/disputes/receive-dispute.mdx

# Receive Dispute

GET https://global-api-sandbox.afterpay.com/v2/disputes/{dispute_id}

Get detailed information about a dispute.

Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/disputes/receive-dispute

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/disputes/{dispute_id}:
    get:
      operationId: receive-dispute
      summary: Receive Dispute
      description: Get detailed information about a dispute.
      tags:
        - ''
      parameters:
        - name: dispute_id
          in: path
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
          description: application/json
          required: false
          schema:
            type: string
            default: application/json
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/dispute'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    DisputeReason:
      type: string
      enum:
        - product_not_received
        - product_unacceptable
        - credit_not_processed
        - order_canceled
        - duplicate
        - incorrect_amount
        - paid_by_other_means
        - fraudulent
        - fraudulent_merchant
      description: The reason for the dispute.
      title: DisputeReason
    DisputeStatus:
      type: string
      enum:
        - needs_response
        - under_review
        - won
        - lost
        - merchant_refunded
        - merchant_voided
      description: >-
        The current state of the dispute. Values depend on how the dispute state
        machine is modeled.
      title: DisputeStatus
    DisputeClosingReason:
      type: string
      enum:
        - merchant_accepted
        - evidence_accepted
        - evidence_rejected
        - deadline_expired
        - customer_cancelled
      description: >-
        A reason indicating how the final decision on the dispute was reached.
        Recommended possible values listed in Closing Reasons.
      title: DisputeClosingReason
    meta:
      type: object
      properties:
        transactionAmount:
          type: string
          description: The transaction amount for the order.
        network:
          type: string
          description: >-
            The payment network used by the customer. (For example, `Visa` or
            `MasterCard`)
        networkReferenceId:
          type: string
          description: The identifier for the payment.
        orderType:
          type: string
          description: The type of order. `ONLINE` or `INSTORE`
      required:
        - transactionAmount
        - orderType
      title: meta
    dispute:
      type: object
      properties:
        id:
          type: string
          description: Dispute identifier
        order:
          type: string
          description: The token of the order that the dispute is for.
        amount:
          type: string
          description: The amount of the dispute
        reason:
          $ref: '#/components/schemas/DisputeReason'
          description: The reason for the dispute.
        status:
          $ref: '#/components/schemas/DisputeStatus'
          description: >-
            The current state of the dispute. Values depend on how the dispute
            state machine is modeled.
        open:
          type: boolean
          default: true
          description: '`True` if a final decision on the dispute hasn''t been made yet.'
        responseDueBy:
          type: string
          description: >-
            Deadline by which the merchant must respond to the dispute. (Epoch
            timestamp in seconds, timezone UTC +0.00)
        createdAt:
          type: string
          description: >-
            A timestamp indicating when the dispute was created. (Epoch
            timestamp in seconds, timezone UTC +0.00)
        openingNote:
          type: string
          description: >-
            Text from the customer describing why the dispute was opened or the
            reason for the complaint. While dispute category codes are helpful
            at informing what a merchant should present, it doesn’t provide
            reasoning behind the customer’s complaint. In some cases, this can
            help merchants troubleshoot the dispute directly with their
            customers.
        openingNoteAttachments:
          type: string
          description: >-
            Attachments to supplement the `openingNote` if the customer provided
            photos or screenshots as part of their dispute description.
        updatedAt:
          type: string
          description: >-
            Timestamp when the dispute was updated. (Epoch timestamp in seconds,
            timezone UTC +0.00)
        closingReason:
          $ref: '#/components/schemas/DisputeClosingReason'
          description: >-
            A reason indicating how the final decision on the dispute was
            reached. Recommended possible values listed in Closing Reasons.
        closingNote:
          type: string
          description: >-
            Text describing in detail how the final decision on the dispute was
            reached. This supplements the `closingReason`.
        merchantOrderId:
          type: string
          description: The identifier for the transaction on the merchant side.
        transactionDate:
          type: string
          description: >-
            The timestamp of the order created by the customer. (Epoch timestamp
            in seconds, timezone UTC +0.00)
        settlementAmount:
          type: string
          description: The settlementAmount for audit usage.
        meta:
          $ref: '#/components/schemas/meta'
          description: The extra information for merchants to match payment.
      required:
        - id
        - order
        - amount
        - reason
        - status
        - open
        - responseDueBy
        - createdAt
        - openingNote
        - closingReason
        - merchantOrderId
        - transactionDate
        - settlementAmount
      description: Dispute object
      title: dispute
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id';
const options = {
  method: 'GET',
  headers: {'User-Agent': 'User-Agent', Authorization: 'Basic <username>:<password>'}
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

	url := "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id");
var request = new RestRequest(Method.GET);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")! as URL,
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

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id';
const options = {
  method: 'GET',
  headers: {'User-Agent': 'User-Agent', Authorization: 'Basic <username>:<password>'}
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

	url := "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id");
var request = new RestRequest(Method.GET);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")! as URL,
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

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id';
const options = {
  method: 'GET',
  headers: {'User-Agent': 'User-Agent', Authorization: 'Basic <username>:<password>'}
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

	url := "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id");
var request = new RestRequest(Method.GET);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")! as URL,
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

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id';
const options = {
  method: 'GET',
  headers: {'User-Agent': 'User-Agent', Authorization: 'Basic <username>:<password>'}
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

	url := "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id");
var request = new RestRequest(Method.GET);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/disputes/dispute_id")! as URL,
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