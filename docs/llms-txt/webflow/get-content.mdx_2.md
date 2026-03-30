# Source: https://developers.webflow.com/data/reference/pages-and-components/components/get-content.mdx

# Get Component Content

GET https://api.webflow.com/v2/sites/{site_id}/components/{component_id}/dom

Get static content from a component definition. This includes text nodes, image nodes, select nodes, text input nodes, submit button nodes, and nested component instances.
To retrieve dynamic content set by component properties, use the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint.

<Note>If you do not provide a Locale ID in your request, the response will return any content that can be localized from the Primary locale.</Note>

Required scope | `components:read`


Reference: https://developers.webflow.com/data/reference/pages-and-components/components/get-content

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/components/{component_id}/dom:
    get:
      operationId: get-content
      summary: Get Component Content
      description: >
        Get static content from a component definition. This includes text
        nodes, image nodes, select nodes, text input nodes, submit button nodes,
        and nested component instances.

        To retrieve dynamic content set by component properties, use the [get
        component
        properties](/data/reference/pages-and-components/components/get-properties)
        endpoint.


        <Note>If you do not provide a Locale ID in your request, the response
        will return any content that can be localized from the Primary
        locale.</Note>


        Required scope | `components:read`
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
                $ref: '#/components/schemas/components_get-content_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-component-contentRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-component-contentRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-component-contentRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-component-contentRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-component-contentRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Type:
      type: string
      enum:
        - text
      default: text
      description: The type of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Type
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Text:
      type: object
      properties:
        html:
          type:
            - string
            - 'null'
          description: The HTML content of the text node.
        text:
          type:
            - string
            - 'null'
          description: The raw text content of the text node.
      description: The text content of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Text
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems0:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Type
          description: The type of the node
        text:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Text
          description: The text content of the node
        attributes:
          type: object
          additionalProperties:
            type: string
          description: The custom attributes of the node
      required:
        - id
        - type
        - text
      description: >
        Represents text content within the DOM. It contains both the raw text
        and its HTML representation. Additional attributes can be associated
        with the text for styling or other purposes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems0
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Type:
      type: string
      enum:
        - image
      default: image
      description: The type of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Type
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Image:
      type: object
      properties:
        alt:
          type:
            - string
            - 'null'
        assetId:
          type: string
      description: The image details of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Image
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems1:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Type
          description: The type of the node
        image:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Image
          description: The image details of the node
        attributes:
          type: object
          additionalProperties:
            type: string
          description: The custom attributes of the node
      required:
        - id
        - type
        - image
      description: >
        Represents an image within the DOM. It contains details about the image,
        such as its alternative text (alt) for accessibility and an asset
        identifier for fetching the actual image resource. Additional attributes
        can be associated with the image for styling or other purposes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems1
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2Type:
      type: string
      enum:
        - component-instance
      default: component-instance
      description: The type of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2Type
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsType:
      type: string
      enum:
        - Plain Text
        - Rich Text
        - Alt Text
      description: The type of the property.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsType
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsText:
      type: object
      properties:
        html:
          type:
            - string
            - 'null'
          description: The HTML content of the text node.
        text:
          type:
            - string
            - 'null'
          description: The raw text content of the text node.
      description: >-
        Represents text content within the DOM. It contains both the raw text
        and its HTML representation.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsText
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItems:
      type: object
      properties:
        propertyId:
          type: string
          description: The ID of the property.
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsType
          description: The type of the property.
        label:
          type: string
          description: The label of the property in the UI.
        text:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsText
          description: >-
            Represents text content within the DOM. It contains both the raw
            text and its HTML representation.
      description: >
        Represents a property of a component instance in the DOM. A property
        contains a list of both the raw text and the HTML representation,
        allowing for flexibility in rendering and processing. Additional
        attributes can be associated with the text for styling or other
        purposes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItems
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems2:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the component instance node
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2Type
          description: The type of the node
        componentId:
          type: string
          description: The unique identifier of the component
        propertyOverrides:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItems
          description: >-
            List of component properties with overrides for a component
            instance.
      required:
        - id
        - type
        - componentId
        - propertyOverrides
      description: >
        Represents a component instance within the DOM. It contains details
        about the component instance, such as its type and properties.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems2
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf3Type:
      type: string
      enum:
        - text-input
      default: text-input
      description: The type of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf3Type
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems3:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf3Type
          description: The type of the node
        placeholder:
          type: string
          description: The placeholder text of the input node
        attributes:
          type: object
          additionalProperties:
            type: string
          description: The custom attributes of the node
      required:
        - id
        - type
        - placeholder
      description: >
        Represents text input and textarea elements within the DOM. It contains
        the placeholder text in the input. Additional attributes can be
        associated with the text for styling or other purposes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems3
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4Type:
      type: string
      enum:
        - select
      default: select
      description: The type of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4Type
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4ChoicesItems:
      type: object
      properties:
        value:
          type: string
          description: The value of the choice when selected.
        text:
          type: string
          description: The text to display for the choice.
      required:
        - value
        - text
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4ChoicesItems
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems4:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4Type
          description: The type of the node
        choices:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4ChoicesItems
          description: The list of choices in this select node.
        attributes:
          type: object
          additionalProperties:
            type: string
          description: The custom attributes of the node
      required:
        - id
        - type
        - choices
      description: >
        Represents select elements within the DOM. It contains the list of
        choices in the select. Additional attributes can be associated with the
        text for styling or other purposes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems4
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf5Type:
      type: string
      enum:
        - submit-button
      default: submit-button
      description: The type of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf5Type
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems5:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf5Type
          description: The type of the node
        value:
          type: string
          description: The text content of the submit button.
        waitingText:
          type: string
          description: The text to show while the form is submitting.
        attributes:
          type: object
          additionalProperties:
            type: string
          description: The custom attributes of the node
      required:
        - id
        - type
        - value
        - waitingText
      description: >
        Represents submit button elements within the DOM. It contains the text
        and waiting text of the button. Additional attributes can be associated
        with the text for styling or other purposes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems5
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf6Type:
      type: string
      enum:
        - search-button
      default: search-button
      description: The type of the node
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf6Type
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems6:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf6Type
          description: The type of the node
        value:
          type: string
          description: The text content of the search button.
        attributes:
          type: object
          additionalProperties:
            type: string
          description: The custom attributes of the node
      required:
        - id
        - type
        - value
      description: >
        Represents search button elements within the DOM. It contains the text
        of the button. Additional attributes can be associated with the text for
        styling or other purposes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems6
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems:
      oneOf:
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems0
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems1
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems2
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems3
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems4
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems5
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems6
      description: >
        A generic representation of a content element within the Document Object
        Model (DOM). Each node has a unique identifier and a specific type that
        determines its content structure and attributes.
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaPagination:
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
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaPagination
    components_get-content_Response_200:
      type: object
      properties:
        componentId:
          type: string
          description: Component ID
        nodes:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaNodesItems
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      description: >
        The Component DOM schema represents the content structure of a
        component. Similar to Page DOM, it captures various content nodes and
        their associated attributes, but specifically for a component's
        structure. Each node has a unique identifier and can contain text,
        images, select or text inputs, submit buttons, or nested component
        instances.
      title: components_get-content_Response_200
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaCode:
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
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-component-contentRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-component-contentRequestBadRequestError
    Get-component-contentRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-component-contentRequestUnauthorizedError
    Get-component-contentRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-component-contentRequestNotFoundError
    Get-component-contentRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-component-contentRequestTooManyRequestsError
    Get-component-contentRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-component-contentRequestInternalServerError
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
client.components.get_content(
    site_id="580e63e98c9a982ac9b8b741",
    component_id="8505ba55-ef72-629e-f85c-33e4b703d48b",
    locale_id="65427cf400e02b306eaa04a0",
    branch_id="68026fa68ef6dc744c75b833",
    limit=1,
    offset=1,
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.components.getContent("580e63e98c9a982ac9b8b741", "8505ba55-ef72-629e-f85c-33e4b703d48b", {
    localeId: "65427cf400e02b306eaa04a0",
    branchId: "68026fa68ef6dc744c75b833",
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833&limit=100&offset=0"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833&limit=100&offset=0")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833&limit=100&offset=0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833&limit=100&offset=0', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833&limit=100&offset=0");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833&limit=100&offset=0")! as URL,
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