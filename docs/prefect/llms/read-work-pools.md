# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/read-work-pools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Work Pools

> Read multiple work pools



## OpenAPI

````yaml post /work_pools/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/filter:
    post:
      tags:
        - Work Pools
      summary: Read Work Pools
      description: Read multiple work pools
      operationId: read_work_pools_work_pools_filter_post
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
              $ref: '#/components/schemas/Body_read_work_pools_work_pools_filter_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/WorkPool'
                title: Response Read Work Pools Work Pools Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_work_pools_work_pools_filter_post:
      properties:
        work_pools:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilter'
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
      title: Body_read_work_pools_work_pools_filter_post
    WorkPool:
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
          description: The name of the work pool.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A description of the work pool.
        type:
          type: string
          title: Type
          description: The work pool type.
        base_job_template:
          additionalProperties: true
          type: object
          title: Base Job Template
          description: The work pool's base job template.
        is_paused:
          type: boolean
          title: Is Paused
          description: Pausing the work pool stops the delivery of all work.
          default: false
        concurrency_limit:
          anyOf:
            - type: integer
              minimum: 0
            - type: 'null'
          title: Concurrency Limit
          description: A concurrency limit for the work pool.
        status:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolStatus'
            - type: 'null'
          description: The current status of the work pool.
        default_queue_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Default Queue Id
          description: The id of the pool's default queue.
        storage_configuration:
          $ref: '#/components/schemas/WorkPoolStorageConfiguration'
          description: The storage configuration for the work pool.
      type: object
      required:
        - name
        - type
        - id
        - created
        - updated
      title: WorkPool
      description: An ORM representation of a work pool
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    WorkPoolFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterId'
            - type: 'null'
          description: Filter criteria for `WorkPool.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterName'
            - type: 'null'
          description: Filter criteria for `WorkPool.name`
        type:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterType'
            - type: 'null'
          description: Filter criteria for `WorkPool.type`
      additionalProperties: false
      type: object
      title: WorkPoolFilter
      description: >-
        Filter work pools. Only work pools matching all criteria will be
        returned
    WorkPoolStatus:
      type: string
      enum:
        - READY
        - NOT_READY
        - PAUSED
      title: WorkPoolStatus
      description: Enumeration of work pool statuses.
    WorkPoolStorageConfiguration:
      properties:
        bundle_upload_step:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Bundle Upload Step
          description: The step to use for uploading bundles to storage.
        bundle_execution_step:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Bundle Execution Step
          description: The step to use for executing bundles.
        default_result_storage_block_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Default Result Storage Block Id
          description: The block document ID of the default result storage block.
      additionalProperties: false
      type: object
      title: WorkPoolStorageConfiguration
      description: A representation of a work pool's storage configuration
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
    WorkPoolFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool ids to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterId
      description: Filter by `WorkPool.id`.
    WorkPoolFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool names to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterName
      description: Filter by `WorkPool.name`.
    WorkPoolFilterType:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool types to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterType
      description: Filter by `WorkPool.type`.

````

Built with [Mintlify](https://mintlify.com).