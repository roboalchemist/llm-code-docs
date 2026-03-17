# Source: https://docs.wandb.ai/weave/reference/service-api/scorers/scorer-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scorer Create

> Create a scorer object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/scorers
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/scorers:
    post:
      tags:
        - Scorers
      summary: Scorer Create
      description: Create a scorer object.
      operationId: scorer_create_v2__entity___project__scorers_post
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
              $ref: '#/components/schemas/ScorerCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScorerCreateRes'
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
    ScorerCreateBody:
      properties:
        name:
          type: string
          title: Name
          description: >-
            The name of this scorer.  Scorers with the same name will be
            versioned together.
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A description of this scorer
        op_source_code:
          type: string
          title: Op Source Code
          description: Complete source code for the Scorer.score op including imports
      type: object
      required:
        - name
        - op_source_code
      title: ScorerCreateBody
    ScorerCreateRes:
      properties:
        digest:
          type: string
          title: Digest
          description: The digest of the created scorer
        object_id:
          type: string
          title: Object Id
          description: The ID of the created scorer
        version_index:
          type: integer
          title: Version Index
          description: The version index of the created scorer
        scorer:
          type: string
          title: Scorer
          description: Full reference to the created scorer
      type: object
      required:
        - digest
        - object_id
        - version_index
        - scorer
      title: ScorerCreateRes
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