# Source: https://docs.helicone.ai/rest/evals/get-v1evalsscores.md

# Get Evaluation Scores

> Retrieve scoring metrics for evaluations

## OpenAPI

````yaml get /v1/evals/scores
paths:
  path: /v1/evals/scores
  method: get
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
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - items:
                      type: string
                    type: array
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_string-Array_'
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
            value:
              data:
                - <string>
        description: Ok
  deprecated: false
  type: path
components:
  schemas: {}

````