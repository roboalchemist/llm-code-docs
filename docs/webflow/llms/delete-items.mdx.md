# Source: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/delete-items.mdx

# Delete Items

DELETE https://api.webflow.com/v2/collections/{collection_id}/items
Content-Type: application/json

Delete Items from a Collection.

<Tip title="Localization Tip">Items will only be deleted in the primary locale unless a `cmsLocaleId` is included in the request.</Tip>

Required scope | `CMS:write`


Reference: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/delete-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items:
    delete:
      operationId: delete-items
      summary: Delete Collection Items
      description: >
        Delete Items from a Collection.


        <Tip title="Localization Tip">Items will only be deleted in the primary
        locale unless a `cmsLocaleId` is included in the request.</Tip>


        Required scope | `CMS:write`
      tags:
        - subpackage_collections.subpackage_collections/items
      parameters:
        - name: collection_id
          in: path
          description: Unique identifier for a Collection
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
        '204':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/collections_items_delete-items_Response_204
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-itemsRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-itemsRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-itemsRequestNotFoundError'
        '409':
          description: Site is published to multiple domains at different times
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-itemsRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-itemsRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-itemsRequestInternalServerError'
      requestBody:
        description: Details of the items to delete
        content:
          application/json:
            schema:
              type: object
              properties:
                items:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/CollectionsCollectionIdItemsDeleteRequestBodyContentApplicationJsonSchemaItemsItems
              required:
                - items
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsCollectionIdItemsDeleteRequestBodyContentApplicationJsonSchemaItemsItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the Item
        cmsLocaleIds:
          type: array
          items:
            type: string
          description: Array of identifiers for the locales where the item will be created
      required:
        - id
      title: >-
        CollectionsCollectionIdItemsDeleteRequestBodyContentApplicationJsonSchemaItemsItems
    collections_items_delete-items_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: collections_items_delete-items_Response_204
    CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems
    Delete-itemsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-itemsRequestBadRequestError
    Delete-itemsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-itemsRequestUnauthorizedError
    Delete-itemsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-itemsRequestNotFoundError
    Delete-itemsRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-itemsRequestConflictError
    Delete-itemsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-itemsRequestTooManyRequestsError
    Delete-itemsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-itemsRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import Webflow
from webflow.resources.collections.resources.items import (
    ItemsDeleteItemsRequestItemsItem,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.delete_items(
    collection_id="580e63fc8c9a982ac9b8b745",
    items=[
        ItemsDeleteItemsRequestItemsItem(
            id="580e64008c9a982ac9b8b754",
        )
    ],
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.deleteItems("580e63fc8c9a982ac9b8b745", {
    items: [{
            id: "580e64008c9a982ac9b8b754"
        }]
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

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items"

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

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

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items', [
  'body' => '{
  "items": [
    {
      "id": "580e64008c9a982ac9b8b754"
    }
  ]
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

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["items": [["id": "580e64008c9a982ac9b8b754"]]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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