# Source: https://docs.wandb.ai/weave/reference/service-api/ops/op-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Op Read

> Get an op object.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /v2/{entity}/{project}/ops/{object_id}/versions/{digest}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /v2/{entity}/{project}/ops/{object_id}/versions/{digest}:
    get:
      tags:
        - Ops
      summary: Op Read
      description: Get an op object.
      operationId: op_read_v2__entity___project__ops__object_id__versions__digest__get
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
        - name: eager
          in: query
          required: false
          schema:
            type: boolean
            description: Whether to eagerly load the op code
            default: false
            title: Eager
          description: Whether to eagerly load the op code
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OpReadRes'
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
    OpReadRes:
      properties:
        object_id:
          type: string
          title: Object Id
          description: The op ID
        digest:
          type: string
          title: Digest
          description: The digest of the op
        version_index:
          type: integer
          title: Version Index
          description: The version index of this op
        created_at:
          type: string
          format: date-time
          title: Created At
          description: When this op was created
        code:
          type: string
          title: Code
          description: The actual op source code
      type: object
      required:
        - object_id
        - digest
        - version_index
        - created_at
        - code
      title: OpReadRes
      description: |-
        Response model for reading an Op object.

        The code field contains the actual source code of the op.
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