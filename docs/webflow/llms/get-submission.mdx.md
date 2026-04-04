# Source: https://developers.webflow.com/data/reference/forms/form-submissions/get-submission.mdx

# Get Form Submission

GET https://api.webflow.com/v2/sites/{site_id}/form_submissions/{form_submission_id}

Get information about a form submission within a specific site.

Required scope | `forms:read`


Reference: https://developers.webflow.com/data/reference/forms/form-submissions/get-submission

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/form_submissions/{form_submission_id}:
    get:
      operationId: get-submission
      summary: Get Form Submission by Site
      description: |
        Get information about a form submission within a specific site.

        Required scope | `forms:read`
      tags:
        - subpackage_sites.subpackage_sites/forms
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: objectid
        - name: form_submission_id
          in: path
          description: Unique identifier for a Form Submission
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
                $ref: '#/components/schemas/sites_forms_get-submission_Response_200'
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-form-submission-by-siteRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-form-submission-by-siteRequestUnauthorizedError
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-form-submission-by-siteRequestForbiddenError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-form-submission-by-siteRequestNotFoundError
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-form-submission-by-siteRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-form-submission-by-siteRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaFormResponse:
      type: object
      properties: {}
      description: The data submitted in the Form
      title: >-
        SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaFormResponse
    sites_forms_get-submission_Response_200:
      type: object
      properties:
        id:
          type: string
          format: objectid
          description: The unique ID of the Form submission
        displayName:
          type: string
          description: The Form name displayed on the site
        siteId:
          type: string
          format: objectid
          description: The unique ID of the Site the Form belongs to
        workspaceId:
          type: string
          format: objectid
          description: The unique ID of the Workspace the Site belongs to
        dateSubmitted:
          type: string
          format: date-time
          description: Date that the Form was submitted on
        formResponse:
          $ref: >-
            #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaFormResponse
          description: The data submitted in the Form
      description: A form submission
      title: sites_forms_get-submission_Response_200
    SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode:
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
      title: >-
        SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: >-
        SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems
    Get-form-submission-by-siteRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-form-submission-by-siteRequestBadRequestError
    Get-form-submission-by-siteRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-form-submission-by-siteRequestUnauthorizedError
    Get-form-submission-by-siteRequestForbiddenError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-form-submission-by-siteRequestForbiddenError
    Get-form-submission-by-siteRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-form-submission-by-siteRequestNotFoundError
    Get-form-submission-by-siteRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-form-submission-by-siteRequestTooManyRequestsError
    Get-form-submission-by-siteRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdFormSubmissionsFormSubmissionIdGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: Get-form-submission-by-siteRequestInternalServerError
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
client.sites.forms.get_submission(
    site_id="580e63e98c9a982ac9b8b741",
    form_submission_id="580e63e98c9a982ac9b8b741",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.forms.getSubmission("580e63e98c9a982ac9b8b741", "580e63e98c9a982ac9b8b741");

```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/form_submissions/580e63e98c9a982ac9b8b741"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/form_submissions/580e63e98c9a982ac9b8b741")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/form_submissions/580e63e98c9a982ac9b8b741")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/form_submissions/580e63e98c9a982ac9b8b741', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/form_submissions/580e63e98c9a982ac9b8b741");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/form_submissions/580e63e98c9a982ac9b8b741")! as URL,
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