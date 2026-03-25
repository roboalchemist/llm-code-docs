# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/task-runs/update-task-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Task Run

> Updates a task run.



## OpenAPI

````yaml patch /task_runs/{id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /task_runs/{id}:
    patch:
      tags:
        - Task Runs
      summary: Update Task Run
      description: Updates a task run.
      operationId: update_task_run_task_runs__id__patch
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The task run id
            title: Id
          description: The task run id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TaskRunUpdate'
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    TaskRunUpdate:
      properties:
        name:
          type: string
          title: Name
          examples:
            - my-task-run
      additionalProperties: false
      type: object
      title: TaskRunUpdate
      description: Data used by the Prefect REST API to update a task run
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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