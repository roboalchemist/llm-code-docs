# Source: https://developers.webflow.com/data/v2.0.0-beta/reference/cms/collection-items/staged-items/create-items.mdx

# Create Localized Collection Item(s)

POST https://api.webflow.com/beta/collections/{collection_id}/items/bulk
Content-Type: application/json

Create an item or multiple items in a CMS Collection across multiple corresponding locales.

**Notes:**
  - This endpoint can create up to 100 items in a request.
  - If the `cmsLocaleIds` parameter is undefined or empty and localization is enabled, items will only be created in the primary locale.

Required scope | `CMS:write`


Reference: https://developers.webflow.com/data/v2.0.0-beta/reference/cms/collection-items/staged-items/create-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/items/bulk:
    post:
      operationId: create-items
      summary: Create Collection Items
      description: >
        Create an item or multiple items in a CMS Collection across multiple
        corresponding locales.


        **Notes:**
          - This endpoint can create up to 100 items in a request.
          - If the `cmsLocaleIds` parameter is undefined or empty and localization is enabled, items will only be created in the primary locale.

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
        '202':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/collections_items_create-items_Response_202
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-itemsRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-itemsRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-itemsRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-itemsRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-itemsRequestInternalServerError'
      requestBody:
        description: Details of the item to create
        content:
          application/json:
            schema:
              type: object
              properties:
                cmsLocaleIds:
                  type: array
                  items:
                    type: string
                  description: >-
                    Array of identifiers for the locales where the item will be
                    created
                lastPublished:
                  type: string
                  format: date-string
                  description: The date and time when the item was last published.
                lastUpdated:
                  type: string
                  format: date-string
                  description: The date and time when the item was last updated.
                createdOn:
                  type: string
                  format: date-string
                  description: The date and time when the item was created.
                isArchived:
                  type: boolean
                  default: false
                  description: Indicates whether the item is archived.
                isDraft:
                  type: boolean
                  default: true
                  description: Indicates whether the item is in draft state.
                fieldData:
                  $ref: >-
                    #/components/schemas/CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData
servers:
  - url: https://api.webflow.com/beta
components:
  schemas:
    CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData0:
      type: object
      properties:
        name:
          type: string
          description: The name of the item.
        slug:
          type: string
          description: >-
            URL slug for the item in your site.

            Note: Updating the item slug will break all links referencing the
            old slug.
      required:
        - name
        - slug
      title: >-
        CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData0
    CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldDataOneOf1Items:
      type: object
      properties:
        name:
          type: string
          description: The name of the item.
        slug:
          type: string
          description: >-
            URL slug for the item in your site.

            Note: Updating the item slug will break all links referencing the
            old slug.
      required:
        - name
        - slug
      title: >-
        CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldDataOneOf1Items
    CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData1:
      type: array
      items:
        $ref: >-
          #/components/schemas/CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldDataOneOf1Items
      title: >-
        CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData1
    CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData:
      oneOf:
        - $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData0
        - $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData1
      title: >-
        CollectionsCollectionIdItemsBulkPostRequestBodyContentApplicationJsonSchemaFieldData
    CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaFieldData:
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
        CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaFieldData
    collections_items_create-items_Response_202:
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
        lastPublished:
          type:
            - string
            - 'null'
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
          default: true
          description: Boolean determining if the Item is set to draft
        fieldData:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaFieldData
      required:
        - id
      description: >
        A list of new Collection Items that will be created in the draft state.


        A Collection Item represents a single entry in your collection. Each
        item includes:


        - **System metadata** - Automatically managed fields like IDs and
        timestamp <br/>

        - **Status flags** - Controls for managing content state: `isDraft`,
        `isArchived `<br/>

        - **Content fields** - Stored in `fieldData`. Each item needs a `name`
        and `slug`, and may include additional fields matching your collection's
        schema definition.
      title: collections_items_create-items_Response_202
    CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaDetailsItems
    Create-itemsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-itemsRequestBadRequestError
    Create-itemsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-itemsRequestUnauthorizedError
    Create-itemsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-itemsRequestNotFoundError
    Create-itemsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-itemsRequestTooManyRequestsError
    Create-itemsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdItemsBulkPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-itemsRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python Single item created across multiple locales
import requests

url = "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.json())
```

```javascript Single item created across multiple locales
const url = 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: undefined
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Single item created across multiple locales
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

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

```ruby Single item created across multiple locales
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'

response = http.request(request)
puts response.read_body
```

```java Single item created across multiple locales
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .asString();
```

```php Single item created across multiple locales
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Single item created across multiple locales
using RestSharp;

var client = new RestClient("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
IRestResponse response = client.Execute(request);
```

```swift Single item created across multiple locales
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")! as URL,
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

```python Multiple items created across multiple locales
import requests

url = "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers)

print(response.json())
```

```javascript Multiple items created across multiple locales
const url = 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: undefined
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Multiple items created across multiple locales
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

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

```ruby Multiple items created across multiple locales
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'

response = http.request(request)
puts response.read_body
```

```java Multiple items created across multiple locales
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .asString();
```

```php Multiple items created across multiple locales
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Multiple items created across multiple locales
using RestSharp;

var client = new RestClient("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
IRestResponse response = client.Execute(request);
```

```swift Multiple items created across multiple locales
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")! as URL,
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

```python Create a single item across multiple locales
import requests

url = "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

