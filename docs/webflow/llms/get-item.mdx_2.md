# Source: https://developers.webflow.com/data/v1.0.0/reference/cms/items/get-item.mdx

# Get Collection Item

GET https://api.webflow.com/collections/{collection_id}/items/{item_id}

Get an item in a collection

Reference: https://developers.webflow.com/data/v1.0.0/reference/cms/items/get-item

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/{item_id}:
    get:
      operationId: get-item
      summary: Get Collection Item
      description: Get an item in a collection
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
        - name: item_id
          in: path
          description: Unique identifier for and Item
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
                $ref: '#/components/schemas/CollectionItemList'
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
    CollectionItem:
      type: object
      properties:
        _archived:
          type: boolean
          default: false
          description: Boolean determining if the Item is set to archived
        _draft:
          type: boolean
          default: false
          description: Boolean determining if the Item is set to draft
        _id:
          type: string
          description: Unique identifier for the Item
        _cid:
          type: string
          description: Unique identifier for the Collection the Item belongs within
        name:
          type: string
          description: Name given to the Item
        slug:
          type: string
          description: >-
            URL structure of the Item in your site. Note: Updates to an item
            slug will break all links referencing the old slug.
      description: >
        The fields that define the schema for a given Item are based on the
        Collection that Item belongs to. Beyond the user defined fields, there
        are a handful of additional fields that are automatically created for
        all items
      title: CollectionItem
    CollectionItemList:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/CollectionItem'
          description: List of Items within the collection
        count:
          type: integer
          description: Number of items returned
        limit:
          type: integer
          default: 100
          description: The limit specified in the request
        offset:
          type: integer
          default: 0
          description: The offset specified for pagination
        total:
          type: integer
          description: Total number of items in the collection
      description: Results from collection items list
      title: CollectionItemList
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.getItem("580e63fc8c9a982ac9b8b745", "580e64008c9a982ac9b8b754", {
    cmsLocaleId: "cmsLocaleId"
});

```

```python
import requests

url = "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754"

headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754"

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

url = URI("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754', [
  'headers' => [
    'Accept-Version' => '1.0.0',
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754")! as URL,
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