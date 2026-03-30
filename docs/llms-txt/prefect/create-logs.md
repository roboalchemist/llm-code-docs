# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/logs/create-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Logs

> Create new logs from the provided schema.

For more information, see https://docs.prefect.io/v3/how-to-guides/workflows/add-logging.



## OpenAPI

````yaml post /logs/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /logs/:
    post:
      tags:
        - Logs
      summary: Create Logs
      description: >-
        Create new logs from the provided schema.


        For more information, see
        https://docs.prefect.io/v3/how-to-guides/workflows/add-logging.
      operationId: create_logs_logs__post
      parameters:
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
              type: array
              items:
                $ref: '#/components/schemas/LogCreate'
              title: Logs
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    LogCreate:
      properties:
        name:
          type: string
          title: Name
          description: The logger name.
        level:
          type: integer
          title: Level
          description: The log level.
        message:
          type: string
          title: Message
          description: The log message.
        timestamp:
          type: string
          format: date-time
          title: Timestamp
          description: The log timestamp.
        flow_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Flow Run Id
        task_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Task Run Id
      additionalProperties: false
      type: object
      required:
        - name
        - level
        - message
        - timestamp
      title: LogCreate
      description: Data used by the Prefect REST API to create a log.
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