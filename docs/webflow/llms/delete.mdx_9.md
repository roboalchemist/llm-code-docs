# Source: https://developers.webflow.com/data/v2.0.0-beta/reference/enterprise/site-configuration/llms-txt/delete.mdx

# Delete LLMS.txt

DELETE https://api.webflow.com/beta/sites/{site_id}/llms_txt

Delete llms.txt for a specific Site.

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope: `site_config:write`


Reference: https://developers.webflow.com/data/v2.0.0-beta/reference/enterprise/site-configuration/llms-txt/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/llms_txt:
    delete:
      operationId: delete
      summary: Delete LLMS.txt
      description: >
        Delete llms.txt for a specific Site.


        <Warning title="Enterprise Only">This endpoint requires an Enterprise
        workspace.</Warning>


        Required scope: `site_config:write`
      tags:
        - subpackage_sites.subpackage_sites/llmsTxt
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
          description: File deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sites_llms-txt_delete_Response_204'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-llms-txtRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-llms-txtRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-llms-txtRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-llms-txtRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-llms-txtRequestInternalServerError'
servers:
  - url: https://api.webflow.com/beta
components:
  schemas:
    sites_llms-txt_delete_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: sites_llms-txt_delete_Response_204
    SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaCode
    SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
    Delete-llms-txtRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-llms-txtRequestBadRequestError
    Delete-llms-txtRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-llms-txtRequestUnauthorizedError
    Delete-llms-txtRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-llms-txtRequestNotFoundError
    Delete-llms-txtRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-llms-txtRequestTooManyRequestsError
    Delete-llms-txtRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdLlmsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-llms-txtRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt';
const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt"

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

url = URI("https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt")

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

HttpResponse<String> response = Unirest.delete("https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/beta/sites/580e63e98c9a982ac9b8b741/llms_txt")! as URL,
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