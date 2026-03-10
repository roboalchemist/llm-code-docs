# Source: https://developers.webflow.com/data/reference/sites/list.mdx

# List Sites

GET https://api.webflow.com/v2/sites

List of all sites the provided access token is able to access.

Required scope | `sites:read`


Reference: https://developers.webflow.com/data/reference/sites/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites:
    get:
      operationId: list
      summary: List Sites
      description: |
        List of all sites the provided access token is able to access.

        Required scope | `sites:read`
      tags:
        - subpackage_sites
      parameters:
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
                $ref: '#/components/schemas/sites_list_Response_200'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-sitesRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-sitesRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-sitesRequestTooManyRequestsError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesGetResponsesContentApplicationJsonSchemaSitesItemsCustomDomainsItems:
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
        SitesGetResponsesContentApplicationJsonSchemaSitesItemsCustomDomainsItems
    SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocalesPrimary:
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
      title: SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocalesPrimary
    SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocalesSecondaryItems:
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
        SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocalesSecondaryItems
    SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocales:
      type: object
      properties:
        primary:
          $ref: >-
            #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocalesPrimary
          description: The primary locale for the site or application.
        secondary:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocalesSecondaryItems
          description: A list of secondary locales available for the site or application.
      title: SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocales
    SitesGetResponsesContentApplicationJsonSchemaSitesItemsDataCollectionType:
      type: string
      enum:
        - always
        - optOut
        - disabled
      description: The type of data collection enabled for the site.
      title: >-
        SitesGetResponsesContentApplicationJsonSchemaSitesItemsDataCollectionType
    SitesGetResponsesContentApplicationJsonSchemaSitesItems:
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
              #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaSitesItemsCustomDomainsItems
        locales:
          $ref: >-
            #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaSitesItemsLocales
        dataCollectionEnabled:
          type: boolean
          description: Indicates if data collection is enabled for the site.
        dataCollectionType:
          $ref: >-
            #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaSitesItemsDataCollectionType
          description: The type of data collection enabled for the site.
      required:
        - id
      title: SitesGetResponsesContentApplicationJsonSchemaSitesItems
    sites_list_Response_200:
      type: object
      properties:
        sites:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaSitesItems
      title: sites_list_Response_200
    SitesGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesGetResponsesContentApplicationJsonSchemaCode
    SitesGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesGetResponsesContentApplicationJsonSchemaDetailsItems
    List-sitesRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-sitesRequestUnauthorizedError
    List-sitesRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-sitesRequestNotFoundError
    List-sitesRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-sitesRequestTooManyRequestsError
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
client.sites.list()

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.list();

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites"

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

url = URI("https://api.webflow.com/v2/sites")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites")! as URL,
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