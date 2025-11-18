# Source: https://docs.venice.ai/api-reference/endpoint/image/generate.md

# Generate Images

> Generate an image based on input parameters

## OpenAPI

````yaml POST /image/generate
paths:
  path: /image/generate
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
              description: >-
                Supported compression encodings (gzip, br). Only applied when
                return_binary is false.
              example: gzip, br
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              cfg_scale:
                allOf:
                  - type: number
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 20
                    description: >-
                      CFG scale parameter. Higher values lead to more adherence
                      to the prompt.
                    example: 7.5
              embed_exif_metadata:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      Embed prompt generation information into the image's EXIF
                      metadata.
                    example: false
              format:
                allOf:
                  - type: string
                    enum:
                      - jpeg
                      - png
                      - webp
                    default: webp
                    description: >-
                      The image format to return. WebP are smaller and optimized
                      for web use. PNG are higher quality but larger in file
                      size. 
                    example: webp
              height:
                allOf:
                  - type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 1280
                    default: 1024
                    description: >-
                      Height of the generated image. Each model has a specific
                      height and width divisor listed in the widthHeightDivisor
                      constraint in the model list endpoint.
                    example: 1024
              hide_watermark:
                allOf:
                  - type: boolean
                    default: false
                    description: >-
                      Whether to hide the Venice watermark. Venice may ignore
                      this parameter for certain generated content.
                    example: false
              inpaint:
                allOf:
                  - nullable: true
                    description: >-
                      This feature is deprecated and was disabled on May 19th,
                      2025. A revised in-painting API will be launched in the
                      near future.
                    deprecated: true
              lora_strength:
                allOf:
                  - type: integer
                    minimum: 0
                    maximum: 100
                    description: >-
                      Lora strength for the model. Only applies if the model
                      uses additional Loras.
                    example: 50
              model:
                allOf:
                  - type: string
                    description: The model to use for image generation.
                    example: hidream
              negative_prompt:
                allOf:
                  - type: string
                    maxLength: 1500
                    description: >-
                      A description of what should not be in the image.
                      Character limit is model specific and is listed in the
                      promptCharacterLimit constraint in the model list
                      endpoint.
                    example: Clouds, Rain, Snow
              prompt:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 1500
                    description: >-
                      The description for the image. Character limit is model
                      specific and is listed in the promptCharacterLimit setting
                      in the model list endpoint.
                    example: A beautiful sunset over a mountain range
              return_binary:
                allOf:
                  - type: boolean
                    default: false
                    description: Whether to return binary image data instead of base64.
                    example: false
              variants:
                allOf:
                  - type: integer
                    minimum: 1
                    maximum: 4
                    description: >-
                      Number of images to generate (1–4). Only supported when
                      return_binary is false.
                    example: 3
              safe_mode:
                allOf:
                  - type: boolean
                    default: true
                    description: >-
                      Whether to use safe mode. If enabled, this will blur
                      images that are classified as having adult content.
                    example: false
              seed:
                allOf:
                  - type: integer
                    minimum: -999999999
                    maximum: 999999999
                    default: 0
                    description: >-
                      Random seed for generation. If not provided, a random seed
                      will be used.
                    example: 123456789
              steps:
                allOf:
                  - type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 50
                    default: 20
                    description: >-
                      Number of inference steps. The following models have
                      reduced max steps from the global max: venice-sd35: 30 max
                      steps, hidream: 50 max steps, lustify-sdxl: 50 max steps,
                      lustify-v7: 50 max steps, qwen-image: 8 max steps,
                      wai-Illustrious: 30 max steps. These constraints are
                      exposed in the model list endpoint for each model.
                    example: 20
              style_preset:
                allOf:
                  - type: string
                    description: >-
                      An image style to apply to the image. Visit
                      https://docs.venice.ai/api-reference/endpoint/image/styles
                      for more details.
                    example: 3D Model
              width:
                allOf:
                  - type: integer
                    minimum: 0
                    exclusiveMinimum: true
                    maximum: 1280
                    default: 1024
                    description: >-
                      Width of the generated image. Each model has a specific
                      height and width divisor listed in the widthHeightDivisor
                      constraint in the model list endpoint.
                    example: 1024
            refIdentifier: '#/components/schemas/GenerateImageRequest'
            requiredProperties:
              - model
              - prompt
            additionalProperties: false
        examples:
          example:
            value:
              cfg_scale: 7.5
              embed_exif_metadata: false
              format: webp
              height: 1024
              hide_watermark: false
              inpaint: <any>
              lora_strength: 50
              model: hidream
              negative_prompt: Clouds, Rain, Snow
              prompt: A beautiful sunset over a mountain range
              return_binary: false
              variants: 3
              safe_mode: false
              seed: 123456789
              steps: 20
              style_preset: 3D Model
              width: 1024
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The ID of the request.
                    example: generate-image-1234567890
              images:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: Base64 encoded image data.
              request:
                allOf:
                  - nullable: true
                    description: The original request data sent to the API.
              timing:
                allOf:
                  - type: object
                    properties:
                      inferenceDuration:
                        type: number
                        description: Duration of inference in milliseconds
                      inferencePreprocessingTime:
                        type: number
                        description: Duration of preprocessing in milliseconds
                      inferenceQueueTime:
                        type: number
                        description: Duration of queueing in milliseconds
                      total:
                        type: number
                        description: Total duration of the request in milliseconds
                    required:
                      - inferenceDuration
                      - inferencePreprocessingTime
                      - inferenceQueueTime
                      - total
            requiredProperties:
              - id
              - images
              - timing
        examples:
          example:
            value:
              id: generate-image-1234567890
              images:
                - <string>
              request: <any>
              timing:
                inferenceDuration: 123
                inferencePreprocessingTime: 123
                inferenceQueueTime: 123
                total: 123
        description: Successfully generated image
      image/jpeg:
        schemaArray:
          - type: file
            contentEncoding: binary
            description: Raw image data when return_binary is true and format is jpeg
        examples:
          example: {}
        description: Successfully generated image
      image/png:
        schemaArray:
          - type: file
            contentEncoding: binary
            description: Raw image data when return_binary is true and format is png
        examples:
          example: {}
        description: Successfully generated image
      image/webp:
        schemaArray:
          - type: file
            contentEncoding: binary
            description: Raw image data when return_binary is true and format is webp
        examples:
          example: {}
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