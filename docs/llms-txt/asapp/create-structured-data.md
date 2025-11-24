# Source: https://docs.asapp.com/apis/autosummary/create-structured-data.md

# Create structured data

> Creates and returns set of structured data about a conversation that is already known to ASAPP.

You can use the id from ASAPP's system (conversationId or IssueId) or your own id (externalConversationId).

Provide an agentExternalId if you want to get the structured data for a single agent's involvment with a conversation.


## OpenAPI

````yaml api-specs/autosummary.yaml post /autosummary/v1/structured-data
paths:
  path: /autosummary/v1/structured-data
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
              conversationId:
                allOf:
                  - type: string
                    pattern: ^[A-Z0-9]+$
                    description: The identifier of the conversation from ASAPP's system.
              agentExternalId:
                allOf:
                  - type: string
                    description: >
                      Your agent identifier for structured data generation. This
                      allows retrieval of structured data exclusively for
                      conversation segments involving the specified agent.
            required: true
            requiredProperties:
              - conversationId
            example: &ref_0
              conversationId: 01GCS2XA9446BCQANJF2SXXVA0
              agentExternalId: agent-111
          - type: object
            properties:
              externalConversationId:
                allOf:
                  - type: string
                    description: >-
                      Your unique identifier for the conversation. This must
                      match to the `externalConversationId` you used in the
                      Conversations API.
              agentExternalId:
                allOf:
                  - type: string
                    description: >
                      Your agent identifier for structured data generation. This
                      allows retrieval of structured data exclusively for
                      conversation segments involving the specified agent.
            required: true
            requiredProperties:
              - externalConversationId
            example: *ref_0
          - type: object
            properties:
              issueId:
                allOf:
                  - type: string
                    description: >-
                      The identifier of the conversation from ASAPP's Messaging
                      Platform.
              agentExternalId:
                allOf:
                  - type: string
                    description: >
                      Your agent identifier for structured data generation. This
                      allows retrieval of structured data exclusively for
                      conversation segments involving the specified agent.
            required: true
            requiredProperties:
              - issueId
            example: *ref_0
        examples:
          example:
            value:
              conversationId: 01GCS2XA9446BCQANJF2SXXVA0
              agentExternalId: agent-111
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              conversationId:
                allOf:
                  - type: string
                    description: The id of the conversation.
              id:
                allOf:
                  - type: string
                    description: >
                      A unique identifier for this specific structured data.

                      • Each structured data request generates a new set with a
                      new `id`, even for the same conversation.

                      • The entire structured data content is regenerated with
                      each request.

                      • Use this ID when providing feedback on the structured
                      data.
              structuredDataMetrics:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          description: >
                            A unique code assigned to this structured data
                            field.
                        name:
                          type: string
                          description: >
                            The human readable name of this structured data
                            field
                        value:
                          type: string
                          description: |
                            The value of this structured data field
                    description: >-
                      The result of the structured data, which is a list of
                      field values.
            example:
              conversationId: 01GCS2XA9447BCQANJF2SXXVA0
              id: 0083d936-ff70-49fc-ac19-74f1246d8b27
              structuredDataMetrics:
                - id: q_abc_123
                  name: Issue Resolved
                  value: 'Yes'
                - id: q_xyz_123
                  name: Issue Escalated
                  value: 'No'
                - id: q_abc_124
                  name: Sales Made
                  value: 'No'
                - id: e_abc_123
                  name: Account Number
                  value: 8999246118
        examples:
          example:
            value:
              conversationId: 01GCS2XA9447BCQANJF2SXXVA0
              id: 0083d936-ff70-49fc-ac19-74f1246d8b27
              structuredDataMetrics:
                - id: q_abc_123
                  name: Issue Resolved
                  value: 'Yes'
                - id: q_xyz_123
                  name: Issue Escalated
                  value: 'No'
                - id: q_abc_124
                  name: Sales Made
                  value: 'No'
                - id: e_abc_123
                  name: Account Number
                  value: 8999246118
        description: Successfully generated structured data.
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