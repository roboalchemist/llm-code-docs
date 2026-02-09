# Source: https://docs.asapp.com/apis/generativeagent/create-stream-url.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create stream URL

> This API creates a generative agent event streaming URL to start a streaming connection (SSE).

This API should be called when the client boots-up to request a streaming_url, before it calls endpoints whose responses are delivered asynchronously (and most likely before calling any other endpoint).

Provide the streamId to reconnect to a previous stream.




## OpenAPI

````yaml api-specs/generativeagent.yaml post /generativeagent/v1/streams
openapi: 3.0.1
info:
  title: GenerativeAgent API
  description: >
    GenerativeAgent API allows customers to interact with a chat / voice
    automation bot leveraging LLMs by sending messages and receiving responses
    asynchronously through webhooks
  contact:
    email: api-info@asapp.com
  license:
    name: ASAPP Software License
    url: https://api.asapp.com/LICENSE
  version: '0.1'
servers:
  - url: https://api.sandbox.asapp.com
security:
  - API-ID: []
    API-Secret: []
tags:
  - name: GenerativeAgent
    description: >-
      Operations to send messages and trigger GenerativeAgent to respond or
      query the current state
paths:
  /generativeagent/v1/streams:
    post:
      tags:
        - GenerativeAgent
      summary: Create stream URL
      description: >
        This API creates a generative agent event streaming URL to start a
        streaming connection (SSE).


        This API should be called when the client boots-up to request a
        streaming_url, before it calls endpoints whose responses are delivered
        asynchronously (and most likely before calling any other endpoint).


        Provide the streamId to reconnect to a previous stream.
      operationId: postStreams
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: The parameters to be associated with a given connection.
              properties:
                streamId:
                  type: string
                  description: >-
                    streamId to be associated with the streaming connection. If
                    not present, the llm-bot will provide one.
                  example: 97555020-0276-435f-8104-c378221ba292
              example:
                streamId: 97555020-0276-435f-8104-c378221ba292
      responses:
        '200':
          description: Successfully generated a new streaming URL.
          content:
            application/json:
              schema:
                type: object
                description: >-
                  Streaming URL with its identifier and possible SSE
                  message-types to be received.
                properties:
                  streamId:
                    type: string
                    description: >-
                      If it was provided in the request, this field will just
                      reaffirm the value. Otherwise, a newly generated one will
                      be provided.
                    example: 97555020-0276-435f-8104-c378221ba292
                  streamingUrl:
                    type: string
                    description: >-
                      URL for opening the SSE session. It may be used once, and
                      is valid for only 30 seconds.
                    example: >-
                      https://ws-co82129c.test.asapp.com/push-api/connect/sse\?token\=<token>
                  messageTypes:
                    type: array
                    items:
                      type: string
                    description: Possible message types to be received from the agent.
                    example:
                      - generative-agent-message
                required:
                  - streamId
                  - streamingUrl
                  - messageTypes
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