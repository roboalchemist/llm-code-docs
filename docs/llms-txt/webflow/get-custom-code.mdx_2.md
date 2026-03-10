# Source: https://developers.webflow.com/data/reference/custom-code/custom-code-pages/get-custom-code.mdx

# Get Custom Code

GET https://api.webflow.com/v2/pages/{page_id}/custom_code

Get all scripts applied to a page.

Required scope | `custom_code:read`


Reference: https://developers.webflow.com/data/reference/custom-code/custom-code-pages/get-custom-code

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /pages/{page_id}/custom_code:
    get:
      operationId: get-custom-code
      summary: Get Custom Code
      description: |
        Get all scripts applied to a page.

        Required scope | `custom_code:read`
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
                  #/components/schemas/pages_scripts_get-custom-code_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-page-custom-codeRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-page-custom-codeRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-page-custom-codeRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-page-custom-codeRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-page-custom-codeRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsLocation:
      type: string
      enum:
        - header
        - footer
      default: header
      description: >-
        Location of the script, either in the header or footer of the published
        site
      title: >-
        PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsLocation
    PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsAttributes:
      type: object
      properties: {}
      description: >-
        Developer-specified key/value pairs to be applied as attributes to the
        script
      title: >-
        PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsAttributes
    PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItems:
      type: object
      properties:
        id:
          type: string
          format: objectId
          description: ID of the registered custom code script
        location:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsLocation
          description: >-
            Location of the script, either in the header or footer of the
            published site
        version:
          type: string
          description: Semantic Version String for the registered script *e.g. 0.0.1*
        attributes:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsAttributes
          description: >-
            Developer-specified key/value pairs to be applied as attributes to
            the script
      required:
        - id
        - location
        - version
      title: >-
        PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItems
    pages_scripts_get-custom-code_Response_200:
      type: object
      properties:
        scripts:
          type: array
          items:
            $ref: >-
              #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItems
          description: A list of scripts applied to a Site or a Page
        lastUpdated:
          type: string
          format: date-string
          description: Date when the Site's scripts were last updated
        createdOn:
          type: string
          format: date-string
          description: Date when the Site's scripts were created
      title: pages_scripts_get-custom-code_Response_200
    PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaCode:
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
      title: PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
    PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-page-custom-codeRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-custom-codeRequestBadRequestError
    Get-page-custom-codeRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-custom-codeRequestUnauthorizedError
    Get-page-custom-codeRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-custom-codeRequestNotFoundError
    Get-page-custom-codeRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-custom-codeRequestTooManyRequestsError
    Get-page-custom-codeRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-custom-codeRequestInternalServerError
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
client.pages.scripts.get_custom_code(
    page_id="63c720f9347c2139b248e552",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.pages.scripts.getCustomCode("63c720f9347c2139b248e552");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code"

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

url = URI("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552/custom_code")! as URL,
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