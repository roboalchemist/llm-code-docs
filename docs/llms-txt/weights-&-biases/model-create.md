# Source: https://docs.wandb.ai/weave/reference/service-api/models/model-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Model Create

> Create a model object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/models
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/models:
    post:
      tags:
        - Models
      summary: Model Create
      description: Create a model object.
      operationId: model_create_v2__entity___project__models_post
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
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ModelCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelCreateRes'
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
    ModelCreateBody:
      properties:
        name:
          type: string
          title: Name
          description: >-
            The name of this model. Models with the same name will be versioned
            together.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A description of this model
        source_code:
          type: string
          title: Source Code
          description: Complete source code for the Model class including imports
        attributes:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Attributes
          description: Additional attributes to be stored with the model
      type: object
      required:
        - name
        - source_code
      title: ModelCreateBody
    ModelCreateRes:
      properties:
        digest:
          type: string
          title: Digest
          description: The digest of the created model
        object_id:
          type: string
          title: Object Id
          description: The ID of the created model
        version_index:
          type: integer
          title: Version Index
          description: The version index of the created model
        model_ref:
          type: string
          title: Model Ref
          description: Full reference to the created model
      type: object
      required:
        - digest
        - object_id
        - version_index
        - model_ref
      title: ModelCreateRes
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