# Source: https://developers.webflow.com/data/reference/enterprise/workspace-management/create.mdx

# Create Site

POST https://api.webflow.com/v2/workspaces/{workspace_id}/sites
Content-Type: application/json

Create a site.

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope | `workspace:write`


Reference: https://developers.webflow.com/data/reference/enterprise/workspace-management/create

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /workspaces/{workspace_id}/sites:
    post:
      operationId: create
      summary: Create Site
      description: >
        Create a site.


        <Warning title="Enterprise Only">This endpoint requires an Enterprise
        workspace.</Warning>


        Required scope | `workspace:write`
      tags:
        - subpackage_sites
      parameters:
        - name: workspace_id
          in: path
          description: Unique identifier for a Workspace
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
                $ref: '#/components/schemas/sites_create_Response_201'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-siteRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-siteRequestUnauthorizedError'
        '403':
          description: Forbidden request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-siteRequestForbiddenError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-siteRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-siteRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-siteRequestInternalServerError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: The name of the site
                templateName:
                  type: string
                  description: The workspace or marketplace template to use
                parentFolderId:
                  type:
                    - string
                    - 'null'
                  description: MegaDodo Publications - Potential Book Ideas
              required:
                - name
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCustomDomainsItems:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for the Domain
        url:
          type: string
          description: The registered Domain name
        lastPublished:
          type:
            - string
            - 'null'
          format: date-time
          description: The date the custom domain was last published to
      required:
        - id
      title: >-
        WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCustomDomainsItems
    WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocalesPrimary:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier for the locale.
        cmsLocaleId:
          type: string
          description: A CMS-specific identifier for the locale.
        enabled:
          type: boolean
          description: Indicates if the locale is enabled.
        displayName:
          type: string
          description: The display name of the locale, typically in English.
        displayImageId:
          type:
            - string
            - 'null'
          description: An optional ID for an image associated with the locale, nullable.
        redirect:
          type: boolean
          description: Determines if requests should redirect to the locale's subdirectory.
        subdirectory:
          type: string
          description: The subdirectory path for the locale, used in URLs.
        tag:
          type: string
          description: >-
            A tag or code representing the locale, often following a standard
            format like 'en-US'.
      description: The primary locale for the site or application.
      title: >-
        WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocalesPrimary
    WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocalesSecondaryItems:
      type: object
      properties:
        id:
          type: string
          description: The unique identifier for the locale.
        cmsLocaleId:
          type: string
          description: A CMS-specific identifier for the locale.
        enabled:
          type: boolean
          description: Indicates if the locale is enabled.
        displayName:
          type: string
          description: The display name of the locale, typically in English.
        displayImageId:
          type:
            - string
            - 'null'
          description: An optional ID for an image associated with the locale, nullable.
        redirect:
          type: boolean
          description: Determines if requests should redirect to the locale's subdirectory.
        subdirectory:
          type: string
          description: The subdirectory path for the locale, used in URLs.
        tag:
          type: string
          description: >-
            A tag or code representing the locale, often following a standard
            format like 'en-US'.
      title: >-
        WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocalesSecondaryItems
    WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocales:
      type: object
      properties:
        primary:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocalesPrimary
          description: The primary locale for the site or application.
        secondary:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocalesSecondaryItems
          description: A list of secondary locales available for the site or application.
      title: >-
        WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocales
    WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDataCollectionType:
      type: string
      enum:
        - always
        - optOut
        - disabled
      description: The type of data collection enabled for the site.
      title: >-
        WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDataCollectionType
    sites_create_Response_201:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for the Site
        workspaceId:
          type: string
          format: objectid
          description: Unique identifier for the Workspace
        createdOn:
          type: string
          format: date-time
          description: Date the Site was created
        displayName:
          type: string
          description: Name given to Site
        shortName:
          type: string
          description: Slugified version of name
        lastPublished:
          type: string
          format: date-time
          description: Date the Site was last published
        lastUpdated:
          type: string
          format: date-time
          description: Date the Site was last updated
        previewUrl:
          type: string
          format: uri
          description: URL of a generated image for the given Site
        timeZone:
          type: string
          description: Site timezone set under Site Settings
        parentFolderId:
          type:
            - string
            - 'null'
          format: objectid
          description: The ID of the parent folder the Site exists in
        customDomains:
          type: array
          items:
            $ref: >-
              #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCustomDomainsItems
        locales:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaLocales
        dataCollectionEnabled:
          type: boolean
          description: Indicates if data collection is enabled for the site.
        dataCollectionType:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDataCollectionType
          description: The type of data collection enabled for the site.
      required:
        - id
        - workspaceId
        - createdOn
        - displayName
        - shortName
        - lastPublished
        - lastUpdated
        - previewUrl
        - timeZone
        - dataCollectionEnabled
        - dataCollectionType
      title: sites_create_Response_201
    WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCode:
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
      title: WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCode
    WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDetailsItems
    Create-siteRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-siteRequestBadRequestError
    Create-siteRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-siteRequestUnauthorizedError
    Create-siteRequestForbiddenError:
      oneOf:
        - description: Any type
        - description: Any type
      title: Create-siteRequestForbiddenError
    Create-siteRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-siteRequestNotFoundError
    Create-siteRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-siteRequestTooManyRequestsError
    Create-siteRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WorkspacesWorkspaceIdSitesPostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Create-siteRequestInternalServerError
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
client.sites.create(
    workspace_id="580e63e98c9a982ac9b8b741",
    name="The Hitchhiker's Guide to the Galaxy",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.create("580e63e98c9a982ac9b8b741", {
    name: "The Hitchhiker's Guide to the Galaxy"
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

	url := "https://api.webflow.com/v2/workspaces/580e63e98c9a982ac9b8b741/sites"

	payload := strings.NewReader("{\n  \"name\": \"The Hitchhiker's Guide to the Galaxy\"\n}")

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

url = URI("https://api.webflow.com/v2/workspaces/580e63e98c9a982ac9b8b741/sites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"The Hitchhiker's Guide to the Galaxy\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/v2/workspaces/580e63e98c9a982ac9b8b741/sites")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"The Hitchhiker's Guide to the Galaxy\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/v2/workspaces/580e63e98c9a982ac9b8b741/sites', [
  'body' => '{
  "name": "The Hitchhiker\'s Guide to the Galaxy"
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

var client = new RestClient("https://api.webflow.com/v2/workspaces/580e63e98c9a982ac9b8b741/sites");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"The Hitchhiker's Guide to the Galaxy\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["name": "The Hitchhiker's Guide to the Galaxy"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/workspaces/580e63e98c9a982ac9b8b741/sites")! as URL,
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