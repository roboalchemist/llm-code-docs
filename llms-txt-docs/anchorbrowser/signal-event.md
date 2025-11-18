# Source: https://docs.anchorbrowser.io/api-reference/event-coordination/signal-event.md

# Signal Event

> Signals an event with associated data, unblocking any clients waiting for this event.
This enables coordination between different browser sessions, workflows, or external processes.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/events/{event_name}
paths:
  path: /v1/events/{event_name}
  method: post
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path:
        event_name:
          schema:
            - type: string
              required: true
              description: The name of the event to signal
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    description: Event data to be passed to waiting clients
                    additionalProperties: true
                    example:
                      message: Task completed
                      result: success
                      timestamp: '2024-01-01T12:00:00Z'
            required: true
            refIdentifier: '#/components/schemas/SignalEventRequestSchema'
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                message: Task completed
                result: success
                timestamp: '2024-01-01T12:00:00Z'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      status:
                        type: string
            refIdentifier: '#/components/schemas/SuccessResponse'
        examples:
          example:
            value:
              data:
                status: <string>
        description: Event signaled successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Invalid request - Event data is required
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Unauthorized - Invalid API key
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Failed to signal event
  deprecated: false
  type: path
components:
  schemas: {}

````