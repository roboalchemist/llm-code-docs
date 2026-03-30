# Source: https://docs.cohere.com/reference/create-embed-job.mdx

# Create an Embed Job

POST https://api.cohere.com/v1/embed-jobs
Content-Type: application/json

This API launches an async Embed job for a [Dataset](https://docs.cohere.com/docs/datasets) of type `embed-input`. The result of a completed embed job is new Dataset of type `embed-output`, which contains the original text entries and the corresponding embeddings.

Reference: https://docs.cohere.com/reference/create-embed-job

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/embed-jobs:
    post:
      operationId: create
      summary: Create an Embed Job
      description: >-
        This API launches an async Embed job for a
        [Dataset](https://docs.cohere.com/docs/datasets) of type `embed-input`.
        The result of a completed embed job is new Dataset of type
        `embed-output`, which contains the original text entries and the
        corresponding embeddings.
      tags:
        - subpackage_embedJobs
      parameters:
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
                $ref: '#/components/schemas/CreateEmbedJobResponse'
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
                $ref: '#/components/schemas/Create-embed-jobRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-embed-jobRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-embed-jobRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-embed-jobRequestNotFoundError'
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
                  #/components/schemas/Create-embed-jobRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-embed-jobRequestTooManyRequestsError
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-embed-jobRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-embed-jobRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-embed-jobRequestInternalServerError
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-embed-jobRequestNotImplementedError
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-embed-jobRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-embed-jobRequestGatewayTimeoutError
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateEmbedJobRequest'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    EmbedInputType:
      type: string
      enum:
        - search_document
        - search_query
        - classification
        - clustering
        - image
      description: >
        Specifies the type of input passed to the model. Required for embedding
        models v3 and higher.


        - `"search_document"`: Used for embeddings stored in a vector database
        for search use-cases.

        - `"search_query"`: Used for embeddings of search queries run against a
        vector DB to find relevant documents.

        - `"classification"`: Used for embeddings passed through a text
        classifier.

        - `"clustering"`: Used for the embeddings run through a clustering
        algorithm.

        - `"image"`: Used for embeddings with image input.
      title: EmbedInputType
    EmbeddingType:
      type: string
      enum:
        - float
        - int8
        - uint8
        - binary
        - ubinary
        - base64
      title: EmbeddingType
    CreateEmbedJobRequestTruncate:
      type: string
      enum:
        - START
        - END
      default: END
      description: >
        One of `START|END` to specify how the API will handle inputs longer than
        the maximum token length.


        Passing `START` will discard the start of the input. `END` will discard
        the end of the input. In both cases, input is discarded until the
        remaining input is exactly the maximum input token length for the model.
      title: CreateEmbedJobRequestTruncate
    CreateEmbedJobRequest:
      type: object
      properties:
        model:
          type: string
          format: string
          description: |
            ID of the embedding model.

            Available models and corresponding embedding dimensions:

            - `embed-english-v3.0` : 1024
            - `embed-multilingual-v3.0` : 1024
            - `embed-english-light-v3.0` : 384
            - `embed-multilingual-light-v3.0` : 384
        dataset_id:
          type: string
          description: >-
            ID of a [Dataset](https://docs.cohere.com/docs/datasets). The
            Dataset must be of type `embed-input` and must have a validation
            status `Validated`
        input_type:
          $ref: '#/components/schemas/EmbedInputType'
        name:
          type: string
          description: The name of the embed job.
        embedding_types:
          type: array
          items:
            $ref: '#/components/schemas/EmbeddingType'
          description: >-
            Specifies the types of embeddings you want to get back. Not required
            and default is None, which returns the Embed Floats response type.
            Can be one or more of the following types.


            * `"float"`: Use this when you want to get back the default float
            embeddings. Valid for all models.

            * `"int8"`: Use this when you want to get back signed int8
            embeddings. Valid for v3 and newer model versions.

            * `"uint8"`: Use this when you want to get back unsigned int8
            embeddings. Valid for v3 and newer model versions.

            * `"binary"`: Use this when you want to get back signed binary
            embeddings. Valid for v3 and newer model versions.

            * `"ubinary"`: Use this when you want to get back unsigned binary
            embeddings. Valid for v3 and newer model versions.
        truncate:
          $ref: '#/components/schemas/CreateEmbedJobRequestTruncate'
          description: >
            One of `START|END` to specify how the API will handle inputs longer
            than the maximum token length.


            Passing `START` will discard the start of the input. `END` will
            discard the end of the input. In both cases, input is discarded
            until the remaining input is exactly the maximum input token length
            for the model.
      required:
        - model
        - dataset_id
        - input_type
      title: CreateEmbedJobRequest
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
    CreateEmbedJobResponse:
      type: object
      properties:
        job_id:
          type: string
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - job_id
      description: Response from creating an embed job.
      title: CreateEmbedJobResponse
    Create-embed-jobRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestBadRequestError
    Create-embed-jobRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestUnauthorizedError
    Create-embed-jobRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestForbiddenError
    Create-embed-jobRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestNotFoundError
    Create-embed-jobRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestUnprocessableEntityError
    Create-embed-jobRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestTooManyRequestsError
    Create-embed-jobRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestInvalidTokenError
    Create-embed-jobRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestClientClosedRequestError
    Create-embed-jobRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestInternalServerError
    Create-embed-jobRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestNotImplementedError
    Create-embed-jobRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestServiceUnavailableError
    Create-embed-jobRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-embed-jobRequestGatewayTimeoutError
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

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.EmbedJobs.Create(
		context.TODO(),
		&cohere.CreateEmbedJobRequest{
			DatasetId: "dataset_id",
			Model:     "embed-english-v3.0",
			InputType: cohere.EmbedInputTypeSearchDocument,
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# start an embed job
job = co.embed_jobs.create(
    dataset_id="my-dataset-id", input_type="search_document", model="embed-english-v3.0"
)

# poll the server until the job is complete
response = co.wait(job)

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    # start an embed job
    job = await co.embed_jobs.create(
        dataset_id="my-dataset-id",
        input_type="search_document",
        model="embed-english-v3.0",
    )

    # poll the server until the job is complete
    response = await co.wait(job)

    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.embed_jobs.create(
    model="embed-english-v3.0",
    dataset_id="dataset-12345",
    input_type="search_document"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.embedjobs.requests.CreateEmbedJobRequest;
import com.cohere.api.types.CreateEmbedJobResponse;
import com.cohere.api.types.EmbedInputType;

public class EmbedJobsPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    CreateEmbedJobResponse response =
        cohere
            .embedJobs()
            .create(
                CreateEmbedJobRequest.builder()
                    .model("embed-v4.0")
                    .datasetId("ds.id")
                    .inputType(EmbedInputType.SEARCH_DOCUMENT)
                    .build());

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embedJob = await cohere.embedJobs.create({
    datasetId: 'my-dataset',
    inputType: 'search_document',
    model: 'embed-v4.0',
  });

  console.log(embedJob);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.embedJobs.create({
        model: "embed-english-v3.0",
        datasetId: "dataset-12345",
        inputType: "search_document",
    });
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/embed-jobs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"embed-english-v3.0\",\n  \"dataset_id\": \"dataset-12345\",\n  \"input_type\": \"search_document\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/embed-jobs', [
  'body' => '{
  "model": "embed-english-v3.0",
  "dataset_id": "dataset-12345",
  "input_type": "search_document"
}',
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

var client = new RestClient("https://api.cohere.com/v1/embed-jobs");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"embed-english-v3.0\",\n  \"dataset_id\": \"dataset-12345\",\n  \"input_type\": \"search_document\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "model": "embed-english-v3.0",
  "dataset_id": "dataset-12345",
  "input_type": "search_document"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/embed-jobs")! as URL,
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