# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/task-workers/read-task-workers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Task Workers

> Read active task workers. Optionally filter by task keys.

For more information, see https://docs.prefect.io/v3/how-to-guides/workflows/run-background-tasks.



## OpenAPI

````yaml post /task_workers/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /task_workers/filter:
    post:
      tags:
        - Task Workers
      summary: Read Task Workers
      description: >-
        Read active task workers. Optionally filter by task keys.


        For more information, see
        https://docs.prefect.io/v3/how-to-guides/workflows/run-background-tasks.
      operationId: read_task_workers_task_workers_filter_post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_read_task_workers_task_workers_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/TaskWorkerResponse'
                title: Response Read Task Workers Task Workers Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_task_workers_task_workers_filter_post:
      properties:
        task_worker_filter:
          anyOf:
            - $ref: '#/components/schemas/TaskWorkerFilter'
            - type: 'null'
          description: The task worker filter
      type: object
      title: Body_read_task_workers_task_workers_filter_post
    TaskWorkerResponse:
      properties:
        identifier:
          type: string
          title: Identifier
        task_keys:
          items:
            type: string
          type: array
          title: Task Keys
        timestamp:
          type: string
          format: date-time
          title: Timestamp
      type: object
      required:
        - identifier
        - task_keys
        - timestamp
      title: TaskWorkerResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    TaskWorkerFilter:
      properties:
        task_keys:
          items:
            type: string
          type: array
          title: Task Keys
      type: object
      required:
        - task_keys
      title: TaskWorkerFilter
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