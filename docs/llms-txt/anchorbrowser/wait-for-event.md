# Source: https://docs.anchorbrowser.io/api-reference/event-coordination/wait-for-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Wait for Event

> Waits for a specific event to be signaled by another process, workflow, or session. 
This endpoint blocks until the event is signaled or the timeout is reached.
Useful for coordinating between multiple browser sessions or workflows.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/events/{event_name}/wait
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/events/{event_name}/wait:
    post:
      tags:
        - Event Coordination
      summary: Wait for Event
      description: >
        Waits for a specific event to be signaled by another process, workflow,
        or session. 

        This endpoint blocks until the event is signaled or the timeout is
        reached.

        Useful for coordinating between multiple browser sessions or workflows.
      parameters:
        - name: event_name
          in: path
          required: true
          description: The name of the event to wait for
          schema:
            type: string
      requestBody:
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WaitForEventRequestSchema'
      responses:
        '200':
          description: Event was signaled successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EventResponseSchema'
        '401':
          description: Unauthorized - Invalid API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '408':
          description: Timeout - Event was not signaled within the specified timeout
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to wait for event
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    WaitForEventRequestSchema:
      type: object
      properties:
        timeoutMs:
          type: integer
          description: >-
            Timeout in milliseconds to wait for the event. Defaults to 60000ms
            (1 minute).
    EventResponseSchema:
      type: object
      properties:
        data:
          type: object
          description: The event data that was signaled
          additionalProperties: true
          example:
            message: Task completed
            result: success
            timestamp: '2024-01-01T12:00:00Z'
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````