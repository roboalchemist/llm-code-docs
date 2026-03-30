# Source: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/publish-item.mdx

# Publish Items

POST https://api.webflow.com/v2/collections/{collection_id}/items/publish
Content-Type: application/json

Publish an item or multiple items.

Required scope | `cms:write`


Reference: https://developers.webflow.com/data/reference/cms/collection-items/staged-items/publish-item

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/publish:
    post:
      operationId: publish-item
      summary: Publish Collection Item
      description: |
        Publish an item or multiple items.

        Required scope | `cms:write`
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
        '202':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/collections_items_publish-item_Response_202
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Publish-itemRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Publish-itemRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Publish-itemRequestNotFoundError'
        '409':
          description: Site is published to multiple domains at different times
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Publish-itemRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Publish-itemRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Publish-itemRequestInternalServerError'
      requestBody:
        description: An array of Item IDs
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/collections_items_publish-item_Request'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsItemsPublishItemRequest0:
      type: object
      properties:
        itemIds:
          type: array
          items:
            type: string
            format: objectid
      description: An array of Item IDs in a single locale
      title: CollectionsItemsPublishItemRequest0
    CollectionsCollectionIdItemsPublishPostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItems:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: The ID of the CMS item
        cmsLocaleIds:
          type: array
          items:
            type: string
          description: >-
            Array of identifiers for the locales where the item will be
            published
      required:
        - id
      title: >-
        CollectionsCollectionIdItemsPublishPostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItems
    CollectionsItemsPublishItemRequest1:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/CollectionsCollectionIdItemsPublishPostRequestBodyContentApplicationJsonSchemaOneOf1ItemsItems
      description: An array of Item IDs with included `cmsLocaleIds`
      title: CollectionsItemsPublishItemRequest1
    collections_items_publish-item_Request:
      oneOf:
        - $ref: '#/components/schemas/CollectionsItemsPublishItemRequest0'
        - $ref: '#/components/schemas/CollectionsItemsPublishItemRequest1'
      title: collections_items_publish-item_Request
    collections_items_publish-item_Response_202:
      type: object
      properties:
        publishedItemIds:
          type: array
          items:
            type: string
        errors:
          type: array
          items:
            type: string
      title: collections_items_publish-item_Response_202
    CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems
    Publish-itemRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Publish-itemRequestBadRequestError
    Publish-itemRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Publish-itemRequestUnauthorizedError
    Publish-itemRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Publish-itemRequestNotFoundError
    Publish-itemRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Publish-itemRequestConflictError
    Publish-itemRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Publish-itemRequestTooManyRequestsError
    Publish-itemRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsPublishPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Publish-itemRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python collections_items_publish-item_example
from webflow import Webflow
from webflow.resources.collections.resources.items import ItemIDs

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.publish_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    request=ItemIDs(
        item_ids=[
            "643fd856d66b6528195ee2ca",
            "643fd856d66b6528195ee2cb",
            "643fd856d66b6528195ee2cc",
        ],
    ),
)

```

```typescript collections_items_publish-item_example
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.publishItem("580e63fc8c9a982ac9b8b745", {
    itemIds: ["643fd856d66b6528195ee2ca", "643fd856d66b6528195ee2cb", "643fd856d66b6528195ee2cc"]
});

```

```go collections_items_publish-item_example
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish"

	req, _ := http.NewRequest("POST", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby collections_items_publish-item_example
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'

response = http.request(request)
puts response.read_body
```

```java collections_items_publish-item_example
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .asString();
```

```php collections_items_publish-item_example
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp collections_items_publish-item_example
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
IRestResponse response = client.Execute(request);
```

```swift collections_items_publish-item_example
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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

```python PrimaryLocale
from webflow import Webflow
from webflow.resources.collections.resources.items import ItemIDs

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.publish_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    request=ItemIDs(
        item_ids=[
            "643fd856d66b6528195ee2ca",
            "643fd856d66b6528195ee2cb",
            "643fd856d66b6528195ee2cc",
        ],
    ),
)

```

```typescript PrimaryLocale
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.publishItem("580e63fc8c9a982ac9b8b745", {
    itemIds: ["643fd856d66b6528195ee2ca", "643fd856d66b6528195ee2cb", "643fd856d66b6528195ee2cc"]
});

```

```go PrimaryLocale
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish"

	payload := strings.NewReader("{\n  \"itemIds\": [\n    \"643fd856d66b6528195ee2ca\",\n    \"643fd856d66b6528195ee2cb\",\n    \"643fd856d66b6528195ee2cc\"\n  ]\n}")

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

```ruby PrimaryLocale
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"itemIds\": [\n    \"643fd856d66b6528195ee2ca\",\n    \"643fd856d66b6528195ee2cb\",\n    \"643fd856d66b6528195ee2cc\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java PrimaryLocale
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"itemIds\": [\n    \"643fd856d66b6528195ee2ca\",\n    \"643fd856d66b6528195ee2cb\",\n    \"643fd856d66b6528195ee2cc\"\n  ]\n}")
  .asString();
