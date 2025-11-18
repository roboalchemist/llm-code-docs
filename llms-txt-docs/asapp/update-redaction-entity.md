# Source: https://docs.asapp.com/apis/configuration/redaction-entities/update-redaction-entity.md

# Update a redaction entity

> Update the policies of a specific redaction entity. Only the policies field can be modified.


## OpenAPI

````yaml api-specs/partner-configuration.yaml patch /configuration/v1/redaction-entities/{entityId}
paths:
  path: /configuration/v1/redaction-entities/{entityId}
  method: patch
  servers:
    - url: https://api.sandbox.asapp.com
  request:
    security:
      - title: API ID & API Secret
        parameters:
          query: {}
          header:
            asapp-api-id:
              type: apiKey
            asapp-api-secret:
              type: apiKey
          cookie: {}
    parameters:
      path:
        entityId:
          schema:
            - type: string
              required: true
              description: Identifier of the entity
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              policies:
                allOf:
                  - description: >-
                      A set of policies that control when and how redaction is
                      applied. Each policy can be enabled or disabled
                      independently. Some entities may have a subset of
                      policies. Specifying a policy that is not applicable to an
                      entity will be ignored.
                    type: object
                    properties:
                      customerImmediate:
                        type: boolean
                        description: >-
                          Immediately redact sensitive information from the
                          customer's view during the live conversation. This is
                          typically used for highly sensitive data like credit
                          card numbers that should never be visible to
                          customers.
                        example: true
                      customerDelayed:
                        type: boolean
                        description: >-
                          Temporarily show sensitive information to the customer
                          before applying redaction. This allows customers to
                          verify the information was captured correctly before
                          it gets redacted.
                        example: false
                      agentImmediate:
                        type: boolean
                        description: >-
                          Immediately redact sensitive information from the
                          agent's view. This prevents agents from seeing
                          confidential customer data while still allowing them
                          to assist with the interaction.
                        example: false
                      autoTranscribe:
                        type: boolean
                        description: >-
                          Redact sensitive information from conversation
                          transcripts. This ensures sensitive data is not stored
                          in transcription records while preserving the context
                          of the conversation.
                        example: false
                      voice:
                        type: boolean
                        description: Redact sensitive information during voice calls.
                        example: false
            required: true
            requiredProperties:
              - policies
            example:
              policies:
                customerImmediate: false
                customerDelayed: false
                agentImmediate: false
        examples:
          example:
            value:
              policies:
                customerImmediate: false
                customerDelayed: false
                agentImmediate: false
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The id of the redaction entity
                    example: CREDIT_CARD_NUMBER
              description:
                allOf:
                  - type: string
                    description: The description of the redaction entity
                    example: ''
              policies:
                allOf:
                  - description: >-
                      A set of policies that control when and how redaction is
                      applied. Each policy can be enabled or disabled
                      independently. Some entities may have a subset of
                      policies. Specifying a policy that is not applicable to an
                      entity will be ignored.
                    type: object
                    properties:
                      customerImmediate:
                        type: boolean
                        description: >-
                          Immediately redact sensitive information from the
                          customer's view during the live conversation. This is
                          typically used for highly sensitive data like credit
                          card numbers that should never be visible to
                          customers.
                        example: true
                      customerDelayed:
                        type: boolean
                        description: >-
                          Temporarily show sensitive information to the customer
                          before applying redaction. This allows customers to
                          verify the information was captured correctly before
                          it gets redacted.
                        example: false
                      agentImmediate:
                        type: boolean
                        description: >-
                          Immediately redact sensitive information from the
                          agent's view. This prevents agents from seeing
                          confidential customer data while still allowing them
                          to assist with the interaction.
                        example: false
                      autoTranscribe:
                        type: boolean
                        description: >-
                          Redact sensitive information from conversation
                          transcripts. This ensures sensitive data is not stored
                          in transcription records while preserving the context
                          of the conversation.
                        example: false
                      voice:
                        type: boolean
                        description: Redact sensitive information during voice calls.
                        example: false
            requiredProperties:
              - id
              - description
              - policies
            example:
              id: CREDIT_CARD_NUMBER
              description: Redacts credit card number
              policies:
                customerImmediate: false
                customerDelayed: false
                agentImmediate: false
        examples:
          example:
            value:
              id: CREDIT_CARD_NUMBER
              description: Redacts credit card number
              policies:
                customerImmediate: false
                customerDelayed: false
                agentImmediate: false
        description: Successfully updated the redaction entity.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 400-01
                      message: Bad request
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Bad request response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 400-01
                message: Bad request
        description: 400 - Bad request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 401-01
                      message: Unauthorized
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Unauthorized response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 401-01
                message: Unauthorized
        description: 401 - Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 403-01
                      message: Forbidden Response
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Forbidden response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 403-01
                message: Forbidden Response
        description: 403 - Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 404-01
                      message: Not Found
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Not Found response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 404-01
                message: Not Found
        description: 404 - Not Found
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 409-01
                      message: Conflict
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Conflict response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 409-01
                message: Conflict
        description: 409 - Conflict
    '413':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 413-01
                      message: Request Entity Too Large
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Request Entity Too Large response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 413-01
                message: Request Entity Too Large
        description: 413 - Request Entity Too Large
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 422-01
                      message: Unprocessable Entity
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Unprocessable Entity response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 422-01
                message: Unprocessable Entity
        description: 422 - Unprocessable Entity
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 429-01
                      message: Too Many Requests
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Too Many Requests response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 429-01
                message: Too Many Requests
        description: 429 - Too Many Requests
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 500-01
                      message: Internal server error
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Default error response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 500-01
                message: Internal server error
        description: 500 - Internal Server Error
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - example:
                      requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                      code: 503-01
                      message: Service Unavailable
                    description: Error details
                    type: object
                    properties:
                      requestId:
                        type: string
                        description: Unique ID of the failing request
                      message:
                        type: string
                        description: Error message
                      code:
                        type: string
                        description: Error code
                    required:
                      - requestId
                      - message
            description: Service Unavailable response
        examples:
          example:
            value:
              error:
                requestId: 8e033668-9f1a-11ec-b909-0242ac120002
                code: 503-01
                message: Service Unavailable
        description: 503 - Service Unavailable
  deprecated: false
  type: path
components:
  schemas: {}

````