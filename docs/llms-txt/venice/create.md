# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/create.md

# Create API Key

> Create a new API key.

## OpenAPI

````yaml POST /api_keys
paths:
  path: /api_keys
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              apiKeyType:
                allOf:
                  - type: string
                    enum:
                      - INFERENCE
                      - ADMIN
                    description: >-
                      The API Key type. Admin keys have full access to the API
                      while inference keys are only able to call inference
                      endpoints.
                    example: ADMIN
              consumptionLimit:
                allOf:
                  - type: object
                    properties:
                      usd:
                        anyOf:
                          - type: number
                            minimum: 0
                          - nullable: true
                            title: 'null'
                          - nullable: true
                            title: 'null'
                        description: USD limit
                        example: 50
                      diem:
                        anyOf:
                          - type: number
                            minimum: 0
                          - nullable: true
                            title: 'null'
                          - nullable: true
                            title: 'null'
                        description: Diem limit
                        example: 10
                      vcu:
                        anyOf:
                          - type: number
                            minimum: 0
                          - nullable: true
                            title: 'null'
                          - nullable: true
                            title: 'null'
                        description: VCU limit (deprecated - use Diem instead)
                        deprecated: true
                        example: 100
                    description: The API Key consumption limits for each epoch.
                    example:
                      usd: 50
                      diem: 10
                      vcu: 30
              description:
                allOf:
                  - type: string
                    description: The API Key description
                    example: Example API Key
              expiresAt:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - ''
                      - type: string
                        pattern: ^\d{4}-\d{2}-\d{2}$
                      - type: string
                        pattern: ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z$
                    description: >-
                      The API Key expiration date. If not provided, the key will
                      not expire.
                    example: '2023-10-01T12:00:00.000Z'
            description: >-
              The request body for creating a new API key. API key creation is
              rate limited to 20 requests per minute and a maximum of 500 active
              API keys per user. VCU (Legacy Diem) is being deprecated in favor
              of tokenized Diem. Please update your API calls to use Diem
              instead.
            requiredProperties:
              - apiKeyType
              - description
            additionalProperties: false
        examples:
          example:
            value:
              apiKeyType: ADMIN
              consumptionLimit:
                usd: 50
                diem: 10
                vcu: 30
              description: Example API Key
              expiresAt: '2023-10-01T12:00:00.000Z'
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
                      apiKey:
                        type: string
                        description: >-
                          The API Key. This is only shown once, so make sure to
                          save it somewhere safe.
                      apiKeyType:
                        type: string
                        enum:
                          - INFERENCE
                          - ADMIN
                        description: The API Key type
                        example: ADMIN
                      consumptionLimit:
                        type: object
                        properties:
                          usd:
                            anyOf:
                              - type: number
                                minimum: 0
                              - nullable: true
                                title: 'null'
                              - nullable: true
                                title: 'null'
                            description: USD limit
                            example: 50
                          diem:
                            anyOf:
                              - type: number
                                minimum: 0
                              - nullable: true
                                title: 'null'
                              - nullable: true
                                title: 'null'
                            description: Diem limit
                            example: 10
                          vcu:
                            anyOf:
                              - type: number
                                minimum: 0
                              - nullable: true
                                title: 'null'
                              - nullable: true
                                title: 'null'
                            description: VCU limit (deprecated - use Diem instead)
                            deprecated: true
                            example: 100
                        description: The API Key consumption limits for each epoch.
                        example:
                          usd: 50
                          diem: 10
                          vcu: 30
                      description:
                        type: string
                        description: The API Key description
                        example: Example API Key
                      expiresAt:
                        type: string
                        nullable: true
                        description: The API Key expiration date
                        example: '2023-10-01T12:00:00.000Z'
                      id:
                        type: string
                        description: The API Key ID
                        example: e28e82dc-9df2-4b47-b726-d0a222ef2ab5
                    required:
                      - apiKey
                      - apiKeyType
                      - consumptionLimit
                      - expiresAt
                      - id
                    additionalProperties: false
              success:
                allOf:
                  - type: boolean
            requiredProperties:
              - data
              - success
            additionalProperties: false
        examples:
          example:
            value:
              data:
                apiKey: <string>
                apiKeyType: ADMIN
                consumptionLimit:
                  usd: 50
                  diem: 10
                  vcu: 30
                description: Example API Key
                expiresAt: '2023-10-01T12:00:00.000Z'
                id: e28e82dc-9df2-4b47-b726-d0a222ef2ab5
              success: true
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - type: object
                    properties: {}
                    description: Details about the incorrect input
                    example:
                      _errors: []
                      field:
                        _errors:
                          - Field is required
              error:
                allOf:
                  - type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/DetailedError'
            requiredProperties:
              - error
        examples:
          example:
            value:
              details:
                _errors: []
                field:
                  _errors:
                    - Field is required
              error: <string>
        description: Invalid request parameters
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
    '429':
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
        description: Rate limit exceeded
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