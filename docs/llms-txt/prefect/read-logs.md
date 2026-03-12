# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/logs/read-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Logs

> Query for logs.



## OpenAPI

````yaml post /logs/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /logs/filter:
    post:
      tags:
        - Logs
      summary: Read Logs
      description: Query for logs.
      operationId: read_logs_logs_filter_post
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
              $ref: '#/components/schemas/Body_read_logs_logs_filter_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Log'
                title: Response Read Logs Logs Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_logs_logs_filter_post:
      properties:
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        logs:
          anyOf:
            - $ref: '#/components/schemas/LogFilter'
            - type: 'null'
        sort:
          $ref: '#/components/schemas/LogSort'
          default: TIMESTAMP_ASC
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_logs_logs_filter_post
    Log:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
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
          description: The flow run ID associated with the log.
        task_run_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Task Run Id
          description: The task run ID associated with the log.
      type: object
      required:
        - name
        - level
        - message
        - timestamp
        - id
        - created
        - updated
      title: Log
      description: An ORM representation of log data.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    LogFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        level:
          anyOf:
            - $ref: '#/components/schemas/LogFilterLevel'
            - type: 'null'
          description: Filter criteria for `Log.level`
        timestamp:
          anyOf:
            - $ref: '#/components/schemas/LogFilterTimestamp'
            - type: 'null'
          description: Filter criteria for `Log.timestamp`
        flow_run_id:
          anyOf:
            - $ref: '#/components/schemas/LogFilterFlowRunId'
            - type: 'null'
          description: Filter criteria for `Log.flow_run_id`
        task_run_id:
          anyOf:
            - $ref: '#/components/schemas/LogFilterTaskRunId'
            - type: 'null'
          description: Filter criteria for `Log.task_run_id`
        text:
          anyOf:
            - $ref: '#/components/schemas/LogFilterTextSearch'
            - type: 'null'
          description: Filter criteria for text search across log content
      additionalProperties: false
      type: object
      title: LogFilter
      description: Filter logs. Only logs matching all criteria will be returned
    LogSort:
      type: string
      enum:
        - TIMESTAMP_ASC
        - TIMESTAMP_DESC
      title: LogSort
      description: Defines log sorting options.
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
    Operator:
      type: string
      enum:
        - and_
        - or_
      title: Operator
      description: Operators for combining filter criteria.
    LogFilterLevel:
      properties:
        ge_:
          anyOf:
            - type: integer
            - type: 'null'
          title: Ge
          description: Include logs with a level greater than or equal to this level
          examples:
            - 20
        le_:
          anyOf:
            - type: integer
            - type: 'null'
          title: Le
          description: Include logs with a level less than or equal to this level
          examples:
            - 50
      additionalProperties: false
      type: object
      title: LogFilterLevel
      description: Filter by `Log.level`.
    LogFilterTimestamp:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: Only include logs with a timestamp at or before this time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: Only include logs with a timestamp at or after this time
      additionalProperties: false
      type: object
      title: LogFilterTimestamp
      description: Filter by `Log.timestamp`.
    LogFilterFlowRunId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of flow run IDs to include
      additionalProperties: false
      type: object
      title: LogFilterFlowRunId
      description: Filter by `Log.flow_run_id`.
    LogFilterTaskRunId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of task run IDs to include
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include logs without a task run id
      additionalProperties: false
      type: object
      title: LogFilterTaskRunId
      description: Filter by `Log.task_run_id`.
    LogFilterTextSearch:
      properties:
        query:
          type: string
          maxLength: 200
          title: Query
          description: Text search query string
          examples:
            - error
            - error -debug
            - '"connection timeout"'
            - +required -excluded
      additionalProperties: false
      type: object
      required:
        - query
      title: LogFilterTextSearch
      description: Filter by text search across log content.

````

Built with [Mintlify](https://mintlify.com).