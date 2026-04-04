# Source: https://docs.ultravox.ai/api-reference/calls/calls-messages-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Call Messages

> Returns all messages generated during the given call



## OpenAPI

````yaml get /api/calls/{call_id}/messages
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/messages:
    get:
      tags:
        - calls
      operationId: calls_messages_list
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - in: query
          name: mode
          schema:
            enum:
              - last_stage
              - in_call
            type: string
            default: last_stage
            minLength: 1
          description: >-
            * `last_stage` - Returns all messages for the call's last stage,
            similar to most call fields

            * `in_call` - Returns messages from all stages, excluding
            initialMessages
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Paginatedultravox.v1.MessageList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    Paginatedultravox.v1.MessageList:
      type: object
      required:
        - results
      properties:
        next:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cD00ODY%3D"
        previous:
          type: string
          nullable: true
          format: uri
          example: http://api.example.org/accounts/?cursor=cj0xJnA9NDg3
        results:
          type: array
          items:
            $ref: '#/components/schemas/ultravox.v1.Message'
        total:
          type: integer
          example: 123
    ultravox.v1.Message:
      type: object
      properties:
        role:
          enum:
            - MESSAGE_ROLE_UNSPECIFIED
            - MESSAGE_ROLE_USER
            - MESSAGE_ROLE_AGENT
            - MESSAGE_ROLE_TOOL_CALL
            - MESSAGE_ROLE_TOOL_RESULT
          type: string
          description: The message's role.
          format: enum
        text:
          type: string
          description: >-
            The message text for user and agent messages, tool arguments for
            tool_call messages, tool results for tool_result messages.
        invocationId:
          type: string
          description: >-
            The invocation ID for tool messages. Used to pair tool calls with
            their results.
        toolName:
          type: string
          description: The tool name for tool messages.
        errorDetails:
          type: string
          description: >-
            For failed tool calls, additional debugging information. While the
            text field is
             presented to the model so it can respond to failures gracefully, the full details
             are only exposed via the Ultravox REST API.
        medium:
          enum:
            - MESSAGE_MEDIUM_UNSPECIFIED
            - MESSAGE_MEDIUM_VOICE
            - MESSAGE_MEDIUM_TEXT
          type: string
          description: The medium of the message.
          format: enum
        callStageMessageIndex:
          type: integer
          description: The index of the message within the call stage.
          format: int32
        callStageId:
          type: string
          description: The call stage this message appeared in.
        callState:
          type: object
          description: If the message updated the call state, the new call state.
        timespan:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.InCallTimespan'
          description: |-
            The timespan during the call when this message occurred, according
             to the input audio stream.
             This is only set for messages that occurred during the call (stage)
             and not for messages in the call's (call stage's) initial messages.
        wallClockTimespan:
          allOf:
            - $ref: '#/components/schemas/ultravox.v1.InCallTimespan'
          description: |-
            The timespan during the call when this message occurred, according
             the wall clock, relative to the call's joined time.
             This is only set for messages that occurred during the call (stage)
             and not for messages in the call's (call stage's) initial messages.
      description: A message exchanged during a call.
    ultravox.v1.InCallTimespan:
      type: object
      properties:
        start:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: The offset relative to the start of the call.
        end:
          pattern: ^-?(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,9})?s$
          type: string
          description: The offset relative to the start of the call.
      description: A timespan during a call.
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````