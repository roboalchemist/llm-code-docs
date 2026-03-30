# Source: https://docs.wandb.ai/weave/reference/service-api/datasets/dataset-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dataset Read

> Get a dataset object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/datasets/{object_id}/versions/{digest}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/datasets/{object_id}/versions/{digest}:
    get:
      tags:
        - Datasets
      summary: Dataset Read
      description: Get a dataset object.
      operationId: >-
        dataset_read_v2__entity___project__datasets__object_id__versions__digest__get
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
                $ref: '#/components/schemas/DatasetReadRes'
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
    DatasetReadRes:
      properties:
        object_id:
          type: string
          title: Object Id
          description: The dataset ID
        digest:
          type: string
          title: Digest
          description: The digest of the dataset object
        version_index:
          type: integer
          title: Version Index
          description: The version index of the object
        created_at:
          type: string
          format: date-time
          title: Created At
          description: When the object was created
        name:
          type: string
          title: Name
          description: The name of the dataset
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: Description of the dataset
        rows:
          type: string
          title: Rows
          description: Reference to the dataset rows data
      type: object
      required:
        - object_id
        - digest
        - version_index
        - created_at
        - name
        - rows
      title: DatasetReadRes
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