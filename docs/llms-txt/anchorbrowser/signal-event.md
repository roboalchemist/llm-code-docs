# Source: https://docs.anchorbrowser.io/api-reference/event-coordination/signal-event.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Signal Event

> Signals an event with associated data, unblocking any clients waiting for this event.
This enables coordination between different browser sessions, workflows, or external processes.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/events/{event_name}
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
  /v1/events/{event_name}:
    post:
      tags:
        - Event Coordination
      summary: Signal Event
      description: >
        Signals an event with associated data, unblocking any clients waiting
        for this event.

        This enables coordination between different browser sessions, workflows,
        or external processes.
      parameters:
        - name: event_name
          in: path
          required: true
          description: The name of the event to signal
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SignalEventRequestSchema'
      responses:
        '200':
          description: Event signaled successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SuccessResponse'
        '400':
          description: Invalid request - Event data is required
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '401':
          description: Unauthorized - Invalid API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to signal event
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    SignalEventRequestSchema:
      type: object
      required:
        - data
      properties:
        data:
          type: object
          description: Event data to be passed to waiting clients
          additionalProperties: true
          example:
            message: Task completed
            result: success
            timestamp: '2024-01-01T12:00:00Z'
    SuccessResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            status:
              type: string
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