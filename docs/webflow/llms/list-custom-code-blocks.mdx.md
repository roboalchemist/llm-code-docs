# Source: https://developers.webflow.com/data/reference/custom-code/custom-code/list-custom-code-blocks.mdx

# List Custom Code Blocks

GET https://api.webflow.com/v2/sites/{site_id}/custom_code/blocks

Get a list of scripts that have been applied to a site and/or individual pages.

<Note title="Script Registration">
  To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints.

  See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
</Note>

Required scope | `custom_code:read`


Reference: https://developers.webflow.com/data/reference/custom-code/custom-code/list-custom-code-blocks

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/custom_code/blocks:
    get:
      operationId: list-custom-code-blocks
      summary: List Custom Code Blocks
      description: >
        Get a list of scripts that have been applied to a site and/or individual
        pages.


        <Note title="Script Registration">
          To apply a script to a site or page, the script must first be registered to a site via the [Register Script](/data/reference/custom-code/custom-code/register-hosted) endpoints. Once registered, the script can be applied to a Site or Page using the appropriate endpoints.

          See the documentation on [working with Custom Code](/data/docs/custom-code) for more information.
        </Note>


        Required scope | `custom_code:read`
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
        - name: offset
          in: query
          description: >-
            Offset used for pagination if the results have more than limit
            records
          required: false
          schema:
            type: integer
        - name: limit
          in: query
          description: 'Maximum number of records to be returned (max limit: 100)'
          required: false
          schema:
            type: integer
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
                $ref: >-
                  #/components/schemas/sites_scripts_list-custom-code-blocks_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-code-blocksRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-code-blocksRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-code-blocksRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-code-blocksRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-custom-code-blocksRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsType:
      type: string
      enum:
        - page
        - site
      description: >-
        Whether the Custom Code script is applied at the Site-level or
        Page-level
      title: >-
        SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsType
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItemsLocation:
      type: string
      enum:
        - header
        - footer
      default: header
      description: >-
        Location of the script, either in the header or footer of the published
        site
      title: >-
        SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItemsLocation
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItemsAttributes:
      type: object
      properties: {}
      description: >-
        Developer-specified key/value pairs to be applied as attributes to the
        script
      title: >-
        SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItemsAttributes
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItems:
      type: object
      properties:
        id:
          type: string
          format: objectId
          description: ID of the registered custom code script
        location:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItemsLocation
          description: >-
            Location of the script, either in the header or footer of the
            published site
        version:
          type: string
          description: Semantic Version String for the registered script *e.g. 0.0.1*
        attributes:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItemsAttributes
          description: >-
            Developer-specified key/value pairs to be applied as attributes to
            the script
      required:
        - id
        - location
        - version
      title: >-
        SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItems
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItems:
      type: object
      properties:
        siteId:
          type: string
          description: The Site ID where the custom code was applied
        pageId:
          type:
            - string
            - 'null'
          description: The Page ID (if applied at Page-level)
        type:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsType
            - type: 'null'
          description: >-
            Whether the Custom Code script is applied at the Site-level or
            Page-level
        scripts:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItemsScriptsItems
          description: A list of scripts applied to a Site or a Page
        createdOn:
          type: string
          format: date-time
          description: The date the Block was created
        lastUpdated:
          type: string
          format: date-time
          description: The date the Block was most recently updated
      description: A specific instance of Custom Code applied to a Site or Page
      title: >-
        SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItems
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaPagination:
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
        SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaPagination
    sites_scripts_list-custom-code-blocks_Response_200:
      type: object
      properties:
        blocks:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaBlocksItems
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      description: Custom Code Blocks corresponding to where scripts were applied
      title: sites_scripts_list-custom-code-blocks_Response_200
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-site-custom-code-blocksRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-code-blocksRequestBadRequestError
    Get-site-custom-code-blocksRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-code-blocksRequestUnauthorizedError
    Get-site-custom-code-blocksRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-code-blocksRequestNotFoundError
    Get-site-custom-code-blocksRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-code-blocksRequestTooManyRequestsError
    Get-site-custom-code-blocksRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCustomCodeBlocksGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-custom-code-blocksRequestInternalServerError
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
client.sites.scripts.list_custom_code_blocks(
    site_id="580e63e98c9a982ac9b8b741",
    offset=1,
    limit=1,
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.scripts.listCustomCodeBlocks("580e63e98c9a982ac9b8b741", {
    offset: 1,
    limit: 1
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code/blocks?offset=0&limit=100"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code/blocks?offset=0&limit=100")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code/blocks?offset=0&limit=100")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code/blocks?offset=0&limit=100', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code/blocks?offset=0&limit=100");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/custom_code/blocks?offset=0&limit=100")! as URL,
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