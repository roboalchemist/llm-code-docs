# Source: https://io.net/docs/reference/caas/price-estimation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Price Check

> Calculates the estimated deployment cost based on selected location, hardware, GPU count, duration, and number of replicas. Returns a detailed price breakdown.

**Once** `location_id` **and** `hardware_id`**are known, you can estimate the deployment cost based on the desired configuration.**

As a result, a detailed price breakdown will be returned.\
**This step is optional.**


## OpenAPI

````yaml openapi/caas/price-estimation.json get /enterprise/v1/io-cloud/caas/price
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/price:
    get:
      tags:
        - enterprise-io-cloud-caas
      summary: Get Deployment Price
      operationId: get_deployment_price_enterprise_v1_io_cloud_caas_price_get
      parameters:
        - name: location_ids
          in: query
          required: true
          schema:
            type: string
            description: list of ids in a form of json array
            title: Location Ids
          description: list of ids in a form of json array
        - name: hardware_id
          in: query
          required: true
          schema:
            type: integer
            title: Hardware Id
        - name: duration_hours
          in: query
          required: true
          schema:
            type: integer
            minimum: 1
            title: Duration Hours
        - name: gpus_per_container
          in: query
          required: true
          schema:
            type: integer
            minimum: 1
            title: Gpus Per Container
        - name: replica_count
          in: query
          required: true
          schema:
            type: integer
            minimum: 1
            title: Replica Count
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
                $ref: 5c3a72a2-7431-41aa-968a-79ecb504d9da
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