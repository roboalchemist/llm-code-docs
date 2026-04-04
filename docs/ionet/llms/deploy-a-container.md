# Source: https://io.net/docs/reference/caas/deploy-a-container.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

> This endpoint is used to deploy a CaaS cluster on IO.NET infrastructure. The container must expose an HTTP server on a single port, and it must run within a single node.

# Deploy a Container

## **Important Constraints:**

* **Only HTTP server containers are supported.**
* **Only a single traffic port is allowed.**
* **Each container must use a minimum of 1 GPU, with no maximum GPU limit.**
  * Multi-node GPU configurations are not supported at this time.


## OpenAPI

````yaml openapi/caas/deploy-a-container.json post /enterprise/v1/io-cloud/caas/deploy
openapi: 3.1.0
info:
  title: IO API
  version: '1.0'
servers:
  - url: https://api.io.solutions/
security:
  - sec0: []
paths:
  /enterprise/v1/io-cloud/caas/deploy:
    post:
      tags:
        - enterprise-io-cloud-caas
      summary: Deploy Containers
      operationId: deploy_containers_enterprise_v1_io_cloud_caas_deploy_post
      parameters:
        - name: x-api-key
          in: header
          required: true
          schema:
            type: string
            description: io.net provided API Key
            title: X-Api-Key
          description: io.net provided API Key
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: e2fcad3b-90c3-44b7-98e6-5a429085d3ea
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