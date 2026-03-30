# Source: https://developers.webflow.com/data/v1.0.0/reference/cms/items/patch-item.mdx

# Patch Collection Item

PATCH https://api.webflow.com/collections/{collection_id}/items/{item_id}
Content-Type: application/json

Update only fields that need to be changed. To upload a new image set the image URL to the corresponding item's field. Collection items that reuse images previously uploaded can just reference their fileId property.


Reference: https://developers.webflow.com/data/v1.0.0/reference/cms/items/patch-item

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/{item_id}:
    patch:
      operationId: patch-item
      summary: Patch Collection Item
      description: >
        Update only fields that need to be changed. To upload a new image set
        the image URL to the corresponding item's field. Collection items that
        reuse images previously uploaded can just reference their fileId
        property.
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
        - name: live
          in: query
          description: >-
            Boolean indicating if the item(s) should be published/unpublished
            to/from the live site
          required: false
          schema:
            type: boolean
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
                $ref: '#/components/schemas/CollectionItem'
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
        description: The item to update
        content:
          application/json:
            schema:
              type: object
              properties:
                fields:
                  $ref: '#/components/schemas/Field'
servers:
  - url: https://api.webflow.com
components:
  schemas:
    Field:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the item
        slug:
          type: string
          default: new-item
          description: Slug of the item
        name:
          type: string
          default: My New Item
          description: item name
        _archived:
          type: boolean
          default: false
          description: item archive status
        _draft:
          type: boolean
          default: false
          description: item draft status
      required:
        - slug
        - name
        - _archived
        - _draft
      description: Fields in your collection item
      title: Field
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
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.updateItem("580e63fc8c9a982ac9b8b745", "580e64008c9a982ac9b8b754", {
    skipInvalidFiles: true,
    body: {
        isArchived: false,
        isDraft: false,
        fieldData: {
            name: "The Hitchhiker's Guide to the Galaxy",
            slug: "hitchhikers-guide-to-the-galaxy",
            "plain-text": "Don't Panic.",
            "rich-text": "<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>",
            "main-image": {
                "fileId": "62b720ef280c7a7a3be8cabe",
                "url": "/files/62b720ef280c7a7a3be8cabe_image.png"
            },
            "image-gallery": [
                {
                    "fileId": "62b720ef280c7a7a3be8cabd",
                    "url": "/files/62b720ef280c7a7a3be8cabd_image.png"
                },
                {
                    "fileId": "62b720ef280c7a7a3be8cabe",
                    "url": "/files/62b720ef280c7a7a3be8cabe_image.png"
                }
            ],
            "intro-video": "https://www.youtube.com/watch?v=aJ83KAggd-4",
            "official-site": "https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy",
            "contact-email": "zaphod.beeblebrox@heartofgold.gov",
            "support-phone": "424-242-4242",
            "answer-to-everything": 42,
            "release-date": "1979-10-12T00:00:00.000Z",
            "is-featured": true,
            "brand-color": "#000000",
            category: "62b720ef280c7a7a3be8cabf",
            author: "62b720ef280c7a7a3be8cab0",
            tags: [
                "62b720ef280c7a7a3be8cab1",
                "62b720ef280c7a7a3be8cab2"
            ],
            "downloadable-asset": {
                "fileId": "62b720ef280c7a7a3be8cab3",
                "url": "/files/62b720ef280c7a7a3be8cab3_document.pdf"
            }
        }
    }
});

```

```python
import requests

url = "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754"

querystring = {"live":"true"}

payload = {}
headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers, params=querystring)

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

	url := "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?live=true"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?live=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
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

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?live=true")
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

$response = $client->request('PATCH', 'https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?live=true', [
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

var client = new RestClient("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?live=true");
var request = new RestRequest(Method.PATCH);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?live=true")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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