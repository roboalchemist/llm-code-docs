# Source: https://docs.baseten.co/reference/management-api/deployments/activate/activates-a-deployment-associated-with-an-environment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Activate environment deployment

> Activates an inactive deployment associated with an environment and returns the activation status.



## OpenAPI

````yaml post /v1/models/{model_id}/environments/{env_name}/activate
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
  /v1/models/{model_id}/environments/{env_name}/activate:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/env_name'
    post:
      summary: Activates a deployment associated with an environment
      description: >-
        Activates an inactive deployment associated with an environment and
        returns the activation status.
      responses:
        '200':
          description: The response to a request to activate a deployment.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActivateResponseV1'
components:
  parameters:
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
    env_name:
      schema:
        type: string
      name: env_name
      in: path
      required: true
  schemas:
    ActivateResponseV1:
      description: The response to a request to activate a deployment.
      properties:
        success:
          default: true
          description: Whether the deployment was successfully activated
          title: Success
          type: boolean
      title: ActivateResponseV1
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