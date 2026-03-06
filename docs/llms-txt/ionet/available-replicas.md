# Source: https://io.net/docs/reference/caas/available-replicas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Check available replicas per location

> Returns the number of deployable replicas in each location based on selected hardware type and GPU count per container, useful for matching supply to workload needs.

By leveraging this endpoint, it's possible to discover the current supply on the platform that fits workload requirements and use this data during the deployment process.


## OpenAPI

````yaml openapi/caas/available-replicas.json get /enterprise/v1/io-cloud/caas/available-replicas
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/available-replicas:
    get:
      tags:
        - enterprise-io-cloud-caas
      summary: Get Available Replicas
      operationId: >-
        get_available_replicas_enterprise_v1_io_cloud_caas_available_replicas_get
      parameters:
        - name: hardware_id
          in: query
          required: true
          schema:
            type: integer
            title: Hardware Id
        - name: hardware_qty
          in: query
          required: true
          schema:
            type: integer
            minimum: 1
            title: Hardware Qty
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
                $ref: >-
                  #/components/schemas/io_cloud__schemas__response__enterprise__caas__GetAvailableReplicasPerLocationResponse
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
    io_cloud__schemas__response__enterprise__caas__GetAvailableReplicasPerLocationResponse:
      properties:
        data:
          items:
            $ref: >-
              #/components/schemas/io_cloud__schemas__response__enterprise__caas__ReplicasPerLocation
          type: array
          title: Data
      type: object
      required:
        - data
      title: GetAvailableReplicasPerLocationResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    io_cloud__schemas__response__enterprise__caas__ReplicasPerLocation:
      properties:
        id:
          type: integer
          title: Id
        iso2:
          type: string
          title: Iso2
        name:
          type: string
          title: Name
        available_replicas:
          type: integer
          title: Available Replicas
      type: object
      required:
        - id
        - iso2
        - name
        - available_replicas
      title: ReplicasPerLocation
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