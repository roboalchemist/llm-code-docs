# Source: https://docs.helicone.ai/rest/webhooks/post-v1webhooks.md

# Create Webhook

> Create a new webhook

## OpenAPI

````yaml post /v1/webhooks
paths:
  path: /v1/webhooks
  method: post
  servers:
    - url: https://api.helicone.ai/
    - url: http://localhost:8585/
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''
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
              destination:
                allOf:
                  - type: string
              config:
                allOf:
                  - $ref: '#/components/schemas/Record_string.any_'
              includeData:
                allOf:
                  - type: boolean
            required: true
            refIdentifier: '#/components/schemas/WebhookData'
            requiredProperties:
              - destination
              - config
            additionalProperties: false
        examples:
          example:
            value:
              destination: <string>
              config: {}
              includeData: true
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - {}
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_unknown_'
            requiredProperties:
              - data
              - error
            additionalProperties: false
          - type: object
            properties:
              data:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
              error:
                allOf:
                  - {}
            refIdentifier: '#/components/schemas/ResultError_unknown_'
            requiredProperties:
              - data
              - error
            additionalProperties: false
        examples:
          example:
            value:
              data: <any>
        description: Ok
  deprecated: false
  type: path
components:
  schemas:
    Record_string.any_:
      properties: {}
      additionalProperties: {}
      type: object
      description: Construct a type with a set of properties K of type T

````