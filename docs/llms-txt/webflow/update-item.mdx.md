# Source: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/update-item.mdx

# Update Single Item

PATCH https://api.webflow.com/v2/collections/{collection_id}/items/{item_id}
Content-Type: application/json

Update a selected Item in a Collection.

Required scope | `CMS:write`


Reference: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/update-item

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/{item_id}:
    patch:
      operationId: update-item
      summary: Update Collection Item
      description: |
        Update a selected Item in a Collection.

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
        - name: item_id
          in: path
          description: Unique identifier for an Item
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
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/collections_items_update-item_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemRequestInternalServerError'
      requestBody:
        description: Details of the item to update
        content:
          application/json:
            schema:
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
                  description: Boolean determining if the Item is set to archived
                isDraft:
                  type: boolean
                  description: Boolean determining if the Item is set to draft
                fieldData:
                  $ref: >-
                    #/components/schemas/CollectionsCollectionIdItemsItemIdPatchRequestBodyContentApplicationJsonSchemaFieldData
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsCollectionIdItemsItemIdPatchRequestBodyContentApplicationJsonSchemaFieldData:
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
      title: >-
        CollectionsCollectionIdItemsItemIdPatchRequestBodyContentApplicationJsonSchemaFieldData
    CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaFieldData:
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
        CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaFieldData
    collections_items_update-item_Response_200:
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
            #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaFieldData
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
      title: collections_items_update-item_Response_200
    CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaDetailsItems
    Update-itemRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemRequestBadRequestError
    Update-itemRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemRequestUnauthorizedError
    Update-itemRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemRequestNotFoundError
    Update-itemRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemRequestTooManyRequestsError
    Update-itemRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsItemIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import CollectionItemPatchSingleFieldData, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.update_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    item_id="580e64008c9a982ac9b8b754",
    skip_invalid_files=True,
    is_archived=False,
    is_draft=False,
    field_data=CollectionItemPatchSingleFieldData(
        name="The Hitchhiker's Guide to the Galaxy",
        slug="hitchhikers-guide-to-the-galaxy",
    ),
)

```

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

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?skipInvalidFiles=true"

	payload := strings.NewReader("{\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"name\": \"The Hitchhiker's Guide to the Galaxy\",\n    \"slug\": \"hitchhikers-guide-to-the-galaxy\",\n    \"plain-text\": \"Don't Panic.\",\n    \"rich-text\": \"<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>\",\n    \"main-image\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n    },\n    \"image-gallery\": [\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabd\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabd_image.png\"\n      },\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n      }\n    ],\n    \"intro-video\": \"https://www.youtube.com/watch?v=aJ83KAggd-4\",\n    \"official-site\": \"https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy\",\n    \"contact-email\": \"zaphod.beeblebrox@heartofgold.gov\",\n    \"support-phone\": \"424-242-4242\",\n    \"answer-to-everything\": 42,\n    \"release-date\": \"1979-10-12T00:00:00.000Z\",\n    \"is-featured\": true,\n    \"brand-color\": \"#000000\",\n    \"category\": \"62b720ef280c7a7a3be8cabf\",\n    \"author\": \"62b720ef280c7a7a3be8cab0\",\n    \"tags\": [\n      \"62b720ef280c7a7a3be8cab1\",\n      \"62b720ef280c7a7a3be8cab2\"\n    ],\n    \"downloadable-asset\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cab3\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cab3_document.pdf\"\n    }\n  }\n}")

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

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?skipInvalidFiles=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"name\": \"The Hitchhiker's Guide to the Galaxy\",\n    \"slug\": \"hitchhikers-guide-to-the-galaxy\",\n    \"plain-text\": \"Don't Panic.\",\n    \"rich-text\": \"<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>\",\n    \"main-image\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n    },\n    \"image-gallery\": [\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabd\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabd_image.png\"\n      },\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n      }\n    ],\n    \"intro-video\": \"https://www.youtube.com/watch?v=aJ83KAggd-4\",\n    \"official-site\": \"https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy\",\n    \"contact-email\": \"zaphod.beeblebrox@heartofgold.gov\",\n    \"support-phone\": \"424-242-4242\",\n    \"answer-to-everything\": 42,\n    \"release-date\": \"1979-10-12T00:00:00.000Z\",\n    \"is-featured\": true,\n    \"brand-color\": \"#000000\",\n    \"category\": \"62b720ef280c7a7a3be8cabf\",\n    \"author\": \"62b720ef280c7a7a3be8cab0\",\n    \"tags\": [\n      \"62b720ef280c7a7a3be8cab1\",\n      \"62b720ef280c7a7a3be8cab2\"\n    ],\n    \"downloadable-asset\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cab3\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cab3_document.pdf\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?skipInvalidFiles=true")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"isArchived\": false,\n  \"isDraft\": false,\n  \"fieldData\": {\n    \"name\": \"The Hitchhiker's Guide to the Galaxy\",\n    \"slug\": \"hitchhikers-guide-to-the-galaxy\",\n    \"plain-text\": \"Don't Panic.\",\n    \"rich-text\": \"<h3>A Guide to Interstellar Travel</h3><p>A towel is about the most massively useful thing an interstellar hitchhiker can have. <strong>Don't forget yours!</strong></p>\",\n    \"main-image\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n    },\n    \"image-gallery\": [\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabd\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabd_image.png\"\n      },\n      {\n        \"fileId\": \"62b720ef280c7a7a3be8cabe\",\n        \"url\": \"/files/62b720ef280c7a7a3be8cabe_image.png\"\n      }\n    ],\n    \"intro-video\": \"https://www.youtube.com/watch?v=aJ83KAggd-4\",\n    \"official-site\": \"https://hitchhikers.fandom.com/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy\",\n    \"contact-email\": \"zaphod.beeblebrox@heartofgold.gov\",\n    \"support-phone\": \"424-242-4242\",\n    \"answer-to-everything\": 42,\n    \"release-date\": \"1979-10-12T00:00:00.000Z\",\n    \"is-featured\": true,\n    \"brand-color\": \"#000000\",\n    \"category\": \"62b720ef280c7a7a3be8cabf\",\n    \"author\": \"62b720ef280c7a7a3be8cab0\",\n    \"tags\": [\n      \"62b720ef280c7a7a3be8cab1\",\n      \"62b720ef280c7a7a3be8cab2\"\n    ],\n    \"downloadable-asset\": {\n      \"fileId\": \"62b720ef280c7a7a3be8cab3\",\n      \"url\": \"/files/62b720ef280c7a7a3be8cab3_document.pdf\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?skipInvalidFiles=true', [
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

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?skipInvalidFiles=true");
var request = new RestRequest(Method.PATCH);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/580e64008c9a982ac9b8b754?skipInvalidFiles=true")! as URL,
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