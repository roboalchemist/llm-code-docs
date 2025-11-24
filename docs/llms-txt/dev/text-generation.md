# Source: https://dev.writer.com/no-code/text-generation.md

# Source: https://dev.writer.com/home/text-generation.md

# Source: https://dev.writer.com/api-reference/completion-api/text-generation.md

# Text generation

> Generate text completions using the specified model and prompt. This endpoint is useful for text generation tasks that don't require conversational context.

## OpenAPI

````yaml post /v1/completions
paths:
  path: /v1/completions
  method: post
  servers:
    - url: https://api.writer.com
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              model:
                allOf:
                  - type: string
                    description: >-
                      The [ID of the model](https://dev.writer.com/home/models)
                      to use for generating text. Supports `palmyra-x5`,
                      `palmyra-x4`, `palmyra-fin`, `palmyra-med`,
                      `palmyra-creative`, and `palmyra-x-003-instruct`.
              prompt:
                allOf:
                  - type: string
                    description: >-
                      The input text that the model will process to generate a
                      response.
              max_tokens:
                allOf:
                  - type: integer
                    format: int64
                    description: >-
                      The maximum number of tokens that the model can generate
                      in the response.
              temperature:
                allOf:
                  - type: number
                    format: double
                    description: >-
                      Controls the randomness of the model's outputs. Higher
                      values lead to more random outputs, while lower values
                      make the model more deterministic.
              top_p:
                allOf:
                  - type: number
                    format: double
                    description: >-
                      Used to control the nucleus sampling, where only the most
                      probable tokens with a cumulative probability of top_p are
                      considered for sampling, providing a way to fine-tune the
                      randomness of predictions.
              stop:
                allOf:
                  - oneOf:
                      - type: array
                        items:
                          type: string
                      - type: string
                    description: >-
                      Specifies stopping conditions for the model's output
                      generation. This can be an array of strings or a single
                      string that the model will look for as a signal to stop
                      generating further tokens.
              best_of:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      Specifies the number of completions to generate and return
                      the best one. Useful for generating multiple outputs and
                      choosing the best based on some criteria.
              random_seed:
                allOf:
                  - type: integer
                    format: int32
                    description: >-
                      A seed used to initialize the random number generator for
                      the model, ensuring reproducibility of the output when the
                      same inputs are provided.
              stream:
                allOf:
                  - type: boolean
                    description: >-
                      Determines whether the model's output should be streamed.
                      If true, the output is generated and sent incrementally,
                      which can be useful for real-time applications.
            required: true
            refIdentifier: '#/components/schemas/completions_request'
            requiredProperties:
              - model
              - prompt
            example:
              model: palmyra-x-003-instruct
              prompt: Write me an SEO article about...
              max_tokens: 150
              temperature: 0.7
              top_p: 0.9
              stop:
                - .
              best_of: 1
              random_seed: 42
              stream: false
        examples:
          example:
            value:
              model: palmyra-x-003-instruct
              prompt: Write me an SEO article about...
              max_tokens: 150
              temperature: 0.7
              top_p: 0.9
              stop:
                - .
              best_of: 1
              random_seed: 42
              stream: false
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST https://api.writer.com/v1/completions \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"model":"palmyra-x-003-instruct","prompt":"Write me a
          short SEO article about camping
          gear","max_tokens":150,"temperature":0.7,"top_p":0.9,"stop":["."],"best_of":1,"random_seed":42,"stream":false}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const completion = await client.completions.create({
              model: 'palmyra-x-003-instruct',
              prompt: 'Write me a short SEO article about camping gear',
            });

            console.log(completion.choices);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          completion = client.completions.create(
              model="palmyra-x-003-instruct",
              prompt="Write me a short SEO article about camping gear",
          )
          print(completion.choices)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              choices:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/completions_choice'
                    minItems: 1
                    description: >-
                      A list of choices generated by the model, each containing
                      the text of the completion and associated metadata such as
                      log probabilities.
              model:
                allOf:
                  - type: string
                    description: >-
                      The identifier of the model that was used to generate the
                      responses in the 'choices' array.
            refIdentifier: '#/components/schemas/completions_response'
            requiredProperties:
              - choices
            example:
              choices:
                - text: Sure! Here's a search engine optimized article about...
                  log_probs: null
              model: palmyra-x-003-instruct
        examples:
          example:
            value:
              choices:
                - text: Sure! Here's a search engine optimized article about...
                  log_probs: null
              model: palmyra-x-003-instruct
        description: Successful response
      text/event-stream:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/streaming_data'
        examples:
          example:
            value:
              - value: <string>
        description: Successful response
  deprecated: false
  type: path
components:
  schemas:
    logprobs:
      type: object
      required:
        - content
        - refusal
      nullable: true
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/logprobs_token'
          nullable: true
        refusal:
          type: array
          items:
            $ref: '#/components/schemas/logprobs_token'
          nullable: true
    logprobs_token:
      title: logprobs_token
      required:
        - token
        - logprob
        - top_logprobs
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type: array
          items:
            type: integer
            format: int32
        top_logprobs:
          type: array
          items:
            $ref: '#/components/schemas/top_log_prob'
    top_log_prob:
      title: top_log_prob
      description: >-
        An array of mappings for each token to its top log probabilities,
        showing detailed prediction probabilities.
      required:
        - token
        - logprob
      type: object
      properties:
        token:
          type: string
        logprob:
          type: number
          format: double
        bytes:
          type: array
          items:
            type: integer
            format: int32
    completions_choice:
      required:
        - text
      type: object
      properties:
        text:
          type: string
          description: >-
            The generated text output from the model, which forms the main
            content of the response.
        log_probs:
          $ref: '#/components/schemas/logprobs'
    streaming_data:
      required:
        - value
      type: object
      properties:
        value:
          type: string

````