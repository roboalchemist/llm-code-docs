# Source: https://docs.wandb.ai/weave/reference/service-api/datasets/dataset-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dataset Delete

> Delete a dataset object. If digests are provided, only those versions are deleted. Otherwise, all versions are deleted.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json delete /v2/{entity}/{project}/datasets/{object_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/datasets/{object_id}:
    delete:
      tags:
        - Datasets
      summary: Dataset Delete
      description: >-
        Delete a dataset object. If digests are provided, only those versions
        are deleted. Otherwise, all versions are deleted.
      operationId: dataset_delete_v2__entity___project__datasets__object_id__delete
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
        - name: digests
          in: query
          required: false
          schema:
            anyOf:
              - items:
                  type: string
                type: array
              - type: 'null'
            description: >-
              List of digests to delete. If not provided, all digests for the
              dataset will be deleted.
            title: Digests
          description: >-
            List of digests to delete. If not provided, all digests for the
            dataset will be deleted.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetDeleteRes'
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
    DatasetDeleteRes:
      properties:
        num_deleted:
          type: integer
          title: Num Deleted
          description: Number of dataset versions deleted
      type: object
      required:
        - num_deleted
      title: DatasetDeleteRes
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