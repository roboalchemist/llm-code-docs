# Source: https://docs.baseten.co/reference/management-api/chains/deletes-a-chain-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete chains



## OpenAPI

````yaml delete /v1/chains/{chain_id}
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
    delete:
      summary: Deletes a chain by ID
      responses:
        '200':
          description: A chain tombstone.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChainTombstoneV1'
components:
  parameters:
    chain_id:
      schema:
        type: string
      name: chain_id
      in: path
      required: true
  schemas:
    ChainTombstoneV1:
      description: A chain tombstone.
      properties:
        id:
          description: Unique identifier of the chain
          title: Id
          type: string
        deleted:
          description: Whether the chain was deleted
          title: Deleted
          type: boolean
      required:
        - id
        - deleted
      title: ChainTombstoneV1
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