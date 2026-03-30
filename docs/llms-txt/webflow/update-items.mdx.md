# Source: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/update-items.mdx

# Update Items

PATCH https://api.webflow.com/v2/collections/{collection_id}/items
Content-Type: application/json

Update a single item or multiple items in a Collection.

The limit for this endpoint is 100 items.

<Tip title="Localization Tip">Items will only be updated in the primary locale, unless a `cmsLocaleId` is included in the request.</Tip>

Required scope | `CMS:write`


Reference: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/update-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items:
    patch:
      operationId: update-items
      summary: Update Collection Items
      description: >
        Update a single item or multiple items in a Collection.


        The limit for this endpoint is 100 items.


        <Tip title="Localization Tip">Items will only be updated in the primary
        locale, unless a `cmsLocaleId` is included in the request.</Tip>


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
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/collections_items_update-items_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemsRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemsRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemsRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemsRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-itemsRequestInternalServerError'
      requestBody:
        description: Details of the item to update
        content:
          application/json:
            schema:
              type: object
              properties:
                items:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/CollectionsCollectionIdItemsPatchRequestBodyContentApplicationJsonSchemaItemsItems
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsCollectionIdItemsPatchRequestBodyContentApplicationJsonSchemaItemsItemsFieldData:
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
        CollectionsCollectionIdItemsPatchRequestBodyContentApplicationJsonSchemaItemsItemsFieldData
    CollectionsCollectionIdItemsPatchRequestBodyContentApplicationJsonSchemaItemsItems:
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
            #/components/schemas/CollectionsCollectionIdItemsPatchRequestBodyContentApplicationJsonSchemaItemsItemsFieldData
      required:
        - id
      description: >
        The fields that define the schema for a given Item are based on the
        Collection that Item belongs to. Beyond the user defined fields, there
        are a handful of additional fields that are automatically created for
        all items
      title: >-
        CollectionsCollectionIdItemsPatchRequestBodyContentApplicationJsonSchemaItemsItems
    CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf0FieldData:
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
        CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf0FieldData
    CollectionsItemsUpdateItemsResponse2000:
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
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf0FieldData
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
      title: CollectionsItemsUpdateItemsResponse2000
    CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1ItemsItemsFieldData:
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
        CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1ItemsItemsFieldData
    CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1ItemsItems:
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
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1ItemsItemsFieldData
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
        CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1ItemsItems
    CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1Pagination:
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
        CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1Pagination
    CollectionsItemsUpdateItemsResponse2001:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1ItemsItems
          description: List of Items within the collection
        pagination:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaOneOf1Pagination
      description: Results from collection items list
      title: CollectionsItemsUpdateItemsResponse2001
    collections_items_update-items_Response_200:
      oneOf:
        - $ref: '#/components/schemas/CollectionsItemsUpdateItemsResponse2000'
        - $ref: '#/components/schemas/CollectionsItemsUpdateItemsResponse2001'
      title: collections_items_update-items_Response_200
    CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaDetailsItems
    Update-itemsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemsRequestBadRequestError
    Update-itemsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemsRequestUnauthorizedError
    Update-itemsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemsRequestNotFoundError
    Update-itemsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemsRequestTooManyRequestsError
    Update-itemsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-itemsRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python LocalizedItems
