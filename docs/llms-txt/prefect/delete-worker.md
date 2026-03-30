# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/delete-worker.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Worker

> Delete a work pool's worker



## OpenAPI

````yaml delete /work_pools/{work_pool_name}/workers/{name}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/{work_pool_name}/workers/{name}:
    delete:
      tags:
        - Work Pools
      summary: Delete Worker
      description: Delete a work pool's worker
      operationId: delete_worker_work_pools__work_pool_name__workers__name__delete
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
            description: The work pool's worker name
            title: Name
          description: The work pool's worker name
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
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