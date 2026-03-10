# Source: https://developers.webflow.com/data/reference/ecommerce/inventory/update.mdx

# Update Item Inventory

PATCH https://api.webflow.com/v2/collections/{sku_collection_id}/items/{sku_id}/inventory
Content-Type: application/json

Updates the current inventory levels for a particular SKU item.

Updates may be given in one or two methods, absolutely or incrementally.
- Absolute updates are done by setting `quantity` directly.
- Incremental updates are by specifying the inventory delta in `updateQuantity` which is then added to the `quantity` stored on the server.

Required scope | `ecommerce:write`


Reference: https://developers.webflow.com/data/reference/ecommerce/inventory/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{sku_collection_id}/items/{sku_id}/inventory:
    patch:
      operationId: update
      summary: Update Item Inventory
      description: >
        Updates the current inventory levels for a particular SKU item.


        Updates may be given in one or two methods, absolutely or incrementally.

        - Absolute updates are done by setting `quantity` directly.

        - Incremental updates are by specifying the inventory delta in
        `updateQuantity` which is then added to the `quantity` stored on the
        server.


        Required scope | `ecommerce:write`
      tags:
        - subpackage_inventory
      parameters:
        - name: sku_collection_id
          in: path
          description: >-
            Unique identifier for a SKU collection. Use the List Collections API
            to find this ID.
          required: true
          schema:
            type: string
            format: objectid
        - name: sku_id
          in: path
          description: Unique identifier for a SKU
          required: true
          schema:
            type: string
            format: objectid
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/inventory_update_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-inventoryRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-inventoryRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-inventoryRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-inventoryRequestNotFoundError'
        '409':
          description: The site does not have ecommerce enabled.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-inventoryRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-inventoryRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-inventoryRequestInternalServerError
      requestBody:
        description: The updated inventory
        content:
          application/json:
            schema:
              type: object
              properties:
                inventoryType:
                  $ref: >-
                    #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchRequestBodyContentApplicationJsonSchemaInventoryType
                  description: infinite or finite
                updateQuantity:
                  type: number
                  format: double
                  description: >-
                    Adds this quantity to currently store quantity. Can be
                    negative.
                quantity:
                  type: number
                  format: double
                  description: Immediately sets quantity to this value.
              required:
                - inventoryType
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsSkuCollectionIdItemsSkuIdInventoryPatchRequestBodyContentApplicationJsonSchemaInventoryType:
      type: string
      enum:
        - infinite
        - finite
      description: infinite or finite
      title: >-
        CollectionsSkuCollectionIdItemsSkuIdInventoryPatchRequestBodyContentApplicationJsonSchemaInventoryType
    CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaInventoryType:
      type: string
      enum:
        - infinite
        - finite
      description: infinite or finite
      title: >-
        CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaInventoryType
    inventory_update_Response_200:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for a SKU item
        quantity:
          type: number
          format: double
          description: >-
            Total quantity of items remaining in inventory (if inventoryType is
            finite)
        inventoryType:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaInventoryType
          description: infinite or finite
      description: The availabile inventory for an item
      title: inventory_update_Response_200
    CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode:
      type: string
      enum:
        - bad_request
        - collection_not_found
        - conflict
        - duplicate_collection
        - duplicate_user_email
        - ecommerce_not_enabled
        - forbidden
        - forms_require_republish
        - incompatible_webhook_filter
        - internal_error
        - invalid_auth_version
        - invalid_credentials
        - invalid_domain
        - invalid_user_email
        - item_not_found
        - missing_scopes
        - no_domains
        - not_authorized
        - not_enterprise_plan_site
        - not_enterprise_plan_workspace
        - order_not_found
        - resource_not_found
        - too_many_requests
        - unsupported_version
        - unsupported_webhook_trigger_type
        - user_limit_reached
        - user_not_found
        - users_not_enabled
        - validation_error
      description: Error code
      title: >-
        CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
    CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
    Update-inventoryRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-inventoryRequestBadRequestError
    Update-inventoryRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-inventoryRequestUnauthorizedError
    Update-inventoryRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-inventoryRequestForbiddenError
    Update-inventoryRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-inventoryRequestNotFoundError
    Update-inventoryRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-inventoryRequestConflictError
    Update-inventoryRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-inventoryRequestTooManyRequestsError
    Update-inventoryRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaCode
          description: Error code
        message:
          type: string
          description: Error message
        externalReference:
          type: string
          description: Link to more information
        details:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsSkuCollectionIdItemsSkuIdInventoryPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-inventoryRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.inventory.update(
    sku_collection_id="6377a7c4b7a79608c34a46f7",
    sku_id="5e8518516e147040726cc415",
    inventory_type="infinite",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.inventory.update("6377a7c4b7a79608c34a46f7", "5e8518516e147040726cc415", {
    inventoryType: "infinite"
});

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

	url := "https://api.webflow.com/v2/collections/6377a7c4b7a79608c34a46f7/items/5e8518516e147040726cc415/inventory"

	payload := strings.NewReader("{\n  \"inventoryType\": \"finite\"\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("https://api.webflow.com/v2/collections/6377a7c4b7a79608c34a46f7/items/5e8518516e147040726cc415/inventory")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inventoryType\": \"finite\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/v2/collections/6377a7c4b7a79608c34a46f7/items/5e8518516e147040726cc415/inventory")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"inventoryType\": \"finite\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.webflow.com/v2/collections/6377a7c4b7a79608c34a46f7/items/5e8518516e147040726cc415/inventory', [
  'body' => '{
  "inventoryType": "finite"
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/6377a7c4b7a79608c34a46f7/items/5e8518516e147040726cc415/inventory");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inventoryType\": \"finite\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["inventoryType": "finite"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/6377a7c4b7a79608c34a46f7/items/5e8518516e147040726cc415/inventory")! as URL,
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