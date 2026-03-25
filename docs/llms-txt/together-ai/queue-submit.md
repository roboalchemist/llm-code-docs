# Source: https://docs.together.ai/reference/queue-submit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Submit Queue Job

> Submit a new job to the queue for asynchronous processing. Jobs are
processed in strict priority order (higher priority first, FIFO within
the same priority). Returns a request ID that can be used to poll status
or cancel the job.




## OpenAPI

````yaml POST /queue/submit
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
  /queue/submit:
    post:
      tags:
        - Queue
      summary: Submit a queued job
      description: |
        Submit a new job to the queue for asynchronous processing. Jobs are
        processed in strict priority order (higher priority first, FIFO within
        the same priority). Returns a request ID that can be used to poll status
        or cancel the job.
      operationId: submitQueueJob
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QueueJobRequest'
        description: Job request
        required: true
      responses:
        '200':
          description: Successfully queued request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueJobResponse'
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
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueError'
components:
  schemas:
    QueueJobRequest:
      properties:
        info:
          description: |
            Arbitrary JSON metadata stored with the job and returned in status
            responses. The model and system may add or update keys during
            processing.
          additionalProperties: true
          type: object
        model:
          description: Required model identifier
          type: string
        payload:
          description: >-
            Freeform model input. Passed unchanged to the model. Contents are
            model-specific.
          additionalProperties: true
          type: object
        priority:
          default: 0
          description: |
            Job priority. Higher values are processed first (strict priority
            ordering). Jobs with equal priority are processed in submission
            order (FIFO).
          type: integer
      required:
        - model
        - payload
      type: object
    QueueJobResponse:
      properties:
        error:
          $ref: '#/components/schemas/QueueError'
        requestId:
          description: >-
            Unique identifier for the submitted job. Use this to poll status or
            cancel.
          type: string
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