payload = {
    "cmsLocaleIds": ["66f6e966c9e1dc700a857ca3", "66f6e966c9e1dc700a857ca4", "66f6e966c9e1dc700a857ca5"],
    "isArchived": False,
    "isDraft": True,
    "fieldData": {
        "name": "Don’t Panic",
        "slug": "dont-panic"
    }
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript Create a single item across multiple locales
const url = 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"cmsLocaleIds":["66f6e966c9e1dc700a857ca3","66f6e966c9e1dc700a857ca4","66f6e966c9e1dc700a857ca5"],"isArchived":false,"isDraft":true,"fieldData":{"name":"Don’t Panic","slug":"dont-panic"}}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Create a single item across multiple locales
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

	payload := strings.NewReader("{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\",\n    \"66f6e966c9e1dc700a857ca5\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": {\n    \"name\": \"Don’t Panic\",\n    \"slug\": \"dont-panic\"\n  }\n}")

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

```ruby Create a single item across multiple locales
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\",\n    \"66f6e966c9e1dc700a857ca5\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": {\n    \"name\": \"Don’t Panic\",\n    \"slug\": \"dont-panic\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java Create a single item across multiple locales
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\",\n    \"66f6e966c9e1dc700a857ca5\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": {\n    \"name\": \"Don’t Panic\",\n    \"slug\": \"dont-panic\"\n  }\n}")
  .asString();
```

```php Create a single item across multiple locales
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk', [
  'body' => '{
  "cmsLocaleIds": [
    "66f6e966c9e1dc700a857ca3",
    "66f6e966c9e1dc700a857ca4",
    "66f6e966c9e1dc700a857ca5"
  ],
  "isArchived": false,
  "isDraft": true,
  "fieldData": {
    "name": "Don’t Panic",
    "slug": "dont-panic"
  }
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Create a single item across multiple locales
using RestSharp;

var client = new RestClient("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\",\n    \"66f6e966c9e1dc700a857ca5\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": {\n    \"name\": \"Don’t Panic\",\n    \"slug\": \"dont-panic\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Create a single item across multiple locales
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "cmsLocaleIds": ["66f6e966c9e1dc700a857ca3", "66f6e966c9e1dc700a857ca4", "66f6e966c9e1dc700a857ca5"],
  "isArchived": false,
  "isDraft": true,
  "fieldData": [
    "name": "Don’t Panic",
    "slug": "dont-panic"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")! as URL,
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

```python Create multiple items across multiple locales
import requests

url = "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

payload = {
    "cmsLocaleIds": ["66f6e966c9e1dc700a857ca3", "66f6e966c9e1dc700a857ca4"],
    "isArchived": False,
    "isDraft": True,
    "fieldData": [
        {
            "name": "Don't Panic",
            "slug": "dont-panic"
        },
        {
            "name": "So Long and Thanks for All the Fish",
            "slug": "so-long-and-thanks"
        }
    ]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript Create multiple items across multiple locales
const url = 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"cmsLocaleIds":["66f6e966c9e1dc700a857ca3","66f6e966c9e1dc700a857ca4"],"isArchived":false,"isDraft":true,"fieldData":[{"name":"Don\'t Panic","slug":"dont-panic"},{"name":"So Long and Thanks for All the Fish","slug":"so-long-and-thanks"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Create multiple items across multiple locales
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk"

	payload := strings.NewReader("{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": [\n    {\n      \"name\": \"Don't Panic\",\n      \"slug\": \"dont-panic\"\n    },\n    {\n      \"name\": \"So Long and Thanks for All the Fish\",\n      \"slug\": \"so-long-and-thanks\"\n    }\n  ]\n}")

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

```ruby Create multiple items across multiple locales
require 'uri'
require 'net/http'

url = URI("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": [\n    {\n      \"name\": \"Don't Panic\",\n      \"slug\": \"dont-panic\"\n    },\n    {\n      \"name\": \"So Long and Thanks for All the Fish\",\n      \"slug\": \"so-long-and-thanks\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java Create multiple items across multiple locales
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": [\n    {\n      \"name\": \"Don't Panic\",\n      \"slug\": \"dont-panic\"\n    },\n    {\n      \"name\": \"So Long and Thanks for All the Fish\",\n      \"slug\": \"so-long-and-thanks\"\n    }\n  ]\n}")
  .asString();
```

```php Create multiple items across multiple locales
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk', [
  'body' => '{
  "cmsLocaleIds": [
    "66f6e966c9e1dc700a857ca3",
    "66f6e966c9e1dc700a857ca4"
  ],
  "isArchived": false,
  "isDraft": true,
  "fieldData": [
    {
      "name": "Don\'t Panic",
      "slug": "dont-panic"
    },
    {
      "name": "So Long and Thanks for All the Fish",
      "slug": "so-long-and-thanks"
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

```csharp Create multiple items across multiple locales
using RestSharp;

var client = new RestClient("https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"cmsLocaleIds\": [\n    \"66f6e966c9e1dc700a857ca3\",\n    \"66f6e966c9e1dc700a857ca4\"\n  ],\n  \"isArchived\": false,\n  \"isDraft\": true,\n  \"fieldData\": [\n    {\n      \"name\": \"Don't Panic\",\n      \"slug\": \"dont-panic\"\n    },\n    {\n      \"name\": \"So Long and Thanks for All the Fish\",\n      \"slug\": \"so-long-and-thanks\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Create multiple items across multiple locales
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "cmsLocaleIds": ["66f6e966c9e1dc700a857ca3", "66f6e966c9e1dc700a857ca4"],
  "isArchived": false,
  "isDraft": true,
  "fieldData": [
    [
      "name": "Don't Panic",
      "slug": "dont-panic"
    ],
    [
      "name": "So Long and Thanks for All the Fish",
      "slug": "so-long-and-thanks"
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/beta/collections/580e63fc8c9a982ac9b8b745/items/bulk")! as URL,
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