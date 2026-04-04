# Source: https://docs.wandb.ai/weave/reference/service-api/tables/table-create-from-digests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Create From Digests



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /table/create_from_digests
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /table/create_from_digests:
    post:
      tags:
        - Tables
      summary: Table Create From Digests
      operationId: table_create_from_digests_table_create_from_digests_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TableCreateFromDigestsReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableCreateFromDigestsRes'
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
    TableCreateFromDigestsReq:
      properties:
        project_id:
          type: string
          title: Project Id
        row_digests:
          items:
            type: string
          type: array
          title: Row Digests
      additionalProperties: false
      type: object
      required:
        - project_id
        - row_digests
      title: TableCreateFromDigestsReq
    TableCreateFromDigestsRes:
      properties:
        digest:
          type: string
          title: Digest
      type: object
      required:
        - digest
      title: TableCreateFromDigestsRes
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