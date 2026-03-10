# Source: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/inventory/update-inventory.mdx

# Update Item Inventory

PATCH https://api.webflow.com/collections/{collection_id}/items/{item_id}/inventory
Content-Type: application/json

Updates the current inventory levels for a particular SKU item. Updates may be
given in one or two methods, absolutely or incrementally. Absolute updates
are done by setting `quantity` directly. Incremental updates are by specifying
the inventory delta in `updateQuantity` which is then added to the `quantity`
stored on the server.


Reference: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/inventory/update-inventory

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/{item_id}/inventory:
    patch:
      operationId: update-inventory
      summary: Update Item Inventory
      description: >
        Updates the current inventory levels for a particular SKU item. Updates
        may be

        given in one or two methods, absolutely or incrementally. Absolute
        updates

        are done by setting `quantity` directly. Incremental updates are by
        specifying

        the inventory delta in `updateQuantity` which is then added to the
        `quantity`

        stored on the server.
      tags:
        - subpackage_inventory
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
                $ref: '#/components/schemas/InventoryItem'
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
        description: The updated inventory
        content:
          application/json:
            schema:
              type: object
              properties:
                fields:
                  $ref: >-
                    #/components/schemas/CollectionsCollectionIdItemsItemIdInventoryPatchRequestBodyContentApplicationJsonSchemaFields
                  description: The inventory fields to update
servers:
  - url: https://api.webflow.com
components:
  schemas:
    CollectionsCollectionIdItemsItemIdInventoryPatchRequestBodyContentApplicationJsonSchemaFieldsInventoryType:
      type: string
      enum:
        - infinite
        - finite
      description: infinite or finite
      title: >-
        CollectionsCollectionIdItemsItemIdInventoryPatchRequestBodyContentApplicationJsonSchemaFieldsInventoryType
    CollectionsCollectionIdItemsItemIdInventoryPatchRequestBodyContentApplicationJsonSchemaFields:
      type: object
      properties:
        inventoryType:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdInventoryPatchRequestBodyContentApplicationJsonSchemaFieldsInventoryType
          description: infinite or finite
        updateQuantity:
          type: number
          format: double
          description: Adds this quantity to currently store quantity. Can be negative.
        quantity:
          type: number
          format: double
          description: Immediately sets quantity to this value.
      description: The inventory fields to update
      title: >-
        CollectionsCollectionIdItemsItemIdInventoryPatchRequestBodyContentApplicationJsonSchemaFields
    InventoryItemInventoryType:
      type: string
      enum:
        - infinite
        - finite
      description: infinite or finite
      title: InventoryItemInventoryType
    InventoryItem:
      type: object
      properties:
        _id:
          type: string
          format: uuid
          description: Unique identifier for a SKU item
        quantity:
          type: number
          format: double
          description: Total quantity of items remaining in inventory (if finite)
        inventoryType:
          $ref: '#/components/schemas/InventoryItemInventoryType'
          description: infinite or finite
      description: The availabile inventory for an item
      title: InventoryItem
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory"

payload = {}
headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory';
const options = {
  method: 'PATCH',
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

	url := "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory"

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

url = URI("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory")

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

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory")
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

$response = $client->request('PATCH', 'https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory', [
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

var client = new RestClient("https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754/inventory")! as URL,
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