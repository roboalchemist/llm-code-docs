# Source: https://docs.wandb.ai/weave/reference/service-api/scorers/scorer-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scorer Delete

> Delete a scorer object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json delete /v2/{entity}/{project}/scorers/{object_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/scorers/{object_id}:
    delete:
      tags:
        - Scorers
      summary: Scorer Delete
      description: Delete a scorer object.
      operationId: scorer_delete_v2__entity___project__scorers__object_id__delete
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
              scorer will be deleted.
            title: Digests
          description: >-
            List of digests to delete. If not provided, all digests for the
            scorer will be deleted.
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScorerDeleteRes'
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
    ScorerDeleteRes:
      properties:
        num_deleted:
          type: integer
          title: Num Deleted
          description: Number of scorer versions deleted
      type: object
      required:
        - num_deleted
      title: ScorerDeleteRes
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