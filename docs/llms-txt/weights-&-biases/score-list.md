# Source: https://docs.wandb.ai/weave/reference/service-api/scores/score-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Score List

> List scores.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/scores
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/scores:
    get:
      tags:
        - Scores
      summary: Score List
      description: List scores.
      operationId: score_list_v2__entity___project__scores_get
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
        - name: evaluation_run_id
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: Filter by evaluation run ID
            title: Evaluation Run Id
          description: Filter by evaluation run ID
        - name: limit
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Maximum number of scores to return
            title: Limit
          description: Maximum number of scores to return
        - name: offset
          in: query
          required: false
          schema:
            anyOf:
              - type: integer
              - type: 'null'
            description: Number of scores to skip
            title: Offset
          description: Number of scores to skip
      responses:
        '200':
          description: Stream of data in JSONL format
          content:
            application/jsonl:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ScoreReadRes'
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
    ScoreReadRes:
      properties:
        score_id:
          type: string
          title: Score Id
          description: The score ID
        scorer:
          type: string
          title: Scorer
          description: The scorer reference (weave:// URI)
        value:
          type: number
          title: Value
          description: The value of the score
        evaluation_run_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Evaluation Run Id
          description: Evaluation run ID if this score is linked to one
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
      type: object
      required:
        - score_id
        - scorer
        - value
      title: ScoreReadRes
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