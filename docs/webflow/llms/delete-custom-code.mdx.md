# Source: https://developers.webflow.com/data/reference/custom-code/custom-code-sites/delete-custom-code.mdx

# Delete Custom Code

DELETE https://api.webflow.com/v2/sites/{site_id}/custom_code

Remove all scripts from a site applied by the App. This endpoint will not remove scripts from the site's registered scripts.

To remove individual scripts applied by the App, use the [Add/Update Custom Code](/data/reference/custom-code/custom-code-sites/upsert-custom-code) endpoint.

<Note>Access to this endpoint requires a bearer token obtained from an [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>

Required scope | `custom_code:write`


Reference: https://developers.webflow.com/data/reference/custom-code/custom-code-sites/delete-custom-code

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/custom_code:
    delete:
      operationId: delete-custom-code
      summary: Delete Custom Code
      description: >
        Remove all scripts from a site applied by the App. This endpoint will
        not remove scripts from the site's registered scripts.


        To remove individual scripts applied by the App, use the [Add/Update
        Custom
        Code](/data/reference/custom-code/custom-code-sites/upsert-custom-code)
        endpoint.


        <Note>Access to this endpoint requires a bearer token obtained from an
        [OAuth Code Grant Flow](/data/reference/oauth-app).</Note>


        Required scope | `custom_code:write`
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
        '204':
          description: Request was successful. No Content is returned.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/sites_scripts_delete-custom-code_Response_204
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-site-custom-codeRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-site-custom-codeRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-site-custom-codeRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-site-custom-codeRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-site-custom-codeRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    sites_scripts_delete-custom-code_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: sites_scripts_delete-custom-code_Response_204
    SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaCode
    SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaDetailsItems
    Delete-site-custom-codeRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-site-custom-codeRequestBadRequestError
    Delete-site-custom-codeRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-site-custom-codeRequestUnauthorizedError
    Delete-site-custom-codeRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-site-custom-codeRequestNotFoundError
    Delete-site-custom-codeRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-site-custom-codeRequestTooManyRequestsError
    Delete-site-custom-codeRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-site-custom-codeRequestInternalServerError
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
client.sites.scripts.delete_custom_code(
    site_id="580e63e98c9a982ac9b8b741",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.scripts.deleteCustomCode("580e63e98c9a982ac9b8b741");

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

	req, _ := http.NewRequest("DELETE", url, nil)

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

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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