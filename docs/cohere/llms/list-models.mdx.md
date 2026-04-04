# Source: https://docs.cohere.com/reference/list-models.mdx

# List Models

GET https://api.cohere.com/v1/models

Returns a list of models available for use.

Reference: https://docs.cohere.com/reference/list-models

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/models:
    get:
      operationId: list
      summary: List Models
      description: Returns a list of models available for use.
      tags:
        - subpackage_models
      parameters:
        - name: page_size
          in: query
          description: |-
            Maximum number of models to include in a page
            Defaults to `20`, min value of `1`, max value of `1000`.
          required: false
          schema:
            type: number
            format: double
        - name: page_token
          in: query
          description: >-
            Page token provided in the `next_page_token` field of a previous
            response.
          required: false
          schema:
            type: string
        - name: endpoint
          in: query
          description: >-
            When provided, filters the list of models to only those that are
            compatible with the specified endpoint.
          required: false
          schema:
            $ref: '#/components/schemas/CompatibleEndpoint'
        - name: default_only
          in: query
          description: >-
            When provided, filters the list of models to only the default model
            to the endpoint. This parameter is only valid when `endpoint` is
            provided.
          required: false
          schema:
            type: boolean
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListModelsResponse'
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
                $ref: '#/components/schemas/List-modelsRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestNotFoundError'
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
                  #/components/schemas/List-modelsRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/List-modelsRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/List-modelsRequestGatewayTimeoutError'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    CompatibleEndpoint:
      type: string
      enum:
        - chat
        - embed
        - classify
        - summarize
        - rerank
        - rate
        - generate
      description: One of the Cohere API endpoints that the model can be used with.
      title: CompatibleEndpoint
    GetModelResponse:
      type: object
      properties:
        name:
          type: string
          description: >-
            Specify this name in the `model` parameter of API requests to use
            your chosen model.
        is_deprecated:
          type: boolean
          description: Whether the model is deprecated or not.
        endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
          description: The API endpoints that the model is compatible with.
        finetuned:
          type: boolean
          description: Whether the model has been fine-tuned or not.
        context_length:
          type: number
          format: double
          description: >-
            The maximum number of tokens that the model can process in a single
            request. Note that not all of these tokens are always available due
            to special tokens and preambles that Cohere has added by default.
        tokenizer_url:
          type: string
          description: Public URL to the tokenizer's configuration file.
        default_endpoints:
          type: array
          items:
            $ref: '#/components/schemas/CompatibleEndpoint'
          description: The API endpoints that the model is default to.
        features:
          type: array
          items:
            type: string
          description: The features that the model supports.
      description: >-
        Contains information about the model and which API endpoints it can be
        used with.
      title: GetModelResponse
    ListModelsResponse:
      type: object
      properties:
        models:
          type: array
          items:
            $ref: '#/components/schemas/GetModelResponse'
        next_page_token:
          type: string
          description: >-
            A token to retrieve the next page of results. Provide in the
            page_token parameter of the next request.
      required:
        - models
      title: ListModelsResponse
    List-modelsRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestBadRequestError
    List-modelsRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestUnauthorizedError
    List-modelsRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestForbiddenError
    List-modelsRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestNotFoundError
    List-modelsRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestUnprocessableEntityError
    List-modelsRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestTooManyRequestsError
    List-modelsRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestInvalidTokenError
    List-modelsRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestClientClosedRequestError
    List-modelsRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestInternalServerError
    List-modelsRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestNotImplementedError
    List-modelsRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestServiceUnavailableError
    List-modelsRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: List-modelsRequestGatewayTimeoutError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python Sync
import cohere

co = cohere.Client()
response = co.models.list()
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.models.list()
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.models.list()

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.ListModelsResponse;

public class ModelsListGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListModelsResponse response = cohere.models().list();

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const models = await cohere.models.list();

  console.log(models);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.models.list({});
}
main();

```

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

	resp, err := co.Models.List(context.TODO(), &cohere.ModelsListRequest{})

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
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

$response = $client->request('GET', 'https://api.cohere.com/v1/models', [
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

var client = new RestClient("https://api.cohere.com/v1/models");
var request = new RestRequest(Method.GET);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/models")! as URL,
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