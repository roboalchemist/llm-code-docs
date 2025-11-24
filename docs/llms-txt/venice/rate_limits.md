# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/rate_limits.md

# Rate Limits and Balances

> Return details about user balances and rate limits.

## OpenAPI

````yaml GET /api_keys/rate_limits
paths:
  path: /api_keys/rate_limits
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
                  - type: object
                    properties:
                      accessPermitted:
                        type: boolean
                        description: >-
                          Does the API key have access to consume the inference
                          APIs?
                        example: true
                      apiTier:
                        type: object
                        properties:
                          id:
                            type: string
                            description: The ID of the API tier.
                            example: paid
                          isCharged:
                            type: boolean
                            description: Is the API key pay per use (in Diem or USD).
                            example: true
                        required:
                          - id
                          - isCharged
                      balances:
                        type: object
                        properties:
                          USD:
                            type: number
                            description: The USD balance of the key.
                            example: 50.23
                          DIEM:
                            type: number
                            description: The Diem balance of the key.
                            example: 100.023
                      keyExpiration:
                        type: string
                        nullable: true
                        description: >-
                          The timestamp the API key expires. If null, the key
                          never expires.
                        example: '2025-06-01T00:00:00.000Z'
                      nextEpochBegins:
                        type: string
                        description: >-
                          The timestamp when the next epoch begins. This is
                          relevant for rate limits that reset at the start of
                          each epoch.
                        example: '2025-05-07T00:00:00.000Z'
                      rateLimits:
                        type: array
                        items:
                          type: object
                          properties:
                            apiModelId:
                              type: string
                              description: The ID of the API model.
                              example: zai-org-glm-4.6
                            rateLimits:
                              type: array
                              items:
                                type: object
                                properties:
                                  amount:
                                    type: number
                                    description: The rate limit for the API model.
                                    example: 100
                                  type:
                                    type: string
                                    description: >-
                                      The time period for the rate limit. Can be
                                      Requests Per Minute (RPM), Requests Per
                                      Day (RPD), or Tokens Per Minute (TPM).
                                    example: RPM
                                required:
                                  - amount
                                  - type
                          required:
                            - rateLimits
                    required:
                      - accessPermitted
                      - apiTier
                      - balances
                      - keyExpiration
                      - nextEpochBegins
                      - rateLimits
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                accessPermitted: true
                apiTier:
                  id: paid
                  isCharged: true
                balances:
                  USD: 50.23
                  DIEM: 100.023
                keyExpiration: '2025-06-01T00:00:00.000Z'
                nextEpochBegins: '2025-05-07T00:00:00.000Z'
                rateLimits:
                  - apiModelId: zai-org-glm-4.6
                    rateLimits:
                      - amount: 100
                        type: RPM
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