# Source: https://developers.webflow.com/data/reference/pages-and-components/components/update-properties.mdx

# Update Component Properties

POST https://api.webflow.com/v2/sites/{site_id}/components/{component_id}/properties
Content-Type: application/json

Update the default property values of a component definition in a specificed locale.

Before making updates:
1. Use the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint to identify properties that can be updated in a secondary locale.
2. Rich Text properties may include a `data-w-id` attribute. This attribute is used by Webflow to maintain links across locales. Always include the original `data-w-id` value in your update requests to ensure consistent behavior across all locales.

<Note>The request requires a secondary locale ID. If a `localeId` is missing, the request will not be processed and will result in an error.</Note>

Required scope | `components:write`


Reference: https://developers.webflow.com/data/reference/pages-and-components/components/update-properties

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/components/{component_id}/properties:
    post:
      operationId: update-properties
      summary: Update Component Properties
      description: >
        Update the default property values of a component definition in a
        specificed locale.


        Before making updates:

        1. Use the [get component
        properties](/data/reference/pages-and-components/components/get-properties)
        endpoint to identify properties that can be updated in a secondary
        locale.

        2. Rich Text properties may include a `data-w-id` attribute. This
        attribute is used by Webflow to maintain links across locales. Always
        include the original `data-w-id` value in your update requests to ensure
        consistent behavior across all locales.


        <Note>The request requires a secondary locale ID. If a `localeId` is
        missing, the request will not be processed and will result in an
        error.</Note>


        Required scope | `components:write`
      tags:
        - subpackage_components
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: objectid
        - name: component_id
          in: path
          description: Unique identifier for a Component
          required: true
          schema:
            type: string
        - name: localeId
          in: query
          description: >
            Unique identifier for a specific Locale.


            [Lear more about
            localization.](/data/v2.0.0/docs/working-with-localization)
          required: false
          schema:
            type: string
        - name: branchId
          in: query
          description: Scope the operation to work on a specific branch.
          required: false
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
                $ref: '#/components/schemas/components_update-properties_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-propertiesRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-propertiesRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-propertiesRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-propertiesRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-propertiesRequestInternalServerError
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                properties:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostRequestBodyContentApplicationJsonSchemaItems
                  description: >-
                    A list of component properties to update within the
                    specified secondary locale.
              required:
                - properties
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdComponentsComponentIdPropertiesPostRequestBodyContentApplicationJsonSchemaItems:
      type: object
      properties:
        propertyId:
          type: string
          description: The ID of the property.
        text:
          type: string
          description: >
            The new string or HTML value used to update the component property
            in the secondary locale.


            The provided value must be compatible with the type of the component
            property.


            For example, attempting to update a single-line plain-text property
            with a multi-line

            value will result in an error.
      required:
        - propertyId
        - text
      title: >-
        SitesSiteIdComponentsComponentIdPropertiesPostRequestBodyContentApplicationJsonSchemaItems
    components_update-properties_Response_200:
      type: object
      properties:
        errors:
          type: array
          items:
            type: string
          description: A list of error messages, if any.
      required:
        - errors
      title: components_update-properties_Response_200
    SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaCode:
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
        SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaCode
    SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaDetailsItems
    Update-component-propertiesRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-propertiesRequestBadRequestError
    Update-component-propertiesRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-propertiesRequestUnauthorizedError
    Update-component-propertiesRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-propertiesRequestNotFoundError
    Update-component-propertiesRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-propertiesRequestTooManyRequestsError
    Update-component-propertiesRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdPropertiesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-propertiesRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import Webflow
from webflow.resources.components import ComponentPropertiesWritePropertiesItem

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.components.update_properties(
    site_id="580e63e98c9a982ac9b8b741",
    component_id="8505ba55-ef72-629e-f85c-33e4b703d48b",
    locale_id="65427cf400e02b306eaa04a0",
    branch_id="68026fa68ef6dc744c75b833",
    properties=[
        ComponentPropertiesWritePropertiesItem(
            property_id="a245c12d-995b-55ee-5ec7-aa36a6cad623",
            text="The Hitchhiker’s Guide to the Galaxy",
        ),
        ComponentPropertiesWritePropertiesItem(
            property_id="a245c12d-995b-55ee-5ec7-aa36a6cad627",
            text="<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>",
        ),
    ],
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.components.updateProperties("580e63e98c9a982ac9b8b741", "8505ba55-ef72-629e-f85c-33e4b703d48b", {
    localeId: "65427cf400e02b306eaa04a0",
    branchId: "68026fa68ef6dc744c75b833",
    properties: [{
            propertyId: "a245c12d-995b-55ee-5ec7-aa36a6cad623",
            text: "The Hitchhiker\u2019s Guide to the Galaxy"
        }, {
            propertyId: "a245c12d-995b-55ee-5ec7-aa36a6cad627",
            text: "<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>"
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/properties?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833"

	payload := strings.NewReader("{\n  \"properties\": [\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"The Hitchhiker’s Guide to the Galaxy\"\n    },\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>\"\n    }\n  ]\n}")

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/properties?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"properties\": [\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"The Hitchhiker’s Guide to the Galaxy\"\n    },\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/properties?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"properties\": [\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"The Hitchhiker’s Guide to the Galaxy\"\n    },\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/properties?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833', [
  'body' => '{
  "properties": [
    {
      "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad623",
      "text": "The Hitchhiker’s Guide to the Galaxy"
    },
    {
      "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad627",
      "text": "<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>"
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/properties?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"properties\": [\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"The Hitchhiker’s Guide to the Galaxy\"\n    },\n    {\n      \"propertyId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["properties": [
    [
      "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad623",
      "text": "The Hitchhiker’s Guide to the Galaxy"
    ],
    [
      "propertyId": "a245c12d-995b-55ee-5ec7-aa36a6cad627",
      "text": "<div><h3>Dont Panic!</h3><p>Always know where your towel is.</p></div>"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/properties?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833")! as URL,
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