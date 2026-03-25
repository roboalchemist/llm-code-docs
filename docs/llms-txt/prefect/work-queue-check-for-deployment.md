# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/deployments/work-queue-check-for-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Work Queue Check For Deployment

> Get list of work-queues that are able to pick up the specified deployment.

This endpoint is intended to be used by the UI to provide users warnings
about deployments that are unable to be executed because there are no work
queues that will pick up their runs, based on existing filter criteria. It
may be deprecated in the future because there is not a strict relationship
between work queues and deployments.



## OpenAPI

````yaml get /deployments/{id}/work_queue_check
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /deployments/{id}/work_queue_check:
    get:
      tags:
        - Deployments
      summary: Work Queue Check For Deployment
      description: >-
        Get list of work-queues that are able to pick up the specified
        deployment.


        This endpoint is intended to be used by the UI to provide users warnings

        about deployments that are unable to be executed because there are no
        work

        queues that will pick up their runs, based on existing filter criteria.
        It

        may be deprecated in the future because there is not a strict
        relationship

        between work queues and deployments.
      operationId: work_queue_check_for_deployment_deployments__id__work_queue_check_get
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The deployment id
            title: Id
          description: The deployment id
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
                type: array
                items:
                  $ref: '#/components/schemas/WorkQueue'
                title: >-
                  Response Work Queue Check For Deployment Deployments  Id  Work
                  Queue Check Get
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      deprecated: true
components:
  schemas:
    WorkQueue:
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
      type: object
      required:
        - name
        - id
        - created
        - updated
      title: WorkQueue
      description: An ORM representation of a work queue
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