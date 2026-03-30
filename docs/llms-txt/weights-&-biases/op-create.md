# Source: https://docs.wandb.ai/weave/reference/service-api/ops/op-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Op Create

> Create an op object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /v2/{entity}/{project}/ops
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/ops:
    post:
      tags:
        - Ops
      summary: Op Create
      description: Create an op object.
      operationId: op_create_v2__entity___project__ops_post
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
              $ref: '#/components/schemas/OpCreateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OpCreateRes'
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
    OpCreateBody:
      properties:
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: >-
            The name of this op. Ops with the same name will be versioned
            together.
        source_code:
          anyOf:
            - type: string
            - type: 'null'
          title: Source Code
          description: Complete source code for this op, including imports
      type: object
      title: OpCreateBody
      description: >-
        Request body for creating an Op object via REST API.


        This model excludes project_id since it comes from the URL path in
        RESTful endpoints.
    OpCreateRes:
      properties:
        digest:
          type: string
          title: Digest
          description: The digest of the created op
        object_id:
          type: string
          title: Object Id
          description: The ID of the created op
        version_index:
          type: integer
          title: Version Index
          description: The version index of the created op
      type: object
      required:
        - digest
        - object_id
        - version_index
      title: OpCreateRes
      description: Response model for creating an Op object.
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