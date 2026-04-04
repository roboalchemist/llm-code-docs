# Source: https://developers.webflow.com/data/reference/enterprise/site-configuration/301-redirects/get.mdx

# Get 301 redirects

GET https://api.webflow.com/v2/sites/{site_id}/redirects

Fetch a list of all 301 redirect rules configured for a specific site.

Use this endpoint to review, audit, or manage the redirection rules that control how traffic is rerouted on your site.

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope: `sites:read`


Reference: https://developers.webflow.com/data/reference/enterprise/site-configuration/301-redirects/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/redirects:
    get:
      operationId: list
      summary: Get 301 redirects
      description: >
        Fetch a list of all 301 redirect rules configured for a specific site.


        Use this endpoint to review, audit, or manage the redirection rules that
        control how traffic is rerouted on your site.


        <Warning title="Enterprise Only">This endpoint requires an Enterprise
        workspace.</Warning>


        Required scope: `sites:read`
      tags:
        - subpackage_sites.subpackage_sites/redirects
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
                $ref: '#/components/schemas/sites_redirects_list_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-redirectsRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-redirectsRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-redirectsRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-redirectsRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-redirectsRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaRedirectsItems:
      type: object
      properties:
        id:
          type: string
          description: The ID of the specific redirect rule
        fromUrl:
          type: string
          description: The source URL path that will be redirected.
        toUrl:
          type: string
          description: The target URL path where the user or client will be redirected.
      description: >-
        A single redirection rule, specifying a source URL and a destination
        URL.
      title: >-
        SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaRedirectsItems
    SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaPagination:
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
      title: SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaPagination
    sites_redirects_list_Response_200:
      type: object
      properties:
        redirects:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaRedirectsItems
          description: List of redirects for a given site
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      description: Site redirects response
      title: sites_redirects_list_Response_200
    SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-redirectsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-redirectsRequestBadRequestError
    Get-redirectsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-redirectsRequestUnauthorizedError
    Get-redirectsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-redirectsRequestNotFoundError
    Get-redirectsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-redirectsRequestTooManyRequestsError
    Get-redirectsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-redirectsRequestInternalServerError
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
client.sites.redirects.list(
    site_id="580e63e98c9a982ac9b8b741",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.redirects.list("580e63e98c9a982ac9b8b741");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects")! as URL,
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