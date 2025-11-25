# Source: https://docs.helicone.ai/rest/ai-gateway/get-v1models-multimodal.md

# Get Multimodal Models

> Returns all available multimodal models supported by Helicone AI Gateway (OpenAI-compatible endpoint)

## OpenAPI

````yaml get /v1/models/multimodal
paths:
  path: /v1/models/multimodal
  method: get
  servers:
    - url: https://api.helicone.ai/
    - url: http://localhost:8585/
  request:
    security: []
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              object:
                allOf:
                  - type: string
                    enum:
                      - list
                    nullable: false
              data:
                allOf:
                  - items:
                      $ref: '#/components/schemas/OAIModel'
                    type: array
            refIdentifier: '#/components/schemas/OAIModelsResponse'
            requiredProperties:
              - object
              - data
            additionalProperties: false
        examples:
          example:
            value:
              object: list
              data:
                - id: <string>
                  object: model
                  created: 123
                  owned_by: <string>
        description: Ok
  deprecated: false
  type: path
components:
  schemas:
    OAIModel:
      properties:
        id:
          type: string
        object:
          type: string
          enum:
            - model
          nullable: false
        created:
          type: number
          format: double
        owned_by:
          type: string
      required:
        - id
        - object
        - created
        - owned_by
      type: object
      additionalProperties: false

````