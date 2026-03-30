# Source: https://developers.webflow.com/data/v1.0.0/reference/sites/webhooks/list-webhooks.mdx

# List Webhooks

GET https://api.webflow.com/sites/{site_id}/webhooks

List of all webhooks in a given site

Reference: https://developers.webflow.com/data/v1.0.0/reference/sites/webhooks/list-webhooks

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/webhooks:
    get:
      operationId: list-webhooks
      summary: List Webhooks
      description: List of all webhooks in a given site
      tags:
        - subpackage_webhooks
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: uuid
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
        - name: Accept-Version
          in: header
          description: The API version
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Webhook'
        '400':
          description: >-
            Request body was incorrectly formatted. Likely invalid JSON being
            sent up.
          content:
            application/json:
              schema:
                description: Any type
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                description: Any type
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                description: Any type
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                description: Any type
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: https://api.webflow.com
components:
  schemas:
    TriggerType:
      type: string
      enum:
        - form_submission
        - site_publish
        - ecomm_new_order
        - ecomm_order_changed
        - ecomm_inventory_changed
        - collection_item_created
        - collection_item_changed
        - collection_item_deleted
        - collection_item_unpublished
        - comment_created
      description: >
        * `form_submission` - Sends the [form_submission](#form_submission)
        event

        * `site_publish` - Sends a [site_publish](#site_publish) event

        * `ecomm_new_order` - Sends the new [ecomm_new_order](#ecomm_new_order)
        event

        * `ecomm_order_changed` - Sends the
        [ecomm_order_changed](#ecomm_order_changed) event

        * `ecomm_inventory_changed` - Sends the
        [ecomm_inventory_changed](#ecomm_inventory_changed) event

        * `collection_item_created` - Sends the
        [collection_item_created](#collection_item_created) event

        * `collection_item_changed` - Sends the
        [collection_item_changed](#collection_item_changed) event

        * `collection_item_deleted` - Sends the
        [collection_item_deleted](#collection_item_deleted) event

        * `collection_item_unpublished` - Sends the
        [collection_item_unpublished](#collection_item_unpublished) event

        * `comment_created` - Sends the [comment_created](#comment_created)
        event
      title: TriggerType
    WebhookFilter:
      type: object
      properties: {}
      description: filter for selecting which events you want webhooks to be triggered for.
      title: WebhookFilter
    Webhook:
      type: object
      properties:
        _id:
          type: string
          format: uuid
          description: Unique identifier for a Webhook
        triggerType:
          $ref: '#/components/schemas/TriggerType'
        triggerId:
          type: string
          format: uuid
          description: Unique identifier for the Webhook Trigger
        site:
          type: string
          format: uuid
          description: Unique identifier for a Webhook
        filter:
          $ref: '#/components/schemas/WebhookFilter'
          description: >-
            filter for selecting which events you want webhooks to be triggered
            for.
        lastUsed:
          type: string
          format: date-time
          description: Date trigger was last used
        createdOn:
          type: string
          format: date-time
          description: Date trigger was created
      title: Webhook
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.webhooks.list("580e63e98c9a982ac9b8b741");

```

```python
import requests

url = "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/webhooks"

headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/webhooks"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Accept-Version", "1.0.0")
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

url = URI("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/webhooks")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Accept-Version"] = '1.0.0'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/webhooks")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/webhooks', [
  'headers' => [
    'Accept-Version' => '1.0.0',
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/webhooks");
var request = new RestRequest(Method.GET);
request.AddHeader("Accept-Version", "1.0.0");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept-Version": "1.0.0",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/webhooks")! as URL,
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