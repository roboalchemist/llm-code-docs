# Source: https://docs.baseten.co/reference/management-api/models/deletes-a-model-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete models



## OpenAPI

````yaml delete /v1/models/{model_id}
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
  /v1/models/{model_id}:
    parameters:
      - $ref: '#/components/parameters/model_id'
    delete:
      summary: Deletes a model by ID
      responses:
        '200':
          description: A model tombstone.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelTombstoneV1'
components:
  parameters:
    model_id:
      schema:
        type: string
      name: model_id
      in: path
      required: true
  schemas:
    ModelTombstoneV1:
      description: A model tombstone.
      properties:
        id:
          description: Unique identifier of the model
          title: Id
          type: string
        deleted:
          description: Whether the model was deleted
          title: Deleted
          type: boolean
      required:
        - id
        - deleted
      title: ModelTombstoneV1
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