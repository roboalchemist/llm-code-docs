# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-queues/read-work-queues.md

# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/read-work-queues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Work Queues

> Read all work pool queues



## OpenAPI

````yaml post /work_pools/{work_pool_name}/queues/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/{work_pool_name}/queues/filter:
    post:
      tags:
        - Work Pools
      summary: Read Work Queues
      description: Read all work pool queues
      operationId: read_work_queues_work_pools__work_pool_name__queues_filter_post
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
                #/components/schemas/Body_read_work_queues_work_pools__work_pool_name__queues_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/WorkQueueResponse'
                title: >-
                  Response Read Work Queues Work Pools  Work Pool Name  Queues
                  Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_work_queues_work_pools__work_pool_name__queues_filter_post:
      properties:
        work_queues:
          $ref: '#/components/schemas/WorkQueueFilter'
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
      title: Body_read_work_queues_work_pools__work_pool_name__queues_filter_post
    WorkQueueResponse:
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
          pattern: ^[^/%&><]+$
          title: Name
          description: The name of the work queue.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: An optional description for the work queue.
          default: ''
        is_paused:
          type: boolean
          title: Is Paused
          description: Whether or not the work queue is paused.
          default: false
        concurrency_limit:
          anyOf:
            - type: integer
              minimum: 0
            - type: 'null'
          title: Concurrency Limit
          description: An optional concurrency limit for the work queue.
        priority:
          type: integer
          exclusiveMinimum: 0
          title: Priority
          description: >-
            The queue's priority. Lower values are higher priority (1 is the
            highest).
          default: 1
        work_pool_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Work Pool Id
          description: The work pool with which the queue is associated.
        filter:
          anyOf:
            - $ref: '#/components/schemas/QueueFilter'
            - type: 'null'
          description: 'DEPRECATED: Filter criteria for the work queue.'
          deprecated: true
        last_polled:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Polled
          description: The last time an agent polled this queue for work.
        work_pool_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Work Pool Name
          description: The name of the work pool the work pool resides within.
        status:
          anyOf:
            - $ref: '#/components/schemas/WorkQueueStatus'
            - type: 'null'
          description: The queue status.
      type: object
      required:
        - name
        - id
        - created
        - updated
      title: WorkQueueResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    WorkQueueFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/WorkQueueFilterId'
            - type: 'null'
          description: Filter criteria for `WorkQueue.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/WorkQueueFilterName'
            - type: 'null'
          description: Filter criteria for `WorkQueue.name`
      additionalProperties: false
      type: object
      title: WorkQueueFilter
      description: |-
        Filter work queues. Only work queues matching all criteria will be
        returned
    QueueFilter:
      properties:
        tags:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Tags
          description: Only include flow runs with these tags in the work queue.
        deployment_ids:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Deployment Ids
          description: Only include flow runs from these deployments in the work queue.
      type: object
      title: QueueFilter
      description: Filter criteria definition for a work queue.
    WorkQueueStatus:
      type: string
      enum:
        - READY
        - NOT_READY
        - PAUSED
      title: WorkQueueStatus
      description: Enumeration of work queue statuses.
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
    WorkQueueFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of work queue ids to include
      additionalProperties: false
      type: object
      title: WorkQueueFilterId
      description: Filter by `WorkQueue.id`.
    WorkQueueFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work queue names to include
          examples:
            - - wq-1
              - wq-2
        startswith_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Startswith
          description: >-
            A list of case-insensitive starts-with matches. For example, 
            passing 'marvin' will match 'marvin', and 'Marvin-robot', but not
            'sad-marvin'.
          examples:
            - - marvin
              - Marvin-robot
      additionalProperties: false
      type: object
      title: WorkQueueFilterName
      description: Filter by `WorkQueue.name`.

````

Built with [Mintlify](https://mintlify.com).