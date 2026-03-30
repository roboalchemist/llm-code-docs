# Source: https://io.net/docs/reference/caas/check-maximum-gpus-per-container.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check maximum GPUs per container

> Returns the maximum number of GPUs available per hardware type across all locations, helping to determine deployment limits by hardware.

By leveraging this endpoint, it's possible to discover the current supply on the platform that fits workload requirements and use this data during the deployment process.


## OpenAPI

````yaml openapi/caas/check-maximum-gpus-per-container.json get /enterprise/v1/io-cloud/caas/hardware/max-gpus-per-container
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/hardware/max-gpus-per-container:
    get:
      tags:
        - enterprise-io-cloud-caas
      summary: Get Max Gpu Count Per Container
      operationId: >-
        get_max_gpu_count_per_container_enterprise_v1_io_cloud_caas_hardware_max_gpus_per_container_get
      parameters:
        - name: node_pool_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
                format: uuid
              - type: 'null'
            title: Node Pool Id
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: io.net provided API Key
            title: X-Api-Key
          description: io.net provided API Key
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: 17e63be5-2451-456d-8855-337f9f15763f
        '404':
          description: Not found
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
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````