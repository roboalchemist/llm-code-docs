# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-queues/update-work-queue.md

# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/update-work-queue.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Work Queue

> Update a work pool queue



## OpenAPI

````yaml patch /work_pools/{work_pool_name}/queues/{name}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/{work_pool_name}/queues/{name}:
    patch:
      tags:
        - Work Pools
      summary: Update Work Queue
      description: Update a work pool queue
      operationId: update_work_queue_work_pools__work_pool_name__queues__name__patch
      parameters:
        - name: work_pool_name
          in: path
          required: true
          schema:
            type: string
            description: The work pool name
            title: Work Pool Name
          description: The work pool name
        - name: name
          in: path
          required: true
          schema:
            type: string
            description: The work pool queue name
            title: Name
          description: The work pool queue name
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
              $ref: '#/components/schemas/WorkQueueUpdate'
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
    WorkQueueUpdate:
      properties:
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
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
        priority:
          anyOf:
            - type: integer
              exclusiveMinimum: 0
            - type: 'null'
          title: Priority
        last_polled:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Last Polled
        filter:
          anyOf:
            - $ref: '#/components/schemas/QueueFilter'
            - type: 'null'
          description: 'DEPRECATED: Filter criteria for the work queue.'
          deprecated: true
      additionalProperties: false
      type: object
      title: WorkQueueUpdate
      description: Data used by the Prefect REST API to update a work queue.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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