# Source: https://docs.anchorbrowser.io/api-reference/batch-sessions/get-batch-session-status.md

# Get Batch Session Status

> Retrieves detailed status information for a specific batch, including progress,
individual session details, and any errors that occurred.


## OpenAPI

````yaml openapi-mintlify.yaml get /v1/batch-sessions/{batch_id}
paths:
  path: /v1/batch-sessions/{batch_id}
  method: get
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
        batch_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the batch
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/BatchSessionStatusResponseSchema'
        examples:
          example:
            value:
              data:
                batch_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                status: pending
                total_requests: 123
                completed_requests: 123
                failed_requests: 123
                processing_requests: 123
                pending_requests: 123
                created_at: '2023-11-07T05:31:56Z'
                actual_completion_time: '2023-11-07T05:31:56Z'
                error: <string>
                sessions:
                  - item_index: 123
                    session_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                    status: pending
                    cdp_url: <string>
                    live_view_url: <string>
                    error: <string>
                    retry_count: 123
                    started_at: '2023-11-07T05:31:56Z'
                    completed_at: '2023-11-07T05:31:56Z'
                    metadata: {}
                progress:
                  percentage: 50
                  current_phase: queued
        description: Batch status retrieved successfully
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
        description: Invalid API Key
    '404':
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
        description: Batch not found
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
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas:
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

````