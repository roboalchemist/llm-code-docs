# Source: https://developers.webflow.com/data/reference/enterprise/site-activity-logs/list.mdx

# Get Site Activity Logs

GET https://api.webflow.com/v2/sites/{site_id}/activity_logs

Retrieve Activity Logs for a specific Site.

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope: `site_activity:read`


Reference: https://developers.webflow.com/data/reference/enterprise/site-activity-logs/list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/activity_logs:
    get:
      operationId: list
      summary: Get Site Activity Logs
      description: >
        Retrieve Activity Logs for a specific Site.


        <Warning title="Enterprise Only">This endpoint requires an Enterprise
        workspace.</Warning>


        Required scope: `site_activity:read`
      tags:
        - subpackage_sites.subpackage_sites/activityLogs
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: objectid
        - name: limit
          in: query
          description: 'Maximum number of records to be returned (max limit: 100)'
          required: false
          schema:
            type: integer
        - name: offset
          in: query
          description: >-
            Offset used for pagination if the results have more than limit
            records
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
          description: A list of site activity logs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sites_activity-logs_list_Response_200'
        '403':
          description: Forbidden request
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-activity-logsRequestForbiddenError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-activity-logsRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-activity-logsRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-site-activity-logsRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsEvent:
      type: string
      enum:
        - styles_modified
        - site_published
        - ix2_modified_on_page
        - page_dom_modified
        - cms_item
        - backup_created
        - page_custom_code_modified
        - symbols_modified
        - variable_modified
        - variables_modified
        - cms_collection
        - page_settings_modified
        - page_settings_custom_code_modified
        - ix2_modified_on_component
        - ix2_modified_on_class
        - site_custom_code_modified
        - page_duplicated
        - secondary_locale_page_content_modified
        - page_renamed
        - page_created
        - page_deleted
        - site_unpublished
        - backup_restored
        - locale_added
        - branch_created
        - locale_display_name_updated
        - locale_subdirectory_updated
        - branch_merged
        - locale_tag_updated
        - branch_deleted
        - locale_enabled
        - locale_removed
        - locale_disabled
        - library_shared
        - library_unshared
        - library_installed
        - library_uninstalled
        - library_update_shared
        - library_update_accepted
        - branch_review_created
        - branch_review_approved
        - branch_review_canceled
      title: >-
        SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsEvent
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsResourceOperation:
      type: string
      enum:
        - CREATED
        - MODIFIED
        - PUBLISHED
        - UNPUBLISHED
        - DELETED
        - GROUP_REORDERED
        - GROUP_CREATED
        - GROUP_DELETED
        - REORDERED
      title: >-
        SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsResourceOperation
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsUser:
      type: object
      properties:
        id:
          type: string
        displayName:
          type: string
      title: >-
        SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsUser
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsPayload:
      type: object
      properties: {}
      title: >-
        SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsPayload
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItems:
      type: object
      properties:
        id:
          type: string
        createdOn:
          type: string
          format: date-time
        lastUpdated:
          type: string
          format: date-time
        event:
          $ref: >-
            #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsEvent
        resourceOperation:
          $ref: >-
            #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsResourceOperation
        user:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsUser
            - type: 'null'
        resourceId:
          type:
            - string
            - 'null'
        resourceName:
          type:
            - string
            - 'null'
        newValue:
          type:
            - string
            - 'null'
        previousValue:
          type:
            - string
            - 'null'
        payload:
          oneOf:
            - $ref: >-
                #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItemsPayload
            - type: 'null'
      title: >-
        SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItems
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaPagination:
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
        SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaPagination
    sites_activity-logs_list_Response_200:
      type: object
      properties:
        items:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaItemsItems
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaPagination
          description: Pagination object
      title: sites_activity-logs_list_Response_200
    Get-site-activity-logsRequestForbiddenError:
      oneOf:
        - description: Any type
        - description: Any type
      title: Get-site-activity-logsRequestForbiddenError
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-site-activity-logsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-activity-logsRequestNotFoundError
    Get-site-activity-logsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-activity-logsRequestTooManyRequestsError
    Get-site-activity-logsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdActivityLogsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-site-activity-logsRequestInternalServerError
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
client.sites.activity_logs.list(
    site_id="580e63e98c9a982ac9b8b741",
    limit=1,
    offset=1,
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.activityLogs.list("580e63e98c9a982ac9b8b741", {
    limit: 1,
    offset: 1
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/activity_logs?limit=100&offset=0"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/activity_logs?limit=100&offset=0")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/activity_logs?limit=100&offset=0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/activity_logs?limit=100&offset=0', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/activity_logs?limit=100&offset=0");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/activity_logs?limit=100&offset=0")! as URL,
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