# Source: https://developers.webflow.com/data/reference/custom-code/custom-code-pages/upsert-custom-code.mdx

# Add/Update Custom Code

PUT https://api.webflow.com/v2/pages/{page_id}/custom_code
Content-Type: application/json

Apply registered scripts to a page. If you have multiple scripts your App needs to apply or maintain on a page, ensure they are always included in the request body for this endpoint. To remove individual scripts, simply call this endpoint without the script in the request body.

<Note title="Script Registration">
  To apply a script to a page, the script must first be registered to a Site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:write`


Reference: https://developers.webflow.com/data/reference/custom-code/custom-code-pages/upsert-custom-code

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /pages/{page_id}/custom_code:
    put:
      operationId: upsert-custom-code
      summary: Add/Update Custom Code
      description: >
        Apply registered scripts to a page. If you have multiple scripts your
        App needs to apply or maintain on a page, ensure they are always
        included in the request body for this endpoint. To remove individual
        scripts, simply call this endpoint without the script in the request
        body.


        <Note title="Script Registration">
          To apply a script to a page, the script must first be registered to a Site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>


        Required scope | `custom_code:write`
      tags:
        - subpackage_pages.subpackage_pages/scripts
      parameters:
        - name: page_id
          in: path
          description: Unique identifier for a Page
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
                $ref: >-
                  #/components/schemas/pages_scripts_upsert-custom-code_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Add-custom-code-to-pageRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Add-custom-code-to-pageRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Add-custom-code-to-pageRequestNotFoundError
        '409':
          description: The maximum number of registered scripts has been reached.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Add-custom-code-to-pageRequestConflictError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Add-custom-code-to-pageRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Add-custom-code-to-pageRequestInternalServerError
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                scripts:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItems
                  description: A list of scripts applied to a Site or a Page
                lastUpdated:
                  type: string
                  format: date-string
                  description: Date when the Site's scripts were last updated
                createdOn:
                  type: string
                  format: date-string
                  description: Date when the Site's scripts were created
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItemsLocation:
      type: string
      enum:
        - header
        - footer
      default: header
      description: >-
        Location of the script, either in the header or footer of the published
        site
      title: >-
        PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItemsLocation
    PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItemsAttributes:
      type: object
      properties: {}
      description: >-
        Developer-specified key/value pairs to be applied as attributes to the
        script
      title: >-
        PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItemsAttributes
    PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItems:
      type: object
      properties:
        id:
          type: string
          format: objectId
          description: ID of the registered custom code script
        location:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItemsLocation
          description: >-
            Location of the script, either in the header or footer of the
            published site
        version:
          type: string
          description: Semantic Version String for the registered script *e.g. 0.0.1*
        attributes:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItemsAttributes
          description: >-
            Developer-specified key/value pairs to be applied as attributes to
            the script
      required:
        - id
        - location
        - version
      title: >-
        PagesPageIdCustomCodePutRequestBodyContentApplicationJsonSchemaScriptsItems
    PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItemsLocation:
      type: string
      enum:
        - header
        - footer
      default: header
      description: >-
        Location of the script, either in the header or footer of the published
        site
      title: >-
        PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItemsLocation
    PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItemsAttributes:
      type: object
      properties: {}
      description: >-
        Developer-specified key/value pairs to be applied as attributes to the
        script
      title: >-
        PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItemsAttributes
    PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItems:
      type: object
      properties:
        id:
          type: string
          format: objectId
          description: ID of the registered custom code script
        location:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItemsLocation
          description: >-
            Location of the script, either in the header or footer of the
            published site
        version:
          type: string
          description: Semantic Version String for the registered script *e.g. 0.0.1*
        attributes:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItemsAttributes
          description: >-
            Developer-specified key/value pairs to be applied as attributes to
            the script
      required:
        - id
        - location
        - version
      title: >-
        PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItems
    pages_scripts_upsert-custom-code_Response_200:
      type: object
      properties:
        scripts:
          type: array
          items:
            $ref: >-
              #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaScriptsItems
          description: A list of scripts applied to a Site or a Page
        lastUpdated:
          type: string
          format: date-string
          description: Date when the Site's scripts were last updated
        createdOn:
          type: string
          format: date-string
          description: Date when the Site's scripts were created
      title: pages_scripts_upsert-custom-code_Response_200
    PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode:
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
      title: PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode
    PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems
    Add-custom-code-to-pageRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Add-custom-code-to-pageRequestBadRequestError
    Add-custom-code-to-pageRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Add-custom-code-to-pageRequestUnauthorizedError
    Add-custom-code-to-pageRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Add-custom-code-to-pageRequestNotFoundError
    Add-custom-code-to-pageRequestConflictError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Add-custom-code-to-pageRequestConflictError
    Add-custom-code-to-pageRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Add-custom-code-to-pageRequestTooManyRequestsError
    Add-custom-code-to-pageRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodePutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Add-custom-code-to-pageRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import ScriptApply, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.pages.scripts.upsert_custom_code(
    page_id="63c720f9347c2139b248e552",
    scripts=[
        ScriptApply(
            id="cms_slider",
            location="header",
            version="1.0.0",
            attributes={"my-attribute": "some-value"},
        ),
        ScriptApply(
            id="alert",
            location="header",
            version="0.0.1",
        ),
    ],
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.pages.scripts.upsertCustomCode("63c720f9347c2139b248e552", {
    scripts: [{
            id: "cms_slider",
            location: "header",
            version: "1.0.0",
            attributes: {
                "my-attribute": "some-value"
            }
        }, {
            id: "alert",
            location: "header",
            version: "0.0.1"
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

	url := "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code"

	payload := strings.NewReader("{\n  \"scripts\": [\n    {\n      \"id\": \"cms_slider\",\n      \"location\": \"header\",\n      \"version\": \"1.0.0\",\n      \"attributes\": {\n        \"my-attribute\": \"some-value\"\n      }\n    },\n    {\n      \"id\": \"alert\",\n      \"location\": \"header\",\n      \"version\": \"0.0.1\"\n    }\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"scripts\": [\n    {\n      \"id\": \"cms_slider\",\n      \"location\": \"header\",\n      \"version\": \"1.0.0\",\n      \"attributes\": {\n        \"my-attribute\": \"some-value\"\n      }\n    },\n    {\n      \"id\": \"alert\",\n      \"location\": \"header\",\n      \"version\": \"0.0.1\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"scripts\": [\n    {\n      \"id\": \"cms_slider\",\n      \"location\": \"header\",\n      \"version\": \"1.0.0\",\n      \"attributes\": {\n        \"my-attribute\": \"some-value\"\n      }\n    },\n    {\n      \"id\": \"alert\",\n      \"location\": \"header\",\n      \"version\": \"0.0.1\"\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code', [
  'body' => '{
  "scripts": [
    {
      "id": "cms_slider",
      "location": "header",
      "version": "1.0.0",
      "attributes": {
        "my-attribute": "some-value"
      }
    },
    {
      "id": "alert",
      "location": "header",
      "version": "0.0.1"
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

var client = new RestClient("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"scripts\": [\n    {\n      \"id\": \"cms_slider\",\n      \"location\": \"header\",\n      \"version\": \"1.0.0\",\n      \"attributes\": {\n        \"my-attribute\": \"some-value\"\n      }\n    },\n    {\n      \"id\": \"alert\",\n      \"location\": \"header\",\n      \"version\": \"0.0.1\"\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["scripts": [
    [
      "id": "cms_slider",
      "location": "header",
      "version": "1.0.0",
      "attributes": ["my-attribute": "some-value"]
    ],
    [
      "id": "alert",
      "location": "header",
      "version": "0.0.1"
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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