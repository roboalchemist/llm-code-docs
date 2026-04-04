# Source: https://docs.cohere.com/reference/embed.mdx

# Embed API (v2)

POST https://api.cohere.com/v2/embed
Content-Type: application/json

This endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents.

Embeddings can be used to create text classifiers as well as empower semantic search. To learn more about embeddings, see the embedding page.

If you want to learn more how to use the embedding model, have a look at the [Semantic Search Guide](https://docs.cohere.com/docs/semantic-search).

Reference: https://docs.cohere.com/reference/embed

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v2/embed:
    post:
      operationId: embed
      summary: Embed API (v2)
      description: >-
        This endpoint returns text embeddings. An embedding is a list of
        floating point numbers that captures semantic information about the text
        that it represents.


        Embeddings can be used to create text classifiers as well as empower
        semantic search. To learn more about embeddings, see the embedding page.


        If you want to learn more how to use the embedding model, have a look at
        the [Semantic Search
        Guide](https://docs.cohere.com/docs/semantic-search).
      tags:
        - subpackage_v2
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
                $ref: '#/components/schemas/EmbedByTypeResponse'
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
                $ref: '#/components/schemas/Embedv2RequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestNotFoundError'
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
                $ref: '#/components/schemas/Embedv2RequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Embedv2RequestGatewayTimeoutError'
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                texts:
                  type: array
                  items:
                    type: string
                  description: >-
                    An array of strings for the model to embed. Maximum number
                    of texts per call is `96`.
                images:
                  type: array
                  items:
                    type: string
                  description: >-
                    An array of image data URIs for the model to embed. Maximum
                    number of images per call is `1`.


                    The image must be a valid [data
                    URI](https://developer.mozilla.org/en-US/docs/Web/URI/Schemes/data).
                    The image must be in either `image/jpeg`, `image/png`,
                    `image/webp`, or `image/gif` format and has a maximum size
                    of 5MB.


                    Image embeddings are supported with Embed v3.0 and newer
                    models.
                model:
                  type: string
                  description: >-
                    ID of one of the available [Embedding
                    models](https://docs.cohere.com/docs/cohere-embed).
                input_type:
                  $ref: '#/components/schemas/EmbedInputType'
                inputs:
                  type: array
                  items:
                    $ref: '#/components/schemas/EmbedInput'
                  description: >-
                    An array of inputs for the model to embed. Maximum number of
                    inputs per call is `96`. An input can contain a mix of text
                    and image components.
                max_tokens:
                  type: integer
                  description: >-
                    The maximum number of tokens to embed per input. If the
                    input text is longer than this, it will be truncated
                    according to the `truncate` parameter.
                output_dimension:
                  type: integer
                  description: >-
                    The number of dimensions of the output embedding. This is
                    only available for `embed-v4` and newer models.

                    Possible values are `256`, `512`, `1024`, and `1536`. The
                    default is `1536`.
                embedding_types:
                  type: array
                  items:
                    $ref: '#/components/schemas/EmbeddingType'
                  description: >-
                    Specifies the types of embeddings you want to get back. Can
                    be one or more of the following types.


                    * `"float"`: Use this when you want to get back the default
                    float embeddings. Supported with all Embed models.

                    * `"int8"`: Use this when you want to get back signed int8
                    embeddings. Supported with Embed v3.0 and newer Embed
                    models.

                    * `"uint8"`: Use this when you want to get back unsigned
                    int8 embeddings. Supported with Embed v3.0 and newer Embed
                    models.

                    * `"binary"`: Use this when you want to get back signed
                    binary embeddings. Supported with Embed v3.0 and newer Embed
                    models.

                    * `"ubinary"`: Use this when you want to get back unsigned
                    binary embeddings. Supported with Embed v3.0 and newer Embed
                    models.

                    * `"base64"`: Use this when you want to get back base64
                    embeddings. Supported with Embed v3.0 and newer Embed
                    models.
                truncate:
                  $ref: >-
                    #/components/schemas/V2EmbedPostRequestBodyContentApplicationJsonSchemaTruncate
                  description: >-
                    One of `NONE|START|END` to specify how the API will handle
                    inputs longer than the maximum token length.


                    Passing `START` will discard the start of the input. `END`
                    will discard the end of the input. In both cases, input is
                    discarded until the remaining input is exactly the maximum
                    input token length for the model.


                    If `NONE` is selected, when the input exceeds the maximum
                    input token length an error will be returned.
                priority:
                  type: integer
                  default: 0
                  description: >-
                    Controls how early the request is handled. Lower numbers
                    indicate higher priority (default: 0, the highest). When the
                    system is under load, higher-priority requests are processed
                    first and are the least likely to be dropped.
              required:
                - model
                - input_type
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
    EmbedImageUrl:
      type: object
      properties:
        url:
          type: string
      required:
        - url
      description: Base64 url of image.
      title: EmbedImageUrl
    EmbedContent:
      oneOf:
        - type: object
          properties:
            type:
              type: string
              enum:
                - image_url
              description: 'Discriminator value: image_url'
            image_url:
              $ref: '#/components/schemas/EmbedImageUrl'
          required:
            - type
          description: image_url variant
        - type: object
          properties:
            type:
              type: string
              enum:
                - text
              description: 'Discriminator value: text'
            text:
              type: string
          required:
            - type
          description: text variant
      discriminator:
        propertyName: type
      title: EmbedContent
    EmbedInput:
      type: object
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/EmbedContent'
          description: >-
            An array of objects containing the input data for the model to
            embed.
      required:
        - content
      title: EmbedInput
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
    V2EmbedPostRequestBodyContentApplicationJsonSchemaTruncate:
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
      title: V2EmbedPostRequestBodyContentApplicationJsonSchemaTruncate
    EmbedByTypeResponseEmbeddings:
      type: object
      properties:
        float:
          type: array
          items:
            type: array
            items:
              type: number
              format: double
          description: An array of float embeddings.
        int8:
          type: array
          items:
            type: array
            items:
              type: integer
          description: >-
            An array of signed int8 embeddings. Each value is between -128 and
            127.
        uint8:
          type: array
          items:
            type: array
            items:
              type: integer
          description: >-
            An array of unsigned int8 embeddings. Each value is between 0 and
            255.
        binary:
          type: array
          items:
            type: array
            items:
              type: integer
          description: >-
            An array of packed signed binary embeddings. The length of each
            binary embedding is 1/8 the length of the float embeddings of the
            provided model. Each value is between -128 and 127.
        ubinary:
          type: array
          items:
            type: array
            items:
              type: integer
          description: >-
            An array of packed unsigned binary embeddings. The length of each
            binary embedding is 1/8 the length of the float embeddings of the
            provided model. Each value is between 0 and 255.
        base64:
          type: array
          items:
            type: string
          description: >-
            An array of base64 embeddings. Each string is the result of
            appending the float embedding bytes together and base64 encoding
            that.
      description: >-
        An object with different embedding types. The length of each embedding
        type array will be the same as the length of the original `texts` array.
      title: EmbedByTypeResponseEmbeddings
    Image:
      type: object
      properties:
        width:
          type: integer
          format: int64
          description: Width of the image in pixels
        height:
          type: integer
          format: int64
          description: Height of the image in pixels
        format:
          type: string
          description: Format of the image
        bit_depth:
          type: integer
          format: int64
          description: Bit depth of the image
      required:
        - width
        - height
        - format
        - bit_depth
      title: Image
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
    EmbedByTypeResponse:
      type: object
      properties:
        id:
          type: string
        embeddings:
          $ref: '#/components/schemas/EmbedByTypeResponseEmbeddings'
          description: >-
            An object with different embedding types. The length of each
            embedding type array will be the same as the length of the original
            `texts` array.
        texts:
          type: array
          items:
            type: string
          description: The text entries for which embeddings were returned.
        images:
          type: array
          items:
            $ref: '#/components/schemas/Image'
          description: The image entries for which embeddings were returned.
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - id
        - embeddings
      title: EmbedByTypeResponse
    Embedv2RequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestBadRequestError
    Embedv2RequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestUnauthorizedError
    Embedv2RequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestForbiddenError
    Embedv2RequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestNotFoundError
    Embedv2RequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestUnprocessableEntityError
    Embedv2RequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestTooManyRequestsError
    Embedv2RequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestInvalidTokenError
    Embedv2RequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestClientClosedRequestError
    Embedv2RequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestInternalServerError
    Embedv2RequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestNotImplementedError
    Embedv2RequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestServiceUnavailableError
    Embedv2RequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Embedv2RequestGatewayTimeoutError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```go Texts
package main

import (
	"context"
	"log"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.V2.Embed(
		context.TODO(),
		&cohere.V2EmbedRequest{
			Texts:          []string{"hello", "goodbye"},
			Model:          "embed-v4.0",
			InputType:      cohere.EmbedInputTypeSearchDocument,
			EmbeddingTypes: []cohere.EmbeddingType{cohere.EmbeddingTypeFloat},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```typescript Texts
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const embed = await cohere.v2.embed({
    texts: ['hello', 'goodbye'],
    model: 'embed-v4.0',
    inputType: 'classification',
    embeddingTypes: ['float'],
  });
  console.log(embed);
})();

```

```typescript Texts
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.v2.embed({
        model: "embed-v4.0",
        inputType: "classification",
        texts: [
            "hello",
            "goodbye",
        ],
        embeddingTypes: [
            "float",
        ],
    });
}
main();

```

```python Texts
import cohere

co = cohere.ClientV2()

text_inputs = [
    {
        "content": [
            {"type": "text", "text": "hello"},
            {"type": "text", "text": "goodbye"}
        ]
    },
]

response = co.embed(
    inputs=text_inputs,
    model="embed-v4.0",
    input_type="classification",
    embedding_types=["float"],
)
print(response)

```

```python Texts (async)
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.embed(
        texts=["hello", "goodbye"],
        model="embed-v4.0",
        input_type="classification",
    )
    print(response)


asyncio.run(main())

```

```python Texts
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.v2.embed(
    model="embed-v4.0",
    input_type="classification",
    texts=[
        "hello",
        "goodbye"
    ],
    embedding_types=[
        "float"
    ]
)

```

```java Texts
package embedv2post; /* (C)2024 */

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2EmbedRequest;
import com.cohere.api.types.EmbedByTypeResponse;
import com.cohere.api.types.EmbedInputType;
import java.util.List;

public class EmbedPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    EmbedByTypeResponse response =
        cohere
            .v2()
            .embed(
                V2EmbedRequest.builder()
                    .model("embed-v4.0")
                    .inputType(EmbedInputType.CLASSIFICATION)
                    .texts(List.of("hello", "goodbye"))
                    .build());

    System.out.println(response);
  }
}

