# Source: https://docs.baseten.co/reference/management-api/deployments/deactivate/deactivates-a-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Any deployment by ID

> Deactivates a deployment and returns the deactivation status.



## OpenAPI

````yaml post /v1/models/{model_id}/deployments/{deployment_id}/deactivate
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/models/{model_id}/deployments/{deployment_id}/deactivate:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    post:
      summary: Deactivates a deployment
      description: Deactivates a deployment and returns the deactivation status.
      responses:
        '200':
          description: The response to a request to deactivate a deployment.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeactivateResponseV1'
components:
  parameters:
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
    deployment_id:
      schema:
        type: string
      name: deployment_id
      in: path
      required: true
  schemas:
    DeactivateResponseV1:
      description: The response to a request to deactivate a deployment.
      properties:
        success:
          default: true
          description: Whether the deployment was successfully deactivated
          title: Success
          type: boolean
      title: DeactivateResponseV1
      type: object
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````