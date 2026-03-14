# Source: https://docs.together.ai/reference/queue-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Queue Status

> Poll the current status of a previously submitted job. Provide the request_id and model as query parameters.



## OpenAPI

````yaml GET /queue/status
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
  /queue/status:
    get:
      tags:
        - Queue
      summary: Get job status
      description: >-
        Poll the current status of a previously submitted job. Provide the
        request_id and model as query parameters.
      operationId: getQueueJobStatus
      parameters:
        - name: request_id
          in: query
          required: true
          schema:
            description: Request ID returned from the submit endpoint
            type: string
        - name: model
          in: query
          required: true
          schema:
            description: Model name the job was submitted to
            type: string
      responses:
        '200':
          description: Status information
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueJobStatusResponse'
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueError'
        '401':
          description: Unauthorized
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
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueError'
components:
  schemas:
    QueueJobStatusResponse:
      required:
        - request_id
        - model
        - status
      properties:
        claimed_at:
          description: Timestamp when a worker claimed the job
          format: date-time
          type: string
        created_at:
          description: Timestamp when the job was created
          format: date-time
          type: string
        done_at:
          description: Timestamp when the job completed (done or failed)
          format: date-time
          type: string
        info:
          description: |
            Job metadata. Contains keys from the submit request, plus any
            modifications from the model or system (e.g. progress, retry
            history).
          additionalProperties: true
          type: object
        inputs:
          description: Freeform model input, as submitted
          additionalProperties: true
          type: object
        model:
          description: Model identifier the job was submitted to
          type: string
        outputs:
          description: >-
            Freeform model output, populated when the job reaches done status.
            Contents are model-specific.
          additionalProperties: true
          type: object
        priority:
          description: Job priority. Higher values are processed first.
          type: integer
        request_id:
          description: The request ID that was returned from the submit endpoint
          type: string
        retries:
          description: |
            Number of times this job has been retried. Workers set a claim
            timeout and must send periodic status updates to keep the job alive.
            If no update is received within the timeout, the job is returned to
            the queue and retried. After 3 retries the job is permanently
            failed. Jobs explicitly failed by the model are not retried.
          type: integer
        status:
          description: >
            Current job status. Transitions: pending → running → done/failed. A
            pending job may also be canceled.
          enum:
            - pending
            - running
            - done
            - failed
            - canceled
          type: string
        warnings:
          description: Non-fatal messages about the request (e.g. deprecation notices)
          items:
            type: string
          type: array
      type: object
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