# Source: https://docs.cohere.com/reference/generate-v1.mdx

# generate

POST https://api.cohere.com/v1/generate
Content-Type: application/json

<Warning>
This API is marked as "Legacy" and is no longer maintained. Follow the [migration guide](https://docs.cohere.com/docs/migrating-from-cogenerate-to-cochat) to start using the Chat API.
</Warning>
Generates realistic text conditioned on a given input.


Reference: https://docs.cohere.com/reference/generate-v1

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/generate:
    post:
      operationId: generate
      summary: Generate
      description: >
        <Warning>

        This API is marked as "Legacy" and is no longer maintained. Follow the
        [migration
        guide](https://docs.cohere.com/docs/migrating-from-cogenerate-to-cochat)
        to start using the Chat API.

        </Warning>

        Generates realistic text conditioned on a given input.
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
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/generate_Response_stream'
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
                $ref: '#/components/schemas/GenerateRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestNotFoundError'
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
                $ref: '#/components/schemas/GenerateRequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateRequestGatewayTimeoutError'
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                prompt:
                  type: string
                  description: >
                    The input text that serves as the starting point for
                    generating the response.

                    Note: The prompt will be pre-processed and modified before
                    reaching the model.
                model:
                  type: string
                  description: >-
                    The identifier of the model to generate with. Currently
                    available models are `command` (default), `command-nightly`
                    (experimental), `command-light`, and `command-light-nightly`
                    (experimental).

                    Smaller, "light" models are faster, while larger models will
                    perform better. [Custom
                    models](https://docs.cohere.com/docs/training-custom-models)
                    can also be supplied with their full ID.
                num_generations:
                  type: integer
                  description: >
                    The maximum number of generations that will be returned.
                    Defaults to `1`, min value of `1`, max value of `5`.
                stream:
                  type: boolean
                  enum:
                    - false
                  description: >
                    When `true`, the response will be a JSON stream of events.
                    Streaming is beneficial for user interfaces that render the
                    contents of the response piece by piece, as it gets
                    generated.


                    The final event will contain the complete response, and will
                    contain an `is_finished` field set to `true`. The event will
                    also contain a `finish_reason`, which can be one of the
                    following:

                    - `COMPLETE` - the model sent back a finished reply

                    - `MAX_TOKENS` - the reply was cut off because the model
                    reached the maximum number of tokens for its context length

                    - `ERROR` - something went wrong when generating the reply

                    - `ERROR_TOXIC` - the model generated a reply that was
                    deemed toxic
                max_tokens:
                  type: integer
                  description: >
                    The maximum number of tokens the model will generate as part
                    of the response. Note: Setting a low value may result in
                    incomplete generations.


                    This parameter is off by default, and if it's not specified,
                    the model will continue generating until it emits an EOS
                    completion token. See [BPE Tokens](/bpe-tokens-wiki) for
                    more details.


                    Can only be set to `0` if `return_likelihoods` is set to
                    `ALL` to get the likelihood of the prompt.
                truncate:
                  $ref: >-
                    #/components/schemas/V1GeneratePostRequestBodyContentApplicationJsonSchemaTruncate
                  description: >-
                    One of `NONE|START|END` to specify how the API will handle
                    inputs longer than the maximum token length.


                    Passing `START` will discard the start of the input. `END`
                    will discard the end of the input. In both cases, input is
                    discarded until the remaining input is exactly the maximum
                    input token length for the model.


                    If `NONE` is selected, when the input exceeds the maximum
                    input token length an error will be returned.
                temperature:
                  type: number
                  format: double
                  description: >
                    A non-negative float that tunes the degree of randomness in
                    generation. Lower temperatures mean less random generations.
                    See [Temperature](/temperature-wiki) for more details.

                    Defaults to `0.75`, min value of `0.0`, max value of `5.0`.
                seed:
                  type: integer
                  description: >
                    If specified, the backend will make a best effort to sample
                    tokens

                    deterministically, such that repeated requests with the same

                    seed and parameters should return the same result. However,

                    determinism cannot be totally guaranteed.

                    Compatible Deployments: Cohere Platform, Azure, AWS
                    Sagemaker/Bedrock, Private Deployments
                preset:
                  type: string
                  description: >
                    Identifier of a custom preset. A preset is a combination of
                    parameters, such as prompt, temperature etc. You can create
                    presets in the
                    [playground](https://dashboard.cohere.com/playground/generate).

                    When a preset is specified, the `prompt` parameter becomes
                    optional, and any included parameters will override the
                    preset's parameters.
                end_sequences:
                  type: array
                  items:
                    type: string
                  description: >-
                    The generated text will be cut at the beginning of the
                    earliest occurrence of an end sequence. The sequence will be
                    excluded from the text.
                stop_sequences:
                  type: array
                  items:
                    type: string
                  description: >-
                    The generated text will be cut at the end of the earliest
                    occurrence of a stop sequence. The sequence will be included
                    the text.
                k:
                  type: integer
                  description: >
                    Ensures only the top `k` most likely tokens are considered
                    for generation at each step.

                    Defaults to `0`, min value of `0`, max value of `500`.
                p:
                  type: number
                  format: double
                  description: >
                    Ensures that only the most likely tokens, with total
                    probability mass of `p`, are considered for generation at
                    each step. If both `k` and `p` are enabled, `p` acts after
                    `k`.

                    Defaults to `0.75`. min value of `0.01`, max value of
                    `0.99`.
                frequency_penalty:
                  type: number
                  format: double
                  description: >
                    Used to reduce repetitiveness of generated tokens. The
                    higher the value, the stronger a penalty is applied to
                    previously present tokens, proportional to how many times
                    they have already appeared in the prompt or prior
                    generation.


                    Using `frequency_penalty` in combination with
                    `presence_penalty` is not supported on newer models.
                presence_penalty:
                  type: number
                  format: double
                  description: >
                    Defaults to `0.0`, min value of `0.0`, max value of `1.0`.


                    Can be used to reduce repetitiveness of generated tokens.
                    Similar to `frequency_penalty`, except that this penalty is
                    applied equally to all tokens that have already appeared,
                    regardless of their exact frequencies.


                    Using `frequency_penalty` in combination with
                    `presence_penalty` is not supported on newer models.
                return_likelihoods:
                  $ref: >-
                    #/components/schemas/V1GeneratePostRequestBodyContentApplicationJsonSchemaReturnLikelihoods
                  description: >-
                    One of `GENERATION|NONE` to specify how and if the token
                    likelihoods are returned with the response. Defaults to
                    `NONE`.


                    If `GENERATION` is selected, the token likelihoods will only
                    be provided for generated text.


                    WARNING: `ALL` is deprecated, and will be removed in a
                    future release.
                raw_prompting:
                  type: boolean
                  description: >-
                    When enabled, the user's prompt will be sent to the model
                    without any pre-processing.
              required:
                - prompt
                - stream
servers:
  - url: https://api.cohere.com
components:
  schemas:
    V1GeneratePostRequestBodyContentApplicationJsonSchemaTruncate:
      type: string
      enum:
        - NONE
        - START
        - END
      default: END
      description: >-
        One of `NONE|START|END` to specify how the API will handle inputs longer
        than the maximum token length.


        Passing `START` will discard the start of the input. `END` will discard
        the end of the input. In both cases, input is discarded until the
        remaining input is exactly the maximum input token length for the model.


        If `NONE` is selected, when the input exceeds the maximum input token
        length an error will be returned.
      title: V1GeneratePostRequestBodyContentApplicationJsonSchemaTruncate
    V1GeneratePostRequestBodyContentApplicationJsonSchemaReturnLikelihoods:
      type: string
      enum:
        - GENERATION
        - ALL
        - NONE
      default: NONE
      description: >-
        One of `GENERATION|NONE` to specify how and if the token likelihoods are
        returned with the response. Defaults to `NONE`.


        If `GENERATION` is selected, the token likelihoods will only be provided
        for generated text.


        WARNING: `ALL` is deprecated, and will be removed in a future release.
      title: V1GeneratePostRequestBodyContentApplicationJsonSchemaReturnLikelihoods
    SingleGenerationTokenLikelihoodsItems:
      type: object
      properties:
        token:
          type: string
        likelihood:
          type: number
          format: double
      required:
        - token
        - likelihood
      title: SingleGenerationTokenLikelihoodsItems
    SingleGeneration:
      type: object
      properties:
        id:
          type: string
        text:
          type: string
        index:
          type: integer
          description: >-
            Refers to the nth generation. Only present when `num_generations` is
            greater than zero.
        likelihood:
          type: number
          format: double
        token_likelihoods:
          type: array
          items:
            $ref: '#/components/schemas/SingleGenerationTokenLikelihoodsItems'
          description: >-
            Only returned if `return_likelihoods` is set to `GENERATION` or
            `ALL`. The likelihood refers to the average log-likelihood of the
            entire specified string, which is useful for [evaluating the
            performance of your model](likelihood-eval), especially if you've
            created a [custom
            model](https://docs.cohere.com/docs/training-custom-models).
            Individual token likelihoods provide the log-likelihood of each
            token. The first token will not have a likelihood.
      required:
        - id
        - text
      title: SingleGeneration
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
    generate_Response_stream:
      type: object
      properties:
        id:
          type: string
        prompt:
          type: string
          description: Prompt used for generations.
        generations:
          type: array
          items:
            $ref: '#/components/schemas/SingleGeneration'
          description: List of generated results
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - id
        - generations
      title: generate_Response_stream
    GenerateRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestBadRequestError
    GenerateRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestUnauthorizedError
    GenerateRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestForbiddenError
    GenerateRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestNotFoundError
    GenerateRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestUnprocessableEntityError
    GenerateRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestTooManyRequestsError
    GenerateRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestInvalidTokenError
    GenerateRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestClientClosedRequestError
    GenerateRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestInternalServerError
    GenerateRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestNotImplementedError
    GenerateRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestServiceUnavailableError
    GenerateRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: GenerateRequestGatewayTimeoutError
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
	"errors"
	"io"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.GenerateStream(
		context.TODO(),
		&cohere.GenerateStreamRequest{
			Prompt: "Please explain to me how LLMs work",
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	// Make sure to close the stream when you're done reading.
	// This is easily handled with defer.
	defer resp.Close()

	for {
		message, err := resp.Recv()

		if errors.Is(err, io.EOF) {
			// An io.EOF error means the server is done sending messages
			// and should be treated as a success.
			break
		}

		if message.TextGeneration != nil {
			log.Printf("%+v", resp)
		}
	}
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const generate = await cohere.generate({
    prompt: 'Please explain to me how LLMs work',
  });

  console.log(generate);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.generateStream({
        prompt: "Please explain to me how LLMs work",
        stream: true,
    });
}
main();

```

```python Sync
import cohere

co = cohere.Client()

response = co.generate(
    prompt="Please explain to me how LLMs work",
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.generate(
        prompt="Please explain to me how LLMs work",
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.generate_stream(
    prompt="Please explain to me how LLMs work"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.GenerateRequest;
import com.cohere.api.types.Generation;

public class GeneratePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    Generation response =
        cohere.generate(
            GenerateRequest.builder().prompt("Please explain to me how LLMs work").build());

    System.out.println(response);
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/generate")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"prompt\": \"Please explain to me how LLMs work\",\n  \"stream\": true\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/generate', [
  'body' => '{
  "prompt": "Please explain to me how LLMs work",
  "stream": true
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

var client = new RestClient("https://api.cohere.com/v1/generate");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"prompt\": \"Please explain to me how LLMs work\",\n  \"stream\": true\n}", ParameterType.RequestBody);
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
  "prompt": "Please explain to me how LLMs work",
  "stream": true
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/generate")! as URL,
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