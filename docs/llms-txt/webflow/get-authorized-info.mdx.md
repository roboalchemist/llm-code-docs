# Source: https://developers.webflow.com/data/v1.0.0/reference/meta/get-authorized-info.mdx

# Authorized Info

GET https://api.webflow.com/info

Basic information about the authorization being used.

Reference: https://developers.webflow.com/data/v1.0.0/reference/meta/get-authorized-info

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /info:
    get:
      operationId: get-authorized-info
      summary: Authorized Info
      description: Basic information about the authorization being used.
      tags:
        - subpackage_meta
      parameters:
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
                $ref: '#/components/schemas/Authorization'
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
    Application:
      type: object
      properties:
        _id:
          type: string
          format: uuid
        description:
          type: string
        homepage:
          type: string
          format: uri
        name:
          type: string
        owner:
          type: string
        ownerType:
          type: string
      title: Application
    Authorization:
      type: object
      properties:
        _id:
          type: string
          format: uuid
          description: The uniqueID of the authorization
        createdOn:
          type: string
          format: date-time
          description: The date the authorization was created
        grantType:
          type: string
          description: The grant type of the authorization
        lastUsed:
          type: string
          format: date-time
          description: The date the authorization was last used
        sites:
          type: array
          items:
            type: string
          description: The sites authorized
        orgs:
          type: array
          items:
            type: string
          description: The organizations authorized
        workspaces:
          type: array
          items:
            type: string
          description: The workspaces authorized
        users:
          type: array
          items:
            type: string
          description: The users authorized
        rateLimit:
          type: integer
          description: The default rate limit for the authorization
        status:
          type: string
          description: The status of the authorization
        application:
          $ref: '#/components/schemas/Application'
      title: Authorization
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/info"

headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/info';
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

	url := "https://api.webflow.com/info"

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

url = URI("https://api.webflow.com/info")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/info")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/info', [
  'headers' => [
    'Accept-Version' => '1.0.0',
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/info");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/info")! as URL,
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