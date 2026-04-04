# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/rate_limit_logs.md

# Rate Limit Logs

> Returns the last 50 rate limits that the account exceeded.

## OpenAPI

````yaml GET /api_keys/rate_limits/log
paths:
  path: /api_keys/rate_limits/log
  method: get
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
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        apiKeyId:
                          type: string
                          description: The ID of the API key that exceeded the limit.
                        modelId:
                          type: string
                          default: zai-org-glm-4.6
                          description: >-
                            The ID of the model that was used when the rate
                            limit was exceeded.
                        rateLimitTier:
                          type: string
                          description: The API tier of the rate limit.
                          example: paid
                        rateLimitType:
                          type: string
                          description: The type of rate limit that was exceeded.
                          example: RPM
                        timestamp:
                          type: string
                          description: The timestamp when the rate limit was exceeded.
                          example: '2023-10-01T12:00:00.000Z'
                      required:
                        - apiKeyId
                        - modelId
                        - rateLimitTier
                        - rateLimitType
                        - timestamp
                      additionalProperties: false
                    description: The last 50 rate limit logs for the account.
              object:
                allOf:
                  - type: string
                    enum:
                      - list
            requiredProperties:
              - data
              - object
            additionalProperties: false
        examples:
          example:
            value:
              data:
                - apiKeyId: <string>
                  modelId: zai-org-glm-4.6
                  rateLimitTier: paid
                  rateLimitType: RPM
                  timestamp: '2023-10-01T12:00:00.000Z'
              object: list
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
  schemas: {}

````