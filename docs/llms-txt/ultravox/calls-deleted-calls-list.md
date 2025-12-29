# Source: https://docs.ultravox.ai/api-reference/calls/calls-deleted-calls-list.md

# List Deleted Calls

> Returns details for all deleted calls



## OpenAPI

````yaml get /api/deleted_calls
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/deleted_calls:
    get:
      tags:
        - deleted_calls
      operationId: deleted_calls_list
      parameters:
        - in: query
          name: agentIds
          schema:
            type: array
            items:
              type: string
              format: uuid
          description: Filter calls by the agent IDs.
        - name: cursor
          required: false
          in: query
          description: The pagination cursor value.
          schema:
            type: string
        - in: query
          name: durationMax
          schema:
            type: string
          description: Maximum duration of calls
        - in: query
          name: durationMin
          schema:
            type: string
          description: Minimum duration of calls
        - in: query
          name: fromDate
          schema:
            type: string
            format: date
          description: Start date (inclusive) for filtering calls by creation date
        - in: query
          name: metadata
          schema:
            type: object
            additionalProperties:
              type: string
          description: >-
            Filter calls by metadata. Use metadata.key=value to filter by
            specific key-value pairs.
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
        - in: query
          name: search
          schema:
            type: string
            minLength: 1
          description: The search string used to filter results
        - in: query
          name: toDate
          schema:
            type: string
            format: date
          description: End date (inclusive) for filtering calls by creation date
        - in: query
          name: voiceId
          schema:
            type: string
            format: uuid
          description: Filter calls by the associated voice ID
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedCallTombstoneList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedCallTombstoneList:
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
            $ref: '#/components/schemas/CallTombstone'
        total:
          type: integer
          example: 123
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt