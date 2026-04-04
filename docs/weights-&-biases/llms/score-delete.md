# Source: https://docs.wandb.ai/weave/reference/service-api/scores/score-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Score Delete

> Delete scores.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json delete /v2/{entity}/{project}/scores
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/scores:
    delete:
      tags:
        - Scores
      summary: Score Delete
      description: Delete scores.
      operationId: score_delete_v2__entity___project__scores_delete
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
        - name: score_ids
          in: query
          required: true
          schema:
            type: array
            items:
              type: string
            description: List of score IDs to delete
            title: Score Ids
          description: List of score IDs to delete
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScoreDeleteRes'
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
    ScoreDeleteRes:
      properties:
        num_deleted:
          type: integer
          title: Num Deleted
          description: Number of scores deleted
      type: object
      required:
        - num_deleted
      title: ScoreDeleteRes
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