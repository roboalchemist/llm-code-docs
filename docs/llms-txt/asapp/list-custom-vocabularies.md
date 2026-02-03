# Source: https://docs.asapp.com/apis/configuration/custom-vocabularies/list-custom-vocabularies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List custom vocabularies

> Retrieves all custom vocabulary configurations.




## OpenAPI

````yaml api-specs/partner-configuration.yaml get /configuration/v1/custom-vocabularies
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
  /configuration/v1/custom-vocabularies:
    get:
      tags:
        - Configuration
      summary: List custom vocabularies
      description: |
        Retrieves all custom vocabulary configurations.
      operationId: getCustomVocabularyConfigurations
      parameters:
        - in: query
          name: cursor
          schema:
            type: string
            nullable: true
          description: The cursor pointing to the current position
        - in: query
          name: limit
          schema:
            type: integer
            nullable: true
            minimum: 1
            maximum: 100
            default: 20
          description: The maximum amount of objects to retrieve
      responses:
        '200':
          description: Custom vocabulary configurations.
          content:
            application/json:
              schema:
                type: object
                properties:
                  customVocabularies:
                    type: array
                    items:
                      description: A list of custom vocabularies.
                      example:
                        id: '1'
                        phrase: IEEE
                        soundsLike:
                          - I triple E
                      type: object
                      allOf:
                        - type: object
                          properties:
                            phrase:
                              type: string
                              description: >-
                                The phrase to be added to the custom vocabulary.
                                This is the phrase you want to end up with in
                                the transcription.
                            soundsLike:
                              type: array
                              description: >-
                                An array of phonetic representations of the
                                phrase.
                              items:
                                type: string
                          required:
                            - phrase
                            - soundsLike
                          example:
                            phrase: IEEE
                            soundsLike:
                              - I triple E
                        - type: object
                          properties:
                            id:
                              type: string
                              description: The id of the custom vocabulary
                  nextCursor:
                    type: string
                    nullable: true
                    description: The next cursor to fetch
                    example: 6b29fc40-ca47-1067-b31d-00dd010662da
                  prevCursor:
                    type: string
                    nullable: true
                    description: The previous cursor to fetch
                    example: 04719ebd-13e1-40e9-8b92-0941cd16a19c
                required:
                  - customVocabularies
                  - nextCursor
                  - prevCursor
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