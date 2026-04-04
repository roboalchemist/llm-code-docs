# Source: https://developers.webflow.com/data/v1.0.0/reference/cms/items/publish-items.mdx

# Publish Collection Items

PUT https://api.webflow.com/collections/{collection_id}/items/publish
Content-Type: application/json

Publish items in a Collection.


Reference: https://developers.webflow.com/data/v1.0.0/reference/cms/items/publish-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/publish:
    put:
      operationId: publish-items
      summary: Publish Collection Items
      description: |
        Publish items in a Collection.
      tags:
        - subpackage_items
      parameters:
        - name: collection_id
          in: path
          description: Unique identifier for a Collection
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
                $ref: '#/components/schemas/PublishedItems'
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
        description: The collection item ids to publish
        content:
          application/json:
            schema:
              type: object
              properties:
                itemIds:
                  type: array
                  items:
                    type: string
                    format: uuid
                  description: Array of item ids to publish
servers:
  - url: https://api.webflow.com
components:
  schemas:
    PublishedItems:
      type: object
      properties:
        publishedItemIds:
          type: array
          items:
            type: string
            format: uuid
          description: Array of published item ids
        errors:
          type: array
          items:
            type: string
          description: Array of errors
      description: A list of items published
      title: PublishedItems
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish"

payload = {}
headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish';
const options = {
  method: 'PUT',
  headers: {
    'Accept-Version': '1.0.0',
    Authorization: 'Bearer <token>',
    'Content-Type': 'application/json'
  },
  body: '{}'
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

	url := "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Accept-Version"] = '1.0.0'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish', [
  'body' => '{}',
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

var client = new RestClient("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish");
var request = new RestRequest(Method.PUT);
request.AddHeader("Accept-Version", "1.0.0");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept-Version": "1.0.0",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/publish")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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