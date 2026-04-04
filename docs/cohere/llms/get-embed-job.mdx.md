# Source: https://docs.cohere.com/reference/get-embed-job.mdx

# Fetch an Embed Job

GET https://api.cohere.com/v1/embed-jobs/{id}

This API retrieves the details about an embed job started by the same user.

Reference: https://docs.cohere.com/reference/get-embed-job

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/embed-jobs/{id}:
    get:
      operationId: get
      summary: Fetch an Embed Job
      description: >-
        This API retrieves the details about an embed job started by the same
        user.
      tags:
        - subpackage_embedJobs
      parameters:
        - name: id
          in: path
          description: The ID of the embed job to retrieve.
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
                $ref: '#/components/schemas/EmbedJob'
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
                $ref: '#/components/schemas/Get-embed-jobRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestNotFoundError'
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
                  #/components/schemas/Get-embed-jobRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-embed-jobRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-embed-jobRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-embed-jobRequestGatewayTimeoutError'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    EmbedJobStatus:
      type: string
      enum:
        - processing
        - complete
        - cancelling
        - cancelled
        - failed
      description: The status of the embed job
      title: EmbedJobStatus
    EmbedJobTruncate:
      type: string
      enum:
        - START
        - END
      description: The truncation option used
      title: EmbedJobTruncate
    ApiMetaApiVersion:
      type: object
      properties:
        version:
          type: string
        is_deprecated:
          type: boolean
        is_experimental:
          type: boolean
      required:
        - version
      title: ApiMetaApiVersion
    ApiMetaBilledUnits:
      type: object
      properties:
        images:
          type: number
          format: double
          description: |
            The number of billed images.
        input_tokens:
          type: number
          format: double
          description: |
            The number of billed input tokens.
        image_tokens:
          type: number
          format: double
          description: |
            The number of billed image tokens.
        output_tokens:
          type: number
          format: double
          description: |
            The number of billed output tokens.
        search_units:
          type: number
          format: double
          description: |
            The number of billed search units.
        classifications:
          type: number
          format: double
          description: |
            The number of billed classifications units.
      title: ApiMetaBilledUnits
    ApiMetaTokens:
      type: object
      properties:
        input_tokens:
          type: number
          format: double
          description: |
            The number of tokens used as input to the model.
        output_tokens:
          type: number
          format: double
          description: |
            The number of tokens produced by the model.
      title: ApiMetaTokens
    ApiMeta:
      type: object
      properties:
        api_version:
          $ref: '#/components/schemas/ApiMetaApiVersion'
        billed_units:
          $ref: '#/components/schemas/ApiMetaBilledUnits'
        tokens:
          $ref: '#/components/schemas/ApiMetaTokens'
        cached_tokens:
          type: number
          format: double
          description: |
            The number of prompt tokens that hit the inference cache.
        warnings:
          type: array
          items:
            type: string
      title: ApiMeta
    EmbedJob:
      type: object
      properties:
        job_id:
          type: string
          description: ID of the embed job
        name:
          type: string
          description: The name of the embed job
        status:
          $ref: '#/components/schemas/EmbedJobStatus'
          description: The status of the embed job
        created_at:
          type: string
          format: date-time
          description: The creation date of the embed job
        input_dataset_id:
          type: string
          description: ID of the input dataset
        output_dataset_id:
          type: string
          description: ID of the resulting output dataset
        model:
          type: string
          description: ID of the model used to embed
        truncate:
          $ref: '#/components/schemas/EmbedJobTruncate'
          description: The truncation option used
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - job_id
        - status
        - created_at
        - input_dataset_id
        - model
        - truncate
      title: EmbedJob
    Get-embed-jobRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestBadRequestError
    Get-embed-jobRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestUnauthorizedError
    Get-embed-jobRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestForbiddenError
    Get-embed-jobRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestNotFoundError
    Get-embed-jobRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestUnprocessableEntityError
    Get-embed-jobRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestTooManyRequestsError
    Get-embed-jobRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestInvalidTokenError
    Get-embed-jobRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestClientClosedRequestError
    Get-embed-jobRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestInternalServerError
    Get-embed-jobRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestNotImplementedError
    Get-embed-jobRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestServiceUnavailableError
    Get-embed-jobRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-embed-jobRequestGatewayTimeoutError
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

	resp, err := co.EmbedJobs.List(context.TODO())

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# get embed job
response = co.embed_jobs.get("job_id")

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.embed_jobs.get("job_id")

    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.embed_jobs.get(
    id="id"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.ListEmbedJobResponse;

public class EmbedJobsGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListEmbedJobResponse response = cohere.embedJobs().list();

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embedJob = await cohere.embedJobs.get('job_id');

  console.log(embedJob);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.embedJobs.get("id");
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/embed-jobs/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
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

$response = $client->request('GET', 'https://api.cohere.com/v1/embed-jobs/id', [
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

var client = new RestClient("https://api.cohere.com/v1/embed-jobs/id");
var request = new RestRequest(Method.GET);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/embed-jobs/id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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