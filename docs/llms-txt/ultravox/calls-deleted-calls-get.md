# Source: https://docs.ultravox.ai/api-reference/calls/calls-deleted-calls-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Deleted Call

> Gets details for the specified deleted call



## OpenAPI

````yaml get /api/deleted_calls/{call_id}
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/deleted_calls/{call_id}:
    get:
      tags:
        - deleted_calls
      operationId: deleted_calls_retrieve
      parameters:
        - in: path
          name: call_id
          schema:
            type: string
            format: uuid
          required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallTombstone'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    CallTombstone:
      type: object
      properties:
        callId:
          type: string
          format: uuid
          readOnly: true
        accountId:
          type: string
          format: uuid
          readOnly: true
        created:
          type: string
          format: date-time
        deletionTime:
          type: string
          format: date-time
          readOnly: true
        joined:
          type: string
          format: date-time
          nullable: true
        ended:
          type: string
          format: date-time
          nullable: true
        maxDuration:
          type: string
          default: 3600s
        endReason:
          readOnly: true
          nullable: true
          description: |-
            The reason the call ended.

            * `unjoined` - Client never joined
            * `hangup` - Client hung up
            * `agent_hangup` - Agent hung up
            * `timeout` - Call timed out
            * `connection_error` - Connection error
            * `system_error` - System error
          oneOf:
            - $ref: '#/components/schemas/EndReasonEnum'
            - $ref: '#/components/schemas/NullEnum'
        recordingEnabled:
          type: boolean
          readOnly: true
        hadSummary:
          type: boolean
          readOnly: true
      required:
        - accountId
        - callId
        - created
        - deletionTime
        - endReason
        - hadSummary
        - recordingEnabled
    EndReasonEnum:
      enum:
        - unjoined
        - hangup
        - agent_hangup
        - timeout
        - connection_error
        - system_error
      type: string
      description: |-
        * `unjoined` - Client never joined
        * `hangup` - Client hung up
        * `agent_hangup` - Agent hung up
        * `timeout` - Call timed out
        * `connection_error` - Connection error
        * `system_error` - System error
    NullEnum:
      enum:
        - null
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````