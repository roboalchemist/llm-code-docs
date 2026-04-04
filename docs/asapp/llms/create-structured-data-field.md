# Source: https://docs.asapp.com/apis/configuration/structured-data-fields/create-structured-data-field.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

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
openapi: 3.0.0
info:
  title: Partner Configuration API
  description: >
    This is the Partner Configuration API which allows ASAPP partners to manage
    configurations. Currently we are offering:
     - Custom Vocabularies: API endpoints to create, delete, update, and retrieve custom vocabularies.
     - Redaction Entities: API endpoints to update and retrieve redaction entities.
     - Structured Data Fields: API endpoints to create, delete, update, and retrieve structured data fields.

    Important Note: Custom Vocabularies and Redaction Entities do not support
    concurrent operations within the same category. You can perform updates,
    creations or deletes concurrently between Custom Vocabularies and Redaction
    Entities, but not within each one. Each operation may take up to 45 seconds
    to complete.
  version: 1.0.0
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: Configuration
    description: Operations to manage ASAPP configurations
paths:
  /configuration/v1/structured-data-fields:
    post:
      tags:
        - Configuration
      summary: Create a structured data field
      description: >
        Creates a new structured data field configuration that defines what
        information should be

        extracted from conversations.


        This endpoint supports creating two types of structured data fields:

        1. QUESTION type: Defines specific questions to be answered about the
        conversation
           Example: "Did the agent offer the correct promotion?"

        2. ENTITY type: Defines entities to be identified and extracted
           Example: Product names mentioned in the conversation

        These fields are used by the Structured Data API
        (/apis/autosummary/create-structured-data)

        to automatically extract the configured information from conversations.
      operationId: postStructuredDataField
      requestBody:
        required: true
        content:
          application/json:
            schema:
              oneOf:
                - title: Question
                  type: object
                  properties:
                    id:
                      type: string
                      description: The id of the structured data field
                      example: q_promotion_was_offered
                    name:
                      type: string
                      description: The name of the structured data field
                      example: Promotion was offered
                    categoryId:
                      type: string
                      description: |
                        The category of the structured data field.
                        Possible values:
                        - OUTCOME
                      example: OUTCOME
                    type:
                      type: string
                      description: |
                        The type of the structured data field. Must be either:
                        - QUESTION
                        - ENTITY
                      example: QUESTION
                    active:
                      type: boolean
                      description: Indicates if the structured data is active or not.
                      example: false
                    question:
                      type: object
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
                      type: array
                      items:
                        type: string
                        description: >-
                          The segment ids that the structured data field is
                          associated with
                        example: GLOBAL
                  required:
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
                - title: Entity
                  type: object
                  properties:
                    id:
                      type: string
                      description: The id of the structured data field
                      example: e_product
                    name:
                      type: string
                      description: The name of the structured data field
                      example: Product Name
                    categoryId:
                      type: string
                      description: The category id assigned
                      example: OUTCOME
                    type:
                      type: string
                      description: |
                        The type of the structured data field. Must be either:
                        - QUESTION
                        - ENTITY
                      example: ENTITY
                    active:
                      type: boolean
                      description: Indicates if the structured data is active or not
                      example: false
                    entity:
                      type: object
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
                            A list of example entities that can be extracted
                            from the conversation.
                      required:
                        - name
                        - description
                        - examples
                    segmentIds:
                      type: array
                      items:
                        type: string
                        description: >-
                          The segment ids that the structured data field is
                          associated with
                        example: GLOBAL
                  required:
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
                      description: >-
                        Product of the company being discussed in the
                        conversation
                      examples:
                        - Pink blazer
                        - Special trekking socks
                        - Super Backpack
                    active: true
              example:
                id: q_promotion_was_offered
                name: Promotion was offered
                categoryId: OUTCOME
                type: QUESTION
                question:
                  question: Did the agent offer the correct promotion?
                active: true
      responses:
        '201':
          description: Structured data field created.
          content:
            application/json:
              schema:
                oneOf:
                  - title: Question
                    type: object
                    properties:
                      id:
                        type: string
                        description: The id of the structured data field
                        example: q_promotion_was_offered
                      name:
                        type: string
                        description: The name of the structured data field
                        example: Promotion was offered
                      categoryId:
                        type: string
                        description: |
                          The category of the structured data field.
                          Possible values:
                          - OUTCOME
                        example: OUTCOME
                      type:
                        type: string
                        description: |
                          The type of the structured data field. Must be either:
                          - QUESTION
                          - ENTITY
                        example: QUESTION
                      active:
                        type: boolean
                        description: Indicates if the structured data is active or not.
                        example: false
                      question:
                        type: object
                        properties:
                          question:
                            type: string
                            description: >-
                              The question that will be answered using the
                              context of the conversation
                            example: Did the agent offer the correct promotion?
                        required:
                          - question
                      segmentIds:
                        type: array
                        items:
                          type: string
                          description: >-
                            The segment ids that the structured data field is
                            associated with
                          example: GLOBAL
                    required:
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
                  - title: Entity
                    type: object
                    properties:
                      id:
                        type: string
                        description: The id of the structured data field
                        example: e_product
                      name:
                        type: string
                        description: The name of the structured data field
                        example: Product Name
                      categoryId:
                        type: string
                        description: The category id assigned
                        example: OUTCOME
                      type:
                        type: string
                        description: |
                          The type of the structured data field. Must be either:
                          - QUESTION
                          - ENTITY
                        example: ENTITY
                      active:
                        type: boolean
                        description: Indicates if the structured data is active or not
                        example: false
                      entity:
                        type: object
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
                              A list of example entities that can be extracted
                              from the conversation.
                        required:
                          - name
                          - description
                          - examples
                      segmentIds:
                        type: array
                        items:
                          type: string
                          description: >-
                            The segment ids that the structured data field is
                            associated with
                          example: GLOBAL
                    required:
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
                        description: >-
                          Product of the company being discussed in the
                          conversation
                        examples:
                          - Pink blazer
                          - Special trekking socks
                          - Super Backpack
                      active: true
        '400':
          description: 400 - Bad request
          content:
            application/json:
              schema:
                description: Bad request response
                type: object
                properties:
                  error:
                    example:
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
        '401':
          description: 401 - Unauthorized
          content:
            application/json:
              schema:
                description: Unauthorized response
                type: object
                properties:
                  error:
                    example:
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
        '403':
          description: 403 - Forbidden
          content:
            application/json:
              schema:
                description: Forbidden response
                type: object
                properties:
                  error:
                    example:
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
        '404':
          description: 404 - Not Found
          content:
            application/json:
              schema:
                description: Not Found response
                type: object
                properties:
                  error:
                    example:
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
        '409':
          description: 409 - Conflict
          content:
            application/json:
              schema:
                description: Conflict response
                type: object
                properties:
                  error:
                    example:
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
        '413':
          description: 413 - Request Entity Too Large
          content:
            application/json:
              schema:
                description: Request Entity Too Large response
                type: object
                properties:
                  error:
                    example:
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
        '422':
          description: 422 - Unprocessable Entity
          content:
            application/json:
              schema:
                description: Unprocessable Entity response
                type: object
                properties:
                  error:
                    example:
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
        '429':
          description: 429 - Too Many Requests
          content:
            application/json:
              schema:
                description: Too Many Requests response
                type: object
                properties:
                  error:
                    example:
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
        '500':
          description: 500 - Internal Server Error
          content:
            application/json:
              schema:
                description: Default error response
                type: object
                properties:
                  error:
                    example:
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
        '503':
          description: 503 - Service Unavailable
          content:
            application/json:
              schema:
                description: Service Unavailable response
                type: object
                properties:
                  error:
                    example:
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
components:
  securitySchemes:
    API-ID:
      type: apiKey
      in: header
      name: asapp-api-id
    API-Secret:
      type: apiKey
      in: header
      name: asapp-api-secret

````