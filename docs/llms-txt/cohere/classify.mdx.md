# Source: https://docs.cohere.com/reference/classify.mdx

# Classify

POST https://api.cohere.com/v1/classify
Content-Type: application/json

This endpoint makes a prediction about which label fits the specified text inputs best. To make a prediction, Classify uses the provided `examples` of text + label pairs as a reference.
Note: [Fine-tuned models](https://docs.cohere.com/docs/classify-fine-tuning) trained on classification examples don't require the `examples` parameter to be passed in explicitly.

Reference: https://docs.cohere.com/reference/classify

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/classify:
    post:
      operationId: classify
      summary: Classify
      description: >-
        This endpoint makes a prediction about which label fits the specified
        text inputs best. To make a prediction, Classify uses the provided
        `examples` of text + label pairs as a reference.

        Note: [Fine-tuned
        models](https://docs.cohere.com/docs/classify-fine-tuning) trained on
        classification examples don't require the `examples` parameter to be
        passed in explicitly.
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
                $ref: '#/components/schemas/classify_Response_200'
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
                $ref: '#/components/schemas/ClassifyRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestNotFoundError'
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
                $ref: '#/components/schemas/ClassifyRequestUnprocessableEntityError'
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestClientClosedRequestError'
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ClassifyRequestGatewayTimeoutError'
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              type: object
              properties:
                inputs:
                  type: array
                  items:
                    type: string
                  description: >-
                    A list of up to 96 texts to be classified. Each one must be
                    a non-empty string.

                    There is, however, no consistent, universal limit to the
                    length a particular input can be. We perform classification
                    on the first `x` tokens of each input, and `x` varies
                    depending on which underlying model is powering
                    classification. The maximum token length for each model is
                    listed in the "max tokens" column
                    [here](https://docs.cohere.com/docs/models).

                    Note: by default the `truncate` parameter is set to `END`,
                    so tokens exceeding the limit will be automatically dropped.
                    This behavior can be disabled by setting `truncate` to
                    `NONE`, which will result in validation errors for longer
                    texts.
                examples:
                  type: array
                  items:
                    $ref: '#/components/schemas/ClassifyExample'
                  description: >-
                    An array of examples to provide context to the model. Each
                    example is a text string and its associated label/class.
                    Each unique label requires at least 2 examples associated
                    with it; the maximum number of examples is 2500, and each
                    example has a maximum length of 512 tokens. The values
                    should be structured as `{text: "...",label: "..."}`.

                    Note: [Fine-tuned
                    Models](https://docs.cohere.com/docs/classify-fine-tuning)
                    trained on classification examples don't require the
                    `examples` parameter to be passed in explicitly.
                model:
                  type: string
                  description: >-
                    ID of a
                    [Fine-tuned](https://docs.cohere.com/v2/docs/classify-starting-the-training)
                    Classify model
                preset:
                  type: string
                  description: >-
                    The ID of a custom playground preset. You can create presets
                    in the
                    [playground](https://dashboard.cohere.com/playground). If
                    you use a preset, all other parameters become optional, and
                    any included parameters will override the preset's
                    parameters.
                truncate:
                  $ref: >-
                    #/components/schemas/V1ClassifyPostRequestBodyContentApplicationJsonSchemaTruncate
                  description: >-
                    One of `NONE|START|END` to specify how the API will handle
                    inputs longer than the maximum token length.

                    Passing `START` will discard the start of the input. `END`
                    will discard the end of the input. In both cases, input is
                    discarded until the remaining input is exactly the maximum
                    input token length for the model.

                    If `NONE` is selected, when the input exceeds the maximum
                    input token length an error will be returned.
              required:
                - inputs
servers:
  - url: https://api.cohere.com
components:
  schemas:
    ClassifyExample:
      type: object
      properties:
        text:
          type: string
        label:
          type: string
      title: ClassifyExample
    V1ClassifyPostRequestBodyContentApplicationJsonSchemaTruncate:
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
      title: V1ClassifyPostRequestBodyContentApplicationJsonSchemaTruncate
    V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsLabels:
      type: object
      properties:
        confidence:
          type: number
          format: double
      title: >-
        V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsLabels
    V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsClassificationType:
      type: string
      enum:
        - single-label
        - multi-label
      description: The type of classification performed
      title: >-
        V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsClassificationType
    V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItems:
      type: object
      properties:
        id:
          type: string
        input:
          type: string
          description: The input text that was classified
        prediction:
          type: string
          description: >-
            The predicted label for the associated query (only filled for
            single-label models)
        predictions:
          type: array
          items:
            type: string
          description: >-
            An array containing the predicted labels for the associated query
            (only filled for single-label classification)
        confidence:
          type: number
          format: double
          description: >-
            The confidence score for the top predicted class (only filled for
            single-label classification)
        confidences:
          type: array
          items:
            type: number
            format: double
          description: >-
            An array containing the confidence scores of all the predictions in
            the same order
        labels:
          type: object
          additionalProperties:
            $ref: >-
              #/components/schemas/V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsLabels
          description: >-
            A map containing each label and its confidence score according to
            the classifier. All the confidence scores add up to 1 for
            single-label classification. For multi-label classification the
            label confidences are independent of each other, so they don't have
            to sum up to 1.
        classification_type:
          $ref: >-
            #/components/schemas/V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItemsClassificationType
          description: The type of classification performed
      required:
        - id
        - predictions
        - confidences
        - labels
        - classification_type
      title: V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItems
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
    classify_Response_200:
      type: object
      properties:
        id:
          type: string
        classifications:
          type: array
          items:
            $ref: >-
              #/components/schemas/V1ClassifyPostResponsesContentApplicationJsonSchemaClassificationsItems
        meta:
          $ref: '#/components/schemas/ApiMeta'
      required:
        - id
        - classifications
      title: classify_Response_200
    ClassifyRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestBadRequestError
    ClassifyRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestUnauthorizedError
    ClassifyRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestForbiddenError
    ClassifyRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestNotFoundError
    ClassifyRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestUnprocessableEntityError
    ClassifyRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestTooManyRequestsError
    ClassifyRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestInvalidTokenError
    ClassifyRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestClientClosedRequestError
    ClassifyRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestInternalServerError
    ClassifyRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestNotImplementedError
    ClassifyRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestServiceUnavailableError
    ClassifyRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: ClassifyRequestGatewayTimeoutError
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
	model := "<YOUR-FINE-TUNED-MODEL-ID>"

	resp, err := co.Classify(
		context.TODO(),
		&cohere.ClassifyRequest{
			Model: &model,
			Examples: []*cohere.ClassifyExample{
				{
					Text:  cohere.String("orange"),
					Label: cohere.String("fruit"),
				},
				{
					Text:  cohere.String("pear"),
					Label: cohere.String("fruit"),
				},
				{
					Text:  cohere.String("lettuce"),
					Label: cohere.String("vegetable"),
				},
				{
					Text:  cohere.String("cauliflower"),
					Label: cohere.String("vegetable"),
				},
			},
			Inputs: []string{"peach"},
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
  const classify = await cohere.classify({
    model: '<YOUR-FINE-TUNED-MODEL-ID>',
    examples: [
      { text: "Dermatologists don't like her!", label: 'Spam' },
      { text: "'Hello, open to this?'", label: 'Spam' },
      { text: 'I need help please wire me $1000 right now', label: 'Spam' },
      { text: 'Nice to know you ;)', label: 'Spam' },
      { text: 'Please help me?', label: 'Spam' },
      { text: 'Your parcel will be delivered today', label: 'Not spam' },
      { text: 'Review changes to our Terms and Conditions', label: 'Not spam' },
      { text: 'Weekly sync notes', label: 'Not spam' },
      { text: "'Re: Follow up from today's meeting'", label: 'Not spam' },
      { text: 'Pre-read for tomorrow', label: 'Not spam' },
    ],
    inputs: ['Confirm your email address', 'hey i need u to send some $'],
  });

  console.log(classify);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.classify({
        inputs: [
            "Confirm your email address",
            "hey i need u to send some $",
        ],
        examples: [
            {
                text: "Dermatologists don't like her!",
                label: "Spam",
            },
            {
                text: "'Hello, open to this?'",
                label: "Spam",
            },
            {
                text: "I need help please wire me $1000 right now",
                label: "Spam",
            },
            {
                text: "Nice to know you ;)",
                label: "Spam",
            },
            {
                text: "Please help me?",
                label: "Spam",
            },
            {
                text: "Your parcel will be delivered today",
                label: "Not spam",
            },
            {
                text: "Review changes to our Terms and Conditions",
                label: "Not spam",
            },
            {
                text: "Weekly sync notes",
                label: "Not spam",
            },
            {
                text: "'Re: Follow up from today's meeting'",
                label: "Not spam",
            },
            {
                text: "Pre-read for tomorrow",
                label: "Not spam",
            },
        ],
        model: "YOUR-FINE-TUNED-MODEL-ID",
    });
}
main();

```

```python Sync
import cohere
from cohere import ClassifyExample

co = cohere.Client()
examples = [
    ClassifyExample(text="Dermatologists don't like her!", label="Spam"),
    ClassifyExample(text="'Hello, open to this?'", label="Spam"),
    ClassifyExample(text="I need help please wire me $1000 right now", label="Spam"),
    ClassifyExample(text="Nice to know you ;)", label="Spam"),
    ClassifyExample(text="Please help me?", label="Spam"),
    ClassifyExample(text="Your parcel will be delivered today", label="Not spam"),
    ClassifyExample(
        text="Review changes to our Terms and Conditions", label="Not spam"
    ),
    ClassifyExample(text="Weekly sync notes", label="Not spam"),
    ClassifyExample(text="'Re: Follow up from today's meeting'", label="Not spam"),
    ClassifyExample(text="Pre-read for tomorrow", label="Not spam"),
]
inputs = [
    "Confirm your email address",
    "hey i need u to send some $",
]
response = co.classify(
    model="<YOUR-FINE-TUNED-MODEL-ID>",
    inputs=inputs,
    examples=examples,
)
print(response)

```

```python Async
import cohere
import asyncio
from cohere import ClassifyExample

co = cohere.AsyncClient()
examples = [
    ClassifyExample(text="Dermatologists don't like her!", label="Spam"),
    ClassifyExample(text="'Hello, open to this?'", label="Spam"),
    ClassifyExample(text="I need help please wire me $1000 right now", label="Spam"),
    ClassifyExample(text="Nice to know you ;)", label="Spam"),
    ClassifyExample(text="Please help me?", label="Spam"),
    ClassifyExample(text="Your parcel will be delivered today", label="Not spam"),
    ClassifyExample(
        text="Review changes to our Terms and Conditions", label="Not spam"
    ),
    ClassifyExample(text="Weekly sync notes", label="Not spam"),
    ClassifyExample(text="'Re: Follow up from today's meeting'", label="Not spam"),
    ClassifyExample(text="Pre-read for tomorrow", label="Not spam"),
]
inputs = [
    "Confirm your email address",
    "hey i need u to send some $",
]


async def main():
    response = await co.classify(
        model="<YOUR-FINE-TUNED-MODEL-ID>",
        inputs=inputs,
        examples=examples,
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.classify(
    inputs=[
        "Confirm your email address",
        "hey i need u to send some $"
    ],
    examples=[
        {
            "text": "Dermatologists don\'t like her!",
            "label": "Spam"
        },
        {
            "text": "\'Hello, open to this?\'",
            "label": "Spam"
        },
        {
            "text": "I need help please wire me $1000 right now",
            "label": "Spam"
        },
        {
            "text": "Nice to know you ;)",
            "label": "Spam"
        },
        {
            "text": "Please help me?",
            "label": "Spam"
        },
        {
            "text": "Your parcel will be delivered today",
            "label": "Not spam"
        },
        {
            "text": "Review changes to our Terms and Conditions",
            "label": "Not spam"
        },
        {
            "text": "Weekly sync notes",
            "label": "Not spam"
        },
        {
            "text": "\'Re: Follow up from today\'s meeting\'",
            "label": "Not spam"
        },
        {
            "text": "Pre-read for tomorrow",
            "label": "Not spam"
        }
    ],
    model="YOUR-FINE-TUNED-MODEL-ID"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.requests.ClassifyRequest;
import com.cohere.api.types.ClassifyExample;
import com.cohere.api.types.ClassifyResponse;
import java.util.List;

public class ClassifyPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ClassifyResponse response =
        cohere.classify(
            ClassifyRequest.builder()
                .addAllInputs(List.of("Confirm your email address", "hey i need u to send some $"))
                .examples(
                    List.of(
                        ClassifyExample.builder()
                            .text("Dermatologists don't like her!")
                            .label("Spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("'Hello, open to this?'")
                            .label("Spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("I need help please wire me $1000" + " right now")
                            .label("Spam")
                            .build(),
                        ClassifyExample.builder().text("Nice to know you ;)").label("Spam").build(),
                        ClassifyExample.builder().text("Please help me?").label("Spam").build(),
                        ClassifyExample.builder()
                            .text("Your parcel will be delivered today")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("Review changes to our Terms and" + " Conditions")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("Weekly sync notes")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("'Re: Follow up from today's" + " meeting'")
                            .label("Not spam")
                            .build(),
                        ClassifyExample.builder()
                            .text("Pre-read for tomorrow")
                            .label("Not spam")
                            .build()))
                .build());

    System.out.println(response);
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/classify")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"inputs\": [\n    \"Confirm your email address\",\n    \"hey i need u to send some $\"\n  ],\n  \"examples\": [\n    {\n      \"text\": \"Dermatologists don't like her!\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"'Hello, open to this?'\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"I need help please wire me $1000 right now\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Nice to know you ;)\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Please help me?\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Your parcel will be delivered today\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Review changes to our Terms and Conditions\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Weekly sync notes\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"'Re: Follow up from today's meeting'\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Pre-read for tomorrow\",\n      \"label\": \"Not spam\"\n    }\n  ],\n  \"model\": \"YOUR-FINE-TUNED-MODEL-ID\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/classify', [
  'body' => '{
  "inputs": [
    "Confirm your email address",
    "hey i need u to send some $"
  ],
  "examples": [
    {
      "text": "Dermatologists don\'t like her!",
      "label": "Spam"
    },
    {
      "text": "\'Hello, open to this?\'",
      "label": "Spam"
    },
    {
      "text": "I need help please wire me $1000 right now",
      "label": "Spam"
    },
    {
      "text": "Nice to know you ;)",
      "label": "Spam"
    },
    {
      "text": "Please help me?",
      "label": "Spam"
    },
    {
      "text": "Your parcel will be delivered today",
      "label": "Not spam"
    },
    {
      "text": "Review changes to our Terms and Conditions",
      "label": "Not spam"
    },
    {
      "text": "Weekly sync notes",
      "label": "Not spam"
    },
    {
      "text": "\'Re: Follow up from today\'s meeting\'",
      "label": "Not spam"
    },
    {
      "text": "Pre-read for tomorrow",
      "label": "Not spam"
    }
  ],
  "model": "YOUR-FINE-TUNED-MODEL-ID"
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

var client = new RestClient("https://api.cohere.com/v1/classify");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"inputs\": [\n    \"Confirm your email address\",\n    \"hey i need u to send some $\"\n  ],\n  \"examples\": [\n    {\n      \"text\": \"Dermatologists don't like her!\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"'Hello, open to this?'\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"I need help please wire me $1000 right now\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Nice to know you ;)\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Please help me?\",\n      \"label\": \"Spam\"\n    },\n    {\n      \"text\": \"Your parcel will be delivered today\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Review changes to our Terms and Conditions\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Weekly sync notes\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"'Re: Follow up from today's meeting'\",\n      \"label\": \"Not spam\"\n    },\n    {\n      \"text\": \"Pre-read for tomorrow\",\n      \"label\": \"Not spam\"\n    }\n  ],\n  \"model\": \"YOUR-FINE-TUNED-MODEL-ID\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "inputs": ["Confirm your email address", "hey i need u to send some $"],
  "examples": [
    [
      "text": "Dermatologists don't like her!",
      "label": "Spam"
    ],
    [
      "text": "'Hello, open to this?'",
      "label": "Spam"
    ],
    [
      "text": "I need help please wire me $1000 right now",
      "label": "Spam"
    ],
    [
      "text": "Nice to know you ;)",
      "label": "Spam"
    ],
    [
      "text": "Please help me?",
      "label": "Spam"
    ],
    [
      "text": "Your parcel will be delivered today",
      "label": "Not spam"
    ],
    [
      "text": "Review changes to our Terms and Conditions",
      "label": "Not spam"
    ],
    [
      "text": "Weekly sync notes",
      "label": "Not spam"
    ],
    [
      "text": "'Re: Follow up from today's meeting'",
      "label": "Not spam"
    ],
    [
      "text": "Pre-read for tomorrow",
      "label": "Not spam"
    ]
  ],
  "model": "YOUR-FINE-TUNED-MODEL-ID"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/classify")! as URL,
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