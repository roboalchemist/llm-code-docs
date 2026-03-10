# Source: https://developers.webflow.com/data/v2.0.0-beta/reference/token/resolve.mdx

# Resolve ID Token

POST https://api.webflow.com/beta/token/resolve
Content-Type: application/json

Information about the authorized user derived from the resolved ID Token
<Note>Access to this endpoint requires a bearer token from a [Data Client App](/data/docs/getting-started-data-clients).</Note>

Required Scope | `authorized_user:read`


Reference: https://developers.webflow.com/data/v2.0.0-beta/reference/token/resolve

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /token/resolve:
    post:
      operationId: resolve
      summary: Resolve ID Token
      description: >
        Information about the authorized user derived from the resolved ID Token

        <Note>Access to this endpoint requires a bearer token from a [Data
        Client App](/data/docs/getting-started-data-clients).</Note>


        Required Scope | `authorized_user:read`
      tags:
        - subpackage_idToken
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
                $ref: '#/components/schemas/id-token_resolve_Response_200'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResolveRequestUnauthorizedError'
        '403':
          description: Provided access token is valid, but is missing the required scopes.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ResolveRequestForbiddenError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                idToken:
                  type: string
                  description: The ID token created using the Designer API
servers:
  - url: https://api.webflow.com/beta
components:
  schemas:
    id-token_resolve_Response_200:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: The unique ID of the user
        email:
          type: string
          format: email
          description: The user's email address
        firstName:
          type: string
          description: The user's first name
        lastName:
          type: string
          description: The user's last name
        siteId:
          type: string
          description: The ID of the site associated with the user
      title: id-token_resolve_Response_200
    TokenResolvePostResponsesContentApplicationJsonSchemaCode:
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
      title: TokenResolvePostResponsesContentApplicationJsonSchemaCode
    TokenResolvePostResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: TokenResolvePostResponsesContentApplicationJsonSchemaDetailsItems
    ResolveRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/TokenResolvePostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/TokenResolvePostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: ResolveRequestUnauthorizedError
    ResolveRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/TokenResolvePostResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/TokenResolvePostResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: ResolveRequestForbiddenError
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/beta/token/resolve"

payload = {}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/beta/token/resolve';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{}'
};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/beta/token/resolve"

	payload := strings.NewReader("{}")

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

url = URI("https://api.webflow.com/beta/token/resolve")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.webflow.com/beta/token/resolve")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.webflow.com/beta/token/resolve', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/beta/token/resolve");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/beta/token/resolve")! as URL,
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