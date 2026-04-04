# Source: https://io.net/docs/reference/vmaas/get-deployment-details.md

# Source: https://io.net/docs/reference/caas/get-deployment-details.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Deployment Details

> Retrieve detailed information about a specific deployment.



## OpenAPI

````yaml openapi/caas/get-deployment-details.json get /enterprise/v1/io-cloud/caas/deployment/{deployment_id}
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/deployment/{deployment_id}:
    get:
      tags:
        - enterprise-io-cloud-caas
      summary: Get Deployment Details
      operationId: >-
        get_deployment_details_enterprise_v1_io_cloud_caas_deployment__deployment_id__get
      parameters:
        - name: deployment_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Deployment Id
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
                  #/components/schemas/io_cloud__schemas__response__enterprise__caas__GetDeploymentDetails
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
    io_cloud__schemas__response__enterprise__caas__GetDeploymentDetails:
      properties:
        data:
          $ref: >-
            #/components/schemas/io_cloud__schemas__response__enterprise__caas__DeploymentDetails
      type: object
      required:
        - data
      title: GetDeploymentDetails
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    io_cloud__schemas__response__enterprise__caas__DeploymentDetails:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        status:
          type: string
          title: Status
        created_at:
          type: string
          format: date-time
          title: Created At
        started_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Started At
        finished_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Finished At
        amount_paid:
          type: number
          title: Amount Paid
        completed_percent:
          type: number
          title: Completed Percent
        total_gpus:
          type: integer
          title: Total Gpus
        gpus_per_container:
          type: integer
          title: Gpus Per Container
        total_containers:
          type: integer
          title: Total Containers
        hardware_name:
          type: string
          title: Hardware Name
        hardware_id:
          type: integer
          title: Hardware Id
        locations:
          items:
            $ref: '#/components/schemas/LocationData'
          type: array
          title: Locations
        brand_name:
          type: string
          title: Brand Name
        compute_minutes_served:
          type: integer
          title: Compute Minutes Served
        compute_minutes_remaining:
          type: integer
          title: Compute Minutes Remaining
        container_config:
          $ref: '#/components/schemas/ContainerConfig-Output'
      type: object
      required:
        - id
        - status
        - created_at
        - started_at
        - finished_at
        - amount_paid
        - completed_percent
        - total_gpus
        - gpus_per_container
        - total_containers
        - hardware_name
        - hardware_id
        - locations
        - brand_name
        - compute_minutes_served
        - compute_minutes_remaining
        - container_config
      title: DeploymentDetails
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
    LocationData:
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
      type: object
      required:
        - id
        - iso2
        - name
      title: LocationData
    ContainerConfig-Output:
      properties:
        entrypoint:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Entrypoint
        env_variables:
          anyOf:
            - type: object
            - type: 'null'
          title: Env Variables
        traffic_port:
          type: integer
          title: Traffic Port
        image_url:
          type: string
          title: Image Url
        secret_env_keys:
          items:
            type: string
          type: array
          uniqueItems: true
          title: Secret Env Keys
      type: object
      required:
        - entrypoint
        - env_variables
        - traffic_port
        - image_url
        - secret_env_keys
      title: ContainerConfig
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````