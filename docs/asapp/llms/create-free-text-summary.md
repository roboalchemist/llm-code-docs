# Source: https://docs.asapp.com/apis/autosummary/create-free-text-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create free text summary

> Generates a concise, human-readable summary of a conversation.

Provide an agentExternalId if you want to get the summary for a single agent's involvment with a conversation.

You can use the id from ASAPP's system (conversationId or IssueId) or your own id (externalConversationId).

Multilingual support: You can get summaries in languages different from English by making use of the 'Accept-Language' header.




## OpenAPI

````yaml api-specs/autosummary.yaml post /autosummary/v1/free-text-summaries
openapi: 3.0.0
info:
  title: AutoSummary API
  description: >
    This is the AutoSummary API which can be used for summarizing conversations.
    It offers two kind of summaries, structured UMR tags or generated free text.
    In addition, it allows structured data about the conversation to be
    retrieved. The usual usage flow consist on first publishing the content of
    the conversation on Conversations API and, once it has finished, invoking
    the corresponding summarization endpoint of this API. A single request
    containing a reference to the conversation is received and a response
    including the corresponding summary or structured data is returned.


    By automating this activity, organizations decrease after-call work,
    reducing agent time and effort, and produce consistent, structured summaries
    and data well-suited for analytics.
  version: 1.0.0
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: AutoSummary
    description: Endpoints for summarizing conversations and retrieving structured data
paths:
  /autosummary/v1/free-text-summaries:
    post:
      tags:
        - AutoSummary
      summary: Create free text summary
      description: >
        Generates a concise, human-readable summary of a conversation.


        Provide an agentExternalId if you want to get the summary for a single
        agent's involvment with a conversation.


        You can use the id from ASAPP's system (conversationId or IssueId) or
        your own id (externalConversationId).


        Multilingual support: You can get summaries in languages different from
        English by making use of the 'Accept-Language' header.
      operationId: createFreeTextSummary
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              oneOf:
                - type: object
                  properties:
                    conversationId:
                      type: string
                      pattern: ^[A-Z0-9]+$
                      description: The identifier of the conversation from ASAPP's system.
                    agentExternalId:
                      type: string
                      description: Your unique identifier for the agent.
                  required:
                    - conversationId
                - type: object
                  properties:
                    externalConversationId:
                      type: string
                      description: >-
                        Your unique identifier for the conversation. This must
                        match to the `externalConversationId` you used in the
                        Conversations API.
                    agentExternalId:
                      type: string
                      description: Your unique identifier for the agent.
                  required:
                    - externalConversationId
                - type: object
                  properties:
                    issueId:
                      type: string
                      description: >-
                        The identifier of the conversation from ASAPP's
                        Messaging Platform.
                    agentExternalId:
                      type: string
                      description: Your unique identifier for the agent.
                  required:
                    - issueId
              example:
                conversationId: 01GCS2AA9447BCQANJF2SXXVA0
                agentExternalId: agent-111
      responses:
        '200':
          description: Successfully generated free text summary.
          content:
            application/json:
              schema:
                type: object
                properties:
                  conversationId:
                    type: string
                    description: >-
                      The unique identifier of the conversation for which the
                      summary was generated.
                  summaryId:
                    type: string
                    description: >
                      A unique identifier for this specific summary.

                      • Each summary request generates a new summary with a new
                      `summaryId`, even for the same conversation.

                      • The entire summary content is regenerated with each
                      request.

                      • Use this ID when providing feedback on the summary.
                  summaryText:
                    type: string
                    description: |
                      The generated free-text summary of the conversation.
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
        default:
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