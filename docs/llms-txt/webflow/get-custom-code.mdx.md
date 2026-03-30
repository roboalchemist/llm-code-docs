# Source: https://developers.webflow.com/data/reference/custom-code/custom-code-sites/get-custom-code.mdx

# Get Custom Code

GET https://api.webflow.com/v2/sites/{site_id}/custom_code

Get all scripts applied to a site by the App.

<Note title="Script Registration">
  To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:read`


Reference: https://developers.webflow.com/data/reference/custom-code/custom-code-sites/get-custom-code

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/custom_code:
    get:
      operationId: get-custom-code
      summary: Get Custom Code
      description: |
        Get all scripts applied to a site by the App.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        Required scope | `custom_code:read`
      tags:
        - subpackage_sites.subpackage_sites/scripts
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
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
                  #/components/schemas/sites_scripts_get-custom-code_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-codeRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-codeRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-site-custom-codeRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-codeRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-codeRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsLocation:
      type: string
      enum:
        - header
        - footer
      default: header
      description: >-
        Location of the script, either in the header or footer of the published
        site
      title: >-
        SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsLocation
    SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsAttributes:
      type: object
      properties: {}
      description: >-
        Developer-specified key/value pairs to be applied as attributes to the
        script
      title: >-
        SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsAttributes
    SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItems:
      type: object
      properties:
        id:
          type: string
          format: objectId
          description: ID of the registered custom code script
        location:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsLocation
          description: >-
            Location of the script, either in the header or footer of the
            published site
        version:
          type: string
          description: Semantic Version String for the registered script *e.g. 0.0.1*
        attributes:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItemsAttributes
          description: >-
            Developer-specified key/value pairs to be applied as attributes to
            the script
      required:
        - id
        - location
        - version
      title: >-
        SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItems
    sites_scripts_get-custom-code_Response_200:
      type: object
      properties:
        scripts:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaScriptsItems
          description: A list of scripts applied to a Site or a Page
        lastUpdated:
          type: string
          format: date-string
          description: Date when the Site's scripts were last updated
        createdOn:
          type: string
          format: date-string
          description: Date when the Site's scripts were created
      title: sites_scripts_get-custom-code_Response_200
    SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-site-custom-codeRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-codeRequestBadRequestError
    Get-site-custom-codeRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-codeRequestUnauthorizedError
    Get-site-custom-codeRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-codeRequestNotFoundError
    Get-site-custom-codeRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-codeRequestTooManyRequestsError
    Get-site-custom-codeRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-codeRequestInternalServerError
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
client.sites.scripts.get_custom_code(
    site_id="580e63e98c9a982ac9b8b741",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.scripts.getCustomCode("580e63e98c9a982ac9b8b741");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code")! as URL,
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