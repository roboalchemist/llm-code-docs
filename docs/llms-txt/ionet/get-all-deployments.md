# Source: https://io.net/docs/reference/vmaas/get-all-deployments.md

# Source: https://io.net/docs/reference/caas/get-all-deployments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get All Deployments

> View a list of all your active and past deployments.



## OpenAPI

````yaml openapi/caas/get-all-deployments.json get /enterprise/v1/io-cloud/caas/deployments
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/deployments:
    get:
      tags:
        - enterprise-io-cloud-caas
      summary: Get All Deployments
      operationId: get_all_deployments_enterprise_v1_io_cloud_caas_deployments_get
      parameters:
        - name: status
          in: query
          required: false
          schema:
            allOf:
              - $ref: '#/components/schemas/CaaSResourceStatus'
            title: Status
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
            default: 10
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
                $ref: >-
                  #/components/schemas/io_cloud__schemas__response__enterprise__caas__GetDeploymentsData
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
    CaaSResourceStatus:
      type: string
      enum:
        - running
        - completed
        - failed
        - deployment requested
        - termination requested
        - destroyed
      title: CaaSResourceStatus
    io_cloud__schemas__response__enterprise__caas__GetDeploymentsData:
      properties:
        data: 2cfdd216-a43c-430e-8b9f-106c24fcff03
      type: object
      required:
        - data
      title: GetDeploymentsData
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