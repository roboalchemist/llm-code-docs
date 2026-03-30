# Source: https://developers.webflow.com/data/v2.0.0-beta/reference/app-subscriptions/app-subscriptions.mdx

# Get app subscriptions

GET https://api.webflow.com/beta/app_subscriptions

Information about subscriptions for a specific authorization token
<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>
Required Scope | `app_subscriptions:read`


Reference: https://developers.webflow.com/data/v2.0.0-beta/reference/app-subscriptions/app-subscriptions

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /app_subscriptions:
    get:
      operationId: app-subscriptions
      summary: Get app subscriptions
      description: >
        Information about subscriptions for a specific authorization token

        <Note>Access to this endpoint requires a bearer token from a [Data
        Client App](/data/docs/getting-started-data-clients).</Note>

        Required Scope | `app_subscriptions:read`
      tags:
        - subpackage_appSubscriptions
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
                $ref: >-
                  #/components/schemas/app-subscriptions_app-subscriptions_Response_200
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/App_subscriptionsRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/App_subscriptionsRequestForbiddenError'
servers:
  - url: https://api.webflow.com/beta
components:
  schemas:
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsPriceInterval:
      type: string
      enum:
        - MONTHLY
        - YEARLY
        - ONE_TIME
      description: Interval of payment
      title: >-
        AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsPriceInterval
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsPrice:
      type: object
      properties:
        value:
          type: number
          format: double
          description: Price in cents
        unit:
          type: string
          description: Currency unit
        interval:
          $ref: >-
            #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsPriceInterval
          description: Interval of payment
      description: The price of the Subscription
      title: >-
        AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsPrice
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsAccessGrant:
      type: object
      properties:
        id:
          type: string
          format: objectId
          description: The unique ID of the granted resource
        type:
          type: string
          description: The type of granted resource
      description: Information about the granted access for the subscription.
      title: >-
        AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsAccessGrant
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsStatus:
      type: string
      enum:
        - active
        - cancelled
        - past due
      description: Status of the subscription
      title: >-
        AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsStatus
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptions:
      type: object
      properties:
        appId:
          type: string
          format: objectId
          description: The unique ID of the App
        price:
          $ref: >-
            #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsPrice
          description: The price of the Subscription
        accessGrant:
          $ref: >-
            #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsAccessGrant
          description: Information about the granted access for the subscription.
        status:
          $ref: >-
            #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptionsStatus
          description: Status of the subscription
        startsAt:
          type: string
          format: date-time
          description: Start time of the current billing period
        endsAt:
          type: string
          format: date-time
          description: End time of the current billing period
      title: >-
        AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptions
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItems:
      type: object
      properties:
        appSubscriptions:
          $ref: >-
            #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItemsAppSubscriptions
      description: Subscription details for a site
      title: >-
        AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItems
    app-subscriptions_app-subscriptions_Response_200:
      type: object
      properties:
        appSubscriptions:
          type: array
          items:
            $ref: >-
              #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaAppSubscriptionsItems
      description: List of subscriptions for a specific site
      title: app-subscriptions_app-subscriptions_Response_200
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaCode:
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
      title: AppSubscriptionsGetResponsesContentApplicationJsonSchemaCode
    AppSubscriptionsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: AppSubscriptionsGetResponsesContentApplicationJsonSchemaDetailsItems
    App_subscriptionsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: App_subscriptionsRequestUnauthorizedError
    App_subscriptionsRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/AppSubscriptionsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: App_subscriptionsRequestForbiddenError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/beta/app_subscriptions"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/beta/app_subscriptions';
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

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

	url := "https://api.webflow.com/beta/app_subscriptions"

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

url = URI("https://api.webflow.com/beta/app_subscriptions")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/beta/app_subscriptions")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/beta/app_subscriptions', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/beta/app_subscriptions");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/beta/app_subscriptions")! as URL,
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