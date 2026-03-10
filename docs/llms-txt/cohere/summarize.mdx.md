# Source: https://docs.cohere.com/reference/summarize.mdx

# Summarize

POST https://api.cohere.com/v1/summarize
Content-Type: application/json

<Warning>
This API is marked as "Legacy" and is no longer maintained. Follow the [migration guide](https://docs.cohere.com/docs/migrating-from-cogenerate-to-cochat) to start using the Chat API.
</Warning>
Generates a summary in English for a given text.


Reference: https://docs.cohere.com/reference/summarize

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/summarize:
    post:
      operationId: summarize
      summary: Summarize
      description: >
        <Warning>

        This API is marked as "Legacy" and is no longer maintained. Follow the
        [migration
        guide](https://docs.cohere.com/docs/migrating-from-cogenerate-to-cochat)
        to start using the Chat API.

        </Warning>

        Generates a summary in English for a given text.
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
                $ref: '#/components/schemas/summarize_Response_200'
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
                $ref: '#/components/schemas/SummarizeRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestNotFoundError'
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
                $ref: '#/components/schemas/SummarizeRequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeRequestGatewayTimeoutError'
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
                    The text to generate a summary for. Can be up to 100,000
                    characters long. Currently the only supported language is
                    English.
                length:
                  $ref: >-
                    #/components/schemas/V1SummarizePostRequestBodyContentApplicationJsonSchemaLength
                  description: >-
                    One of `short`, `medium`, `long`, or `auto` defaults to
                    `auto`. Indicates the approximate length of the summary. If
                    `auto` is selected, the best option will be picked based on
                    the input text.
                format:
                  $ref: >-
                    #/components/schemas/V1SummarizePostRequestBodyContentApplicationJsonSchemaFormat
                  description: >-
                    One of `paragraph`, `bullets`, or `auto`, defaults to
                    `auto`. Indicates the style in which the summary will be
                    delivered - in a free form paragraph or in bullet points. If
                    `auto` is selected, the best option will be picked based on
                    the input text.
                model:
                  type: string
                  description: >-
                    The identifier of the model to generate the summary with.
                    Currently available models are `command` (default),
                    `command-nightly` (experimental), `command-light`, and
                    `command-light-nightly` (experimental). Smaller, "light"
                    models are faster, while larger models will perform better.
                extractiveness:
                  $ref: >-
                    #/components/schemas/V1SummarizePostRequestBodyContentApplicationJsonSchemaExtractiveness
                  description: >-
                    One of `low`, `medium`, `high`, or `auto`, defaults to
                    `auto`. Controls how close to the original text the summary
                    is. `high` extractiveness summaries will lean towards
                    reusing sentences verbatim, while `low` extractiveness
                    summaries will tend to paraphrase more. If `auto` is
                    selected, the best option will be picked based on the input
                    text.
                temperature:
                  type: number
                  format: double
                  default: 0.3
                  description: >-
                    Ranges from 0 to 5. Controls the randomness of the output.
                    Lower values tend to generate more “predictable” output,
                    while higher values tend to generate more “creative” output.
                    The sweet spot is typically between 0 and 1.
                additional_command:
                  type: string
                  description: >-
                    A free-form instruction for modifying how the summaries get
                    generated. Should complete the sentence "Generate a summary
                    _". Eg. "focusing on the next steps" or "written by Yoda"
              required:
                - text
servers:
  - url: https://api.cohere.com
components:
  schemas:
    V1SummarizePostRequestBodyContentApplicationJsonSchemaLength:
      type: string
      enum:
        - short
        - medium
        - long
      default: medium
      description: >-
        One of `short`, `medium`, `long`, or `auto` defaults to `auto`.
        Indicates the approximate length of the summary. If `auto` is selected,
        the best option will be picked based on the input text.
      title: V1SummarizePostRequestBodyContentApplicationJsonSchemaLength
    V1SummarizePostRequestBodyContentApplicationJsonSchemaFormat:
      type: string
      enum:
        - paragraph
        - bullets
      default: paragraph
      description: >-
        One of `paragraph`, `bullets`, or `auto`, defaults to `auto`. Indicates
        the style in which the summary will be delivered - in a free form
        paragraph or in bullet points. If `auto` is selected, the best option
        will be picked based on the input text.
      title: V1SummarizePostRequestBodyContentApplicationJsonSchemaFormat
    V1SummarizePostRequestBodyContentApplicationJsonSchemaExtractiveness:
      type: string
      enum:
        - low
        - medium
        - high
      default: low
      description: >-
        One of `low`, `medium`, `high`, or `auto`, defaults to `auto`. Controls
        how close to the original text the summary is. `high` extractiveness
        summaries will lean towards reusing sentences verbatim, while `low`
        extractiveness summaries will tend to paraphrase more. If `auto` is
        selected, the best option will be picked based on the input text.
      title: V1SummarizePostRequestBodyContentApplicationJsonSchemaExtractiveness
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
    summarize_Response_200:
      type: object
      properties:
        id:
          type: string
          description: Generated ID for the summary
        summary:
          type: string
          description: Generated summary for the text
        meta:
          $ref: '#/components/schemas/ApiMeta'
      title: summarize_Response_200
    SummarizeRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestBadRequestError
    SummarizeRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestUnauthorizedError
    SummarizeRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestForbiddenError
    SummarizeRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestNotFoundError
    SummarizeRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestUnprocessableEntityError
    SummarizeRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestTooManyRequestsError
    SummarizeRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestInvalidTokenError
    SummarizeRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestClientClosedRequestError
    SummarizeRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestInternalServerError
    SummarizeRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestNotImplementedError
    SummarizeRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestServiceUnavailableError
    SummarizeRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: SummarizeRequestGatewayTimeoutError
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

	resp, err := co.Summarize(
		context.TODO(),
		&cohere.SummarizeRequest{
			Text: "the quick brown fox jumped over the lazy dog and then the dog jumped over the fox the quick brown fox jumped over the lazy dog the quick brown fox jumped over the lazy dog the quick brown fox jumped over the lazy dog the quick brown fox jumped over the lazy dog",
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
  const summarize = await cohere.summarize({
    text:
      'Ice cream is a sweetened frozen food typically eaten as a snack or dessert. ' +
      'It may be made from milk or cream and is flavoured with a sweetener, ' +
      'either sugar or an alternative, and a spice, such as cocoa or vanilla, ' +
      'or with fruit such as strawberries or peaches. ' +
      'It can also be made by whisking a flavored cream base and liquid nitrogen together. ' +
      'Food coloring is sometimes added, in addition to stabilizers. ' +
      'The mixture is cooled below the freezing point of water and stirred to incorporate air spaces ' +
      'and to prevent detectable ice crystals from forming. The result is a smooth, ' +
      'semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). ' +
      'It becomes more malleable as its temperature increases.\n\n' +
      'The meaning of the name "ice cream" varies from one country to another. ' +
      'In some countries, such as the United States, "ice cream" applies only to a specific variety, ' +
      'and most governments regulate the commercial use of the various terms according to the ' +
      'relative quantities of the main ingredients, notably the amount of cream. ' +
      'Products that do not meet the criteria to be called ice cream are sometimes labelled ' +
      '"frozen dairy dessert" instead. In other countries, such as Italy and Argentina, ' +
      'one word is used fo\r all variants. Analogues made from dairy alternatives, ' +
      "such as goat's or sheep's milk, or milk substitutes " +
      '(e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are ' +
      'lactose intolerant, allergic to dairy protein or vegan.',
  });

  console.log(summarize);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.summarize({
        text: `Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together. Food coloring is sometimes added, in addition to stabilizers. The mixture is cooled below the freezing point of water and stirred to incorporate air spaces and to prevent detectable ice crystals from forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). It becomes more malleable as its temperature increases.

The meaning of the name "ice cream" varies from one country to another. In some countries, such as the United States, "ice cream" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream. Products that do not meet the criteria to be called ice cream are sometimes labelled "frozen dairy dessert" instead. In other countries, such as Italy and Argentina, one word is used fo
 all variants. Analogues made from dairy alternatives, such as goat's or sheep's milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein or vegan.`,
    });
}
main();

```

```python Sync
import cohere

co = cohere.Client()

text = (
    "Ice cream is a sweetened frozen food typically eaten as a snack or dessert. "
    "It may be made from milk or cream and is flavoured with a sweetener, "
    "either sugar or an alternative, and a spice, such as cocoa or vanilla, "
    "or with fruit such as strawberries or peaches. "
    "It can also be made by whisking a flavored cream base and liquid nitrogen together. "
    "Food coloring is sometimes added, in addition to stabilizers. "
    "The mixture is cooled below the freezing point of water and stirred to incorporate air spaces "
    "and to prevent detectable ice crystals from forming. The result is a smooth, "
    "semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). "
    "It becomes more malleable as its temperature increases.\n\n"
    'The meaning of the name "ice cream" varies from one country to another. '
    'In some countries, such as the United States, "ice cream" applies only to a specific variety, '
    "and most governments regulate the commercial use of the various terms according to the "
    "relative quantities of the main ingredients, notably the amount of cream. "
    "Products that do not meet the criteria to be called ice cream are sometimes labelled "
    '"frozen dairy dessert" instead. In other countries, such as Italy and Argentina, '
    "one word is used fo\r all variants. Analogues made from dairy alternatives, "
    "such as goat's or sheep's milk, or milk substitutes "
    "(e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are "
    "lactose intolerant, allergic to dairy protein or vegan."
)

response = co.summarize(
    text=text,
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()

text = (
    "Ice cream is a sweetened frozen food typically eaten as a snack or dessert. "
    "It may be made from milk or cream and is flavoured with a sweetener, "
    "either sugar or an alternative, and a spice, such as cocoa or vanilla, "
    "or with fruit such as strawberries or peaches. "
    "It can also be made by whisking a flavored cream base and liquid nitrogen together. "
    "Food coloring is sometimes added, in addition to stabilizers. "
    "The mixture is cooled below the freezing point of water and stirred to incorporate air spaces "
    "and to prevent detectable ice crystals from forming. The result is a smooth, "
    "semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). "
    "It becomes more malleable as its temperature increases.\n\n"
    'The meaning of the name "ice cream" varies from one country to another. '
    'In some countries, such as the United States, "ice cream" applies only to a specific variety, '
    "and most governments regulate the commercial use of the various terms according to the "
    "relative quantities of the main ingredients, notably the amount of cream. "
    "Products that do not meet the criteria to be called ice cream are sometimes labelled "
    '"frozen dairy dessert" instead. In other countries, such as Italy and Argentina, '
    "one word is used fo\r all variants. Analogues made from dairy alternatives, "
    "such as goat's or sheep's milk, or milk substitutes "
    "(e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are "
    "lactose intolerant, allergic to dairy protein or vegan."
)


async def main():
    response = await co.summarize(
        text=text,
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.summarize(
    text="Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together. Food coloring is sometimes added, in addition to stabilizers. The mixture is cooled below the freezing point of water and stirred to incorporate air spaces and to prevent detectable ice crystals from forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). It becomes more malleable as its temperature increases.\n\nThe meaning of the name \"ice cream\" varies from one country to another. In some countries, such as the United States, \"ice cream\" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream. Products that do not meet the criteria to be called ice cream are sometimes labelled \"frozen dairy dessert\" instead. In other countries, such as Italy and Argentina, one word is used fo\r all variants. Analogues made from dairy alternatives, such as goat\'s or sheep\'s milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein or vegan."
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.SummarizeRequest;
import com.cohere.api.types.SummarizeResponse;

public class SummarizePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    SummarizeResponse response =
        cohere.summarize(
            SummarizeRequest.builder()
                .text(
                    """
                              Ice cream is a sweetened frozen food typically eaten as a snack or dessert.\s
                              It may be made from milk or cream and is flavoured with a sweetener,\s
                              either sugar or an alternative, and a spice, such as cocoa or vanilla,\s
                              or with fruit such as strawberries or peaches.\s
                              It can also be made by whisking a flavored cream base and liquid nitrogen together.\s
                              Food coloring is sometimes added, in addition to stabilizers.\s
                              The mixture is cooled below the freezing point of water and stirred to incorporate air spaces\s
                              and to prevent detectable ice crystals from forming. The result is a smooth,\s
                              semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F).\s
                              It becomes more malleable as its temperature increases.\\n\\n
                              The meaning of the name "ice cream" varies from one country to another.\s
                              In some countries, such as the United States, "ice cream" applies only to a specific variety,\s
                              and most governments regulate the commercial use of the various terms according to the\s
                              relative quantities of the main ingredients, notably the amount of cream.\s
                              Products that do not meet the criteria to be called ice cream are sometimes labelled\s
                              "frozen dairy dessert" instead. In other countries, such as Italy and Argentina,\s
                              one word is used fo\\r all variants. Analogues made from dairy alternatives,\s
                              such as goat's or sheep's milk, or milk substitutes\s
                              (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are\s
                              lactose intolerant, allergic to dairy protein or vegan.
                        """)
                .build());

    System.out.println(response);
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/summarize")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"text\": \"Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together. Food coloring is sometimes added, in addition to stabilizers. The mixture is cooled below the freezing point of water and stirred to incorporate air spaces and to prevent detectable ice crystals from forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). It becomes more malleable as its temperature increases.\\n\\nThe meaning of the name \\\"ice cream\\\" varies from one country to another. In some countries, such as the United States, \\\"ice cream\\\" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream. Products that do not meet the criteria to be called ice cream are sometimes labelled \\\"frozen dairy dessert\\\" instead. In other countries, such as Italy and Argentina, one word is used fo\\r all variants. Analogues made from dairy alternatives, such as goat's or sheep's milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein or vegan.\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/summarize', [
  'body' => '{
  "text": "Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together. Food coloring is sometimes added, in addition to stabilizers. The mixture is cooled below the freezing point of water and stirred to incorporate air spaces and to prevent detectable ice crystals from forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). It becomes more malleable as its temperature increases.\\n\\nThe meaning of the name \\"ice cream\\" varies from one country to another. In some countries, such as the United States, \\"ice cream\\" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream. Products that do not meet the criteria to be called ice cream are sometimes labelled \\"frozen dairy dessert\\" instead. In other countries, such as Italy and Argentina, one word is used fo\\r all variants. Analogues made from dairy alternatives, such as goat\'s or sheep\'s milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein or vegan."
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

var client = new RestClient("https://api.cohere.com/v1/summarize");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"text\": \"Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together. Food coloring is sometimes added, in addition to stabilizers. The mixture is cooled below the freezing point of water and stirred to incorporate air spaces and to prevent detectable ice crystals from forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). It becomes more malleable as its temperature increases.\\n\\nThe meaning of the name \\\"ice cream\\\" varies from one country to another. In some countries, such as the United States, \\\"ice cream\\\" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream. Products that do not meet the criteria to be called ice cream are sometimes labelled \\\"frozen dairy dessert\\\" instead. In other countries, such as Italy and Argentina, one word is used fo\\r all variants. Analogues made from dairy alternatives, such as goat's or sheep's milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein or vegan.\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = ["text": "Ice cream is a sweetened frozen food typically eaten as a snack or dessert. It may be made from milk or cream and is flavoured with a sweetener, either sugar or an alternative, and a spice, such as cocoa or vanilla, or with fruit such as strawberries or peaches. It can also be made by whisking a flavored cream base and liquid nitrogen together. Food coloring is sometimes added, in addition to stabilizers. The mixture is cooled below the freezing point of water and stirred to incorporate air spaces and to prevent detectable ice crystals from forming. The result is a smooth, semi-solid foam that is solid at very low temperatures (below 2 °C or 35 °F). It becomes more malleable as its temperature increases.

The meaning of the name \"ice cream\" varies from one country to another. In some countries, such as the United States, \"ice cream\" applies only to a specific variety, and most governments regulate the commercial use of the various terms according to the relative quantities of the main ingredients, notably the amount of cream. Products that do not meet the criteria to be called ice cream are sometimes labelled \"frozen dairy dessert\" instead. In other countries, such as Italy and Argentina, one word is used fo
 all variants. Analogues made from dairy alternatives, such as goat's or sheep's milk, or milk substitutes (e.g., soy, cashew, coconut, almond milk or tofu), are available for those who are lactose intolerant, allergic to dairy protein or vegan."] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/summarize")! as URL,
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