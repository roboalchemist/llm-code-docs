# Source: https://docs.venice.ai/api-reference/endpoint/image/generations.md

# Generate Images (OpenAI Compatible API)

> Generate an image based on input parameters using an OpenAI compatible endpoint. This endpoint does not support the full feature set of the Venice Image Generation endpoint, but is compatible with the existing OpenAI endpoint.

## OpenAPI

````yaml POST /images/generations
paths:
  path: /images/generations
  method: post
  servers:
    - url: https://api.venice.ai/api/v1
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
      header:
        Accept-Encoding:
          schema:
            - type: string
              required: false
              description: Supported compression encodings (gzip, br).
              example: gzip, br
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              background:
                allOf:
                  - type: string
                    nullable: true
                    enum:
                      - transparent
                      - opaque
                      - auto
                    default: auto
                    description: >-
                      This parameter is not used in Venice image generation but
                      is supported for compatibility with OpenAI API
                    example: auto
              model:
                allOf:
                  - type: string
                    default: default
                    description: >-
                      The model to use for image generation. Defaults to
                      Venice's default image model. If a non-existent model is
                      specified (ie an OpenAI model name), it will default to
                      Venice's default image model.
                    example: hidream
              moderation:
                allOf:
                  - type: string
                    nullable: true
                    enum:
                      - low
                      - auto
                    default: auto
                    description: >-
                      auto enables safe venice mode which will blur out adult
                      content. low disables safe venice mode.
                    example: auto
              'n':
                allOf:
                  - type: integer
                    nullable: true
                    minimum: 1
                    maximum: 1
                    default: 1
                    description: >-
                      Number of images to generate. Venice presently only
                      supports 1 image per request.
                    example: 1
              output_compression:
                allOf:
                  - type: integer
                    nullable: true
                    minimum: 0
                    maximum: 100
                    default: 100
                    description: >-
                      This parameter is not used in Venice image generation but
                      is supported for compatibility with OpenAI API
              output_format:
                allOf:
                  - type: string
                    enum:
                      - jpeg
                      - png
                      - webp
                    default: png
                    description: Output format for generated images
                    example: png
              prompt:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 1500
                    description: A text description of the desired image.
                    example: A beautiful sunset over mountain ranges
              quality:
                allOf:
                  - type: string
                    nullable: true
                    enum:
                      - auto
                      - high
                      - medium
                      - low
                      - hd
                      - standard
                    default: auto
                    description: >-
                      This parameter is not used in Venice image generation but
                      is supported for compatibility with OpenAI API
                    example: auto
              response_format:
                allOf:
                  - type: string
                    nullable: true
                    enum:
                      - b64_json
                      - url
                    default: b64_json
                    description: Response format. URL will be a data URL.
                    example: b64_json
              size:
                allOf:
                  - type: string
                    nullable: true
                    enum:
                      - auto
                      - 256x256
                      - 512x512
                      - 1024x1024
                      - 1536x1024
                      - 1024x1536
                      - 1792x1024
                      - 1024x1792
                    default: auto
                    description: Size of generated images. Default is 1024x1024
                    example: 1024x1024
              style:
                allOf:
                  - type: string
                    nullable: true
                    enum:
                      - vivid
                      - natural
                    default: natural
                    description: >-
                      This parameter is not used in Venice image generation but
                      is supported for compatibility with OpenAI API
                    example: natural
              user:
                allOf:
                  - type: string
                    description: >-
                      This parameter is not used in Venice image generation but
                      is supported for compatibility with OpenAI API
                    example: user123
            refIdentifier: '#/components/schemas/SimpleGenerateImageRequest'
            requiredProperties:
              - prompt
            additionalProperties: false
        examples:
          example:
            value:
              background: auto
              model: hidream
              moderation: auto
              'n': 1
              output_compression: 100
              output_format: png
              prompt: A beautiful sunset over mountain ranges
              quality: auto
              response_format: b64_json
              size: 1024x1024
              style: natural
              user: user123
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              created:
                allOf:
                  - type: integer
                    description: Unix timestamp for when the request was created
                    example: 1713833628
              data:
                allOf:
                  - type: array
                    items:
                      anyOf:
                        - type: object
                          properties:
                            b64_json:
                              type: string
                              description: >-
                                Base64-encoded JSON string of the generated
                                image
                              example: iVBORw0KGgoAAAANSUhEUgAA...
                          required:
                            - b64_json
                        - type: object
                          properties:
                            url:
                              type: string
                              description: Data URL of the generated image
                              example: >-
                                data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...
                          required:
                            - url
            requiredProperties:
              - created
              - data
            additionalProperties: false
        examples:
          example:
            value:
              created: 1713833628
              data:
                - b64_json: iVBORw0KGgoAAAANSUhEUgAA...
        description: Successfully generated image
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - type: object
                    properties: {}
                    description: Details about the incorrect input
                    example:
                      _errors: []
                      field:
                        _errors:
                          - Field is required
              error:
                allOf:
                  - type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/DetailedError'
            requiredProperties:
              - error
        examples:
          example:
            value:
              details:
                _errors: []
                field:
                  _errors:
                    - Field is required
              error: <string>
        description: Invalid request parameters
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_1
              - error
        examples:
          example:
            value:
              error: <string>
        description: Authentication failed
    '402':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Insufficient USD or Diem balance to complete request
    '415':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Invalid request content-type
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Rate limit exceeded
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: Inference processing failed
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: The model is at capacity. Please try again later.
  deprecated: false
  type: path
components:
  schemas: {}

````