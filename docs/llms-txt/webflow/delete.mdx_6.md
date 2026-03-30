# Source: https://developers.webflow.com/data/reference/enterprise/site-configuration/robots-txt/delete.mdx

# Delete robots.txt

DELETE https://api.webflow.com/v2/sites/{site_id}/robots_txt
Content-Type: application/json

Remove specific rules for a user-agent in your `robots.txt` file. To delete all rules for a user-agent, provide an empty rule set. This will remove the user-agent's entry entirely, leaving it subject to your site's default crawling behavior.

**Note:** Deleting a user-agent with no rules will make the user-agent's access unrestricted unless other directives apply.

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope: `site_config:write`


Reference: https://developers.webflow.com/data/reference/enterprise/site-configuration/robots-txt/delete

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/robots_txt:
    delete:
      operationId: delete
      summary: Delete robots.txt
      description: >
        Remove specific rules for a user-agent in your `robots.txt` file. To
        delete all rules for a user-agent, provide an empty rule set. This will
        remove the user-agent's entry entirely, leaving it subject to your
        site's default crawling behavior.


        **Note:** Deleting a user-agent with no rules will make the user-agent's
        access unrestricted unless other directives apply.


        <Warning title="Enterprise Only">This endpoint requires an Enterprise
        workspace.</Warning>


        Required scope: `site_config:write`
      tags:
        - subpackage_sites.subpackage_sites/robotsTxt
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
                $ref: '#/components/schemas/sites_robots-txt_delete_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-robots-txtRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-robots-txtRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-robots-txtRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-robots-txtRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-robots-txtRequestInternalServerError
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                rules:
                  type: array
                  items:
                    $ref: >-
                      #/components/schemas/SitesSiteIdRobotsTxtDeleteRequestBodyContentApplicationJsonSchemaRulesItems
                  description: List of rules for user agents.
                sitemap:
                  type: string
                  description: URL to the sitemap.
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdRobotsTxtDeleteRequestBodyContentApplicationJsonSchemaRulesItems:
      type: object
      properties:
        userAgent:
          type: string
          description: The user agent the rules apply to.
        allows:
          type: array
          items:
            type: string
          description: List of paths allowed for this user agent.
        disallows:
          type: array
          items:
            type: string
          description: List of paths disallowed for this user agent.
      required:
        - userAgent
      title: >-
        SitesSiteIdRobotsTxtDeleteRequestBodyContentApplicationJsonSchemaRulesItems
    SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaRulesItems:
      type: object
      properties:
        userAgent:
          type: string
          description: The user agent the rules apply to.
        allows:
          type: array
          items:
            type: string
          description: List of paths allowed for this user agent.
        disallows:
          type: array
          items:
            type: string
          description: List of paths disallowed for this user agent.
      required:
        - userAgent
      title: >-
        SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaRulesItems
    sites_robots-txt_delete_Response_200:
      type: object
      properties:
        rules:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaRulesItems
          description: List of rules for user agents.
        sitemap:
          type: string
          description: URL to the sitemap.
      description: The robots.txt file for a given site
      title: sites_robots-txt_delete_Response_200
    SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaCode
    SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
    Delete-robots-txtRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-robots-txtRequestBadRequestError
    Delete-robots-txtRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-robots-txtRequestUnauthorizedError
    Delete-robots-txtRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-robots-txtRequestNotFoundError
    Delete-robots-txtRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-robots-txtRequestTooManyRequestsError
    Delete-robots-txtRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdRobotsTxtDeleteResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Delete-robots-txtRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import RobotsRulesItem, Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.sites.robots_txt.delete(
    site_id="580e63e98c9a982ac9b8b741",
    rules=[
        RobotsRulesItem(
            user_agent="*",
            allows=["/public"],
            disallows=["/bubbles"],
        )
    ],
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.robotsTxt.delete("580e63e98c9a982ac9b8b741", {
    rules: [{
            userAgent: "*",
            allows: ["/public"],
            disallows: ["/bubbles"]
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/robots_txt"

	payload := strings.NewReader("{\n  \"rules\": [\n    {\n      \"userAgent\": \"*\",\n      \"allows\": [],\n      \"disallows\": [\n        \"/bubbles\"\n      ]\n    }\n  ]\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/robots_txt")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"rules\": [\n    {\n      \"userAgent\": \"*\",\n      \"allows\": [],\n      \"disallows\": [\n        \"/bubbles\"\n      ]\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/robots_txt")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"rules\": [\n    {\n      \"userAgent\": \"*\",\n      \"allows\": [],\n      \"disallows\": [\n        \"/bubbles\"\n      ]\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/robots_txt', [
  'body' => '{
  "rules": [
    {
      "userAgent": "*",
      "allows": [],
      "disallows": [
        "/bubbles"
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/robots_txt");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"rules\": [\n    {\n      \"userAgent\": \"*\",\n      \"allows\": [],\n      \"disallows\": [\n        \"/bubbles\"\n      ]\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["rules": [
    [
      "userAgent": "*",
      "allows": [],
      "disallows": ["/bubbles"]
    ]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/robots_txt")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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