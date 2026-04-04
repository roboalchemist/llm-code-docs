# Source: https://developers.webflow.com/data/reference/forms/forms/list.mdx

# List Forms

GET https://api.webflow.com/v2/sites/{site_id}/forms

List forms for a given site.

Required scope | `forms:read`


Reference: https://developers.webflow.com/data/reference/forms/forms/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/forms:
    get:
      operationId: list
      summary: List Forms
      description: |
        List forms for a given site.

        Required scope | `forms:read`
      tags:
        - subpackage_forms
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: objectid
        - name: limit
          in: query
          description: 'Maximum number of records to be returned (max limit: 100)'
          required: false
          schema:
            type: integer
        - name: offset
          in: query
          description: >-
            Offset used for pagination if the results have more than limit
            records
          required: false
          schema:
            type: integer
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
                $ref: '#/components/schemas/forms_list_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-formsRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-formsRequestUnauthorizedError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-formsRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-formsRequestNotFoundError'
        '409':
          description: To access this feature, the site needs to be republished.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-formsRequestConflictError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-formsRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-formsRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsFieldsType:
      type: string
      enum:
        - Plain
        - Email
        - Password
        - Phone
        - Number
      description: The field type
      title: >-
        SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsFieldsType
    SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsFields:
      type: object
      properties:
        displayName:
          type: string
          description: The field name displayed on the site
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsFieldsType
          description: The field type
        placeholder:
          type:
            - string
            - 'null'
          description: The placeholder text for the field
        userVisible:
          type: boolean
          description: Whether the field is visible to the user
      description: An object containing field info for a specific fieldID.
      title: SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsFields
    SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsResponseSettings:
      type: object
      properties:
        redirectUrl:
          type: string
          description: The url or path to redirect the user to after form submission
        redirectMethod:
          type:
            - string
            - 'null'
          description: The HTTP request method to use for the redirectUrl (eg. POST or GET)
        redirectAction:
          type:
            - string
            - 'null'
          description: The action to take after form submission
        sendEmailConfirmation:
          type: boolean
          description: Whether to send an email confirmation to the user
      description: Settings for form responses
      title: >-
        SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsResponseSettings
    SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItems:
      type: object
      properties:
        displayName:
          type: string
          description: The Form name displayed on the site
        createdOn:
          type: string
          format: date-time
          description: Date that the Form was created on
        lastUpdated:
          type: string
          format: date-time
          description: Date that the Form was last updated on
        fields:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsFields
          description: A collection of form field objects
        responseSettings:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItemsResponseSettings
          description: Settings for form responses
        id:
          type: string
          format: objectid
          description: The unique ID for the Form
        siteId:
          type: string
          format: objectid
          description: The unique ID of the Site the Form belongs to
        siteDomainId:
          type: string
          format: objectid
          description: The unique ID corresponding to the site's Domain name
        pageId:
          type: string
          format: objectid
          description: The unique ID for the Page on which the Form is placed
        pageName:
          type: string
          description: The user-visible name of the Page where the Form is placed
        formElementId:
          type:
            - string
            - 'null'
          description: The unique ID of the Form element
        workspaceId:
          type: string
          format: objectid
          description: The unique ID of the Workspace the Site belongs to
      description: A Webflow form
      title: SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItems
    SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaPagination:
      type: object
      properties:
        limit:
          type: integer
          description: The limit used for pagination
        offset:
          type: integer
          description: The offset used for pagination
        total:
          type: integer
          description: The total number of records
      required:
        - limit
        - offset
        - total
      description: Pagination object
      title: SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaPagination
    forms_list_Response_200:
      type: object
      properties:
        forms:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaFormsItems
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      required:
        - forms
        - pagination
      description: A list of forms
      title: forms_list_Response_200
    SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
    List-formsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-formsRequestBadRequestError
    List-formsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-formsRequestUnauthorizedError
    List-formsRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-formsRequestForbiddenError
    List-formsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-formsRequestNotFoundError
    List-formsRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-formsRequestConflictError
    List-formsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-formsRequestTooManyRequestsError
    List-formsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-formsRequestInternalServerError
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
client.forms.list(
    site_id="580e63e98c9a982ac9b8b741",
    limit=1,
    offset=1,
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.forms.list("580e63e98c9a982ac9b8b741", {
    limit: 1,
    offset: 1
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/forms?limit=100&offset=0"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/forms?limit=100&offset=0")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/forms?limit=100&offset=0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/forms?limit=100&offset=0', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/forms?limit=100&offset=0");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/forms?limit=100&offset=0")! as URL,
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