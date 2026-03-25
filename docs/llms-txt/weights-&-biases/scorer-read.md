# Source: https://docs.wandb.ai/weave/reference/service-api/scorers/scorer-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scorer Read

> Get a scorer object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/scorers/{object_id}/versions/{digest}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/scorers/{object_id}/versions/{digest}:
    get:
      tags:
        - Scorers
      summary: Scorer Read
      description: Get a scorer object.
      operationId: >-
        scorer_read_v2__entity___project__scorers__object_id__versions__digest__get
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
                $ref: '#/components/schemas/ScorerReadRes'
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
    ScorerReadRes:
      properties:
        object_id:
          type: string
          title: Object Id
          description: The scorer ID
        digest:
          type: string
          title: Digest
          description: The digest of the scorer
        version_index:
          type: integer
          title: Version Index
          description: The version index of the object
        created_at:
          type: string
          format: date-time
          title: Created At
          description: When the scorer was created
        name:
          type: string
          title: Name
          description: The name of the scorer
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: Description of the scorer
        score_op:
          type: string
          title: Score Op
          description: The Scorer.score op reference
      type: object
      required:
        - object_id
        - digest
        - version_index
        - created_at
        - name
        - score_op
      title: ScorerReadRes
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