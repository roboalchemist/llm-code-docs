# Source: https://developers.webflow.com/data/reference/comments/list-comment-threads.mdx

# List Comment Threads

GET https://api.webflow.com/v2/sites/{site_id}/comments

List all comment threads for a site.

<Note title="Timing of comment threads">
  There may be a delay of up to 5 minutes before new comments appear in the system.
</Note>

Required scope | `comments:read`


Reference: https://developers.webflow.com/data/reference/comments/list-comment-threads

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/comments:
    get:
      operationId: list-comment-threads
      summary: List Comment Threads
      description: |
        List all comment threads for a site.

        <Note title="Timing of comment threads">
          There may be a delay of up to 5 minutes before new comments appear in the system.
        </Note>

        Required scope | `comments:read`
      tags:
        - subpackage_sites.subpackage_sites/comments
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
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
        - name: sortBy
          in: query
          description: >-
            Sort results by the provided value. Only allowed when sortOrder is
            provided.
          required: false
          schema:
            $ref: '#/components/schemas/SitesSiteIdCommentsGetParametersSortBy'
        - name: sortOrder
          in: query
          description: Sorts the results by asc or desc
          required: false
          schema:
            $ref: '#/components/schemas/SitesSiteIdCommentsGetParametersSortOrder'
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
                  #/components/schemas/sites_comments_list-comment-threads_Response_200
        '400':
          description: Request body was incorrectly formatted.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-comment-threadsRequestBadRequestError
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-comment-threadsRequestUnauthorizedError
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-comment-threadsRequestNotFoundError'
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-comment-threadsRequestTooManyRequestsError
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-comment-threadsRequestInternalServerError
servers:
  - url: https://api.webflow.com/v2
components:
  schemas:
    SitesSiteIdCommentsGetParametersSortBy:
      type: string
      enum:
        - createdOn
        - lastUpdated
      title: SitesSiteIdCommentsGetParametersSortBy
    SitesSiteIdCommentsGetParametersSortOrder:
      type: string
      enum:
        - asc
        - desc
      title: SitesSiteIdCommentsGetParametersSortOrder
    SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItemsAuthor:
      type: object
      properties:
        userId:
          type: string
          description: The unique identifier of the author
        email:
          type: string
          description: Email of the author
        name:
          type: string
          description: Name of the author
      required:
        - userId
        - email
        - name
      title: >-
        SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItemsAuthor
    SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItemsMentionedUsersItems:
      type: object
      properties:
        userId:
          type: string
          description: The unique identifier of the mentioned user
        email:
          type: string
          description: Email of the user
        name:
          type: string
          description: Name of the  User
      required:
        - userId
        - email
        - name
      title: >-
        SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItemsMentionedUsersItems
    SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItems:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the comment thread
        siteId:
          type: string
          description: The site unique identifier
        pageId:
          type: string
          description: The page unique identifier
        localeId:
          type:
            - string
            - 'null'
          description: The locale unique identifier
        itemId:
          type:
            - string
            - 'null'
          description: The item unique identifier
        breakpoint:
          type: string
          description: The breakpoint the comment was left on
        url:
          type: string
          description: The URL of the page the comment was left on
        content:
          type: string
          description: The content of the comment reply
        isResolved:
          type: boolean
          default: false
          description: Boolean determining if the comment thread is resolved
        author:
          $ref: >-
            #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItemsAuthor
        mentionedUsers:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItemsMentionedUsersItems
          description: >-
            List of mentioned users. This is an empty array until email
            notifications are sent, which can take up to 5 minutes after the
            comment is created.
        createdOn:
          type: string
          format: date-string
          description: The date the item was created
        lastUpdated:
          type: string
          format: date-string
          description: The date the item was last updated
      required:
        - id
        - siteId
        - pageId
        - localeId
        - itemId
        - breakpoint
        - url
        - content
        - isResolved
        - author
        - mentionedUsers
        - createdOn
        - lastUpdated
      description: >
        A comment thread represents a conversation between users on a specific
        page. Each comment thread has a unique identifier and can contain
        multiple comments. Retrieve comment replies using the replies API
        endpoint.
      title: SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItems
    SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaPagination:
      type: object
      properties:
        limit:
          type: integer
          default: 100
          description: The limit specified in the request (default 100)
        offset:
          type: integer
          default: 0
          description: The offset specified for pagination
        total:
          type: integer
          description: Total number of comment threads
      required:
        - limit
        - offset
        - total
      title: SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaPagination
    sites_comments_list-comment-threads_Response_200:
      type: object
      properties:
        comments:
          type: array
          items:
            $ref: >-
              #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCommentsItems
        pagination:
          $ref: >-
            #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaPagination
      required:
        - comments
        - pagination
      description: >
        A list of comment threads on the site. Contains the content of the first
        reply.
      title: sites_comments_list-comment-threads_Response_200
    SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCode:
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
      title: SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCode
    SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaDetailsItems:
      oneOf:
        - type: string
        - type: object
          additionalProperties:
            description: Any type
      title: SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaDetailsItems
    List-comment-threadsRequestBadRequestError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-comment-threadsRequestBadRequestError
    List-comment-threadsRequestUnauthorizedError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-comment-threadsRequestUnauthorizedError
    List-comment-threadsRequestNotFoundError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-comment-threadsRequestNotFoundError
    List-comment-threadsRequestTooManyRequestsError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-comment-threadsRequestTooManyRequestsError
    List-comment-threadsRequestInternalServerError:
      type: object
      properties:
        code:
          $ref: >-
            #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaCode
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
              #/components/schemas/SitesSiteIdCommentsGetResponsesContentApplicationJsonSchemaDetailsItems
          description: Array of errors
      title: List-comment-threadsRequestInternalServerError
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
client.sites.comments.list_comment_threads(
    site_id="580e63e98c9a982ac9b8b741",
    locale_id="65427cf400e02b306eaa04a0",
    offset=1,
    limit=1,
    sort_by="createdOn",
    sort_order="asc",
)

```

```typescript
import { WebflowClient } from "webflow-api";

const client = new WebflowClient({ accessToken: "YOUR_ACCESS_TOKEN" });
await client.sites.comments.listCommentThreads("580e63e98c9a982ac9b8b741", {
    localeId: "65427cf400e02b306eaa04a0",
    offset: 1,
    limit: 1,
    sortBy: "createdOn",
    sortOrder: "asc"
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

	url := "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/comments?localeId=65427cf400e02b306eaa04a0&offset=0&limit=100"

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

url = URI("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/comments?localeId=65427cf400e02b306eaa04a0&offset=0&limit=100")

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

HttpResponse<String> response = Unirest.get("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/comments?localeId=65427cf400e02b306eaa04a0&offset=0&limit=100")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/comments?localeId=65427cf400e02b306eaa04a0&offset=0&limit=100', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/comments?localeId=65427cf400e02b306eaa04a0&offset=0&limit=100");
var request = new RestRequest(Method.GET);
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Authorization": "Bearer <token>"]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/v2/sites/580e63e98c9a982ac9b8b741/comments?localeId=65427cf400e02b306eaa04a0&offset=0&limit=100")! as URL,
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