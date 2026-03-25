# Source: https://docs.wandb.ai/weave/reference/service-api/models/model-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Read

> Get a model object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/models/{object_id}/versions/{digest}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/models/{object_id}/versions/{digest}:
    get:
      tags:
        - Models
      summary: Model Read
      description: Get a model object.
      operationId: >-
        model_read_v2__entity___project__models__object_id__versions__digest__get
      parameters:
        - name: entity
          in: path
          required: true
          schema:
            type: string
            title: Entity
        - name: project
          in: path
          required: true
          schema:
            type: string
            title: Project
        - name: object_id
          in: path
          required: true
          schema:
            type: string
            title: Object Id
        - name: digest
          in: path
          required: true
          schema:
            type: string
            title: Digest
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelReadRes'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBasic: []
components:
  schemas:
    ModelReadRes:
      properties:
        object_id:
          type: string
          title: Object Id
          description: The model ID
        digest:
          type: string
          title: Digest
          description: The digest of the model
        version_index:
          type: integer
          title: Version Index
          description: The version index of the object
        created_at:
          type: string
          format: date-time
          title: Created At
          description: When the model was created
        name:
          type: string
          title: Name
          description: The name of the model
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: Description of the model
        source_code:
          type: string
          title: Source Code
          description: The source code of the model
        attributes:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Attributes
          description: Additional attributes stored with the model
      type: object
      required:
        - object_id
        - digest
        - version_index
        - created_at
        - name
        - source_code
      title: ModelReadRes
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
    HTTPBasic:
      type: http
      scheme: basic

````