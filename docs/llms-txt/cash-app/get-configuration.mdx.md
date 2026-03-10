# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/configuration/get-configuration.mdx

# Get Configuration

GET https://global-api-sandbox.afterpay.com/v2/configuration

Use this endpoint to retrieve the merchant's applicable payment limits.

A request to [Create Checkout](Checkouts.v2.yaml/paths/~1v2~1checkouts/post) may be rejected if the order amount is not between the `minimumAmount` and `maximumAmount` (inclusive).

Cash App Afterpay merchant configuration does not change frequently. For this reason, the configuration response includes Cache-Control headers to minimise network round trips when using a modern HTTP client. You should call Get Configuration on a fixed schedule, preferably once per day.

**Connection Timeouts**
| Timeout | Time (Seconds) |
|---------|----------------|
| Open    | 10             |
| Read    | 20             |

Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/configuration/get-configuration

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/configuration:
    get:
      operationId: get-configuration
      summary: Get Configuration
      description: >-
        Use this endpoint to retrieve the merchant's applicable payment limits.


        A request to [Create
        Checkout](Checkouts.v2.yaml/paths/~1v2~1checkouts/post) may be rejected
        if the order amount is not between the `minimumAmount` and
        `maximumAmount` (inclusive).


        Cash App Afterpay merchant configuration does not change frequently. For
        this reason, the configuration response includes Cache-Control headers
        to minimise network round trips when using a modern HTTP client. You
        should call Get Configuration on a fixed schedule, preferably once per
        day.


        **Connection Timeouts**

        | Timeout | Time (Seconds) |

        |---------|----------------|

        | Open    | 10             |

        | Read    | 20             |
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
          required: false
          schema:
            type: string
            default: application/json
      responses:
        '200':
          description: >
            Returns a
            [configuration](../reference/Configuration.v2.yaml/components/schemas/Merchant-limit)
            object containing the following attributes.

            | Attribute | Type           | Description |

            |-----------|----------------| ----------- |

            | `minimumAmount`    | Money    | Minimum order amount. Note: This
            attribute may not be included if the Merchant account has no minimum
            order amount.

            | `maximumAmount`    | Money    | Maximum order amount.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Merchant-limit'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-configurationRequestUnauthorizedError'
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
    Merchant-limit:
      type: object
      properties:
        minimumAmount:
          $ref: '#/components/schemas/Money'
        maximumAmount:
          $ref: '#/components/schemas/Money'
      title: Merchant-limit
    Get-configurationRequestUnauthorizedError:
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
      title: Get-configurationRequestUnauthorizedError
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/configuration"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/configuration';
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

	url := "https://global-api-sandbox.afterpay.com/v2/configuration"

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

url = URI("https://global-api-sandbox.afterpay.com/v2/configuration")

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

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/v2/configuration")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/v2/configuration', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/configuration");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/configuration")! as URL,
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