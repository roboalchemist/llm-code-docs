# Source: https://docs.helicone.ai/rest/evals/post-v1evals.md

# Create Evaluation

> Create a new evaluation for a specific request

## OpenAPI

````yaml post /v1/evals/{requestId}
paths:
  path: /v1/evals/{requestId}
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
              score:
                allOf:
                  - type: number
                    format: double
              name:
                allOf:
                  - type: string
            required: true
            requiredProperties:
              - score
              - name
        examples:
          example:
            value:
              score: 123
              name: <string>
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