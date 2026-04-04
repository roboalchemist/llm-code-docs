# Source: https://docs.baseten.co/reference/management-api/chains/gets-a-chain-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# By ID



## OpenAPI

````yaml get /v1/chains/{chain_id}
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
  /v1/chains/{chain_id}:
    parameters:
      - $ref: '#/components/parameters/chain_id'
    get:
      summary: Gets a chain by ID
      responses:
        '200':
          description: A chain.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChainV1'
components:
  parameters:
    chain_id:
      schema:
        type: string
      name: chain_id
      in: path
      required: true
  schemas:
    ChainV1:
      description: A chain.
      properties:
        id:
          description: Unique identifier of the chain
          title: Id
          type: string
        created_at:
          description: Time the chain was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the chain
          title: Name
          type: string
        deployments_count:
          description: Number of deployments of the chain
          title: Deployments Count
          type: integer
        team_name:
          description: Name of the team associated with the chain
          title: Team Name
          type: string
      required:
        - id
        - created_at
        - name
        - deployments_count
        - team_name
      title: ChainV1
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