```

```ruby Texts
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/embed")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"classification\",\n  \"texts\": [\n    \"hello\",\n    \"goodbye\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Texts
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/embed', [
  'body' => '{
  "model": "embed-v4.0",
  "input_type": "classification",
  "texts": [
    "hello",
    "goodbye"
  ],
  "embedding_types": [
    "float"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Texts
using RestSharp;

var client = new RestClient("https://api.cohere.com/v2/embed");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"classification\",\n  \"texts\": [\n    \"hello\",\n    \"goodbye\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Texts
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "model": "embed-v4.0",
  "input_type": "classification",
  "texts": ["hello", "goodbye"],
  "embedding_types": ["float"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/embed")! as URL,
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

```go Images
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	cohere "github.com/cohere-ai/cohere-go/v2"
	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	// Fetch the image
	resp, err := http.Get("https://cohere.com/favicon-32x32.png")
	if err != nil {
		log.Println("Error fetching the image:", err)
		return
	}
	defer resp.Body.Close()

	// Read the image content
	buffer, err := io.ReadAll(resp.Body)
	if err != nil {
		log.Println("Error reading the image content:", err)
		return
	}

	stringifiedBuffer := base64.StdEncoding.EncodeToString(buffer)
	contentType := resp.Header.Get("Content-Type")
	imageBase64 := fmt.Sprintf("data:%s;base64,%s", contentType, stringifiedBuffer)

	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	embed, err := co.V2.Embed(
		context.TODO(),
		&cohere.V2EmbedRequest{
			Images:         []string{imageBase64},
			Model:          "embed-v4.0",
			InputType:      cohere.EmbedInputTypeImage,
			EmbeddingTypes: []cohere.EmbeddingType{cohere.EmbeddingTypeFloat},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", embed)
}

```

```typescript Images
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const image = await fetch('https://cohere.com/favicon-32x32.png');
  const buffer = await image.arrayBuffer();
  const stringifiedBuffer = Buffer.from(buffer).toString('base64');
  const contentType = image.headers.get('content-type');
  const imageBase64 = `data:${contentType};base64,${stringifiedBuffer}`;

  const embed = await cohere.v2.embed({
    model: 'embed-v4.0',
    inputType: 'image',
    embeddingTypes: ['float'],
    images: [imageBase64],
  });
  console.log(embed);
})();

```

```typescript Images
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.v2.embed({
        model: "embed-v4.0",
        inputType: "image",
        images: [
            "data:image/jpeg;base64,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",
        ],
        embeddingTypes: [
            "float",
        ],
    });
}
main();

```

```python Images
import cohere
import requests
import base64

co = cohere.ClientV2()

image = requests.get("https://cohere.com/favicon-32x32.png")
stringified_buffer = base64.b64encode(image.content).decode("utf-8")
content_type = image.headers["Content-Type"]
image_base64 = f"data:{content_type};base64,{stringified_buffer}"

image_inputs = [
    {
        "content": [
            {
                "type": "image_url",
                "image_url": {"url": image_base64}
            }
        ]
    }
]

response = co.embed(
    model="embed-v4.0",
    input_type="image",
    embedding_types=["float"],
    inputs=image_inputs
)

print(response)

```

```python Images
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.v2.embed(
    model="embed-v4.0",
    input_type="image",
    images=[
        "data:image/jpeg;base64,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"
    ],
    embedding_types=[
        "float"
    ]
)

```

```java Images
package embedv2post; /* (C)2024 */

import com.cohere.api.Cohere;
import com.cohere.api.resources.v2.requests.V2EmbedRequest;
import com.cohere.api.types.EmbedByTypeResponse;
import com.cohere.api.types.EmbedInputType;
import com.cohere.api.types.EmbeddingType;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;
import java.util.Base64;
import java.util.List;

public class EmbedImagePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    try {
      URI uri = URI.create("https://cohere.com/favicon-32x32.png");
      URL url = uri.toURL();
      HttpURLConnection connection = (HttpURLConnection) url.openConnection();
      connection.connect();

      InputStream inputStream = connection.getInputStream();
      byte[] buffer = inputStream.readAllBytes();
      inputStream.close();

      String imageBase64 =
          String.format(
              "data:%s;base64,%s",
              connection.getHeaderField("Content-Type"),
              Base64.getEncoder().encodeToString(buffer));

      EmbedByTypeResponse response =
          cohere
              .v2()
              .embed(
                  V2EmbedRequest.builder()
                      .model("embed-v4.0")
                      .inputType(EmbedInputType.IMAGE)
                      .images(List.of(imageBase64))
                      .embeddingTypes(List.of(EmbeddingType.FLOAT))
                      .build());

      System.out.println(response);
    } catch (MalformedURLException e) {
      System.err.println("Invalid URL: " + e.getMessage());
    } catch (IOException e) {
      System.err.println("I/O error: " + e.getMessage());
    }
  }
}

```

```ruby Images
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/embed")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"image\",\n  \"images\": [\n    \"data:image/jpeg;base64,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\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```php Images
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/embed', [
  'body' => '{
  "model": "embed-v4.0",
  "input_type": "image",
  "images": [
    "data:image/jpeg;base64,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"
  ],
  "embedding_types": [
    "float"
  ]
}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp Images
using RestSharp;

var client = new RestClient("https://api.cohere.com/v2/embed");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"model\": \"embed-v4.0\",\n  \"input_type\": \"image\",\n  \"images\": [\n    \"data:image/jpeg;base64,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\"\n  ],\n  \"embedding_types\": [\n    \"float\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Images
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "model": "embed-v4.0",
  "input_type": "image",
  "images": ["data:image/jpeg;base64,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"],
  "embedding_types": ["float"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/embed")! as URL,
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