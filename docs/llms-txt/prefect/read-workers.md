# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/read-workers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Workers

> Read all worker processes



## OpenAPI

````yaml post /work_pools/{work_pool_name}/workers/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/{work_pool_name}/workers/filter:
    post:
      tags:
        - Work Pools
      summary: Read Workers
      description: Read all worker processes
      operationId: read_workers_work_pools__work_pool_name__workers_filter_post
      parameters:
        - name: work_pool_name
          in: path
          required: true
          schema:
            type: string
            description: The work pool name
            title: Work Pool Name
          description: The work pool name
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
                #/components/schemas/Body_read_workers_work_pools__work_pool_name__workers_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/WorkerResponse'
                title: >-
                  Response Read Workers Work Pools  Work Pool Name  Workers
                  Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_workers_work_pools__work_pool_name__workers_filter_post:
      properties:
        workers:
          anyOf:
            - $ref: '#/components/schemas/WorkerFilter'
            - type: 'null'
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_workers_work_pools__work_pool_name__workers_filter_post
    WorkerResponse:
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
          description: The name of the worker.
        work_pool_id:
          type: string
          format: uuid
          title: Work Pool Id
          description: The work pool with which the queue is associated.
        last_heartbeat_time:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Heartbeat Time
          description: The last time the worker process sent a heartbeat.
        heartbeat_interval_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          title: Heartbeat Interval Seconds
          description: >-
            The number of seconds to expect between heartbeats sent by the
            worker.
        status:
          $ref: '#/components/schemas/WorkerStatus'
          description: Current status of the worker.
          default: OFFLINE
      type: object
      required:
        - name
        - work_pool_id
        - id
        - created
        - updated
      title: WorkerResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    WorkerFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        last_heartbeat_time:
          anyOf:
            - $ref: '#/components/schemas/WorkerFilterLastHeartbeatTime'
            - type: 'null'
          description: Filter criteria for `Worker.last_heartbeat_time`
        status:
          anyOf:
            - $ref: '#/components/schemas/WorkerFilterStatus'
            - type: 'null'
          description: Filter criteria for `Worker.status`
      additionalProperties: false
      type: object
      title: WorkerFilter
      description: Filter by `Worker.last_heartbeat_time`.
    WorkerStatus:
      type: string
      enum:
        - ONLINE
        - OFFLINE
      title: WorkerStatus
      description: Enumeration of worker statuses.
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
    WorkerFilterLastHeartbeatTime:
      properties:
        before_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Before
          description: >-
            Only include processes whose last heartbeat was at or before this
            time
        after_:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: After
          description: >-
            Only include processes whose last heartbeat was at or after this
            time
      additionalProperties: false
      type: object
      title: WorkerFilterLastHeartbeatTime
      description: Filter by `Worker.last_heartbeat_time`.
    WorkerFilterStatus:
      properties:
        any_:
          anyOf:
            - items:
                $ref: '#/components/schemas/WorkerStatus'
              type: array
            - type: 'null'
          title: Any
          description: A list of worker statuses to include
        not_any_:
          anyOf:
            - items:
                $ref: '#/components/schemas/WorkerStatus'
              type: array
            - type: 'null'
          title: Not Any
          description: A list of worker statuses to exclude
      additionalProperties: false
      type: object
      title: WorkerFilterStatus
      description: Filter by `Worker.status`.

````

Built with [Mintlify](https://mintlify.com).