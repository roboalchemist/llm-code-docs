# Source: https://developers.webflow.com/data/reference/enterprise/site-configuration/301-redirects/create.mdx

# Create a 301 redirect

POST https://api.webflow.com/v2/sites/{site_id}/redirects
Content-Type: application/json

Add a new 301 redirection rule to a site.

This endpoint allows you to define a source path (`fromUrl`) and its corresponding destination path (`toUrl`), which will dictate how traffic is rerouted on your site. This is useful for managing site changes, restructuring URLs, or handling outdated links.

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope: `sites:write`


Reference: https://developers.webflow.com/data/reference/enterprise/site-configuration/301-redirects/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/redirects:
    post:
      operationId: create
      summary: Create a 301 redirect
      description: >
        Add a new 301 redirection rule to a site.


        This endpoint allows you to define a source path (`fromUrl`) and its
        corresponding destination path (`toUrl`), which will dictate how traffic
        is rerouted on your site. This is useful for managing site changes,
        restructuring URLs, or handling outdated links.


        <Warning title="Enterprise Only">This endpoint requires an Enterprise
        workspace.</Warning>


        Required scope: `sites:write`
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
                $ref: '#/components/schemas/sites_redirects_create_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-redirectRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-redirectRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-redirectRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-redirectRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-redirectRequestInternalServerError'
      requestBody:
        content:
          application/json:
            schema:
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
                  description: >-
                    The target URL path where the user or client will be
                    redirected.
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    sites_redirects_create_Response_200:
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
      title: sites_redirects_create_Response_200
    SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaCode
    SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaDetailsItems
    Create-redirectRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-redirectRequestBadRequestError
    Create-redirectRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-redirectRequestUnauthorizedError
    Create-redirectRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-redirectRequestNotFoundError
    Create-redirectRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-redirectRequestTooManyRequestsError
    Create-redirectRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRedirectsPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-redirectRequestInternalServerError
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
client.sites.redirects.create(
    site_id="580e63e98c9a982ac9b8b741",
    id="42e1a2b7aa1a13f768a0042a",
    from_url="/mostly-harmless",
    to_url="/earth",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.redirects.create("580e63e98c9a982ac9b8b741", {
    id: "42e1a2b7aa1a13f768a0042a",
    fromUrl: "/mostly-harmless",
    toUrl: "/earth"
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects"

	payload := strings.NewReader("{\n  \"id\": \"42e1a2b7aa1a13f768a0042a\",\n  \"fromUrl\": \"/mostly-harmless\",\n  \"toUrl\": \"/earth\"\n}")

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"id\": \"42e1a2b7aa1a13f768a0042a\",\n  \"fromUrl\": \"/mostly-harmless\",\n  \"toUrl\": \"/earth\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"id\": \"42e1a2b7aa1a13f768a0042a\",\n  \"fromUrl\": \"/mostly-harmless\",\n  \"toUrl\": \"/earth\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects', [
  'body' => '{
  "id": "42e1a2b7aa1a13f768a0042a",
  "fromUrl": "/mostly-harmless",
  "toUrl": "/earth"
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"id\": \"42e1a2b7aa1a13f768a0042a\",\n  \"fromUrl\": \"/mostly-harmless\",\n  \"toUrl\": \"/earth\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "id": "42e1a2b7aa1a13f768a0042a",
  "fromUrl": "/mostly-harmless",
  "toUrl": "/earth"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/redirects")! as URL,
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