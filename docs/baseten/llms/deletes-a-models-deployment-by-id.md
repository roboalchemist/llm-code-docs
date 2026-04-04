# Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-models-deployment-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete model deployments

> Deletes a model's deployment by ID and returns the tombstone of the deployment.



## OpenAPI

````yaml delete /v1/models/{model_id}/deployments/{deployment_id}
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
  /v1/models/{model_id}/deployments/{deployment_id}:
    parameters:
      - $ref: '#/components/parameters/model_id'
      - $ref: '#/components/parameters/deployment_id'
    delete:
      summary: Deletes a model's deployment by ID
      description: >-
        Deletes a model's deployment by ID and returns the tombstone of the
        deployment.
      responses:
        '200':
          description: A model deployment tombstone.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentTombstoneV1'
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
    DeploymentTombstoneV1:
      description: A model deployment tombstone.
      properties:
        id:
          description: Unique identifier of the deployment
          title: Id
          type: string
        deleted:
          description: Whether the deployment was deleted
          title: Deleted
          type: boolean
        model_id:
          description: Unique identifier of the model
          title: Model Id
          type: string
      required:
        - id
        - deleted
        - model_id
      title: DeploymentTombstoneV1
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