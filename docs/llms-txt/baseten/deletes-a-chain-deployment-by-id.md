# Source: https://docs.baseten.co/reference/management-api/deployments/deletes-a-chain-deployment-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete chain deployment



## OpenAPI

````yaml delete /v1/chains/{chain_id}/deployments/{chain_deployment_id}
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
  /v1/chains/{chain_id}/deployments/{chain_deployment_id}:
    parameters:
      - $ref: '#/components/parameters/chain_id'
      - $ref: '#/components/parameters/chain_deployment_id'
    delete:
      summary: Deletes a chain deployment by ID
      responses:
        '200':
          description: A chain deployment tombstone.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChainDeploymentTombstoneV1'
components:
  parameters:
    chain_id:
      schema:
        type: string
      name: chain_id
      in: path
      required: true
    chain_deployment_id:
      schema:
        type: string
      name: chain_deployment_id
      in: path
      required: true
  schemas:
    ChainDeploymentTombstoneV1:
      description: A chain deployment tombstone.
      properties:
        id:
          description: Unique identifier of the chain deployment
          title: Id
          type: string
        deleted:
          description: Whether the chain deployment was deleted
          title: Deleted
          type: boolean
        chain_id:
          description: Unique identifier of the chain
          title: Chain Id
          type: string
      required:
        - id
        - deleted
        - chain_id
      title: ChainDeploymentTombstoneV1
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