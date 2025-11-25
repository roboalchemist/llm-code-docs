# Source: https://docs.helicone.ai/rest/request/put-v1request-property.md

# Upsert Request Property

> Create or update a property of a specific request.

## OpenAPI

````yaml put /v1/request/{requestId}/property
paths:
  path: /v1/request/{requestId}/property
  method: put
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
      path:
        requestId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              value:
                allOf:
                  - type: string
              key:
                allOf:
                  - type: string
            required: true
            requiredProperties:
              - value
              - key
        examples:
          example:
            value:
              value: <string>
              key: <string>
  response:
    '200':
      application/json:
        schemaArray:
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
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_null_'
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
                  - type: string
            refIdentifier: '#/components/schemas/ResultError_string_'
            requiredProperties:
              - data
              - error
            additionalProperties: false
        examples:
          example:
            value: {}
        description: Ok
  deprecated: false
  type: path
components:
  schemas: {}

````