# Source: https://developers.webflow.com/data/reference/pages-and-components/pages/get-metadata.mdx

# Get Page Metadata

GET https://api.webflow.com/v2/pages/{page_id}

Get metadata information for a single page.

Required scope | `pages:read`


Reference: https://developers.webflow.com/data/reference/pages-and-components/pages/get-metadata

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /pages/{page_id}:
    get:
      operationId: get-metadata
      summary: Get Page Metadata
      description: |
        Get metadata information for a single page.

        Required scope | `pages:read`
      tags:
        - subpackage_pages
      parameters:
        - name: page_id
          in: path
          description: Unique identifier for a Page
          required: true
          schema:
            type: string
            format: objectid
        - name: localeId
          in: query
          description: >
            Unique identifier for a specific Locale.


            [Lear more about
            localization.](/data/v2.0.0/docs/working-with-localization)
          required: false
          schema:
            type: string
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
                $ref: '#/components/schemas/pages_get-metadata_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-page-metadataRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-page-metadataRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-page-metadataRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-page-metadataRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-page-metadataRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    PagesPageIdGetResponsesContentApplicationJsonSchemaSeo:
      type: object
      properties:
        title:
          type: string
          description: The Page title shown in search engine results
        description:
          type: string
          description: The Page description shown in search engine results
      description: SEO-related fields for the Page
      title: PagesPageIdGetResponsesContentApplicationJsonSchemaSeo
    PagesPageIdGetResponsesContentApplicationJsonSchemaOpenGraph:
      type: object
      properties:
        title:
          type: string
          description: The title supplied to Open Graph annotations
        titleCopied:
          type: boolean
          default: true
          description: Indicates the Open Graph title was copied from the SEO title
        description:
          type: string
          description: The description supplied to Open Graph annotations
        descriptionCopied:
          type: boolean
          default: true
          description: >-
            Indicates the Open Graph description was copied from the SEO
            description
      description: Open Graph fields for the Page
      title: PagesPageIdGetResponsesContentApplicationJsonSchemaOpenGraph
    pages_get-metadata_Response_200:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for the Page
        siteId:
          type: string
          format: objectid
          description: Unique identifier for the Site
        title:
          type: string
          description: Title of the Page
        slug:
          type: string
          description: slug of the Page (derived from title)
        parentId:
          type: string
          format: objectid
          description: Identifier of the parent folder
        collectionId:
          type: string
          format: objectid
          description: >-
            Unique identifier for a linked Collection, value will be null if the
            Page is not part of a Collection.
        createdOn:
          type: string
          format: date-time
          description: The date the Page was created
        lastUpdated:
          type: string
          format: date-time
          description: The date the Page was most recently updated
        archived:
          type: boolean
          default: false
          description: Whether the Page has been archived
        draft:
          type: boolean
          default: false
          description: Whether the Page is a draft
        canBranch:
          type: boolean
          default: false
          description: >-
            Indicates whether the Page supports [Page
            Branching](https://university.webflow.com/lesson/page-branching).
            Pages that are already branches cannot be branched again.
        isBranch:
          type: boolean
          default: false
          description: >-
            Indicates whether the Page is a Branch of another Page [Page
            Branching](https://university.webflow.com/lesson/page-branching)
        branchId:
          type:
            - string
            - 'null'
          format: objectid
          description: >-
            If the Page is a Branch of another Page, this is the ID of the
            Branch
        seo:
          $ref: >-
            #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaSeo
          description: SEO-related fields for the Page
        openGraph:
          $ref: >-
            #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaOpenGraph
          description: Open Graph fields for the Page
        localeId:
          type:
            - string
            - 'null'
          format: objectid
          description: Unique ID of the page locale
        publishedPath:
          type: string
          description: Relative path of the published page URL
      required:
        - id
      description: The Page object
      title: pages_get-metadata_Response_200
    PagesPageIdGetResponsesContentApplicationJsonSchemaCode:
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
      title: PagesPageIdGetResponsesContentApplicationJsonSchemaCode
    PagesPageIdGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: PagesPageIdGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-page-metadataRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-metadataRequestBadRequestError
    Get-page-metadataRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-metadataRequestUnauthorizedError
    Get-page-metadataRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-metadataRequestNotFoundError
    Get-page-metadataRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-metadataRequestTooManyRequestsError
    Get-page-metadataRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/PagesPageIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-page-metadataRequestInternalServerError
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
client.pages.get_metadata(
    page_id="63c720f9347c2139b248e552",
    locale_id="65427cf400e02b306eaa04a0",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.pages.getMetadata("63c720f9347c2139b248e552", {
    localeId: "65427cf400e02b306eaa04a0"
});

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552?localeId=65427cf400e02b306eaa04a0"

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

url = URI("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552?localeId=65427cf400e02b306eaa04a0")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552?localeId=65427cf400e02b306eaa04a0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/pages/63c720f9347c2139b248e552?localeId=65427cf400e02b306eaa04a0', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/pages/63c720f9347c2139b248e552?localeId=65427cf400e02b306eaa04a0");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/pages/63c720f9347c2139b248e552?localeId=65427cf400e02b306eaa04a0")! as URL,
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