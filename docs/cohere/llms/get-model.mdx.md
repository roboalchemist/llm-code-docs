# Source: https://docs.cohere.com/reference/get-model.mdx

# Get a Model

GET https://api.cohere.com/v1/models/{model}

Returns the details of a model, provided its name.

Reference: https://docs.cohere.com/reference/get-model

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/models/{model}:
    get:
      operationId: get
      summary: Get a Model
      description: Returns the details of a model, provided its name.
      tags:
        - subpackage_models
      parameters:
        - name: model
          in: path
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
                $ref: '#/components/schemas/GetModelResponse'
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
                $ref: '#/components/schemas/Get-modelRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestNotFoundError'
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
                $ref: '#/components/schemas/Get-modelRequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-modelRequestGatewayTimeoutError'
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
    Get-modelRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestBadRequestError
    Get-modelRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestUnauthorizedError
    Get-modelRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestForbiddenError
    Get-modelRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestNotFoundError
    Get-modelRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestUnprocessableEntityError
    Get-modelRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestTooManyRequestsError
    Get-modelRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestInvalidTokenError
    Get-modelRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestClientClosedRequestError
    Get-modelRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestInternalServerError
    Get-modelRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestNotImplementedError
    Get-modelRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestServiceUnavailableError
    Get-modelRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-modelRequestGatewayTimeoutError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python Sync
from cohere import Client

client = Client()

response = client.models.get(
    model="command-a-03-2025",
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.models.get(
    model="command-a-03-2025",
)
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.models.get(
    model="command-a-03-2025"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.GetModelResponse;

public class ModelsGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    GetModelResponse response = cohere.models().get("command-a-03-2025");
    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const model = await cohere.models.get('command-a-03-2025');

  console.log(model);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.models.get("command-a-03-2025");
}
main();

```

```go Cohere Go SDK
package main

import (
	"context"
	"log"

	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken("<<apiKey>>"))

	resp, err := co.Models.Get(context.TODO(), "command-a-03-2025")

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/models/command-a-03-2025")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/models/command-a-03-2025', [
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

var client = new RestClient("https://api.cohere.com/v1/models/command-a-03-2025");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/models/command-a-03-2025")! as URL,
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