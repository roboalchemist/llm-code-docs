# Source: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/products-sk-us/create-skus.mdx

# Create SKU

POST https://api.webflow.com/sites/{site_id}/products/{product_id}/skus
Content-Type: application/json

Create additional SKUs to cover every variant of your Product. The Default SKU already counts as one of the variants.

Creating additional SKUs will set the product type to `Advanced` for the product associated with the SKUs. The product type is used to determine which Product and SKU fields are shown to users in the `Designer` and the `Editor`. Setting it to `Advanced` ensures that all Product and SKU fields will be shown. The product type can be edited in the `Designer` or the `Editor`.


Reference: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/products-sk-us/create-skus

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products/{product_id}/skus:
    post:
      operationId: create-skus
      summary: Create SKU
      description: >
        Create additional SKUs to cover every variant of your Product. The
        Default SKU already counts as one of the variants.


        Creating additional SKUs will set the product type to `Advanced` for the
        product associated with the SKUs. The product type is used to determine
        which Product and SKU fields are shown to users in the `Designer` and
        the `Editor`. Setting it to `Advanced` ensures that all Product and SKU
        fields will be shown. The product type can be edited in the `Designer`
        or the `Editor`.
      tags:
        - subpackage_productsSkUs
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: uuid
        - name: product_id
          in: path
          description: Unique identifier for a Product
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
                $ref: '#/components/schemas/SKUList'
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
        description: The SKUs to add
        content:
          application/json:
            schema:
              type: object
              properties:
                skus:
                  type: array
                  items:
                    $ref: '#/components/schemas/SKU'
                  description: An array of the SKU data your are adding
servers:
  - url: https://api.webflow.com
components:
  schemas:
    SkuFieldPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          default: 2000
          description: Price of SKU
        unit:
          type: string
          default: USD
          description: Currency of Item
      required:
        - value
        - unit
      description: price of SKU
      title: SkuFieldPrice
    SKUField:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the SKU
        slug:
          type: string
          default: post-body
          description: Slug of the SKU
        name:
          type: string
          default: 'Cloak Of Invisibility Color: Obsidian Black'
          description: SKU name
        _archived:
          type: boolean
          default: false
          description: item archive status
        _draft:
          type: boolean
          default: false
          description: item draft status
        price:
          $ref: '#/components/schemas/SkuFieldPrice'
          description: price of SKU
      required:
        - slug
        - _archived
        - _draft
        - price
      description: Fields in your SKU object
      title: SKUField
    SKU:
      type: object
      properties:
        _id:
          type: string
          format: uuid
          description: Unique identifier for collection
        lastUpdated:
          type: string
          format: date-time
          description: The date the collection was last updated
        createdOn:
          type: string
          format: date-time
          description: The date the collection was create
        name:
          type: string
          description: Name given to Collection
        slug:
          type: string
          description: Slug of Collection in Site URL structure
        singularName:
          type: string
          description: >-
            The name of one Item in Collection (e.g. “sku” if the Collection is
            called “SKU”)
        fields:
          $ref: '#/components/schemas/SKUField'
      required:
        - _id
        - name
        - slug
        - fields
      description: The SKU object
      title: SKU
    SKUList:
      type: object
      properties:
        skus:
          type: array
          items:
            $ref: '#/components/schemas/SKU'
      description: A list of SKUs
      title: SKUList
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.createSku("580e63e98c9a982ac9b8b741", "580e63fc8c9a982ac9b8b745", {
    skus: [{
            id: "66072fb71b89448912e2681c",
            cmsLocaleId: "653ad57de882f528b32e810e",
            lastPublished: new Date("2023-03-17T18:47:35.000Z"),
            lastUpdated: new Date("2023-03-17T18:47:35.000Z"),
            createdOn: new Date("2023-03-17T18:47:35.000Z"),
            fieldData: {
                name: "Colorful T-shirt - Default",
                slug: "colorful-t-shirt-default",
                price: {
                    value: 2499,
                    unit: "USD",
                    currency: "USD"
                }
            }
        }]
});

```

```python
import requests

url = "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus"

payload = {}
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

	url := "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus"

	payload := strings.NewReader("{}")

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

url = URI("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
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

HttpResponse<String> response = Unirest.post("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus")
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

$response = $client->request('POST', 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus', [
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

var client = new RestClient("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus");
var request = new RestRequest(Method.POST);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745/skus")! as URL,
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