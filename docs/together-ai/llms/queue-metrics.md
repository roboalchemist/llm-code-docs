# Source: https://docs.together.ai/reference/queue-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Queue Metrics

> Get the current queue statistics for a model, including pending and running job counts.



## OpenAPI

````yaml GET /queue/metrics
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
  /queue/metrics:
    get:
      tags:
        - Queue
      summary: Get queue metrics
      description: >-
        Get the current queue statistics for a model, including pending and
        running job counts.
      operationId: getQueueMetrics
      parameters:
        - name: model
          in: query
          required: true
          schema:
            description: Model name to get metrics for
            type: string
      responses:
        '200':
          description: Queue metrics
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueMetricsResponse'
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
    QueueMetricsResponse:
      type: object
      required:
        - messages_running
        - messages_waiting
        - total_jobs
      properties:
        messages_running:
          description: Number of jobs currently being processed
          type: integer
        messages_waiting:
          description: Number of jobs waiting to be claimed by a worker
          type: integer
        total_jobs:
          description: Total number of active jobs (waiting + running)
          type: integer
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