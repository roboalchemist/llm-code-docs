# Source: https://developers.webflow.com/data/reference/pages-and-components/pages/get-content.mdx

# Get Page Content

GET https://api.webflow.com/v2/pages/{page_id}/dom

Get text and component instance content from a static page.

<Badge intent="info">Localization</Badge>

Required scope | `pages:read`


Reference: https://developers.webflow.com/data/reference/pages-and-components/pages/get-content

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /pages/{page_id}/dom:
    get:
      operationId: get-content
      summary: Get Page Content
      description: |
        Get text and component instance content from a static page.

        <Badge intent="info">Localization</Badge>

        Required scope | `pages:read`
      tags:
        - subpackage_pages
      parameters:
        - name: page_id
          in: path
          description: Unique identifier for a Page
          required: true
          schema:
            type: string
            format: objectid
        - name: localeId
          in: query
          description: >
            Unique identifier for a specific Locale.


            [Lear more about
            localization.](/data/v2.0.0/docs/working-with-localization)
          required: false
          schema:
            type: string
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
                $ref: '#/components/schemas/pages_get-content_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-static-contentRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-static-contentRequestUnauthorizedError
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-static-contentRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-static-contentRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-static-contentRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-static-contentRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Type:
      type: string
      enum:
        - text
      default: text
      description: The type of the node
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Type
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Text:
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
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Text
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems0:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Type
          description: The type of the node
        text:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf0Text
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems0
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Type:
      type: string
      enum:
        - image
      default: image
      description: The type of the node
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Type
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Image:
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
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Image
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems1:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Type
          description: The type of the node
        image:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf1Image
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems1
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2Type:
      type: string
      enum:
        - component-instance
      default: component-instance
      description: The type of the node
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2Type
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsType:
      type: string
      enum:
        - Plain Text
        - Rich Text
        - Alt Text
      description: The type of the property.
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsType
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsText:
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
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsText
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItems:
      type: object
      properties:
        propertyId:
          type: string
          description: The ID of the property.
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsType
          description: The type of the property.
        label:
          type: string
          description: The label of the property in the UI.
        text:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItemsText
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
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItems
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems2:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier of the component instance node
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2Type
          description: The type of the node
        componentId:
          type: string
          description: The unique identifier of the component
        propertyOverrides:
          type: array
          items:
            $ref: >-
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf2PropertyOverridesItems
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems2
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf3Type:
      type: string
      enum:
        - text-input
      default: text-input
      description: The type of the node
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf3Type
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems3:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf3Type
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems3
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4Type:
      type: string
      enum:
        - select
      default: select
      description: The type of the node
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4Type
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4ChoicesItems:
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
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4ChoicesItems
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems4:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4Type
          description: The type of the node
        choices:
          type: array
          items:
            $ref: >-
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf4ChoicesItems
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems4
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf5Type:
      type: string
      enum:
        - submit-button
      default: submit-button
      description: The type of the node
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf5Type
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems5:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf5Type
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems5
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf6Type:
      type: string
      enum:
        - search-button
      default: search-button
      description: The type of the node
      title: >-
        PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf6Type
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems6:
      type: object
      properties:
        id:
          type: string
          description: Node UUID
        type:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItemsOneOf6Type
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems6
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems:
      oneOf:
        - $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems0
        - $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems1
        - $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems2
        - $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems3
        - $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems4
        - $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems5
        - $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems6
      description: >
        A generic representation of a content element within the Document Object
        Model (DOM). Each node has a unique identifier and a specific type that
        determines its content structure and attributes.
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaPagination:
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaPagination
    pages_get-content_Response_200:
      type: object
      properties:
        pageId:
          type: string
          description: Page ID
        branchId:
          type:
            - string
            - 'null'
          format: objectid
          description: >-
            The unique identifier of a [specific page
            branch.](https://help.webflow.com/hc/en-us/articles/33961355506195-Page-branching)
        nodes:
          type: array
          items:
            $ref: >-
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaNodesItems
        pagination:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
        lastUpdated:
          type:
            - string
            - 'null'
          format: date-time
          description: The date the page dom was most recently updated
      description: >
        The DOM (Document Object Model) schema represents the content structure
        of a web page or component. It captures various content nodes along with
        their associated attributes. Each node has a unique identifier and can
        be of different types like text, image or component-instance. The schema
        also provides pagination details for scenarios where the content nodes
        are too many to be fetched in a single request.
      title: pages_get-content_Response_200
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode:
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
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode
    PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-static-contentRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-static-contentRequestBadRequestError
    Get-static-contentRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-static-contentRequestUnauthorizedError
    Get-static-contentRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-static-contentRequestForbiddenError
    Get-static-contentRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-static-contentRequestNotFoundError
    Get-static-contentRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-static-contentRequestTooManyRequestsError
    Get-static-contentRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdDomGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-static-contentRequestInternalServerError
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
client.pages.get_content(
    page_id="63c720f9347c2139b248e552",
    locale_id="65427cf400e02b306eaa04a0",
    limit=1,
    offset=1,
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.pages.getContent("63c720f9347c2139b248e552", {
    localeId: "65427cf400e02b306eaa04a0",
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

	url := "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/dom?localeId=65427cf400e02b306eaa04a0&limit=100&offset=0"

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

url = URI("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/dom?localeId=65427cf400e02b306eaa04a0&limit=100&offset=0")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/dom?localeId=65427cf400e02b306eaa04a0&limit=100&offset=0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/dom?localeId=65427cf400e02b306eaa04a0&limit=100&offset=0', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/dom?localeId=65427cf400e02b306eaa04a0&limit=100&offset=0");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/dom?localeId=65427cf400e02b306eaa04a0&limit=100&offset=0")! as URL,
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