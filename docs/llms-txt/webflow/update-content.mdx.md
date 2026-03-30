# Source: https://developers.webflow.com/data/reference/pages-and-components/components/update-content.mdx

# Update Component Content

POST https://api.webflow.com/v2/sites/{site_id}/components/{component_id}/dom
Content-Type: application/json

This endpoint updates content within a component defintion for **secondary locales**. It supports updating up to 1000 nodes in a single request.

Before making updates:
1. Use the [get component content](/data/reference/pages-and-components/components/get-content) endpoint to identify available content nodes and their types.
2. If your component definition has a component instance nested within it, retrieve the nested component instance's properties that you'll override using the [get component properties](/data/reference/pages-and-components/components/get-properties) endpoint.
3. DOM elements may include a `data-w-id` attribute. This attribute is used by Webflow to maintain custom attributes and links across locales. Always include the original `data-w-id` value in your update requests to ensure consistent behavior across all locales.

<Note>
  This endpoint is specifically for localizing component definitions. Ensure that the specified `localeId` is a valid **secondary locale** for the site otherwise the request will fail.
</Note>

Required scope | `components:write`


Reference: https://developers.webflow.com/data/reference/pages-and-components/components/update-content

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/components/{component_id}/dom:
    post:
      operationId: update-content
      summary: Update Component Content
      description: >
        This endpoint updates content within a component defintion for
        **secondary locales**. It supports updating up to 1000 nodes in a single
        request.


        Before making updates:

        1. Use the [get component
        content](/data/reference/pages-and-components/components/get-content)
        endpoint to identify available content nodes and their types.

        2. If your component definition has a component instance nested within
        it, retrieve the nested component instance's properties that you'll
        override using the [get component
        properties](/data/reference/pages-and-components/components/get-properties)
        endpoint.

        3. DOM elements may include a `data-w-id` attribute. This attribute is
        used by Webflow to maintain custom attributes and links across locales.
        Always include the original `data-w-id` value in your update requests to
        ensure consistent behavior across all locales.


        <Note>
          This endpoint is specifically for localizing component definitions. Ensure that the specified `localeId` is a valid **secondary locale** for the site otherwise the request will fail.
        </Note>


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
                $ref: '#/components/schemas/components_update-content_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-contentRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-contentRequestUnauthorizedError
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-contentRequestForbiddenError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-contentRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-contentRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-component-contentRequestInternalServerError
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                nodes:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems
                  description: >-
                    List of DOM Nodes with the new content that will be updated
                    in each node.
              required:
                - nodes
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems0:
      type: object
      properties:
        nodeId:
          type: string
          description: Node UUID
        text:
          type: string
          description: >-
            HTML content of the node, including the HTML tag. The HTML tags must
            be the same as what's returned from the Get Content endpoint.
      required:
        - nodeId
        - text
      description: Update a text node
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems0
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItemsOneOf1PropertyOverridesItems:
      type: object
      properties:
        propertyId:
          type: string
          description: The ID of the property.
        text:
          type: string
          description: >
            The new string or HTML value used to override the component instance
            property value.

            The provided value must be compatible with the type of the component
            instance property.

            For example, attempting to override a single-line plain-text
            property with a multi-line

            value will result in an error.
      required:
        - propertyId
        - text
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItemsOneOf1PropertyOverridesItems
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems1:
      type: object
      properties:
        nodeId:
          type: string
          description: Node UUID
        propertyOverrides:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItemsOneOf1PropertyOverridesItems
          description: >-
            A list of component instance properties to override within the
            specified secondary locale.
      required:
        - nodeId
        - propertyOverrides
      description: Update text property overrides of a component instance
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems1
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItemsOneOf2ChoicesItems:
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
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItemsOneOf2ChoicesItems
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems2:
      type: object
      properties:
        nodeId:
          type: string
          description: Node UUID
        choices:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItemsOneOf2ChoicesItems
          description: The list of choices to set on the select node.
      required:
        - nodeId
        - choices
      description: Update choices on a select node
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems2
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems3:
      type: object
      properties:
        nodeId:
          type: string
          description: Node UUID
        placeholder:
          type: string
          description: The placeholder text of the input node
      required:
        - nodeId
        - placeholder
      description: Update placeholder text on a text input node
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems3
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems4:
      type: object
      properties:
        nodeId:
          type: string
          description: Node UUID
        value:
          type: string
          description: The text content of the submit button.
        waitingText:
          type: string
          description: The text to show while the form is submitting.
      required:
        - nodeId
      description: Update a submit button node
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems4
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems5:
      type: object
      properties:
        nodeId:
          type: string
          description: Node UUID
        value:
          type: string
          description: The text content of the search button.
      required:
        - nodeId
        - value
      description: Update a search button node
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems5
    SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems:
      oneOf:
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems0
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems1
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems2
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems3
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems4
        - $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems5
      title: >-
        SitesSiteIdComponentsComponentIdDomPostRequestBodyContentApplicationJsonSchemaNodesItems
    components_update-content_Response_200:
      type: object
      properties:
        errors:
          type: array
          items:
            type: string
          description: A list of error messages, if any.
      required:
        - errors
      title: components_update-content_Response_200
    SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode:
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
        SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode
    SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems
    Update-component-contentRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-contentRequestBadRequestError
    Update-component-contentRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-contentRequestUnauthorizedError
    Update-component-contentRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-contentRequestForbiddenError
    Update-component-contentRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-contentRequestNotFoundError
    Update-component-contentRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-contentRequestTooManyRequestsError
    Update-component-contentRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdComponentsComponentIdDomPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Update-component-contentRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import (
    ComponentInstanceNodePropertyOverridesWrite,
    ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem,
    Select,
    SelectNodeWriteChoicesItem,
    SubmitButtonNodeWrite,
    TextInputNodeWrite,
    TextNodeWrite,
    Webflow,
)

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.components.update_content(
    site_id="580e63e98c9a982ac9b8b741",
    component_id="8505ba55-ef72-629e-f85c-33e4b703d48b",
    locale_id="65427cf400e02b306eaa04a0",
    branch_id="68026fa68ef6dc744c75b833",
    nodes=[
        TextNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad623",
            text="<h1>The Hitchhiker's Guide to the Galaxy</h1>",
        ),
        TextNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad627",
            text="<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>",
        ),
        Select(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad635",
            choices=[
                SelectNodeWriteChoicesItem(
                    value="choice-1",
                    text="First choice",
                ),
                SelectNodeWriteChoicesItem(
                    value="choice-2",
                    text="Second choice",
                ),
            ],
        ),
        TextInputNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad642",
            placeholder="Enter something here...",
        ),
        SubmitButtonNodeWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad671",
            value="Submit",
            waiting_text="Submitting...",
        ),
        ComponentInstanceNodePropertyOverridesWrite(
            node_id="a245c12d-995b-55ee-5ec7-aa36a6cad629",
            property_overrides=[
                ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem(
                    property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
                    text="<div><h1>Time is an <em>illusion</em></h1></div>",
                ),
                ComponentInstanceNodePropertyOverridesWritePropertyOverridesItem(
                    property_id="7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
                    text="Life, the Universe and Everything",
                ),
            ],
        ),
    ],
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.components.updateContent("580e63e98c9a982ac9b8b741", "8505ba55-ef72-629e-f85c-33e4b703d48b", {
    localeId: "65427cf400e02b306eaa04a0",
    branchId: "68026fa68ef6dc744c75b833",
    nodes: [{
            nodeId: "a245c12d-995b-55ee-5ec7-aa36a6cad623",
            text: "<h1>The Hitchhiker's Guide to the Galaxy</h1>"
        }, {
            nodeId: "a245c12d-995b-55ee-5ec7-aa36a6cad627",
            text: "<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>"
        }, {
            nodeId: "a245c12d-995b-55ee-5ec7-aa36a6cad635",
            choices: [{
                    value: "choice-1",
                    text: "First choice"
                }, {
                    value: "choice-2",
                    text: "Second choice"
                }]
        }, {
            nodeId: "a245c12d-995b-55ee-5ec7-aa36a6cad642",
            placeholder: "Enter something here..."
        }, {
            nodeId: "a245c12d-995b-55ee-5ec7-aa36a6cad671",
            value: "Submit",
            waitingText: "Submitting..."
        }, {
            nodeId: "a245c12d-995b-55ee-5ec7-aa36a6cad629",
            propertyOverrides: [{
                    propertyId: "7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
                    text: "<div><h1>Time is an <em>illusion</em></h1></div>"
                }, {
                    propertyId: "7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
                    text: "Life, the Universe and Everything"
                }]
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833"

	payload := strings.NewReader("{\n  \"nodes\": [\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"<h1>The Hitchhiker's Guide to the Galaxy</h1>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad635\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"choices\": [\n        {\n          \"value\": \"choice-1\",\n          \"text\": \"First choice\"\n        },\n        {\n          \"value\": \"choice-2\",\n          \"text\": \"Second choice\"\n        }\n      ]\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad642\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"placeholder\": \"Enter something here...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad671\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"value\": \"Submit\",\n      \"waitingText\": \"Submitting...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad629\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"propertyOverrides\": [\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f0\",\n          \"text\": \"<div><h1>Time is an <em>illusion</em></h1></div>\"\n        },\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f1\",\n          \"text\": \"Life, the Universe and Everything\"\n        }\n      ]\n    }\n  ]\n}")

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"nodes\": [\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"<h1>The Hitchhiker's Guide to the Galaxy</h1>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad635\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"choices\": [\n        {\n          \"value\": \"choice-1\",\n          \"text\": \"First choice\"\n        },\n        {\n          \"value\": \"choice-2\",\n          \"text\": \"Second choice\"\n        }\n      ]\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad642\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"placeholder\": \"Enter something here...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad671\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"value\": \"Submit\",\n      \"waitingText\": \"Submitting...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad629\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"propertyOverrides\": [\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f0\",\n          \"text\": \"<div><h1>Time is an <em>illusion</em></h1></div>\"\n        },\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f1\",\n          \"text\": \"Life, the Universe and Everything\"\n        }\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"nodes\": [\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"<h1>The Hitchhiker's Guide to the Galaxy</h1>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad635\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"choices\": [\n        {\n          \"value\": \"choice-1\",\n          \"text\": \"First choice\"\n        },\n        {\n          \"value\": \"choice-2\",\n          \"text\": \"Second choice\"\n        }\n      ]\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad642\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"placeholder\": \"Enter something here...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad671\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"value\": \"Submit\",\n      \"waitingText\": \"Submitting...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad629\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"propertyOverrides\": [\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f0\",\n          \"text\": \"<div><h1>Time is an <em>illusion</em></h1></div>\"\n        },\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f1\",\n          \"text\": \"Life, the Universe and Everything\"\n        }\n      ]\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833', [
  'body' => '{
  "nodes": [
    {
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad623",
      "text": "<h1>The Hitchhiker\'s Guide to the Galaxy</h1>"
    },
    {
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad627",
      "text": "<div><h3>Don\'t Panic!</h3><p>Always know where your towel is.</p></div>"
    },
    {
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad635",
      "text": "<h1>Hello world</h1>",
      "choices": [
        {
          "value": "choice-1",
          "text": "First choice"
        },
        {
          "value": "choice-2",
          "text": "Second choice"
        }
      ]
    },
    {
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad642",
      "text": "<h1>Hello world</h1>",
      "placeholder": "Enter something here..."
    },
    {
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad671",
      "text": "<h1>Hello world</h1>",
      "value": "Submit",
      "waitingText": "Submitting..."
    },
    {
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad629",
      "text": "<h1>Hello world</h1>",
      "propertyOverrides": [
        {
          "propertyId": "7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
          "text": "<div><h1>Time is an <em>illusion</em></h1></div>"
        },
        {
          "propertyId": "7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
          "text": "Life, the Universe and Everything"
        }
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

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"nodes\": [\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad623\",\n      \"text\": \"<h1>The Hitchhiker's Guide to the Galaxy</h1>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad627\",\n      \"text\": \"<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad635\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"choices\": [\n        {\n          \"value\": \"choice-1\",\n          \"text\": \"First choice\"\n        },\n        {\n          \"value\": \"choice-2\",\n          \"text\": \"Second choice\"\n        }\n      ]\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad642\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"placeholder\": \"Enter something here...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad671\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"value\": \"Submit\",\n      \"waitingText\": \"Submitting...\"\n    },\n    {\n      \"nodeId\": \"a245c12d-995b-55ee-5ec7-aa36a6cad629\",\n      \"text\": \"<h1>Hello world</h1>\",\n      \"propertyOverrides\": [\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f0\",\n          \"text\": \"<div><h1>Time is an <em>illusion</em></h1></div>\"\n        },\n        {\n          \"propertyId\": \"7dd14c08-2e96-8d3d-2b19-b5c03642a0f1\",\n          \"text\": \"Life, the Universe and Everything\"\n        }\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["nodes": [
    [
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad623",
      "text": "<h1>The Hitchhiker's Guide to the Galaxy</h1>"
    ],
    [
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad627",
      "text": "<div><h3>Don't Panic!</h3><p>Always know where your towel is.</p></div>"
    ],
    [
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad635",
      "text": "<h1>Hello world</h1>",
      "choices": [
        [
          "value": "choice-1",
          "text": "First choice"
        ],
        [
          "value": "choice-2",
          "text": "Second choice"
        ]
      ]
    ],
    [
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad642",
      "text": "<h1>Hello world</h1>",
      "placeholder": "Enter something here..."
    ],
    [
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad671",
      "text": "<h1>Hello world</h1>",
      "value": "Submit",
      "waitingText": "Submitting..."
    ],
    [
      "nodeId": "a245c12d-995b-55ee-5ec7-aa36a6cad629",
      "text": "<h1>Hello world</h1>",
      "propertyOverrides": [
        [
          "propertyId": "7dd14c08-2e96-8d3d-2b19-b5c03642a0f0",
          "text": "<div><h1>Time is an <em>illusion</em></h1></div>"
        ],
        [
          "propertyId": "7dd14c08-2e96-8d3d-2b19-b5c03642a0f1",
          "text": "Life, the Universe and Everything"
        ]
      ]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/components/8505ba55-ef72-629e-f85c-33e4b703d48b/dom?localeId=65427cf400e02b306eaa04a0&branchId=68026fa68ef6dc744c75b833")! as URL,
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