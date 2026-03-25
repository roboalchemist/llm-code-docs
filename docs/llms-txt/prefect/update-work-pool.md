# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/update-work-pool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Work Pool

> Update a work pool



## OpenAPI

````yaml patch /work_pools/{name}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/{name}:
    patch:
      tags:
        - Work Pools
      summary: Update Work Pool
      description: Update a work pool
      operationId: update_work_pool_work_pools__name__patch
      parameters:
        - name: name
          in: path
          required: true
          schema:
            type: string
            description: The work pool name
            title: Name
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
              $ref: '#/components/schemas/WorkPoolUpdate'
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
    WorkPoolUpdate:
      properties:
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Paused
        base_job_template:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Base Job Template
        concurrency_limit:
          anyOf:
            - type: integer
              minimum: 0
            - type: 'null'
          title: Concurrency Limit
        storage_configuration:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolStorageConfiguration'
            - type: 'null'
          description: The storage configuration for the work pool.
      additionalProperties: false
      type: object
      title: WorkPoolUpdate
      description: Data used by the Prefect REST API to update a work pool.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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

````

Built with [Mintlify](https://mintlify.com).