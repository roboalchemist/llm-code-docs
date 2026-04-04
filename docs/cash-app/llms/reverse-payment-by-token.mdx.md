# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/reverse-payment-by-token.mdx

# Reverse Payment By Token

POST https://global-api-sandbox.afterpay.com/v2/payments/token:{token}/reversal

This endpoint makes a reversal of the checkout that is used to start the Cash App Afterpay payment process. This cancels the order asynchronously as soon as it is created without the need of an additional call to the void endpoint. For a payment to be eligible, the order must be in an Auth-Approved or Captured state, and it must be issued within 10 minutes of the order being created.

**Connection Timeouts**
| Timeout | Time (Seconds) |
|---------|----------------|
| Open    | 10             |
| Read    | 70             |


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/reverse-payment-by-token

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/payments/token:{token}/reversal:
    post:
      operationId: reverse-payment-by-token
      summary: Reverse Payment By Token
      description: >
        This endpoint makes a reversal of the checkout that is used to start the
        Cash App Afterpay payment process. This cancels the order asynchronously
        as soon as it is created without the need of an additional call to the
        void endpoint. For a payment to be eligible, the order must be in an
        Auth-Approved or Captured state, and it must be issued within 10 minutes
        of the order being created.


        **Connection Timeouts**

        | Timeout | Time (Seconds) |

        |---------|----------------|

        | Open    | 10             |

        | Read    | 70             |
      tags:
        - ''
      parameters:
        - name: token
          in: path
          description: The token of the checkout to be reversed (voided).
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
        '204':
          description: >-
            The Reversal endpoint indicates a successful response with a 204
            status code response. Returns no content in the response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/reverse-payment-by-token_Response_204'
        '402':
          description: Invalid Token. Error code `invalid_token`.
          content:
            application/json:
              schema:
                description: Any type
        '412':
          description: >
            | errorCode | Description |

            | --- | --- |

            | precondition_failed | Payment reversal previously processed |

            | precondition_failed | Payment not eligible for a reversal |

            | precondition_failed | Order outside reversal window |

            | precondition_failed | Order in pending reversal, no captures/auth
            accepted |
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    reverse-payment-by-token_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: reverse-payment-by-token_Response_204
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.post(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal';
const options = {
  method: 'POST',
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

	url := "https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal"

	req, _ := http.NewRequest("POST", url, nil)

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

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal");
var request = new RestRequest(Method.POST);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/token:token/reversal")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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