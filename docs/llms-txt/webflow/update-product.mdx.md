# Source: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/products-sk-us/update-product.mdx

# Update Product

PATCH https://api.webflow.com/sites/{site_id}/products/{product_id}
Content-Type: application/json

Updating an existing Product will set the product type to `Advanced`. The product type is used to determine which Product and SKU fields are shown to users in the `Designer` and the `Editor`. Setting it to `Advanced` ensures that all Product and SKU fields will be shown. The product type can be edited in the `Designer` or the `Editor`.


Reference: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/products-sk-us/update-product

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/products/{product_id}:
    patch:
      operationId: update-product
      summary: Update Product
      description: >
        Updating an existing Product will set the product type to `Advanced`.
        The product type is used to determine which Product and SKU fields are
        shown to users in the `Designer` and the `Editor`. Setting it to
        `Advanced` ensures that all Product and SKU fields will be shown. The
        product type can be edited in the `Designer` or the `Editor`.
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
                $ref: '#/components/schemas/Product'
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
        description: The product to update
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
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.products.update("580e63e98c9a982ac9b8b741", "580e63fc8c9a982ac9b8b745");

```

```python
import requests

url = "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745"

payload = {}
headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

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

	url := "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745"

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

url = URI("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")

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

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")
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

$response = $client->request('PATCH', 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745', [
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

var client = new RestClient("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/products/580e63fc8c9a982ac9b8b745")! as URL,
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