# Source: https://docs.cohere.com/reference/tokenize.mdx

# Tokenize

POST https://api.cohere.com/v1/tokenize
Content-Type: application/json

This endpoint splits input text into smaller units called tokens using byte-pair encoding (BPE). To learn more about tokenization and byte pair encoding, see the tokens page.

Reference: https://docs.cohere.com/reference/tokenize

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/tokenize:
    post:
      operationId: tokenize
      summary: Tokenize
      description: >-
        This endpoint splits input text into smaller units called tokens using
        byte-pair encoding (BPE). To learn more about tokenization and byte pair
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
                $ref: '#/components/schemas/tokenize_Response_200'
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
                $ref: '#/components/schemas/TokenizeRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestNotFoundError'
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
                $ref: '#/components/schemas/TokenizeRequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenizeRequestGatewayTimeoutError'
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                text:
                  type: string
                  description: >-
                    The string to be tokenized, the minimum text length is 1
                    character, and the maximum text length is 65536 characters.
                model:
                  type: string
                  description: >-
                    The input will be tokenized by the tokenizer that is used by
                    this model.
              required:
                - text
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
    tokenize_Response_200:
      type: object
      properties:
        tokens:
          type: array
          items:
            type: integer
          description: An array of tokens, where each token is an integer.
        token_strings:
          type: array
          items:
            type: string
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - tokens
        - token_strings
      title: tokenize_Response_200
    TokenizeRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestBadRequestError
    TokenizeRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestUnauthorizedError
    TokenizeRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestForbiddenError
    TokenizeRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestNotFoundError
    TokenizeRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestUnprocessableEntityError
    TokenizeRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestTooManyRequestsError
    TokenizeRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestInvalidTokenError
    TokenizeRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestClientClosedRequestError
    TokenizeRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestInternalServerError
    TokenizeRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestNotImplementedError
    TokenizeRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestServiceUnavailableError
    TokenizeRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: TokenizeRequestGatewayTimeoutError
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

	resp, err := co.Tokenize(
		context.TODO(),
		&cohere.TokenizeRequest{
			Text:  "cohere <3",
			Model: "base",
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
  const tokenize = await cohere.tokenize({
    text: 'tokenize me! :D',
    model: 'command', // optional
  });

  console.log(tokenize);
})();

```

```typescript Cohere Node.js SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const tokenize = await cohere.tokenize({
    text: 'tokenize me! :D',
    model: 'command', // optional
  });

  console.log(tokenize);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.tokenize({
        text: "tokenize me! :D",
        model: "command",
    });
}
main();

```

```python Sync
import cohere

co = cohere.Client()

response = co.tokenize(
    text="tokenize me! :D", model="command-a-03-2025"
)  # optional
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.tokenize(text="tokenize me! :D", model="command-a-03-2025")
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.tokenize(
    text="tokenize me! :D",
    model="command"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.TokenizeRequest;
import com.cohere.api.types.TokenizeResponse;

public class TokenizePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    TokenizeResponse response =
        cohere.tokenize(
            TokenizeRequest.builder().text("tokenize me").model("command-a-03-2025").build());

    System.out.println(response);
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/tokenize")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"tokenize me! :D\",\n  \"model\": \"command\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/tokenize', [
  'body' => '{
  "text": "tokenize me! :D",
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

var client = new RestClient("https://api.cohere.com/v1/tokenize");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"tokenize me! :D\",\n  \"model\": \"command\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "text": "tokenize me! :D",
  "model": "command"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/tokenize")! as URL,
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