# Source: https://docs.fireworks.ai/api-reference/creates-an-embedding-vector-representing-the-input-text.md

# Create embeddings

## OpenAPI

````yaml post /embeddings
paths:
  path: /embeddings
  method: post
  servers:
    - url: https://api.fireworks.ai/inference/v1/
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
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
              input:
                allOf:
                  - description: >
                      Input text to embed, encoded as a string. To embed
                      multiple inputs in a single request, pass an array of
                      strings. You can pass structured object(s) to use along
                      with the prompt_template. The input must not exceed the
                      max input tokens for the model (8192 tokens for
                      `nomic-ai/nomic-embed-text-v1.5`), cannot be an empty
                      string, and any array must be 2048 dimensions or less.
                    example: The quick brown fox jumped over the lazy dog
                    oneOf:
                      - type: string
                        title: string
                        description: The string that will be turned into an embedding.
                        default: ''
                        example: This is a test.
                      - type: array
                        title: array of strings
                        description: >-
                          The array of strings that will be turned into an
                          embedding.
                        minItems: 1
                        maxItems: 2048
                        items:
                          type: string
                          default: ''
                        example: '[''This is a test.'', ''This is another test.'']'
                      - type: object
                        title: structured data
                        description: >-
                          Structured data to use while forming the input string
                          using the prompt template.
                        example:
                          text: Hello world
                          metadata:
                            id: 1
                            source: user_input
                      - type: array
                        title: array of objects
                        description: >-
                          Array of structured data to use while forming the
                          input strings using the prompt template.
                        items:
                          type: object
                        example:
                          - text: First document
                            metadata:
                              id: 1
                              source: user_input
                          - text: Second document
                            metadata:
                              id: 2
                              source: user_input
                    x-oaiExpandable: true
              model:
                allOf:
                  - description: The model to use for generating embeddings.
                    example: nomic-ai/nomic-embed-text-v1.5
                    type: string
                    x-oaiTypeLabel: string
              prompt_template:
                allOf:
                  - description: >
                      Template string for processing input data before
                      embedding. When provided, fields from the input object are
                      substituted using
                      [Jinja2](https://jinja.palletsprojects.com/en/stable/).
                      For example, simple substitution is done using
                      `{field_name}` syntax. The resulting string(s) are then
                      embedded. For array inputs, each object generates a
                      separate string.


                      Additionally, we expose `truncate_tokens(string)` function
                      to the template that allows to truncate the string based
                      on token lengths instead of characters
                    type: string
                    example: 'Embed this text: {text}'
              dimensions:
                allOf:
                  - description: >
                      The number of dimensions the resulting output embeddings
                      should have. Only supported in
                      `nomic-ai/nomic-embed-text-v1.5` and later models.
                    type: integer
                    minimum: 1
                    example: 768
              return_logits:
                allOf:
                  - description: >
                      If provided, returns raw model logits (pre-softmax scores)
                      for specified token or class indices. If an empty list is
                      provided, returns logits for all available tokens/classes.
                      Otherwise, only the specified indices are returned.


                      When used with normalize=true, softmax is applied to
                      create probability distributions. Softmax is applied only
                      to the selected tokens, so output probabilities will
                      always add up to 1.
                    type: array
                    items:
                      type: integer
                    example:
                      - 0
                      - 1
                      - 2
              normalize:
                allOf:
                  - description: >
                      Controls normalization of the output. When return_logits
                      is not provided, embeddings are L2 normalized (unit
                      vectors). When return_logits is provided, softmax is
                      applied to the selected logits to create probability
                      distributions.
                    type: boolean
                    default: false
                    example: false
            required: true
            refIdentifier: '#/components/schemas/CreateEmbeddingRequest'
            requiredProperties:
              - model
              - input
            additionalProperties: false
        examples:
          example:
            value:
              input: The quick brown fox jumped over the lazy dog
              model: nomic-ai/nomic-embed-text-v1.5
              prompt_template: 'Embed this text: {text}'
              dimensions: 768
              return_logits:
                - 0
                - 1
                - 2
              normalize: false
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    description: The list of embeddings generated by the model.
                    items:
                      $ref: '#/components/schemas/Embedding'
              model:
                allOf:
                  - type: string
                    description: The name of the model used to generate the embedding.
              object:
                allOf:
                  - type: string
                    description: The object type, which is always "list".
                    enum:
                      - list
              usage:
                allOf:
                  - type: object
                    description: The usage information for the request.
                    properties:
                      prompt_tokens:
                        type: integer
                        description: The number of tokens used by the prompt.
                      total_tokens:
                        type: integer
                        description: The total number of tokens used by the request.
                    required:
                      - prompt_tokens
                      - total_tokens
            refIdentifier: '#/components/schemas/CreateEmbeddingResponse'
            requiredProperties:
              - object
              - model
              - data
              - usage
        examples:
          example:
            value:
              data:
                - index: 123
                  embedding:
                    - 123
                  object: embedding
              model: <string>
              object: list
              usage:
                prompt_tokens: 123
                total_tokens: 123
        description: OK
  deprecated: false
  type: path
components:
  schemas:
    Embedding:
      type: object
      description: |
        Represents an embedding vector returned by embedding endpoint.
      properties:
        index:
          type: integer
          description: The index of the embedding in the list of embeddings.
        embedding:
          type: array
          description: >
            The embedding vector, which is a list of floats. The length of
            vector depends on the model as listed in the [embedding
            guide](/guides/querying-embedding-models).
          items:
            type: number
        object:
          type: string
          description: The object type, which is always "embedding".
          enum:
            - embedding
      required:
        - index
        - object
        - embedding
      x-oaiMeta:
        name: The embedding object
        example: |
          {
            "object": "embedding",
            "embedding": [
              0.0023064255,
              -0.009327292,
              .... (1536 floats total for ada-002)
              -0.0028842222,
            ],
            "index": 0
          }

````