# Source: https://docs.venice.ai/api-reference/endpoint/image/upscale.md

# Upscale and Enhance

> Upscale or enhance an image based on the supplied parameters. Using a scale of 1 with enhance enabled will only run the enhancer. The image can be provided either as a multipart form-data file upload or as a base64-encoded string in a JSON request.

## OpenAPI

````yaml POST /image/upscale
paths:
  path: /image/upscale
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
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              enhance:
                allOf:
                  - &ref_0
                    anyOf:
                      - type: boolean
                      - type: string
                        enum:
                          - 'true'
                          - 'false'
                    default: 'false'
                    description: >-
                      Whether to enhance the image using Venice's image engine
                      during upscaling. Must be true if scale is 1.
                    example: true
              enhanceCreativity:
                allOf:
                  - &ref_1
                    type: number
                    nullable: true
                    minimum: 0
                    maximum: 1
                    default: 0.5
                    description: >-
                      Higher values let the enhancement AI change the image
                      more. Setting this to 1 effectively creates an entirely
                      new image.
                    example: 0.5
              enhancePrompt:
                allOf:
                  - &ref_2
                    type: string
                    maxLength: 1500
                    description: >-
                      The text to image style to apply during prompt
                      enhancement. Does best with short descriptive prompts,
                      like gold, marble or angry, menacing.
                    example: gold
              image:
                allOf:
                  - &ref_3
                    anyOf:
                      - {}
                      - type: string
                    description: >-
                      The image to upscale. Can be either a file upload or a
                      base64-encoded string. Image dimensions must be at least
                      65536 pixels and final dimensions after scaling must not
                      exceed 16777216 pixels.
              replication:
                allOf:
                  - &ref_4
                    type: number
                    nullable: true
                    minimum: 0
                    maximum: 1
                    default: 0.35
                    description: >-
                      How strongly lines and noise in the base image are
                      preserved. Higher values are noisier but less plastic/AI
                      "generated"/hallucinated. Must be between 0 and 1.
                    example: 0.35
              scale:
                allOf:
                  - &ref_5
                    type: number
                    minimum: 1
                    maximum: 4
                    default: 2
                    description: >-
                      The scale factor for upscaling the image. Must be a number
                      between 1 and 4. Scale of 1 requires enhance to be set
                      true and will only run the enhancer. Scale must be > 1 if
                      enhance is false. A scale of 4 with large images will
                      result in the scale being dynamically set to ensure the
                      final image stays within the maximum size limits.
                    example: 2
            description: >-
              Upscale or enhance an image based on the supplied parameters.
              Using a scale of 1 with enhance enabled will only run the
              enhancer.
            refIdentifier: '#/components/schemas/UpscaleImageRequest'
            requiredProperties: &ref_6
              - image
            additionalProperties: false
            example: &ref_7
              enhance: true
              enhanceCreativity: 0.5
              enhancePrompt: gold
              image: iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A...
              scale: 2
        examples:
          example:
            value:
              enhance: true
              enhanceCreativity: 0.5
              enhancePrompt: gold
              image: iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A...
              scale: 2
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              enhance:
                allOf:
                  - *ref_0
              enhanceCreativity:
                allOf:
                  - *ref_1
              enhancePrompt:
                allOf:
                  - *ref_2
              image:
                allOf:
                  - *ref_3
              replication:
                allOf:
                  - *ref_4
              scale:
                allOf:
                  - *ref_5
            description: >-
              Upscale or enhance an image based on the supplied parameters.
              Using a scale of 1 with enhance enabled will only run the
              enhancer.
            refIdentifier: '#/components/schemas/UpscaleImageRequest'
            requiredProperties: *ref_6
            additionalProperties: false
            example: *ref_7
        examples:
          example:
            value:
              enhance: true
              enhanceCreativity: 0.5
              enhancePrompt: gold
              image: iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAIAAAB7GkOtAAAAIGNIUk0A...
              scale: 2
  response:
    '200':
      image/png:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: OK
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
                  - &ref_8
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_9
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
                  - *ref_8
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_9
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
                  - *ref_8
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_9
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
                  - *ref_8
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_9
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
                  - *ref_8
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_9
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
                  - *ref_8
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_9
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