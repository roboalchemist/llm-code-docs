# Source: https://developers.webflow.com/data/reference/enterprise/site-configuration/well-known-files/put.mdx

# Set a well-known file

PUT https://api.webflow.com/v2/sites/{site_id}/well_known
Content-Type: application/json

Upload a supported well-known file to a site.

The current restrictions on well-known files are as follows:
  - Each file must be smaller than 100kb
  - Less than 30 total files
  - Have one of the following file extensions (or no extension): `.txt`, `.json`, `.noext`

  <Note title=".noext">
    `.noext` is a special file extension that removes other extensions. For example, `apple-app-site-association.noext.txt` will be uploaded as `apple-app-site-association`. Use this extension for tools that have trouble uploading extensionless files.
  </Note>

<Warning title="Enterprise Only">This endpoint requires an Enterprise workspace.</Warning>

Required scope: `site_config:write`


Reference: https://developers.webflow.com/data/reference/enterprise/site-configuration/well-known-files/put

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/well_known:
    put:
      operationId: put
      summary: Set a well-known file
      description: >
        Upload a supported well-known file to a site.


        The current restrictions on well-known files are as follows:
          - Each file must be smaller than 100kb
          - Less than 30 total files
          - Have one of the following file extensions (or no extension): `.txt`, `.json`, `.noext`

          <Note title=".noext">
            `.noext` is a special file extension that removes other extensions. For example, `apple-app-site-association.noext.txt` will be uploaded as `apple-app-site-association`. Use this extension for tools that have trouble uploading extensionless files.
          </Note>

        <Warning title="Enterprise Only">This endpoint requires an Enterprise
        workspace.</Warning>


        Required scope: `site_config:write`
      tags:
        - subpackage_sites.subpackage_sites/wellKnown
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
        '201':
          description: File uploaded successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/sites_well-known_put_Response_201'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Set-well-knownRequestBadRequestError'
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Set-well-knownRequestUnauthorizedError'
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Set-well-knownRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Set-well-knownRequestTooManyRequestsError'
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Set-well-knownRequestInternalServerError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                fileName:
                  type: string
                  description: The name of the file
                fileData:
                  type: string
                  description: The contents of the file
                contentType:
                  $ref: >-
                    #/components/schemas/SitesSiteIdWellKnownPutRequestBodyContentApplicationJsonSchemaContentType
                  description: The content type of the file. Defaults to application/json
              required:
                - fileName
                - fileData
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdWellKnownPutRequestBodyContentApplicationJsonSchemaContentType:
      type: string
      enum:
        - application/json
        - text/plain
      default: application/json
      description: The content type of the file. Defaults to application/json
      title: >-
        SitesSiteIdWellKnownPutRequestBodyContentApplicationJsonSchemaContentType
    sites_well-known_put_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: sites_well-known_put_Response_201
    SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaCode
    SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaDetailsItems
    Set-well-knownRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Set-well-knownRequestBadRequestError
    Set-well-knownRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Set-well-knownRequestUnauthorizedError
    Set-well-knownRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Set-well-knownRequestNotFoundError
    Set-well-knownRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Set-well-knownRequestTooManyRequestsError
    Set-well-knownRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdWellKnownPutResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Set-well-knownRequestInternalServerError
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
client.sites.well_known.put(
    site_id="580e63e98c9a982ac9b8b741",
    file_name="apple-app-site-association.txt",
    file_data='{\n  "applinks": {\n    "apps": [],\n    "details": [\n  {\n    "appID": "ABCDE12345.com.example.app",\n    "paths": [ "/*", "/some/path/*" ]\n      }\n    ]\n  }\n}\n',
    content_type="application/json",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.wellKnown.put("580e63e98c9a982ac9b8b741", {
    fileName: "apple-app-site-association.txt",
    fileData: "{\n  \"applinks\": {\n    \"apps\": [],\n    \"details\": [\n  {\n    \"appID\": \"ABCDE12345.com.example.app\",\n    \"paths\": [ \"/*\", \"/some/path/*\" ]\n      }\n    ]\n  }\n}\n",
    contentType: "application/json"
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/well_known"

	payload := strings.NewReader("{\n  \"fileName\": {\n    \"summary\": \"Apple App Site Association\",\n    \"value\": \"apple-app-site-association.txt\"\n  },\n  \"fileData\": {\n    \"summary\": \"Apple App Site Association File Example\",\n    \"value\": \"{\\n  \\\"applinks\\\": {\\n    \\\"apps\\\": [],\\n    \\\"details\\\": [\\n      {\\n        \\\"appID\\\": \\\"ABCDE12345.com.example.app\\\",\\n        \\\"paths\\\": [ \\\"/*\\\", \\\"/some/path/*\\\" ]\\n      }\\n    ]\\n  }\\n}\\n\"\n  }\n}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/well_known")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"fileName\": {\n    \"summary\": \"Apple App Site Association\",\n    \"value\": \"apple-app-site-association.txt\"\n  },\n  \"fileData\": {\n    \"summary\": \"Apple App Site Association File Example\",\n    \"value\": \"{\\n  \\\"applinks\\\": {\\n    \\\"apps\\\": [],\\n    \\\"details\\\": [\\n      {\\n        \\\"appID\\\": \\\"ABCDE12345.com.example.app\\\",\\n        \\\"paths\\\": [ \\\"/*\\\", \\\"/some/path/*\\\" ]\\n      }\\n    ]\\n  }\\n}\\n\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/well_known")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"fileName\": {\n    \"summary\": \"Apple App Site Association\",\n    \"value\": \"apple-app-site-association.txt\"\n  },\n  \"fileData\": {\n    \"summary\": \"Apple App Site Association File Example\",\n    \"value\": \"{\\n  \\\"applinks\\\": {\\n    \\\"apps\\\": [],\\n    \\\"details\\\": [\\n      {\\n        \\\"appID\\\": \\\"ABCDE12345.com.example.app\\\",\\n        \\\"paths\\\": [ \\\"/*\\\", \\\"/some/path/*\\\" ]\\n      }\\n    ]\\n  }\\n}\\n\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/well_known', [
  'body' => '{
  "fileName": {
    "summary": "Apple App Site Association",
    "value": "apple-app-site-association.txt"
  },
  "fileData": {
    "summary": "Apple App Site Association File Example",
    "value": "{\\n  \\"applinks\\": {\\n    \\"apps\\": [],\\n    \\"details\\": [\\n      {\\n        \\"appID\\": \\"ABCDE12345.com.example.app\\",\\n        \\"paths\\": [ \\"/*\\", \\"/some/path/*\\" ]\\n      }\\n    ]\\n  }\\n}\\n"
  }
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

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/well_known");
var request = new RestRequest(Method.PUT);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"fileName\": {\n    \"summary\": \"Apple App Site Association\",\n    \"value\": \"apple-app-site-association.txt\"\n  },\n  \"fileData\": {\n    \"summary\": \"Apple App Site Association File Example\",\n    \"value\": \"{\\n  \\\"applinks\\\": {\\n    \\\"apps\\\": [],\\n    \\\"details\\\": [\\n      {\\n        \\\"appID\\\": \\\"ABCDE12345.com.example.app\\\",\\n        \\\"paths\\\": [ \\\"/*\\\", \\\"/some/path/*\\\" ]\\n      }\\n    ]\\n  }\\n}\\n\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "fileName": [
    "summary": "Apple App Site Association",
    "value": "apple-app-site-association.txt"
  ],
  "fileData": [
    "summary": "Apple App Site Association File Example",
    "value": "{
  \"applinks\": {
    \"apps\": [],
    \"details\": [
      {
        \"appID\": \"ABCDE12345.com.example.app\",
        \"paths\": [ \"/*\", \"/some/path/*\" ]
      }
    ]
  }
}
"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/well_known")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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