```

```php PrimaryLocale
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish', [
  'body' => '{
  "itemIds": [
    "643fd856d66b6528195ee2ca",
    "643fd856d66b6528195ee2cb",
    "643fd856d66b6528195ee2cc"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp PrimaryLocale
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"itemIds\": [\n    \"643fd856d66b6528195ee2ca\",\n    \"643fd856d66b6528195ee2cb\",\n    \"643fd856d66b6528195ee2cc\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift PrimaryLocale
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["itemIds": ["643fd856d66b6528195ee2ca", "643fd856d66b6528195ee2cb", "643fd856d66b6528195ee2cc"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")! as URL,
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

```python SecondaryLocale
from webflow import Webflow
from webflow.resources.collections.resources.items import (
    ItemIDsWithLocales,
    ItemsPublishItemRequestItemsItemsItem,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.publish_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    request=ItemIDsWithLocales(
        items=[
            ItemsPublishItemRequestItemsItemsItem(
                id="643fd856d66b6528195ee2ca",
                cms_locale_ids=["653ad57de882f528b32e810e"],
            ),
            ItemsPublishItemRequestItemsItemsItem(
                id="643fd856d66b6528195ee2cb",
                cms_locale_ids=["653ad57de882f528b32e810e"],
            ),
            ItemsPublishItemRequestItemsItemsItem(
                id="643fd856d66b6528195ee2cc",
                cms_locale_ids=["653ad57de882f528b32e810e"],
            ),
        ],
    ),
)

```

```typescript SecondaryLocale
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.publishItem("580e63fc8c9a982ac9b8b745", {
    items: [{
            id: "643fd856d66b6528195ee2ca",
            cmsLocaleIds: ["653ad57de882f528b32e810e"]
        }, {
            id: "643fd856d66b6528195ee2cb",
            cmsLocaleIds: ["653ad57de882f528b32e810e"]
        }, {
            id: "643fd856d66b6528195ee2cc",
            cmsLocaleIds: ["653ad57de882f528b32e810e"]
        }]
});

```

```go SecondaryLocale
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish"

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cb\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cc\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    }\n  ]\n}")

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

```ruby SecondaryLocale
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cb\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cc\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java SecondaryLocale
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cb\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cc\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    }\n  ]\n}")
  .asString();
```

```php SecondaryLocale
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish', [
  'body' => '{
  "items": [
    {
      "id": "643fd856d66b6528195ee2ca",
      "cmsLocaleIds": [
        "653ad57de882f528b32e810e"
      ]
    },
    {
      "id": "643fd856d66b6528195ee2cb",
      "cmsLocaleIds": [
        "653ad57de882f528b32e810e"
      ]
    },
    {
      "id": "643fd856d66b6528195ee2cc",
      "cmsLocaleIds": [
        "653ad57de882f528b32e810e"
      ]
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

```csharp SecondaryLocale
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cb\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    },\n    {\n      \"id\": \"643fd856d66b6528195ee2cc\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\"\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift SecondaryLocale
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["items": [
    [
      "id": "643fd856d66b6528195ee2ca",
      "cmsLocaleIds": ["653ad57de882f528b32e810e"]
    ],
    [
      "id": "643fd856d66b6528195ee2cb",
      "cmsLocaleIds": ["653ad57de882f528b32e810e"]
    ],
    [
      "id": "643fd856d66b6528195ee2cc",
      "cmsLocaleIds": ["653ad57de882f528b32e810e"]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")! as URL,
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

```python MultipleLocales
from webflow import Webflow
from webflow.resources.collections.resources.items import (
    ItemIDsWithLocales,
    ItemsPublishItemRequestItemsItemsItem,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.collections.items.publish_item(
    collection_id="580e63fc8c9a982ac9b8b745",
    request=ItemIDsWithLocales(
        items=[
            ItemsPublishItemRequestItemsItemsItem(
                id="643fd856d66b6528195ee2ca",
                cms_locale_ids=[
                    "653ad57de882f528b32e810e",
                    "6514390aea353fc691d69827",
                    "65143930ea353fc691d69cd8",
                ],
            )
        ],
    ),
)

```

```typescript MultipleLocales
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.items.publishItem("580e63fc8c9a982ac9b8b745", {
    items: [{
            id: "643fd856d66b6528195ee2ca",
            cmsLocaleIds: ["653ad57de882f528b32e810e", "6514390aea353fc691d69827", "65143930ea353fc691d69cd8"]
        }]
});

```

```go MultipleLocales
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish"

	payload := strings.NewReader("{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\",\n        \"6514390aea353fc691d69827\",\n        \"65143930ea353fc691d69cd8\"\n      ]\n    }\n  ]\n}")

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

```ruby MultipleLocales
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\",\n        \"6514390aea353fc691d69827\",\n        \"65143930ea353fc691d69cd8\"\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java MultipleLocales
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\",\n        \"6514390aea353fc691d69827\",\n        \"65143930ea353fc691d69cd8\"\n      ]\n    }\n  ]\n}")
  .asString();
```

```php MultipleLocales
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish', [
  'body' => '{
  "items": [
    {
      "id": "643fd856d66b6528195ee2ca",
      "cmsLocaleIds": [
        "653ad57de882f528b32e810e",
        "6514390aea353fc691d69827",
        "65143930ea353fc691d69cd8"
      ]
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

```csharp MultipleLocales
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"items\": [\n    {\n      \"id\": \"643fd856d66b6528195ee2ca\",\n      \"cmsLocaleIds\": [\n        \"653ad57de882f528b32e810e\",\n        \"6514390aea353fc691d69827\",\n        \"65143930ea353fc691d69cd8\"\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift MultipleLocales
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["items": [
    [
      "id": "643fd856d66b6528195ee2ca",
      "cmsLocaleIds": ["653ad57de882f528b32e810e", "6514390aea353fc691d69827", "65143930ea353fc691d69cd8"]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/items/publish")! as URL,
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