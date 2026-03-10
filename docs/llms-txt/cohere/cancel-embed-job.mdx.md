# Source: https://docs.cohere.com/reference/cancel-embed-job.mdx

# Cancel an Embed Job

POST https://api.cohere.com/v1/embed-jobs/{id}/cancel

This API allows users to cancel an active embed job. Once invoked, the embedding process will be terminated, and users will be charged for the embeddings processed up to the cancellation point. It's important to note that partial results will not be available to users after cancellation.

Reference: https://docs.cohere.com/reference/cancel-embed-job

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/embed-jobs/{id}/cancel:
    post:
      operationId: cancel
      summary: Cancel an Embed Job
      description: >-
        This API allows users to cancel an active embed job. Once invoked, the
        embedding process will be terminated, and users will be charged for the
        embeddings processed up to the cancellation point. It's important to
        note that partial results will not be available to users after
        cancellation.
      tags:
        - subpackage_embedJobs
      parameters:
        - name: id
          in: path
          description: The ID of the embed job to cancel.
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/embed-jobs_cancel_Response_200'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Cancel-embed-jobRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Cancel-embed-jobRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Cancel-embed-jobRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Cancel-embed-jobRequestNotFoundError'
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Cancel-embed-jobRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Cancel-embed-jobRequestTooManyRequestsError
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Cancel-embed-jobRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Cancel-embed-jobRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Cancel-embed-jobRequestInternalServerError
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Cancel-embed-jobRequestNotImplementedError
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Cancel-embed-jobRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Cancel-embed-jobRequestGatewayTimeoutError
servers:
  - url: https://api.cohere.com
components:
  schemas:
    embed-jobs_cancel_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: embed-jobs_cancel_Response_200
    Cancel-embed-jobRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestBadRequestError
    Cancel-embed-jobRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestUnauthorizedError
    Cancel-embed-jobRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestForbiddenError
    Cancel-embed-jobRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestNotFoundError
    Cancel-embed-jobRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestUnprocessableEntityError
    Cancel-embed-jobRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestTooManyRequestsError
    Cancel-embed-jobRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestInvalidTokenError
    Cancel-embed-jobRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestClientClosedRequestError
    Cancel-embed-jobRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestInternalServerError
    Cancel-embed-jobRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestNotImplementedError
    Cancel-embed-jobRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestServiceUnavailableError
    Cancel-embed-jobRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Cancel-embed-jobRequestGatewayTimeoutError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	err := co.EmbedJobs.Cancel(context.TODO(), "embed_job_id")

	if err != nil {
		log.Fatal(err)
	}

}

```

```python Sync
import cohere

co = cohere.Client()

# cancel an embed job
co.embed_jobs.cancel("job_id")

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    await co.embed_jobs.cancel("job_id")

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.embed_jobs.cancel(
    id="id"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;

public class EmbedJobsCancel {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere.embedJobs().cancel("job_id");
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embedJob = await cohere.embedJobs.cancel('job_id');

  console.log(embedJob);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.embedJobs.cancel("id");
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/embed-jobs/id/cancel")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/embed-jobs/id/cancel', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cohere.com/v1/embed-jobs/id/cancel");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/embed-jobs/id/cancel")! as URL,
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