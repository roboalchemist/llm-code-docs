# Source: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/publish-site.mdx

# Publish Site

POST https://api.webflow.com/sites/{site_id}/publish
Content-Type: application/json

Publish a site

Reference: https://developers.webflow.com/data/v1.0.0/reference/sites/sites/publish-site

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/publish:
    post:
      operationId: publish-site
      summary: Publish Site
      description: Publish a site
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
                $ref: '#/components/schemas/PublishedSite'
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
      requestBody:
        description: The domains to publish
        content:
          application/json:
            schema:
              type: object
              properties:
                domains:
                  type: array
                  items:
                    type: string
                  description: An array of domains that should be published
              required:
                - domains
servers:
  - url: https://api.webflow.com
components:
  schemas:
    PublishedSite:
      type: object
      properties:
        queued:
          type: boolean
          description: Indicates if the site has been queued for publish
      required:
        - queued
      title: PublishedSite
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.publish("580e63e98c9a982ac9b8b741", {
    customDomains: ["660c6449dd97ebc7346ac629", "660c6449dd97ebc7346ac62f"],
    publishToWebflowSubdomain: false
});

```

```python
import requests

url = "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/publish"

payload = { "domains": ["test-api-domain.com"] }
headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
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

	url := "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/publish"

	payload := strings.NewReader("{\n  \"domains\": [\n    \"test-api-domain.com\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Accept-Version", "1.0.0")
	req.Header.Add("Authorization", "Bearer <token>")
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

url = URI("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/publish")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept-Version"] = '1.0.0'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"domains\": [\n    \"test-api-domain.com\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/publish")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"domains\": [\n    \"test-api-domain.com\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/publish', [
  'body' => '{
  "domains": [
    "test-api-domain.com"
  ]
}',
  'headers' => [
    'Accept-Version' => '1.0.0',
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/publish");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept-Version", "1.0.0");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"domains\": [\n    \"test-api-domain.com\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept-Version": "1.0.0",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["domains": ["test-api-domain.com"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/publish")! as URL,
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