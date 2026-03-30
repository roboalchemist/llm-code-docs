# Source: https://docs.wandb.ai/weave/reference/service-api/threads/threads-query-stream.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Threads Query Stream



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /threads/stream_query
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /threads/stream_query:
    post:
      tags:
        - Threads
      summary: Threads Query Stream
      operationId: threads_query_stream_threads_stream_query_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ThreadsQueryReq'
        required: true
      responses:
        '200':
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
      security:
        - HTTPBasic: []
components:
  schemas:
    ThreadsQueryReq:
      properties:
        project_id:
          type: string
          title: Project Id
          description: The ID of the project
          examples:
            - my_entity/my_project
        filter:
          anyOf:
            - $ref: '#/components/schemas/ThreadsQueryFilter'
            - type: 'null'
          description: Filter criteria for the threads query
        limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Limit
          description: Maximum number of threads to return
        offset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Offset
          description: Number of threads to skip
        sort_by:
          anyOf:
            - items:
                $ref: '#/components/schemas/SortBy'
              type: array
            - type: 'null'
          title: Sort By
          description: >-
            Sorting criteria for the threads. Supported fields: 'thread_id',
            'turn_count', 'start_time', 'last_updated', 'p50_turn_duration_ms',
            'p99_turn_duration_ms'.
          examples:
            - - direction: desc
                field: last_updated
      additionalProperties: false
      type: object
      required:
        - project_id
      title: ThreadsQueryReq
      description: >-
        Query threads with aggregated statistics based on turn calls only.


        Turn calls are the immediate children of thread contexts (where call.id
        == turn_id).

        This provides meaningful conversation-level statistics rather than
        including all

        nested implementation details.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ThreadsQueryFilter:
      properties:
        after_datetime:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After Datetime
          description: Only include threads with start_time after this timestamp
          examples:
            - '2024-01-01T00:00:00Z'
        before_datetime:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before Datetime
          description: Only include threads with last_updated before this timestamp
          examples:
            - '2024-12-31T23:59:59Z'
        thread_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Thread Ids
          description: Only include threads with thread_ids in this list
          examples:
            - - thread_1
              - thread_2
              - my_thread_id
      additionalProperties: false
      type: object
      title: ThreadsQueryFilter
    SortBy:
      properties:
        field:
          type: string
          title: Field
        direction:
          type: string
          enum:
            - asc
            - desc
          title: Direction
      additionalProperties: false
      type: object
      required:
        - field
        - direction
      title: SortBy
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
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````