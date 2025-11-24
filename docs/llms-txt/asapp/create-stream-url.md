# Source: https://docs.asapp.com/apis/generativeagent/create-stream-url.md

# Create stream URL

> This API creates a generative agent event streaming URL to start a streaming connection (SSE).

This API should be called when the client boots-up to request a streaming_url, before it calls endpoints whose responses are delivered asynchronously (and most likely before calling any other endpoint).

Provide the streamId to reconnect to a previous stream.


## OpenAPI

````yaml api-specs/generativeagent.yaml post /generativeagent/v1/streams
paths:
  path: /generativeagent/v1/streams
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
              streamId:
                allOf:
                  - type: string
                    description: >-
                      streamId to be associated with the streaming connection.
                      If not present, the llm-bot will provide one.
                    example: 97555020-0276-435f-8104-c378221ba292
            required: true
            description: The parameters to be associated with a given connection.
            example:
              streamId: 97555020-0276-435f-8104-c378221ba292
        examples:
          example:
            value:
              streamId: 97555020-0276-435f-8104-c378221ba292
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              streamId:
                allOf:
                  - type: string
                    description: >-
                      If it was provided in the request, this field will just
                      reaffirm the value. Otherwise, a newly generated one will
                      be provided.
                    example: 97555020-0276-435f-8104-c378221ba292
              streamingUrl:
                allOf:
                  - type: string
                    description: >-
                      URL for opening the SSE session. It may be used once, and
                      is valid for only 30 seconds.
                    example: >-
                      https://ws-co82129c.test.asapp.com/push-api/connect/sse\?token\=<token>
              messageTypes:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: Possible message types to be received from the agent.
                    example:
                      - generative-agent-message
            description: >-
              Streaming URL with its identifier and possible SSE message-types
              to be received.
            requiredProperties:
              - streamId
              - streamingUrl
              - messageTypes
        examples:
          example:
            value:
              streamId: 97555020-0276-435f-8104-c378221ba292
              streamingUrl: >-
                https://ws-co82129c.test.asapp.com/push-api/connect/sse\?token\=<token>
              messageTypes:
                - generative-agent-message
        description: Successfully generated a new streaming URL.
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