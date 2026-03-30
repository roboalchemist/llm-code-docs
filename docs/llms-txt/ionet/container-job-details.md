# Source: https://io.net/docs/reference/caas/container-job-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Inspect job-level details of a specific container within a deployment.

# Container Job Details



## OpenAPI

````yaml openapi/caas/container-job-details.json get /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/containers-jobs/{container_id}
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/deployment/{deployment_id}/containers-jobs/{container_id}:
    get:
      tags:
        - enterprise-io-cloud-caas
      summary: Get Containers Jobs History
      operationId: >-
        get_containers_jobs_history_enterprise_v1_io_cloud_caas_deployment__deployment_id__containers_jobs__container_id__get
      parameters:
        - name: deployment_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment Id
        - name: container_id
          in: path
          required: true
          schema:
            type: string
            title: Container Id
        - name: page
          in: query
          required: false
          schema:
            type: integer
            default: 0
            title: Page
        - name: page_size
          in: query
          required: false
          schema:
            type: integer
            maximum: 100
            min: 1
            default: 20
            title: Page Size
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
                $ref: '#/components/schemas/GetContainersJobData'
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      deprecated: false
components:
  schemas:
    GetContainersJobData:
      properties:
        data:
          $ref: '#/components/schemas/ContainersJobsData'
      type: object
      required:
        - data
      title: GetContainersJobData
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ContainersJobsData:
      properties:
        total:
          type: integer
          title: Total
        workers:
          items:
            $ref: >-
              #/components/schemas/io_cloud__schemas__response__enterprise__caas__WorkerData
          type: array
          title: Workers
      type: object
      required:
        - total
        - workers
      title: ContainersJobsData
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
    io_cloud__schemas__response__enterprise__caas__WorkerData:
      properties:
        device_id:
          type: string
          format: uuid
          title: Device Id
        container_id:
          type: string
          title: Container Id
        hardware:
          type: string
          title: Hardware
        brand_name:
          type: string
          title: Brand Name
        created_at:
          type: string
          format: date-time
          title: Created At
        uptime_percent:
          type: number
          title: Uptime Percent
        gpus_per_container:
          type: integer
          title: Gpus Per Container
        status:
          type: string
          title: Status
        container_events:
          anyOf:
            - items:
                $ref: '#/components/schemas/ContainerEvent'
              type: array
            - type: 'null'
          title: Container Events
        public_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Public Url
      type: object
      required:
        - device_id
        - container_id
        - hardware
        - brand_name
        - created_at
        - uptime_percent
        - gpus_per_container
        - status
        - container_events
        - public_url
      title: WorkerData
    ContainerEvent:
      properties:
        time:
          type: string
          format: date-time
          title: Time
        message:
          type: string
          title: Message
      type: object
      required:
        - time
        - message
      title: ContainerEvent
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````