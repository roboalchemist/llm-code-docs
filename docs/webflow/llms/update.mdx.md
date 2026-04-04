# Source: https://developers.webflow.com/data/reference/cms/collection-fields/update.mdx

# Update field

PATCH https://api.webflow.com/v2/collections/{collection_id}/fields/{field_id}
Content-Type: application/json

Update a custom field in a collection.

Required scope | `cms:write`


Reference: https://developers.webflow.com/data/reference/cms/collection-fields/update

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /collections/{collection_id}/fields/{field_id}:
    patch:
      operationId: update
      summary: Update Collection Field
      description: |
        Update a custom field in a collection.

        Required scope | `cms:write`
      tags:
        - subpackage_collections.subpackage_collections/fields
      parameters:
        - name: collection_id
          in: path
          description: Unique identifier for a Collection
          required: true
          schema:
            type: string
            format: objectid
        - name: field_id
          in: path
          description: Unique identifier for a Field in a collection
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
                $ref: '#/components/schemas/collections_fields_update_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-fieldRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-fieldRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-fieldRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-fieldRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-fieldRequestInternalServerError'
      requestBody:
        description: The field details to update
        content:
          application/json:
            schema:
              type: object
              properties:
                isRequired:
                  type: boolean
                  description: Define whether a field is required in a collection
                displayName:
                  type: string
                  description: The name of a field
                helpText:
                  type: string
                  description: Additional text to help anyone filling out this field
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaType:
      type: string
      enum:
        - Color
        - DateTime
        - Email
        - ExtFileRef
        - File
        - Image
        - Link
        - MultiImage
        - MultiReference
        - Number
        - Option
        - Phone
        - PlainText
        - Reference
        - RichText
        - Switch
        - VideoLink
      description: Choose these appropriate field type for your collection data
      title: >-
        CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaType
    CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaValidationsAdditionalProperties:
      oneOf:
        - type: string
        - type: number
          format: double
        - type: boolean
        - type: integer
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaValidationsAdditionalProperties
    CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaValidations:
      type: object
      properties:
        additionalProperties:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaValidationsAdditionalProperties
      description: The validations for the field
      title: >-
        CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaValidations
    collections_fields_update_Response_200:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for a Field
        isRequired:
          type: boolean
          description: define whether a field is required in a collection
        isEditable:
          type: boolean
          description: Define whether the field is editable
        type:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaType
          description: Choose these appropriate field type for your collection data
        slug:
          type: string
          description: >-
            Slug of Field in Site URL structure. Slugs should be all lowercase
            with no spaces. Any spaces will be converted to "-."
        displayName:
          type: string
          description: The name of a field
        helpText:
          type: string
          description: Additional text to help anyone filling out this field
        validations:
          oneOf:
            - $ref: >-
                #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaValidations
            - type: 'null'
          description: The validations for the field
      required:
        - id
        - isRequired
        - type
        - displayName
      description: The details of a field in a collection
      title: collections_fields_update_Response_200
    CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaCode:
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
        CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaCode
    CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaDetailsItems
    Update-fieldRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-fieldRequestBadRequestError
    Update-fieldRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-fieldRequestUnauthorizedError
    Update-fieldRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-fieldRequestNotFoundError
    Update-fieldRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-fieldRequestTooManyRequestsError
    Update-fieldRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/CollectionsCollectionIdFieldsFieldIdPatchResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-fieldRequestInternalServerError
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
client.collections.fields.update(
    collection_id="580e63fc8c9a982ac9b8b745",
    field_id="580e63fc8c9a982ac9b8b745",
    is_required=False,
    display_name="Post Body",
    help_text="Add the body of your post here",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.collections.fields.update("580e63fc8c9a982ac9b8b745", "580e63fc8c9a982ac9b8b745", {
    isRequired: false,
    displayName: "Post Body",
    helpText: "Add the body of your post here"
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

	url := "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/fields/580e63fc8c9a982ac9b8b745"

	payload := strings.NewReader("{\n  \"isRequired\": false,\n  \"displayName\": \"Post Body\",\n  \"helpText\": \"Add the body of your post here\"\n}")

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

url = URI("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/fields/580e63fc8c9a982ac9b8b745")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"isRequired\": false,\n  \"displayName\": \"Post Body\",\n  \"helpText\": \"Add the body of your post here\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/fields/580e63fc8c9a982ac9b8b745")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"isRequired\": false,\n  \"displayName\": \"Post Body\",\n  \"helpText\": \"Add the body of your post here\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/fields/580e63fc8c9a982ac9b8b745', [
  'body' => '{
  "isRequired": false,
  "displayName": "Post Body",
  "helpText": "Add the body of your post here"
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

var client = new RestClient("https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/fields/580e63fc8c9a982ac9b8b745");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"isRequired\": false,\n  \"displayName\": \"Post Body\",\n  \"helpText\": \"Add the body of your post here\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "isRequired": false,
  "displayName": "Post Body",
  "helpText": "Add the body of your post here"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/collections/580e63fc8c9a982ac9b8b745/fields/580e63fc8c9a982ac9b8b745")! as URL,
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