from webflow import (
    CollectionItemWithIdInput,
    CollectionItemWithIdInputFieldData,
    Webflow,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.update_items(
    collection_id="580e63fc8c9a982ac9b8b745",
    skip_invalid_files=True,
    items=[
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5ea6",
            cms_locale_id="66f6e966c9e1dc700a857ca5",
            field_data=CollectionItemWithIdInputFieldData(
                name="Ne Paniquez Pas",
                slug="ne-paniquez-pas",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5ea6",
            cms_locale_id="66f6e966c9e1dc700a857ca4",
            field_data=CollectionItemWithIdInputFieldData(
                name="No Entrar en Pánico",
                slug="no-entrar-en-panico",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5eaa",
            cms_locale_id="66f6e966c9e1dc700a857ca5",
            field_data=CollectionItemWithIdInputFieldData(
                name="Au Revoir et Merci pour Tous les Poissons",
                slug="au-revoir-et-merci",
            ),
        ),
        CollectionItemWithIdInput(
            id="66f6ed9576ddacf3149d5eaa",
            cms_locale_id="66f6e966c9e1dc700a857ca4",
            field_data=CollectionItemWithIdInputFieldData(
                name="Hasta Luego y Gracias por Todo el Pescado",
                slug="hasta-luego-y-gracias",
            ),
        ),
    ],
)

```

```typescript LocalizedItems
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.updateItems("580e63fc8c9a982ac9b8b745", {
    skipInvalidFiles: true,
    items: [{
            id: "66f6ed9576ddacf3149d5ea6",
            cmsLocaleId: "66f6e966c9e1dc700a857ca5",
            fieldData: {
                name: "Ne Paniquez Pas",
                slug: "ne-paniquez-pas",
                featured: false
            }
        }, {
            id: "66f6ed9576ddacf3149d5ea6",
            cmsLocaleId: "66f6e966c9e1dc700a857ca4",
            fieldData: {
                name: "No Entrar en P\u00E1nico",
                slug: "no-entrar-en-panico",
                featured: false
            }
        }, {
            id: "66f6ed9576ddacf3149d5eaa",
            cmsLocaleId: "66f6e966c9e1dc700a857ca5",
            fieldData: {
                name: "Au Revoir et Merci pour Tous les Poissons",
                slug: "au-revoir-et-merci",
                featured: false
            }
        }, {
            id: "66f6ed9576ddacf3149d5eaa",
            cmsLocaleId: "66f6e966c9e1dc700a857ca4",
            fieldData: {
                name: "Hasta Luego y Gracias por Todo el Pescado",
                slug: "hasta-luego-y-gracias",
                featured: false
            }
        }]
});

```

```go LocalizedItems
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true"

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Ne Paniquez Pas\",\n        \"slug\": \"ne-paniquez-pas\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"No Entrar en Pánico\",\n        \"slug\": \"no-entrar-en-panico\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Au Revoir et Merci pour Tous les Poissons\",\n        \"slug\": \"au-revoir-et-merci\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"Hasta Luego y Gracias por Todo el Pescado\",\n        \"slug\": \"hasta-luego-y-gracias\",\n        \"featured\": false\n      }\n    }\n  ]\n}")

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

```ruby LocalizedItems
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Ne Paniquez Pas\",\n        \"slug\": \"ne-paniquez-pas\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"No Entrar en Pánico\",\n        \"slug\": \"no-entrar-en-panico\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Au Revoir et Merci pour Tous les Poissons\",\n        \"slug\": \"au-revoir-et-merci\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"Hasta Luego y Gracias por Todo el Pescado\",\n        \"slug\": \"hasta-luego-y-gracias\",\n        \"featured\": false\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java LocalizedItems
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Ne Paniquez Pas\",\n        \"slug\": \"ne-paniquez-pas\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"No Entrar en Pánico\",\n        \"slug\": \"no-entrar-en-panico\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Au Revoir et Merci pour Tous les Poissons\",\n        \"slug\": \"au-revoir-et-merci\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"Hasta Luego y Gracias por Todo el Pescado\",\n        \"slug\": \"hasta-luego-y-gracias\",\n        \"featured\": false\n      }\n    }\n  ]\n}")
  .asString();
```

```php LocalizedItems
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true', [
  'body' => '{
  "items": [
    {
      "id": "66f6ed9576ddacf3149d5ea6",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca5",
      "fieldData": {
        "name": "Ne Paniquez Pas",
        "slug": "ne-paniquez-pas",
        "featured": false
      }
    },
    {
      "id": "66f6ed9576ddacf3149d5ea6",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca4",
      "fieldData": {
        "name": "No Entrar en Pánico",
        "slug": "no-entrar-en-panico",
        "featured": false
      }
    },
    {
      "id": "66f6ed9576ddacf3149d5eaa",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca5",
      "fieldData": {
        "name": "Au Revoir et Merci pour Tous les Poissons",
        "slug": "au-revoir-et-merci",
        "featured": false
      }
    },
    {
      "id": "66f6ed9576ddacf3149d5eaa",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca4",
      "fieldData": {
        "name": "Hasta Luego y Gracias por Todo el Pescado",
        "slug": "hasta-luego-y-gracias",
        "featured": false
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

```csharp LocalizedItems
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Ne Paniquez Pas\",\n        \"slug\": \"ne-paniquez-pas\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5ea6\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"No Entrar en Pánico\",\n        \"slug\": \"no-entrar-en-panico\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca5\",\n      \"fieldData\": {\n        \"name\": \"Au Revoir et Merci pour Tous les Poissons\",\n        \"slug\": \"au-revoir-et-merci\",\n        \"featured\": false\n      }\n    },\n    {\n      \"id\": \"66f6ed9576ddacf3149d5eaa\",\n      \"cmsLocaleId\": \"66f6e966c9e1dc700a857ca4\",\n      \"fieldData\": {\n        \"name\": \"Hasta Luego y Gracias por Todo el Pescado\",\n        \"slug\": \"hasta-luego-y-gracias\",\n        \"featured\": false\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift LocalizedItems
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["items": [
    [
      "id": "66f6ed9576ddacf3149d5ea6",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca5",
      "fieldData": [
        "name": "Ne Paniquez Pas",
        "slug": "ne-paniquez-pas",
        "featured": false
      ]
    ],
    [
      "id": "66f6ed9576ddacf3149d5ea6",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca4",
      "fieldData": [
        "name": "No Entrar en Pánico",
        "slug": "no-entrar-en-panico",
        "featured": false
      ]
    ],
    [
      "id": "66f6ed9576ddacf3149d5eaa",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca5",
      "fieldData": [
        "name": "Au Revoir et Merci pour Tous les Poissons",
        "slug": "au-revoir-et-merci",
        "featured": false
      ]
    ],
    [
      "id": "66f6ed9576ddacf3149d5eaa",
      "cmsLocaleId": "66f6e966c9e1dc700a857ca4",
      "fieldData": [
        "name": "Hasta Luego y Gracias por Todo el Pescado",
        "slug": "hasta-luego-y-gracias",
        "featured": false
      ]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true")! as URL,
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

```python MultipleItems
from webflow import (
    CollectionItemWithIdInput,
    CollectionItemWithIdInputFieldData,
    Webflow,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.update_items(
    collection_id="580e63fc8c9a982ac9b8b745",
    skip_invalid_files=True,
    items=[
        CollectionItemWithIdInput(
            id="580e64008c9a982ac9b8b754",
            is_archived=False,
            is_draft=False,
            field_data=CollectionItemWithIdInputFieldData(
                name="Senior Data Analyst",
                slug="senior-data-analyst",
            ),
        ),
        CollectionItemWithIdInput(
            id="580e64008c9a982ac9b8b754",
            is_archived=False,
            is_draft=False,
            field_data=CollectionItemWithIdInputFieldData(
                name="Product Manager",
                slug="product-manager",
            ),
        ),
    ],
)

```

```typescript MultipleItems
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.updateItems("580e63fc8c9a982ac9b8b745", {
    skipInvalidFiles: true,
    items: [{
            id: "580e64008c9a982ac9b8b754",
            isArchived: false,
            isDraft: false,
            fieldData: {
                name: "Senior Data Analyst",
                slug: "senior-data-analyst",
                url: "https://boards.greenhouse.io/webflow/jobs/26567701",
                department: "Data"
            }
        }, {
            id: "580e64008c9a982ac9b8b754",
            isArchived: false,
            isDraft: false,
            fieldData: {
                name: "Product Manager",
                slug: "product-manager",
                url: "https://boards.greenhouse.io/webflow/jobs/31234567",
                department: "Product"
            }
        }]
});

```

```go MultipleItems
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true"

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}")

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

```ruby MultipleItems
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java MultipleItems
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}")
  .asString();
```

```php MultipleItems
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true', [
  'body' => '{
  "items": [
    {
      "id": "580e64008c9a982ac9b8b754",
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
      "id": "580e64008c9a982ac9b8b754",
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

```csharp MultipleItems
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Senior Data Analyst\",\n        \"slug\": \"senior-data-analyst\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/26567701\",\n        \"department\": \"Data\"\n      }\n    },\n    {\n      \"id\": \"580e64008c9a982ac9b8b754\",\n      \"isArchived\": false,\n      \"isDraft\": false,\n      \"fieldData\": {\n        \"name\": \"Product Manager\",\n        \"slug\": \"product-manager\",\n        \"url\": \"https://boards.greenhouse.io/webflow/jobs/31234567\",\n        \"department\": \"Product\"\n      }\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift MultipleItems
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["items": [
    [
      "id": "580e64008c9a982ac9b8b754",
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
      "id": "580e64008c9a982ac9b8b754",
      "isArchived": false,
      "isDraft": false,
      "fieldData": [
        "name": "Product Manager",
        "slug": "product-manager",
        "url": "https://boards.greenhouse.io/webflow/jobs/31234567",
        "department": "Product"
      ]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items?skipInvalidFiles=true")! as URL,
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