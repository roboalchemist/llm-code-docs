# Source: https://docs.asapp.com/apis/autosummary/provide-feedback.md

# Provide feedback.

> Create a feedback event with the full and updated summary. Each event is associated with a specific summary id. 

The event must contain the final summary, in the form of text.        


## OpenAPI

````yaml api-specs/autosummary.yaml post /autosummary/v1/feedback/free-text-summaries/{conversationId}
paths:
  path: /autosummary/v1/feedback/free-text-summaries/{conversationId}
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
      path:
        conversationId:
          schema:
            - type: string
              required: true
              description: The identifier for a conversation.
      query:
        agentExternalId:
          schema:
            - type: string
              required: false
              description: Your unique identifier for the agent.
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              externalConversationId:
                allOf:
                  - description: >
                      Your unique identifier for the conversation. This must
                      match to the `externalConversationId` you used in the
                      Conversations API.
                    type: string
              summaryId:
                allOf:
                  - description: >
                      The identifier of the summary you are providing feedback
                      on.
                    type: string
              summaryText:
                allOf:
                  - description: The full text of the final summary.
                    type: string
            required: true
            description: >
              Information regarding the updated free-text summary. It must
              contain the full updated summary as a string.
            requiredProperties:
              - summaryId
              - summaryText
            example:
              externalConversationId: 01GCS2XA9447BCQANJF2SXXVA0
              summaryId: 0083d936-ff70-49fc-ac19-74f1246d8b27
              summaryText: |
                The customer has issues with his symmetric internet service.
                The customer explained the service has not enough bandwidth.
                The customer explained the service has not enough bandwidth.
                The agent explained how to run a diagnosis.
                The customer ran the diagnosis.
        examples:
          example:
            value:
              externalConversationId: 01GCS2XA9447BCQANJF2SXXVA0
              summaryId: 0083d936-ff70-49fc-ac19-74f1246d8b27
              summaryText: |
                The customer has issues with his symmetric internet service.
                The customer explained the service has not enough bandwidth.
                The customer explained the service has not enough bandwidth.
                The agent explained how to run a diagnosis.
                The customer ran the diagnosis.
  response:
    '202':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Successfully accepted a feedback event for the summary.
        examples: {}
        description: Successfully accepted a feedback event for the summary.
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
    default:
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
  deprecated: false
  type: path
components:
  schemas: {}

````