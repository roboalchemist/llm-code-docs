# Source: https://docs.baseten.co/reference/management-api/api-keys/delete-an-api-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an API key

> Deletes an API key by prefix and returns info about the API key.



## OpenAPI

````yaml delete /v1/api_keys/{api_key_prefix}
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
  /v1/api_keys/{api_key_prefix}:
    parameters:
      - $ref: '#/components/parameters/api_key_prefix'
    delete:
      summary: Deletes an API key by prefix
      description: Deletes an API key by prefix and returns info about the API key.
      responses:
        '200':
          description: An API key tombstone.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/APIKeyTombstoneV1'
components:
  parameters:
    api_key_prefix:
      schema:
        type: string
      name: api_key_prefix
      in: path
      required: true
  schemas:
    APIKeyTombstoneV1:
      description: An API key tombstone.
      properties:
        prefix:
          description: Unique prefix of the API key
          title: Prefix
          type: string
      required:
        - prefix
      title: APIKeyTombstoneV1
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