# Source: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/get-item.mdx

# Get Item

GET https://api.webflow.com/v2/collections/{collection_id}/items/{item_id}

Get details of a selected Collection Item.

Required scope | `CMS:read`


Reference: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/get-item

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
      description: |
        Get details of a selected Collection Item.

        Required scope | `CMS:read`
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
        - name: item_id
          in: path
          description: Unique identifier for an Item
          required: true
          schema:
            type: string
            format: objectid
        - name: cmsLocaleId
          in: query
          description: >-
            Unique identifier for a CMS Locale. This UID is different from the
            Site locale identifier and is listed as `cmsLocaleId` in the Sites
            response. To query multiple locales, input a comma separated string.
          required: false
          schema:
            type: string
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
                $ref: '#/components/schemas/collections_items_get-item_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-ItemRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-ItemRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-ItemRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-ItemRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-ItemRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaFieldData:
      type: object
      properties:
        name:
          type: string
          description: Name of the Item
        slug:
          type: string
          description: >-
            URL structure of the Item in your site. Note: Updates to an item
            slug will break all links referencing the old slug.
      required:
        - name
        - slug
      title: >-
        CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaFieldData
    collections_items_get-item_Response_200:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the Item
        cmsLocaleId:
          type: string
          description: Identifier for the locale of the CMS item
        lastPublished:
          type: string
          format: date-string
          description: The date the item was last published
        lastUpdated:
          type: string
          format: date-string
          description: The date the item was last updated
        createdOn:
          type: string
          format: date-string
          description: The date the item was created
        isArchived:
          type: boolean
          default: false
          description: Boolean determining if the Item is set to archived
        isDraft:
          type: boolean
          default: false
          description: Boolean determining if the Item is set to draft
        fieldData:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaFieldData
      required:
        - id
        - lastPublished
        - lastUpdated
        - createdOn
        - fieldData
      description: >
        A Collection Item represents a single entry in your collection. Each
        item includes:


        - **System metadata** - Automatically managed fields like IDs and
        timestamp <br/>

        - **Status flags** - Controls for managing content state: `isDraft`,
        `isArchived `<br/>

        - **Content fields** - Stored in `fieldData`. Each item needs a `name`
        and `slug`, and may include additional fields matching your collection's
        schema definition.
      title: collections_items_get-item_Response_200
    CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-ItemRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-ItemRequestBadRequestError
    Get-ItemRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-ItemRequestUnauthorizedError
    Get-ItemRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-ItemRequestNotFoundError
    Get-ItemRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-ItemRequestTooManyRequestsError
    Get-ItemRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-ItemRequestInternalServerError
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
client.collections.items.get_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
    cms_locale_id="cmsLocaleId",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.getItem("580e63fc8c9a982ac9b8b745", "580e64008c9a982ac9b8b754", {
    cmsLocaleId: "cmsLocaleId"
});

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754")! as URL,
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