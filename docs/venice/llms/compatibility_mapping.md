# Source: https://docs.venice.ai/api-reference/endpoint/models/compatibility_mapping.md

# Compatibility Mapping

> Returns a list of model compatibility mappings and the associated model.

## OpenAPI

````yaml GET /models/compatibility_mapping
paths:
  path: /models/compatibility_mapping
  method: get
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
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
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - asr
                - embedding
                - image
                - text
                - tts
                - upscale
                - inpaint
                - video
              required: false
              description: Filter models by type.
              default: text
              example: text
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/ModelCompatibilitySchema'
              object:
                allOf:
                  - type: string
                    enum:
                      - list
              type:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - asr
                          - embedding
                          - image
                          - text
                          - tts
                          - upscale
                          - inpaint
                          - video
                      - type: string
                        enum:
                          - all
                          - code
                    description: Type of models returned.
                    example: text
            requiredProperties:
              - data
              - object
              - type
        examples:
          example:
            value:
              data:
                gpt-4o: llama-3.3-70b
              object: list
              type: text
        description: OK
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
        description: An unknown error occurred
  deprecated: false
  type: path
components:
  schemas:
    ModelCompatibilitySchema:
      type: object
      additionalProperties:
        type: string
      description: List of available models
      example:
        gpt-4o: llama-3.3-70b

````