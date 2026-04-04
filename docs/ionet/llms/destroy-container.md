# Source: https://io.net/docs/reference/caas/destroy-container.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> Shut down a deployment and release associated resources.

# Destroy Container



## OpenAPI

````yaml openapi/caas/destroy-container.json delete /enterprise/v1/io-cloud/caas/deployment/{deployment_id}
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
    delete:
      tags:
        - enterprise-io-cloud-caas
      summary: Destroy Container
      operationId: >-
        destroy_container_enterprise_v1_io_cloud_caas_deployment__deployment_id__delete
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
                $ref: '#/components/schemas/SuccessResponse'
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
    SuccessResponse:
      properties:
        status:
          type: string
          title: Status
        deployment_id:
          type: string
          format: uuid
          title: Deployment Id
      type: object
      required:
        - status
        - deployment_id
      title: SuccessResponse
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