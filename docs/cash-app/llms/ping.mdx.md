# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/service-status/ping.mdx

# Ping

GET https://global-api-sandbox.afterpay.com/ping

Use this endpoint to check that the service is available and reachable.

Unlike all other endpoints, this endpoint does not require authentication, and responds with `text/plain` instead of `application/json`.


**Connection Timeouts**
| Timeout | Time (Seconds) |
|---------|----------------|
| Open    | 10             |
| Read    | 20             |


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/service-status/ping

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /ping:
    get:
      operationId: ping
      summary: Ping
      description: >
        Use this endpoint to check that the service is available and reachable.


        Unlike all other endpoints, this endpoint does not require
        authentication, and responds with `text/plain` instead of
        `application/json`.



        **Connection Timeouts**

        | Timeout | Time (Seconds) |

        |---------|----------------|

        | Open    | 10             |

        | Read    | 20             |
      tags:
        - ''
      parameters:
        - name: Accept
          in: header
          required: false
          schema:
            type: string
            default: text/plain
      responses:
        '200':
          description: Response with status 200
          content:
            application/json:
              schema:
                type: object
                properties: {}
        '405':
          description: >-
            The request was made by a HTTP Method other than `GET`, `HEAD` or
            `OPTIONS`. For example, `POST`, `PUT` or `DELETE`.
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/ping"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/ping';
const options = {method: 'GET'};

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

	url := "https://global-api-sandbox.afterpay.com/ping"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://global-api-sandbox.afterpay.com/ping")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/ping")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/ping');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/ping");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/ping")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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