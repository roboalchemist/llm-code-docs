# Source: https://developers.webflow.com/data/reference/custom-code/custom-code/list.mdx

# Get Registered Scripts

GET https://api.webflow.com/v2/sites/{site_id}/registered_scripts

Get a list of scripts that have been registered to a site. A site can have a maximum of 800 registered scripts.

<Note title="Script Registration">
  To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:read`


Reference: https://developers.webflow.com/data/reference/custom-code/custom-code/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/registered_scripts:
    get:
      operationId: list
      summary: Get Registered Scripts
      description: >
        Get a list of scripts that have been registered to a site. A site can
        have a maximum of 800 registered scripts.


        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>


        Required scope | `custom_code:read`
      tags:
        - subpackage_scripts
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
                $ref: '#/components/schemas/scripts_list_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-scriptsRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-scriptsRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-scriptsRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-scriptsRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-scriptsRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaRegisteredScriptsItems:
      type: object
      properties:
        id:
          type: string
          description: Human readable id, derived from the user-specified display name
        canCopy:
          type: boolean
          default: false
          description: >-
            Define whether the script can be copied on site duplication and
            transfer
        displayName:
          type: string
          description: >-
            User-facing name for the script. Must be between 1 and 50
            alphanumeric characters
        hostedLocation:
          type: string
          description: URI for an externally hosted script location
        integrityHash:
          type: string
          format: hash
          description: >-
            Sub-Resource Integrity Hash. Only required for externally hosted
            scripts (passed via hostedLocation)
        createdOn:
          type: string
          format: date-string
          description: Timestamp when the script version was created
        lastUpdated:
          type: string
          format: date-string
          description: Timestamp when the script version was last updated
        version:
          type: string
          description: >-
            A Semantic Version (SemVer) string, denoting the version of the
            script
      description: Registered custom code for application
      title: >-
        SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaRegisteredScriptsItems
    SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaPagination:
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
        SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaPagination
    scripts_list_Response_200:
      type: object
      properties:
        registeredScripts:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaRegisteredScriptsItems
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      description: A list of scripts registered to the site
      title: scripts_list_Response_200
    SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-scriptsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-scriptsRequestBadRequestError
    Get-scriptsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-scriptsRequestUnauthorizedError
    Get-scriptsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-scriptsRequestNotFoundError
    Get-scriptsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-scriptsRequestTooManyRequestsError
    Get-scriptsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-scriptsRequestInternalServerError
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
client.scripts.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.scripts.list("580e63e98c9a982ac9b8b741");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts")! as URL,
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