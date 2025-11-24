# Source: https://docs.venice.ai/api-reference/endpoint/api_keys/generate_web3_key/post.md

# Generate API Key with Web3 Wallet

> Authenticates a wallet holding sVVV and creates an API key.

## OpenAPI

````yaml POST /api_keys/generate_web3_key
paths:
  path: /api_keys/generate_web3_key
  method: post
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security: []
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
                    default: Web3 API Key
                    description: The API Key description
                    example: Web3 API Key
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
              address:
                allOf:
                  - type: string
                    description: The wallet's address
                    example: '0x45B73055F3aDcC4577Bb709db10B19d11b5c94eE'
              signature:
                allOf:
                  - type: string
                    description: The token, signed with the wallet's private key
                    example: >-
                      0xbb5ff2e177f3a97fa553057864ad892eb64120f3eaf9356b4742a10f9a068d42725de895b5e45160b679cbe6961dc4cb552ba10dc97bdd8258d9154810785c451c
              token:
                allOf:
                  - type: string
                    description: >-
                      The token obtained from
                      https://api.venice.ai/api/v1/api_keys/generate_web3_key
                    example: >-
                      eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
            requiredProperties:
              - apiKeyType
              - address
              - signature
              - token
            additionalProperties: false
        examples:
          example:
            value:
              apiKeyType: ADMIN
              consumptionLimit:
                usd: 50
                diem: 10
                vcu: 30
              description: Web3 API Key
              expiresAt: '2023-10-01T12:00:00.000Z'
              address: '0x45B73055F3aDcC4577Bb709db10B19d11b5c94eE'
              signature: >-
                0xbb5ff2e177f3a97fa553057864ad892eb64120f3eaf9356b4742a10f9a068d42725de895b5e45160b679cbe6961dc4cb552ba10dc97bdd8258d9154810785c451c
              token: >-
                eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
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
  deprecated: false
  type: path
components:
  schemas: {}

````