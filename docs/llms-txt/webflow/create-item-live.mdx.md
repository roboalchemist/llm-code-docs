# Source: https://developers.webflow.com/data/reference/cms/collection-items/live-items/create-item-live.mdx

# Create Live Items

POST https://api.webflow.com/v2/collections/{collection_id}/items/live
Content-Type: application/json

Create item(s) in a collection that will be immediately published to the live site.


To create items across multiple locales, [please use this endpoint.](/data/reference/cms/collection-items/staged-items/create-items)


Required scope | `CMS:write`


Reference: https://developers.webflow.com/data/reference/cms/collection-items/live-items/create-item-live

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/live:
    post:
      operationId: create-item-live
      summary: Create Live Collection Item(s)
      description: >
        Create item(s) in a collection that will be immediately published to the
        live site.



        To create items across multiple locales, [please use this
        endpoint.](/data/reference/cms/collection-items/staged-items/create-items)



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
        - name: skipInvalidFiles
          in: query
          description: >-
            When true, invalid files are skipped and processing continues. When
            false, the entire request fails if any file is invalid.
          required: false
          schema:
            type: boolean
            default: true
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '202':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/collections_items_create-item-live_Response_202
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-item-liveRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-item-liveRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-item-liveRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-item-liveRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-item-liveRequestInternalServerError
      requestBody:
        description: Details of the item(s) to create
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/collections_items_create-item-live_Request'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf0FieldData:
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
        CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf0FieldData
    CollectionsItemsCreateItemLiveRequest0:
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
            #/components/schemas/CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf0FieldData
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
      title: CollectionsItemsCreateItemLiveRequest0
    CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItemsFieldData:
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
        CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItemsFieldData
    CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItems:
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
            #/components/schemas/CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItemsFieldData
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
        CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItems
    CollectionsItemsCreateItemLiveRequest1:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsCollectionIdItemsLivePostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItems
          description: List of collection items to create
      title: CollectionsItemsCreateItemLiveRequest1
    collections_items_create-item-live_Request:
      oneOf:
        - $ref: '#/components/schemas/CollectionsItemsCreateItemLiveRequest0'
        - $ref: '#/components/schemas/CollectionsItemsCreateItemLiveRequest1'
      title: collections_items_create-item-live_Request
    CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaFieldData:
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
        CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaFieldData
    collections_items_create-item-live_Response_202:
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
            #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaFieldData
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
      title: collections_items_create-item-live_Response_202
    CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaDetailsItems
    Create-item-liveRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-item-liveRequestBadRequestError
    Create-item-liveRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-item-liveRequestUnauthorizedError
    Create-item-liveRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-item-liveRequestNotFoundError
    Create-item-liveRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-item-liveRequestTooManyRequestsError
    Create-item-liveRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsLivePostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-item-liveRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import CollectionItem, CollectionItemFieldData, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.create_item_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    skip_invalid_files=True,
    request=CollectionItem(
        is_archived=False,
        is_draft=False,
        field_data=CollectionItemFieldData(
            name="The Hitchhiker's Guide to the Galaxy",
            slug="hitchhikers-guide-to-the-galaxy",
        ),
    ),
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.createItemLive("580e63fc8c9a982ac9b8b745", {
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

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true"

	payload := strings.NewReader("{\n  \"fieldData\": {\n    \"name\": \"My new item\",\n    \"slug\": \"my-new-item\",\n    \"date\": \"2022-11-18T00:00:00.000Z\",\n    \"featured\": false,\n    \"color\": \"#db4b68\"\n  },\n  \"items\": [\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"fieldData\": {\n    \"name\": \"My new item\",\n    \"slug\": \"my-new-item\",\n    \"date\": \"2022-11-18T00:00:00.000Z\",\n    \"featured\": false,\n    \"color\": \"#db4b68\"\n  },\n  \"items\": [\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"fieldData\": {\n    \"name\": \"My new item\",\n    \"slug\": \"my-new-item\",\n    \"date\": \"2022-11-18T00:00:00.000Z\",\n    \"featured\": false,\n    \"color\": \"#db4b68\"\n  },\n  \"items\": [\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true', [
  'body' => '{
  "fieldData": {
    "name": "My new item",
    "slug": "my-new-item",
    "date": "2022-11-18T00:00:00.000Z",
    "featured": false,
    "color": "#db4b68"
  },
  "items": [
    {
      "isArchived": false,
      "isDraft": false,
      "fieldData": {
        "name": "Senior Data Analyst",
        "slug": "senior-data-analyst",
        "url": "https://boards.greenhouse.io/webflow/jobs/26567701",
        "department": "Data"
      }
    },
    {
      "isArchived": false,
      "isDraft": false,
      "fieldData": {
        "name": "Product Manager",
        "slug": "product-manager",
        "url": "https://boards.greenhouse.io/webflow/jobs/31234567",
        "department": "Product"
      }
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

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"fieldData\": {\n    \"name\": \"My new item\",\n    \"slug\": \"my-new-item\",\n    \"date\": \"2022-11-18T00:00:00.000Z\",\n    \"featured\": false,\n    \"color\": \"#db4b68\"\n  },\n  \"items\": [\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "fieldData": [
    "name": "My new item",
    "slug": "my-new-item",
    "date": "2022-11-18T00:00:00.000Z",
    "featured": false,
    "color": "#db4b68"
  ],
  "items": [
    [
      "isArchived": false,
      "isDraft": false,
      "fieldData": [
        "name": "Senior Data Analyst",
        "slug": "senior-data-analyst",
        "url": "https://boards.greenhouse.io/webflow/jobs/26567701",
        "department": "Data"
      ]
    ],
    [
      "isArchived": false,
      "isDraft": false,
      "fieldData": [
        "name": "Product Manager",
        "slug": "product-manager",
        "url": "https://boards.greenhouse.io/webflow/jobs/31234567",
        "department": "Product"
      ]
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true")! as URL,
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

```python
from webflow import CollectionItem, CollectionItemFieldData, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.create_item_live(
    collection_id="580e63fc8c9a982ac9b8b745",
    skip_invalid_files=True,
    request=CollectionItem(
        is_archived=False,
        is_draft=False,
        field_data=CollectionItemFieldData(
            name="The Hitchhiker's Guide to the Galaxy",
            slug="hitchhikers-guide-to-the-galaxy",
        ),
    ),
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.createItemLive("580e63fc8c9a982ac9b8b745", {
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

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true"

	payload := strings.NewReader("{\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"name\": \"The Hitchhiker's Guide to the Galaxy\",\n    \"slug\": \"hitchhikers-guide-to-the-galaxy\",\n    \"plain-text\": \"Don't Panic.\",\n    \"rich-text\": \"<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>\",\n    \"main-image\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n    },\n    \"image-gallery\": [\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabd\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabd_image.png\"\n      },\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n      }\n    ],\n    \"intro-video\": \"https://www.youtube.com/watch?v=aJ83KAggd-4\",\n    \"official-site\": \"https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy\",\n    \"contact-email\": \"zaphod.beeblebrox@heartofgold.gov\",\n    \"support-phone\": \"424-242-4242\",\n    \"answer-to-everything\": 42,\n    \"release-date\": \"1979-10-12T00:00:00.000Z\",\n    \"is-featured\": true,\n    \"brand-color\": \"#000000\",\n    \"category\": \"62b720ef280c7a7a3be8cabf\",\n    \"author\": \"62b720ef280c7a7a3be8cab0\",\n    \"tags\": [\n      \"62b720ef280c7a7a3be8cab1\",\n      \"62b720ef280c7a7a3be8cab2\"\n    ],\n    \"downloadable-asset\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cab3\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cab3_document.pdf\"\n    }\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"name\": \"The Hitchhiker's Guide to the Galaxy\",\n    \"slug\": \"hitchhikers-guide-to-the-galaxy\",\n    \"plain-text\": \"Don't Panic.\",\n    \"rich-text\": \"<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>\",\n    \"main-image\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n    },\n    \"image-gallery\": [\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabd\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabd_image.png\"\n      },\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n      }\n    ],\n    \"intro-video\": \"https://www.youtube.com/watch?v=aJ83KAggd-4\",\n    \"official-site\": \"https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy\",\n    \"contact-email\": \"zaphod.beeblebrox@heartofgold.gov\",\n    \"support-phone\": \"424-242-4242\",\n    \"answer-to-everything\": 42,\n    \"release-date\": \"1979-10-12T00:00:00.000Z\",\n    \"is-featured\": true,\n    \"brand-color\": \"#000000\",\n    \"category\": \"62b720ef280c7a7a3be8cabf\",\n    \"author\": \"62b720ef280c7a7a3be8cab0\",\n    \"tags\": [\n      \"62b720ef280c7a7a3be8cab1\",\n      \"62b720ef280c7a7a3be8cab2\"\n    ],\n    \"downloadable-asset\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cab3\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cab3_document.pdf\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"name\": \"The Hitchhiker's Guide to the Galaxy\",\n    \"slug\": \"hitchhikers-guide-to-the-galaxy\",\n    \"plain-text\": \"Don't Panic.\",\n    \"rich-text\": \"<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>\",\n    \"main-image\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n    },\n    \"image-gallery\": [\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabd\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabd_image.png\"\n      },\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n      }\n    ],\n    \"intro-video\": \"https://www.youtube.com/watch?v=aJ83KAggd-4\",\n    \"official-site\": \"https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy\",\n    \"contact-email\": \"zaphod.beeblebrox@heartofgold.gov\",\n    \"support-phone\": \"424-242-4242\",\n    \"answer-to-everything\": 42,\n    \"release-date\": \"1979-10-12T00:00:00.000Z\",\n    \"is-featured\": true,\n    \"brand-color\": \"#000000\",\n    \"category\": \"62b720ef280c7a7a3be8cabf\",\n    \"author\": \"62b720ef280c7a7a3be8cab0\",\n    \"tags\": [\n      \"62b720ef280c7a7a3be8cab1\",\n      \"62b720ef280c7a7a3be8cab2\"\n    ],\n    \"downloadable-asset\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cab3\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cab3_document.pdf\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true', [
  'body' => '{
  "isArchived": false,
  "isDraft": false,
  "fieldData": {
    "name": "The Hitchhiker\'s Guide to the Galaxy",
    "slug": "hitchhikers-guide-to-the-galaxy",
    "plain-text": "Don\'t Panic.",
    "rich-text": "<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don\'t forget yours!</strong></p>",
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
    "category": "62b720ef280c7a7a3be8cabf",
    "author": "62b720ef280c7a7a3be8cab0",
    "tags": [
      "62b720ef280c7a7a3be8cab1",
      "62b720ef280c7a7a3be8cab2"
    ],
    "downloadable-asset": {
      "fileId": "62b720ef280c7a7a3be8cab3",
      "url": "/files/62b720ef280c7a7a3be8cab3_document.pdf"
    }
  }
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

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"name\": \"The Hitchhiker's Guide to the Galaxy\",\n    \"slug\": \"hitchhikers-guide-to-the-galaxy\",\n    \"plain-text\": \"Don't Panic.\",\n    \"rich-text\": \"<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>\",\n    \"main-image\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n    },\n    \"image-gallery\": [\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabd\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabd_image.png\"\n      },\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n      }\n    ],\n    \"intro-video\": \"https://www.youtube.com/watch?v=aJ83KAggd-4\",\n    \"official-site\": \"https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy\",\n    \"contact-email\": \"zaphod.beeblebrox@heartofgold.gov\",\n    \"support-phone\": \"424-242-4242\",\n    \"answer-to-everything\": 42,\n    \"release-date\": \"1979-10-12T00:00:00.000Z\",\n    \"is-featured\": true,\n    \"brand-color\": \"#000000\",\n    \"category\": \"62b720ef280c7a7a3be8cabf\",\n    \"author\": \"62b720ef280c7a7a3be8cab0\",\n    \"tags\": [\n      \"62b720ef280c7a7a3be8cab1\",\n      \"62b720ef280c7a7a3be8cab2\"\n    ],\n    \"downloadable-asset\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cab3\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cab3_document.pdf\"\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "isArchived": false,
  "isDraft": false,
  "fieldData": [
    "name": "The Hitchhiker's Guide to the Galaxy",
    "slug": "hitchhikers-guide-to-the-galaxy",
    "plain-text": "Don't Panic.",
    "rich-text": "<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>",
    "main-image": [
      "fileId": "62b720ef280c7a7a3be8cabe",
      "url": "/files/62b720ef280c7a7a3be8cabe_image.png"
    ],
    "image-gallery": [
      [
        "fileId": "62b720ef280c7a7a3be8cabd",
        "url": "/files/62b720ef280c7a7a3be8cabd_image.png"
      ],
      [
        "fileId": "62b720ef280c7a7a3be8cabe",
        "url": "/files/62b720ef280c7a7a3be8cabe_image.png"
      ]
    ],
    "intro-video": "https://www.youtube.com/watch?v=aJ83KAggd-4",
    "official-site": "https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy",
    "contact-email": "zaphod.beeblebrox@heartofgold.gov",
    "support-phone": "424-242-4242",
    "answer-to-everything": 42,
    "release-date": "1979-10-12T00:00:00.000Z",
    "is-featured": true,
    "brand-color": "#000000",
    "category": "62b720ef280c7a7a3be8cabf",
    "author": "62b720ef280c7a7a3be8cab0",
    "tags": ["62b720ef280c7a7a3be8cab1", "62b720ef280c7a7a3be8cab2"],
    "downloadable-asset": [
      "fileId": "62b720ef280c7a7a3be8cab3",
      "url": "/files/62b720ef280c7a7a3be8cab3_document.pdf"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/live?skipInvalidFiles=true")! as URL,
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