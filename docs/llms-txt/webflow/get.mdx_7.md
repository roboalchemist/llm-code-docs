# Source: https://developers.webflow.com/data/reference/webhooks/get.mdx

# Get Webhook

GET https://api.webflow.com/v2/webhooks/{webhook_id}

Get a specific Webhook instance

Required scope: `sites:read`


Reference: https://developers.webflow.com/data/reference/webhooks/get

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /webhooks/{webhook_id}:
    get:
      operationId: get
      summary: Get Webhook
      description: |
        Get a specific Webhook instance

        Required scope: `sites:read`
      tags:
        - subpackage_webhooks
      parameters:
        - name: webhook_id
          in: path
          description: Unique identifier for a Webhook
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
                $ref: '#/components/schemas/webhooks_get_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-webhookRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-webhookRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-webhookRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-webhookRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-webhookRequestInternalServerError'
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaTriggerType:
      type: string
      enum:
        - form_submission
        - site_publish
        - page_created
        - page_metadata_updated
        - page_deleted
        - ecomm_new_order
        - ecomm_order_changed
        - ecomm_inventory_changed
        - collection_item_created
        - collection_item_changed
        - collection_item_deleted
        - collection_item_published
        - collection_item_unpublished
        - comment_created
      description: >
        The type of event that triggered the request. See the the documentation
        for details on [supported events](/data/reference/all-events).
      title: WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaTriggerType
    WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaFilter:
      type: object
      properties:
        name:
          type: string
          description: The name of the form you'd like to recieve notifications for.
      description: >-
        Only supported for the `form_submission` trigger type. Filter for the
        form you want Webhooks to be sent for.
      title: WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaFilter
    webhooks_get_Response_200:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: Unique identifier for the Webhook registration
        triggerType:
          $ref: >-
            #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaTriggerType
          description: >
            The type of event that triggered the request. See the the
            documentation for details on [supported
            events](/data/reference/all-events).
        url:
          type: string
          description: URL to send the Webhook payload to
        workspaceId:
          type: string
          format: objectid
          description: Unique identifier for the Workspace the Webhook is registered in
        siteId:
          type: string
          format: objectid
          description: Unique identifier for the Site the Webhook is registered in
        filter:
          $ref: >-
            #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaFilter
          description: >-
            Only supported for the `form_submission` trigger type. Filter for
            the form you want Webhooks to be sent for.
        lastTriggered:
          type: string
          format: date-time
          description: Date the Webhook instance was last triggered
        createdOn:
          type: string
          format: date-time
          description: Date the Webhook registration was created
      title: webhooks_get_Response_200
    WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaCode:
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
      title: WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaCode
    WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-webhookRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-webhookRequestBadRequestError
    Get-webhookRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-webhookRequestUnauthorizedError
    Get-webhookRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-webhookRequestNotFoundError
    Get-webhookRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-webhookRequestTooManyRequestsError
    Get-webhookRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/WebhooksWebhookIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-webhookRequestInternalServerError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer
    ApiKey:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
from webflow import Webflow

client = Webflow(
    access_token="YOUR_ACCESS_TOKEN",
)
client.webhooks.get(
    webhook_id="580e64008c9a982ac9b8b754",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.webhooks.get("580e64008c9a982ac9b8b754");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/webhooks/580e64008c9a982ac9b8b754"

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

url = URI("https://api.webflow.com/v2/webhooks/580e64008c9a982ac9b8b754")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/webhooks/580e64008c9a982ac9b8b754")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/webhooks/580e64008c9a982ac9b8b754', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/webhooks/580e64008c9a982ac9b8b754");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/webhooks/580e64008c9a982ac9b8b754")! as URL,
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