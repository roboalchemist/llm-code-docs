# Source: https://docs.wandb.ai/weave/reference/service-api/scores/score-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Score Create

> Create a score.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/scores
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/scores:
    post:
      tags:
        - Scores
      summary: Score Create
      description: Create a score.
      operationId: score_create_v2__entity___project__scores_post
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
              $ref: '#/components/schemas/ScoreCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScoreCreateRes'
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
    ScoreCreateBody:
      properties:
        prediction_id:
          type: string
          title: Prediction Id
          description: The prediction ID
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
          description: Optional evaluation run ID to link this score as a child call
      type: object
      required:
        - prediction_id
        - scorer
        - value
      title: ScoreCreateBody
      description: >-
        Request body for creating a Score via REST API.


        This model excludes project_id since it comes from the URL path in
        RESTful endpoints.
    ScoreCreateRes:
      properties:
        score_id:
          type: string
          title: Score Id
          description: The score ID
      type: object
      required:
        - score_id
      title: ScoreCreateRes
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