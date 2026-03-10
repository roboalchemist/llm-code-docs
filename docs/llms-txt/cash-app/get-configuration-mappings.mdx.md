# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/configuration/get-configuration-mappings.mdx

# Get Configuration Mappings

GET https://global-api-sandbox.afterpay.com/v2/configuration/mappings

To set-up Cash App Pay on file, use this endpoint to retrieve your Cash App Pay brand ID.

Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/configuration/get-configuration-mappings

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/configuration/mappings:
    get:
      operationId: get-configuration-mappings
      summary: Get Configuration Mappings
      description: >-
        To set-up Cash App Pay on file, use this endpoint to retrieve your Cash
        App Pay brand ID.
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
                $ref: '#/components/schemas/ConfigurationMappings'
        '401':
          description: Unauthenticated
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-configuration-mappingsRequestUnauthorizedError
        '403':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-configuration-mappingsRequestForbiddenError
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    ConfigurationMappings:
      type: object
      properties:
        name:
          type: string
          description: Name of the brand to be shown in Cash App next to payments.
        externalBrandId:
          type: string
          description: >-
            The brand identifier for the Cash App Afterpay <> Cash App Pay
            merchant mapping.
      required:
        - name
        - externalBrandId
      title: ConfigurationMappings
    Get-configuration-mappingsRequestUnauthorizedError:
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
      title: Get-configuration-mappingsRequestUnauthorizedError
    Get-configuration-mappingsRequestForbiddenError:
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
      title: Get-configuration-mappingsRequestForbiddenError
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/configuration/mappings"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/configuration/mappings';
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

	url := "https://global-api-sandbox.afterpay.com/v2/configuration/mappings"

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

url = URI("https://global-api-sandbox.afterpay.com/v2/configuration/mappings")

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

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/v2/configuration/mappings")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/v2/configuration/mappings', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/configuration/mappings");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/configuration/mappings")! as URL,
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