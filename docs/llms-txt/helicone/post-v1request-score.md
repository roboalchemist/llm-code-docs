# Source: https://docs.helicone.ai/rest/request/post-v1request-score.md

# Submit Score

> Submit a score for a specific request.

## OpenAPI

````yaml post /v1/request/{requestId}/score
paths:
  path: /v1/request/{requestId}/score
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
              scores:
                allOf:
                  - $ref: '#/components/schemas/Scores'
            required: true
            refIdentifier: '#/components/schemas/ScoreRequest'
            requiredProperties:
              - scores
            additionalProperties: false
        examples:
          example:
            value:
              scores: {}
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
  schemas:
    Record_string.number-or-boolean-or-undefined_:
      properties: {}
      additionalProperties:
        anyOf:
          - type: number
            format: double
          - type: boolean
      type: object
      description: Construct a type with a set of properties K of type T
    Scores:
      $ref: '#/components/schemas/Record_string.number-or-boolean-or-undefined_'

````