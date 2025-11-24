# Source: https://docs.asapp.com/apis/configuration/structured-data-fields/create-structured-data-field.md

# Create a structured data field

> Creates a new structured data field configuration that defines what information should be
extracted from conversations.

This endpoint supports creating two types of structured data fields:
1. QUESTION type: Defines specific questions to be answered about the conversation
   Example: "Did the agent offer the correct promotion?"

2. ENTITY type: Defines entities to be identified and extracted
   Example: Product names mentioned in the conversation

These fields are used by the Structured Data API (/apis/autosummary/create-structured-data)
to automatically extract the configured information from conversations.


## OpenAPI

````yaml api-specs/partner-configuration.yaml post /configuration/v1/structured-data-fields
paths:
  path: /configuration/v1/structured-data-fields
  method: post
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The id of the structured data field
                    example: q_promotion_was_offered
              name:
                allOf:
                  - type: string
                    description: The name of the structured data field
                    example: Promotion was offered
              categoryId:
                allOf:
                  - type: string
                    description: |
                      The category of the structured data field.
                      Possible values:
                      - OUTCOME
                    example: OUTCOME
              type:
                allOf:
                  - type: string
                    description: |
                      The type of the structured data field. Must be either:
                      - QUESTION
                      - ENTITY
                    example: QUESTION
              active:
                allOf:
                  - type: boolean
                    description: Indicates if the structured data is active or not.
                    example: false
              question:
                allOf:
                  - type: object
                    properties:
                      question:
                        type: string
                        description: >-
                          The question that will be answered using the context
                          of the conversation
                        example: Did the agent offer the correct promotion?
                    required:
                      - question
              segmentIds:
                allOf:
                  - type: array
                    items:
                      type: string
                      description: >-
                        The segment ids that the structured data field is
                        associated with
                      example: GLOBAL
            required: true
            title: Question
            requiredProperties:
              - id
              - active
              - question
              - type
              - categoryId
              - name
              - segmentIds
            example:
              id: q_promotion_was_offered
              name: Promotion was offered
              categoryId: OUTCOME
              type: QUESTION
              question:
                question: Did the agent offer the correct promotion?
              active: true
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The id of the structured data field
                    example: e_product
              name:
                allOf:
                  - type: string
                    description: The name of the structured data field
                    example: Product Name
              categoryId:
                allOf:
                  - type: string
                    description: The category id assigned
                    example: OUTCOME
              type:
                allOf:
                  - type: string
                    description: |
                      The type of the structured data field. Must be either:
                      - QUESTION
                      - ENTITY
                    example: ENTITY
              active:
                allOf:
                  - type: boolean
                    description: Indicates if the structured data is active or not
                    example: false
              entity:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                        description: The name of the entity.
                        example: Product Name
                      description:
                        type: string
                        description: The description of the entity.
                        example: >-
                          Product of the company being discussed in the
                          conversation.
                      examples:
                        type: array
                        items:
                          type: string
                          example: Special trekking socks
                        description: >-
                          A list of example entities that can be extracted from
                          the conversation.
                    required:
                      - name
                      - description
                      - examples
              segmentIds:
                allOf:
                  - type: array
                    items:
                      type: string
                      description: >-
                        The segment ids that the structured data field is
                        associated with
                      example: GLOBAL
            required: true
            title: Entity
            requiredProperties:
              - id
              - active
              - entity
              - type
              - categoryId
              - name
              - segmentIds
            example:
              id: e_product
              name: Product Name
              categoryId: OUTCOME
              type: ENTITY
              question:
                question: Did the agent offer the correct promotion?
              active: true
              entity:
                name: Product Name
                description: Product of the company being discussed in the conversation
                examples:
                  - Pink blazer
                  - Special trekking socks
                  - Super Backpack
        examples:
          example:
            value:
              id: q_promotion_was_offered
              name: Promotion was offered
              categoryId: OUTCOME
              type: QUESTION
              question:
                question: Did the agent offer the correct promotion?
              active: true
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The id of the structured data field
                    example: q_promotion_was_offered
              name:
                allOf:
                  - type: string
                    description: The name of the structured data field
                    example: Promotion was offered
              categoryId:
                allOf:
                  - type: string
                    description: |
                      The category of the structured data field.
                      Possible values:
                      - OUTCOME
                    example: OUTCOME
              type:
                allOf:
                  - type: string
                    description: |
                      The type of the structured data field. Must be either:
                      - QUESTION
                      - ENTITY
                    example: QUESTION
              active:
                allOf:
                  - type: boolean
                    description: Indicates if the structured data is active or not.
                    example: false
              question:
                allOf:
                  - type: object
                    properties:
                      question:
                        type: string
                        description: >-
                          The question that will be answered using the context
                          of the conversation
                        example: Did the agent offer the correct promotion?
                    required:
                      - question
              segmentIds:
                allOf:
                  - type: array
                    items:
                      type: string
                      description: >-
                        The segment ids that the structured data field is
                        associated with
                      example: GLOBAL
            title: Question
            requiredProperties:
              - id
              - active
              - question
              - type
              - categoryId
              - name
              - segmentIds
            example:
              id: q_promotion_was_offered
              name: Promotion was offered
              categoryId: OUTCOME
              type: QUESTION
              question:
                question: Did the agent offer the correct promotion?
              active: true
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: The id of the structured data field
                    example: e_product
              name:
                allOf:
                  - type: string
                    description: The name of the structured data field
                    example: Product Name
              categoryId:
                allOf:
                  - type: string
                    description: The category id assigned
                    example: OUTCOME
              type:
                allOf:
                  - type: string
                    description: |
                      The type of the structured data field. Must be either:
                      - QUESTION
                      - ENTITY
                    example: ENTITY
              active:
                allOf:
                  - type: boolean
                    description: Indicates if the structured data is active or not
                    example: false
              entity:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                        description: The name of the entity.
                        example: Product Name
                      description:
                        type: string
                        description: The description of the entity.
                        example: >-
                          Product of the company being discussed in the
                          conversation.
                      examples:
                        type: array
                        items:
                          type: string
                          example: Special trekking socks
                        description: >-
                          A list of example entities that can be extracted from
                          the conversation.
                    required:
                      - name
                      - description
                      - examples
              segmentIds:
                allOf:
                  - type: array
                    items:
                      type: string
                      description: >-
                        The segment ids that the structured data field is
                        associated with
                      example: GLOBAL
            title: Entity
            requiredProperties:
              - id
              - active
              - entity
              - type
              - categoryId
              - name
              - segmentIds
            example:
              id: e_product
              name: Product Name
              categoryId: OUTCOME
              type: ENTITY
              entity:
                name: Product Name
                description: Product of the company being discussed in the conversation
                examples:
                  - Pink blazer
                  - Special trekking socks
                  - Super Backpack
              active: true
        examples:
          example:
            value:
              id: q_promotion_was_offered
              name: Promotion was offered
              categoryId: OUTCOME
              type: QUESTION
              question:
                question: Did the agent offer the correct promotion?
              active: true
        description: Structured data field created.
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