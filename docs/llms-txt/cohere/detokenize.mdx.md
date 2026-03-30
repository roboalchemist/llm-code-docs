# Source: https://docs.cohere.com/reference/detokenize.mdx

# Detokenize

POST https://api.cohere.com/v1/detokenize
Content-Type: application/json

This endpoint takes tokens using byte-pair encoding and returns their text representation. To learn more about tokenization and byte pair encoding, see the tokens page.

Reference: https://docs.cohere.com/reference/detokenize

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/detokenize:
    post:
      operationId: detokenize
      summary: Detokenize
      description: >-
        This endpoint takes tokens using byte-pair encoding and returns their
        text representation. To learn more about tokenization and byte pair
        encoding, see the tokens page.
      tags:
        - ''
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
                $ref: '#/components/schemas/detokenize_Response_200'
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
                $ref: '#/components/schemas/DetokenizeRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestNotFoundError'
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
                $ref: '#/components/schemas/DetokenizeRequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DetokenizeRequestGatewayTimeoutError'
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                tokens:
                  type: array
                  items:
                    type: integer
                  description: The list of tokens to be detokenized.
                model:
                  type: string
                  description: >-
                    An optional parameter to provide the model name. This will
                    ensure that the detokenization is done by the tokenizer used
                    by that model.
              required:
                - tokens
                - model
servers:
  - url: https://api.cohere.com
components:
  schemas:
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
    detokenize_Response_200:
      type: object
      properties:
        text:
          type: string
          description: A string representing the list of tokens.
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - text
      title: detokenize_Response_200
    DetokenizeRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestBadRequestError
    DetokenizeRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestUnauthorizedError
    DetokenizeRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestForbiddenError
    DetokenizeRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestNotFoundError
    DetokenizeRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestUnprocessableEntityError
    DetokenizeRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestTooManyRequestsError
    DetokenizeRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestInvalidTokenError
    DetokenizeRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestClientClosedRequestError
    DetokenizeRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestInternalServerError
    DetokenizeRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestNotImplementedError
    DetokenizeRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestServiceUnavailableError
    DetokenizeRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: DetokenizeRequestGatewayTimeoutError
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

	resp, err := co.Detokenize(
		context.TODO(),
		&cohere.DetokenizeRequest{
			Tokens: []int{10002, 1706, 1722, 5169, 4328},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const detokenize = await cohere.detokenize({
    tokens: [10002, 2261, 2012, 8, 2792, 43],
    model: 'command',
  });

  console.log(detokenize);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.detokenize({
        tokens: [
            10002,
            2261,
            2012,
            8,
            2792,
            43,
        ],
        model: "command",
    });
}
main();

```

```python Sync
import cohere

co = cohere.Client()

response = co.detokenize(
    tokens=[8466, 5169, 2594, 8, 2792, 43], model="command-a-03-2025"  # optional
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.detokenize(
        tokens=[8466, 5169, 2594, 8, 2792, 43],
        model="command-a-03-2025",  # optional
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.detokenize(
    tokens=[
        10002,
        2261,
        2012,
        8,
        2792,
        43
    ],
    model="command"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.DetokenizeRequest;
import com.cohere.api.types.DetokenizeResponse;
import java.util.List;

public class DetokenizePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DetokenizeResponse response =
        cohere.detokenize(
            DetokenizeRequest.builder()
                .model("command-a-03-2025")
                .tokens(List.of(8466, 5169, 2594, 8, 2792, 43))
                .build());

    System.out.println(response);
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/detokenize")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tokens\": [\n    10002,\n    2261,\n    2012,\n    8,\n    2792,\n    43\n  ],\n  \"model\": \"command\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/detokenize', [
  'body' => '{
  "tokens": [
    10002,
    2261,
    2012,
    8,
    2792,
    43
  ],
  "model": "command"
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

var client = new RestClient("https://api.cohere.com/v1/detokenize");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"tokens\": [\n    10002,\n    2261,\n    2012,\n    8,\n    2792,\n    43\n  ],\n  \"model\": \"command\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "tokens": [10002, 2261, 2012, 8, 2792, 43],
  "model": "command"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/detokenize")! as URL,
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