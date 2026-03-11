# Source: https://docs.together.ai/reference/queue-cancel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel Queue Job

> Cancel a pending job. Only jobs in pending status can be canceled.
Running jobs cannot be stopped. Returns the job status after the
attempt. If the job is not pending, returns 409 with the current status
unchanged.




## OpenAPI

````yaml POST /queue/cancel
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /queue/cancel:
    post:
      tags:
        - Queue
      summary: Cancel a queued job
      description: |
        Cancel a pending job. Only jobs in pending status can be canceled.
        Running jobs cannot be stopped. Returns the job status after the
        attempt. If the job is not pending, returns 409 with the current status
        unchanged.
      operationId: cancelQueueJob
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QueueCancelRequest'
        description: Cancel request
        required: true
      responses:
        '200':
          description: Successfully canceled
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueCancelResponse'
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueError'
        '404':
          description: Request not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueError'
        '409':
          description: Job could not be canceled (already completed/failed)
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueCancelResponse'
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueError'
components:
  schemas:
    QueueCancelRequest:
      properties:
        model:
          description: Model identifier the job was submitted to
          type: string
        request_id:
          description: The request ID returned from the submit endpoint
          type: string
      required:
        - model
        - request_id
      type: object
    QueueCancelResponse:
      type: object
      required:
        - status
      properties:
        status:
          description: |
            Job status after the cancel attempt. Only pending jobs can be
            canceled. If the job is already running, done, or failed, the status
            is returned unchanged.
          type: string
          enum:
            - canceled
            - running
            - done
            - failed
    QueueError:
      properties:
        code:
          description: Machine-readable error code
          type: string
        message:
          description: Human-readable error message
          type: string
        param:
          description: The parameter that caused the error, if applicable
          type: string
        type:
          description: Error category (e.g. "invalid_request_error", "not_found_error")
          type: string
      type: object
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).