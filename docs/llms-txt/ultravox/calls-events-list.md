# Source: https://docs.ultravox.ai/api-reference/calls/calls-events-list.md

# List Call Events

> Returns any events logged during the call



## OpenAPI

````yaml get /api/calls/{call_id}/events
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/calls/{call_id}/events:
    get:
      tags:
        - calls
      description: >-
        Fetch the (paginated) event log for a call, possibly filtered by
        severity.
      operationId: calls_events_list
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
          name: minimum_severity
          schema:
            type: string
            enum:
              - debug
              - error
              - info
              - warning
            default: info
          description: The minimum severity of events to include.
        - name: pageSize
          required: false
          in: query
          description: Number of results to return per page.
          schema:
            type: integer
        - in: query
          name: type
          schema:
            type: string
          description: If set, restricts returned events to those of the given type.
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedCallEventList'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    PaginatedCallEventList:
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
            $ref: '#/components/schemas/CallEvent'
        total:
          type: integer
          example: 123
    CallEvent:
      type: object
      properties:
        callId:
          type: string
          format: uuid
          readOnly: true
        callStageId:
          type: string
          format: uuid
          readOnly: true
        callTimestamp:
          type: string
          description: The timestamp of the event, relative to call start.
        severity:
          allOf:
            - $ref: '#/components/schemas/SeverityEnum'
          readOnly: true
        type:
          type: string
          description: The type of the event.
          maxLength: 50
        text:
          type: string
        extras:
          nullable: true
        wallClockTimestamp:
          type: string
          nullable: true
          description: The wall clock timestamp of the event, relative to call start.
      required:
        - callId
        - callStageId
        - callTimestamp
        - severity
        - text
        - type
        - wallClockTimestamp
    SeverityEnum:
      enum:
        - debug
        - info
        - warning
        - error
      type: string
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.ultravox.ai/llms.txt