# Source: https://docs.wandb.ai/weave/reference/service-api/datasets/dataset-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dataset List

> List dataset objects.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/datasets
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/datasets:
    get:
      tags:
        - Datasets
      summary: Dataset List
      description: List dataset objects.
      operationId: dataset_list_v2__entity___project__datasets_get
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
        - name: limit
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Maximum number of datasets to return
            title: Limit
          description: Maximum number of datasets to return
        - name: offset
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Number of datasets to skip
            title: Offset
          description: Number of datasets to skip
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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