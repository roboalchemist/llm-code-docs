# Source: https://developers.webflow.com/data/reference/custom-code/custom-code/register-hosted.mdx

# Register Script - Hosted

POST https://api.webflow.com/v2/sites/{site_id}/registered_scripts/hosted
Content-Type: application/json

Register a hosted script to a site.

<Note title="Script Registration">
  To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:write`


Reference: https://developers.webflow.com/data/reference/custom-code/custom-code/register-hosted

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/registered_scripts/hosted:
    post:
      operationId: register-hosted
      summary: Register Script - Hosted
      description: |
        Register a hosted script to a site.

        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints. See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>

        Required scope | `custom_code:write`
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
        '201':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/scripts_register-hosted_Response_201'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Post-hosted-scriptRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Post-hosted-scriptRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Post-hosted-scriptRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Post-hosted-scriptRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Post-hosted-scriptRequestInternalServerError
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                hostedLocation:
                  type: string
                  description: URI for an externally hosted script location
                integrityHash:
                  type: string
                  format: hash
                  description: Sub-Resource Integrity Hash
                canCopy:
                  type: boolean
                  default: false
                  description: >-
                    Define whether the script can be copied on site duplication
                    and transfer
                version:
                  type: string
                  description: >-
                    A Semantic Version (SemVer) string, denoting the version of
                    the script
                displayName:
                  type: string
                  description: >-
                    User-facing name for the script. Must be between 1 and 50
                    alphanumeric characters
              required:
                - hostedLocation
                - integrityHash
                - version
                - displayName
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    scripts_register-hosted_Response_201:
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
      title: scripts_register-hosted_Response_201
    SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaCode:
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
        SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaCode
    SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaDetailsItems
    Post-hosted-scriptRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Post-hosted-scriptRequestBadRequestError
    Post-hosted-scriptRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Post-hosted-scriptRequestUnauthorizedError
    Post-hosted-scriptRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Post-hosted-scriptRequestNotFoundError
    Post-hosted-scriptRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Post-hosted-scriptRequestTooManyRequestsError
    Post-hosted-scriptRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRegisteredScriptsHostedPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Post-hosted-scriptRequestInternalServerError
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
client.scripts.register_hosted(
    site_id="580e63e98c9a982ac9b8b741",
    hosted_location="hostedLocation",
    integrity_hash="integrityHash",
    version="version",
    display_name="displayName",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.scripts.registerHosted("580e63e98c9a982ac9b8b741", {
    hostedLocation: "hostedLocation",
    integrityHash: "integrityHash",
    version: "version",
    displayName: "displayName"
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts/hosted"

	payload := strings.NewReader("{\n  \"hostedLocation\": \"https://cdn.jsdelivr.net/.../cmsslider.js\",\n  \"integrityHash\": \"sha384-J+YlJ8v0gpaRoKH7SbFbEmxOZlAxLiwNjfSsBhDooGa5roXlPPpXbEevck4J7YZ+\",\n  \"version\": \"1.0.0\",\n  \"displayName\": \"CMS Slider\",\n  \"canCopy\": true\n}")

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts/hosted")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"hostedLocation\": \"https://cdn.jsdelivr.net/.../cmsslider.js\",\n  \"integrityHash\": \"sha384-J+YlJ8v0gpaRoKH7SbFbEmxOZlAxLiwNjfSsBhDooGa5roXlPPpXbEevck4J7YZ+\",\n  \"version\": \"1.0.0\",\n  \"displayName\": \"CMS Slider\",\n  \"canCopy\": true\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts/hosted")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"hostedLocation\": \"https://cdn.jsdelivr.net/.../cmsslider.js\",\n  \"integrityHash\": \"sha384-J+YlJ8v0gpaRoKH7SbFbEmxOZlAxLiwNjfSsBhDooGa5roXlPPpXbEevck4J7YZ+\",\n  \"version\": \"1.0.0\",\n  \"displayName\": \"CMS Slider\",\n  \"canCopy\": true\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts/hosted', [
  'body' => '{
  "hostedLocation": "https://cdn.jsdelivr.net/.../cmsslider.js",
  "integrityHash": "sha384-J+YlJ8v0gpaRoKH7SbFbEmxOZlAxLiwNjfSsBhDooGa5roXlPPpXbEevck4J7YZ+",
  "version": "1.0.0",
  "displayName": "CMS Slider",
  "canCopy": true
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts/hosted");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"hostedLocation\": \"https://cdn.jsdelivr.net/.../cmsslider.js\",\n  \"integrityHash\": \"sha384-J+YlJ8v0gpaRoKH7SbFbEmxOZlAxLiwNjfSsBhDooGa5roXlPPpXbEevck4J7YZ+\",\n  \"version\": \"1.0.0\",\n  \"displayName\": \"CMS Slider\",\n  \"canCopy\": true\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "hostedLocation": "https://cdn.jsdelivr.net/.../cmsslider.js",
  "integrityHash": "sha384-J+YlJ8v0gpaRoKH7SbFbEmxOZlAxLiwNjfSsBhDooGa5roXlPPpXbEevck4J7YZ+",
  "version": "1.0.0",
  "displayName": "CMS Slider",
  "canCopy": true
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/registered_scripts/hosted")! as URL,
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