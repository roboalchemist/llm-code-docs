# Source: https://docs.wandb.ai/weave/reference/service-api/datasets/dataset-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dataset Create

> Create a dataset object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/datasets
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/datasets:
    post:
      tags:
        - Datasets
      summary: Dataset Create
      description: Create a dataset object.
      operationId: dataset_create_v2__entity___project__datasets_post
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
              $ref: '#/components/schemas/DatasetCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetCreateRes'
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
    DatasetCreateBody:
      properties:
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: >-
            The name of this dataset.  Datasets with the same name will be
            versioned together.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A description of this dataset
        rows:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Rows
          description: Dataset rows
      type: object
      required:
        - rows
      title: DatasetCreateBody
    DatasetCreateRes:
      properties:
        digest:
          type: string
          title: Digest
          description: The digest of the created dataset
        object_id:
          type: string
          title: Object Id
          description: The ID of the created dataset
        version_index:
          type: integer
          title: Version Index
          description: The version index of the created dataset
      type: object
      required:
        - digest
        - object_id
        - version_index
      title: DatasetCreateRes
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