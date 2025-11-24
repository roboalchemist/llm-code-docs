# Source: https://docs.perplexity.ai/api-reference/async-chat-completions-get.md

# List Async Chat Completions

> Lists all asynchronous chat completion requests for the authenticated user.

## OpenAPI

````yaml get /async/chat/completions
paths:
  path: /async/chat/completions
  method: get
  servers:
    - url: https://api.perplexity.ai
  request:
    security:
      - title: HTTPBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        limit:
          schema:
            - type: integer
              required: false
              description: Maximum number of requests to return.
              default: 20
        next_token:
          schema:
            - type: string
              required: false
              description: >-
                Token for fetching the next page of results. Ensure this token
                is URL-encoded when passed as a query parameter.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              next_token:
                allOf:
                  - title: Next Token
                    type: string
                    nullable: true
                    description: Token for fetching the next page of results.
              requests:
                allOf:
                  - title: Requests
                    type: array
                    items:
                      $ref: >-
                        #/components/schemas/AsyncApiChatCompletionsResponseSummary
            title: ListAsyncApiChatCompletionsResponse
            refIdentifier: '#/components/schemas/ListAsyncApiChatCompletionsResponse'
            requiredProperties:
              - requests
        examples:
          example:
            value:
              next_token: <string>
              requests:
                - id: <string>
                  created_at: 123
                  started_at: 123
                  completed_at: 123
                  failed_at: 123
                  model: <string>
                  status: CREATED
        description: Successfully retrieved list of async chat completion requests.
  deprecated: false
  type: path
components:
  schemas:
    AsyncProcessingStatus:
      title: AsyncProcessingStatus
      type: string
      enum:
        - CREATED
        - IN_PROGRESS
        - COMPLETED
        - FAILED
      description: The status of an asynchronous processing job.
    AsyncApiChatCompletionsResponseSummary:
      title: AsyncApiChatCompletionsResponseSummary
      type: object
      properties:
        id:
          title: ID
          type: string
        created_at:
          title: Created At
          type: integer
          format: int64
          description: Unix timestamp of when the request was created.
        started_at:
          title: Started At
          type: integer
          format: int64
          nullable: true
          description: Unix timestamp of when processing started.
        completed_at:
          title: Completed At
          type: integer
          format: int64
          nullable: true
          description: Unix timestamp of when processing completed.
        failed_at:
          title: Failed At
          type: integer
          format: int64
          nullable: true
          description: Unix timestamp of when processing failed.
        model:
          title: Model
          type: string
        status:
          $ref: '#/components/schemas/AsyncProcessingStatus'
      required:
        - id
        - created_at
        - model
        - status

````