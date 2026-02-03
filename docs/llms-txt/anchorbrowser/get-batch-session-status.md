# Source: https://docs.anchorbrowser.io/api-reference/batch-sessions/get-batch-session-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Batch Session Status

> Retrieves detailed status information for a specific batch, including progress,
individual session details, and any errors that occurred.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/batch-sessions/{batch_id}
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
  /v1/batch-sessions/{batch_id}:
    get:
      tags:
        - Batch Sessions
      summary: Get Batch Session Status
      description: >
        Retrieves detailed status information for a specific batch, including
        progress,

        individual session details, and any errors that occurred.
      parameters:
        - name: batch_id
          in: path
          required: true
          description: The unique identifier of the batch
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Batch status retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    $ref: '#/components/schemas/BatchSessionStatusResponseSchema'
        '401':
          description: Invalid API Key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Batch not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    BatchSessionStatusResponseSchema:
      type: object
      properties:
        batch_id:
          type: string
          format: uuid
          description: Unique identifier for the batch
        status:
          type: string
          enum:
            - pending
            - processing
            - completed
            - failed
          description: Current status of the batch
        total_requests:
          type: integer
          description: Total number of sessions requested
        completed_requests:
          type: integer
          description: Number of sessions successfully created
        failed_requests:
          type: integer
          description: Number of sessions that failed to create
        processing_requests:
          type: integer
          description: Number of sessions currently being processed
        pending_requests:
          type: integer
          description: Number of sessions waiting to be processed
        created_at:
          type: string
          format: date-time
          description: Timestamp when the batch was created
        actual_completion_time:
          type: string
          format: date-time
          description: Timestamp when the batch completed (if completed)
        error:
          type: string
          description: Error message if batch failed
        sessions:
          type: array
          items:
            $ref: '#/components/schemas/BatchSessionItemSchema'
          description: Array of individual session details
        progress:
          type: object
          properties:
            percentage:
              type: number
              minimum: 0
              maximum: 100
              description: Completion percentage (0-100)
            current_phase:
              type: string
              enum:
                - queued
                - provisioning
                - configuring
                - ready
              description: Current processing phase
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
    BatchSessionItemSchema:
      type: object
      properties:
        item_index:
          type: integer
          description: Index of this session within the batch (0-based)
        session_id:
          type: string
          format: uuid
          description: Unique identifier for the browser session (if created successfully)
        status:
          type: string
          enum:
            - pending
            - processing
            - completed
            - failed
          description: Current status of this individual session
        cdp_url:
          type: string
          description: CDP websocket connection URL (if session is ready)
        live_view_url:
          type: string
          description: Live view URL for the session (if session is ready)
        error:
          type: string
          description: Error message if session creation failed
        retry_count:
          type: integer
          description: Number of times this session creation has been retried
        started_at:
          type: string
          format: date-time
          description: Timestamp when session creation started
        completed_at:
          type: string
          format: date-time
          description: Timestamp when session creation completed
        metadata:
          type: object
          additionalProperties: true
          description: Session-specific metadata
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````