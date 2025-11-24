# Source: https://docs.anchorbrowser.io/api-reference/event-coordination/wait-for-event.md

# Wait for Event

> Waits for a specific event to be signaled by another process, workflow, or session. 
This endpoint blocks until the event is signaled or the timeout is reached.
Useful for coordinating between multiple browser sessions or workflows.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/events/{event_name}/wait
paths:
  path: /v1/events/{event_name}/wait
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
              description: The name of the event to wait for
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              timeoutMs:
                allOf:
                  - type: integer
                    description: >-
                      Timeout in milliseconds to wait for the event. Defaults to
                      60000ms (1 minute).
            required: false
            refIdentifier: '#/components/schemas/WaitForEventRequestSchema'
        examples:
          example:
            value:
              timeoutMs: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    description: The event data that was signaled
                    additionalProperties: true
                    example:
                      message: Task completed
                      result: success
                      timestamp: '2024-01-01T12:00:00Z'
            refIdentifier: '#/components/schemas/EventResponseSchema'
        examples:
          example:
            value:
              data:
                message: Task completed
                result: success
                timestamp: '2024-01-01T12:00:00Z'
        description: Event was signaled successfully
    '401':
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
        description: Unauthorized - Invalid API key
    '408':
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
        description: Timeout - Event was not signaled within the specified timeout
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
        description: Failed to wait for event
  deprecated: false
  type: path
components:
  schemas: {}

````