# Source: https://developers.webflow.com/data/reference/cms/collection-items/live-items/list-items-live.mdx

# List Live Items

GET https://api.webflow.com/v2/collections/{collection_id}/items/live

List all published items in a collection.

<Tip title="Serve data with the Content Delivery API">
  Serving data to applications in real-time? Use the Content Delivery API at `api-cdn.webflow.com` for better performance. The CDN-backed endpoint is optimized for high-volume reads, while the Data API is designed for writes and management operations.
</Tip>

Required scope | `CMS:read`


Reference: https://developers.webflow.com/data/reference/cms/collection-items/live-items/list-items-live

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/live:
    get:
      operationId: list-items-live
      summary: List Live Collection Items
      description: |
        List all published items in a collection.

        <Tip title="Serve data with the Content Delivery API">
          Serving data to applications in real-time? Use the Content Delivery API at `api-cdn.webflow.com` for better performance. The CDN-backed endpoint is optimized for high-volume reads, while the Data API is designed for writes and management operations.
        </Tip>

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
        - name: cmsLocaleId
          in: query
          description: >-
            Unique identifier for a CMS Locale. This UID is different from the
            Site locale identifier and is listed as `cmsLocaleId` in the Sites
            response. To query multiple locales, input a comma separated string.
          required: false
          schema:
            type: string
        - name: offset
          in: query
          description: >-
            Offset used for pagination if the results have more than limit
            records
          required: false
          schema:
            type: integer
        - name: limit
          in: query
          description: 'Maximum number of records to be returned (max limit: 100)'
          required: false
          schema:
            type: integer
        - name: name
          in: query
          description: Filter by the exact name of the item(s)
          required: false
          schema:
            type: string
        - name: slug
          in: query
          description: Filter by the exact slug of the item
          required: false
          schema:
            type: string
        - name: lastPublished
          in: query
          description: Filter by the last published date of the item(s)
          required: false
          schema:
            $ref: >-
              #/components/schemas/CollectionsCollectionIdItemsLiveGetParametersLastPublished
        - name: sortBy
          in: query
          description: Sort results by the provided value
          required: false
          schema:
            $ref: >-
              #/components/schemas/CollectionsCollectionIdItemsLiveGetParametersSortBy
        - name: sortOrder
          in: query
          description: Sorts the results by asc or desc
          required: false
          schema:
            $ref: >-
              #/components/schemas/CollectionsCollectionIdItemsLiveGetParametersSortOrder
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
                $ref: >-
                  #/components/schemas/collections_items_list-items-live_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-collection-items-liveRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-collection-items-liveRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-collection-items-liveRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-collection-items-liveRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-collection-items-liveRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
  - url: https://api-cdn.webflow.com/v2
components:
  schemas:
    CollectionsCollectionIdItemsLiveGetParametersLastPublished:
      type: object
      properties:
        lte:
          type: string
          format: date-time
          description: Filter items last published before this date
        gte:
          type: string
          format: date-time
          description: Filter items last published after this date
      title: CollectionsCollectionIdItemsLiveGetParametersLastPublished
    CollectionsCollectionIdItemsLiveGetParametersSortBy:
      type: string
      enum:
        - lastPublished
        - name
        - slug
      title: CollectionsCollectionIdItemsLiveGetParametersSortBy
    CollectionsCollectionIdItemsLiveGetParametersSortOrder:
      type: string
      enum:
        - asc
        - desc
      title: CollectionsCollectionIdItemsLiveGetParametersSortOrder
    CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaItemsItemsFieldData:
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
        CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaItemsItemsFieldData
    CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaItemsItems:
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
            #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaItemsItemsFieldData
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
      title: >-
        CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaItemsItems
    CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaPagination:
      type: object
      properties:
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
      title: >-
        CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaPagination
    collections_items_list-items-live_Response_200:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaItemsItems
          description: List of Items within the collection
        pagination:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaPagination
      required:
        - items
        - pagination
      description: Results from collection items list
      title: collections_items_list-items-live_Response_200
    CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaDetailsItems
    List-collection-items-liveRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-collection-items-liveRequestBadRequestError
    List-collection-items-liveRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-collection-items-liveRequestUnauthorizedError
    List-collection-items-liveRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-collection-items-liveRequestNotFoundError
    List-collection-items-liveRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-collection-items-liveRequestTooManyRequestsError
    List-collection-items-liveRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLiveGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-collection-items-liveRequestInternalServerError
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
client.collections.items.list_items_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    cms_locale_id="cmsLocaleId",
    offset=1,
    limit=1,
    name="name",
    slug="slug",
    sort_by="lastPublished",
    sort_order="asc",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.listItemsLive("580e63fc8c9a982ac9b8b745", {
    cmsLocaleId: "cmsLocaleId",
    offset: 1,
    limit: 1,
    name: "name",
    slug: "slug",
    sortBy: "lastPublished",
    sortOrder: "asc"
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

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?offset=0&limit=100"

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

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?offset=0&limit=100")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?offset=0&limit=100")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?offset=0&limit=100', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?offset=0&limit=100");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?offset=0&limit=100")! as URL,
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