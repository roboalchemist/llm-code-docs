# Source: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/products-sk-us/get-product.mdx

# Get Product and SKUs

GET https://api.webflow.com/sites/{site_id}/products/{product_id}

Retrieve a single product by its ID. All of its SKUs will also be retrieved. The `count`, `limit`, `offset`
and `total` values in the response represent the Product only and do not include SKUs.


Reference: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/products-sk-us/get-product

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products/{product_id}:
    get:
      operationId: get-product
      summary: Get Product and SKUs
      description: >
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved. The `count`, `limit`, `offset`

        and `total` values in the response represent the Product only and do not
        include SKUs.
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
                $ref: '#/components/schemas/ProductSKUList'
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
    SKUEnum:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a product variant/option
        name:
          type: string
          description: Name of the option/variant
        slug:
          type: string
          description: slug of option/variant in Site URL structure
      description: Enumerated variant/option of a SKU
      title: SKUEnum
    SKUProperty:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for a collection of product options/variants
        name:
          type: string
          description: Nme of the collection of product options/variants
        enum:
          type: array
          items:
            $ref: '#/components/schemas/SKUEnum'
          description: >-
            The individual options/varaiants that are contained within the
            collection
      description: A variant/optiontype for a SKU
      title: SKUProperty
    ProductField:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the item
        slug:
          type: string
          default: product-name
          description: Slug of the item
        name:
          type: string
          default: Product Name
          description: item name
        _archived:
          type: boolean
          default: false
          description: item archive status
        _draft:
          type: boolean
          default: false
          description: item draft status
        sku-properties:
          type: array
          items:
            $ref: '#/components/schemas/SKUProperty'
          description: Variant/Options types to include in SKUs
      required:
        - slug
        - name
        - _archived
        - _draft
      description: Fields in your product object
      title: ProductField
    Product:
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
          description: >
            The name of one Item in Collection (e.g. “product” if the Collection
            is called “Product”)
        fields:
          $ref: '#/components/schemas/ProductField'
      required:
        - _id
      description: The Product object
      title: Product
    ProductSKUList:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: '#/components/schemas/Product'
          description: List of SKUs for a Product
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
      description: Return a Product and all associated SKUs
      title: ProductSKUList
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.get("580e63e98c9a982ac9b8b741", "580e63fc8c9a982ac9b8b745");

```

```python
import requests

url = "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745"

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

	url := "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745"

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

url = URI("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745', [
  'headers' => [
    'Accept-Version' => '1.0.0',
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")! as URL,
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