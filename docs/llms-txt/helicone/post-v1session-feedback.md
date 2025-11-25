# Source: https://docs.helicone.ai/rest/session/post-v1session-feedback.md

# Add Session Feedback

> Submit feedback for a specific session

## OpenAPI

````yaml post /v1/session/{sessionId}/feedback
paths:
  path: /v1/session/{sessionId}/feedback
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
        sessionId:
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
              rating:
                allOf:
                  - type: boolean
            required: true
            requiredProperties:
              - rating
        examples:
          example:
            value:
              rating: true
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