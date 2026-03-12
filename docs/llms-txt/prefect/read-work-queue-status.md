# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-queues/read-work-queue-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Work Queue Status

> Get the status of a work queue.



## OpenAPI

````yaml get /work_queues/{id}/status
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_queues/{id}/status:
    get:
      tags:
        - Work Queues
      summary: Read Work Queue Status
      description: Get the status of a work queue.
      operationId: read_work_queue_status_work_queues__id__status_get
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The work queue id
            title: Id
          description: The work queue id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkQueueStatusDetail'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    WorkQueueStatusDetail:
      properties:
        healthy:
          type: boolean
          title: Healthy
          description: Whether or not the work queue is healthy.
        late_runs_count:
          type: integer
          title: Late Runs Count
          description: The number of late flow runs in the work queue.
          default: 0
        last_polled:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Polled
          description: The last time an agent polled this queue for work.
        health_check_policy:
          $ref: '#/components/schemas/WorkQueueHealthPolicy'
          description: >-
            The policy used to determine whether or not the work queue is
            healthy.
      type: object
      required:
        - healthy
        - health_check_policy
      title: WorkQueueStatusDetail
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    WorkQueueHealthPolicy:
      properties:
        maximum_late_runs:
          anyOf:
            - type: integer
            - type: 'null'
          title: Maximum Late Runs
          description: >-
            The maximum number of late runs in the work queue before it is
            deemed unhealthy. Defaults to `0`.
          default: 0
        maximum_seconds_since_last_polled:
          anyOf:
            - type: integer
            - type: 'null'
          title: Maximum Seconds Since Last Polled
          description: >-
            The maximum number of time in seconds elapsed since work queue has
            been polled before it is deemed unhealthy. Defaults to `60`.
          default: 60
      type: object
      title: WorkQueueHealthPolicy
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).