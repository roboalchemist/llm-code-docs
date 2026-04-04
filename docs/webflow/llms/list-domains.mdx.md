# Source: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/list-domains.mdx

# List Domains

GET https://api.webflow.com/sites/{site_id}/domains

List of all custom domains added to a given site

Reference: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/list-domains

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/domains:
    get:
      operationId: list-domains
      summary: List Domains
      description: List of all custom domains added to a given site
      tags:
        - subpackage_sites
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: uuid
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
        - name: Accept-Version
          in: header
          description: The API version
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Domain'
        '400':
          description: >-
            Request body was incorrectly formatted. Likely invalid JSON being
            sent up.
          content:
            application/json:
              schema:
                description: Any type
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                description: Any type
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                description: Any type
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                description: Any type
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: https://api.webflow.com
components:
  schemas:
    Domain:
      type: object
      properties:
        _id:
          type: string
          format: uuid
          description: Unique identifier for domain
        name:
          type: string
          description: The domain name
      required:
        - _id
      title: Domain
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains"

headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains';
const options = {
  method: 'GET',
  headers: {'Accept-Version': '1.0.0', Authorization: 'Bearer <token>'}
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

	url := "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Accept-Version", "1.0.0")
	req.Header.Add("Authorization", "Bearer <token>")

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

url = URI("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Accept-Version"] = '1.0.0'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains', [
  'headers' => [
    'Accept-Version' => '1.0.0',
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains");
var request = new RestRequest(Method.GET);
request.AddHeader("Accept-Version", "1.0.0");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept-Version": "1.0.0",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/domains")! as URL,
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