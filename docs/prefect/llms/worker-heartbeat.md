# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/worker-heartbeat.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Worker Heartbeat



## OpenAPI

````yaml post /work_pools/{work_pool_name}/workers/heartbeat
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/{work_pool_name}/workers/heartbeat:
    post:
      tags:
        - Work Pools
      summary: Worker Heartbeat
      operationId: worker_heartbeat_work_pools__work_pool_name__workers_heartbeat_post
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
        required: true
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_worker_heartbeat_work_pools__work_pool_name__workers_heartbeat_post
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
    Body_worker_heartbeat_work_pools__work_pool_name__workers_heartbeat_post:
      properties:
        name:
          type: string
          title: Name
          description: The worker process name
        heartbeat_interval_seconds:
          anyOf:
            - type: integer
            - type: 'null'
          title: Heartbeat Interval Seconds
          description: The worker's heartbeat interval in seconds
      type: object
      required:
        - name
      title: Body_worker_heartbeat_work_pools__work_pool_name__workers_heartbeat_post
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