# Source: https://docs.wandb.ai/weave/reference/service-api/tables/table-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Create



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /table/create
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /table/create:
    post:
      tags:
        - Tables
      summary: Table Create
      operationId: table_create_table_create_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TableCreateReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableCreateRes'
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
    TableCreateReq:
      properties:
        table:
          $ref: '#/components/schemas/TableSchemaForInsert'
      additionalProperties: false
      type: object
      required:
        - table
      title: TableCreateReq
    TableCreateRes:
      properties:
        digest:
          type: string
          title: Digest
        row_digests:
          items:
            type: string
          type: array
          title: Row Digests
          description: The digests of the rows that were created
      type: object
      required:
        - digest
      title: TableCreateRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    TableSchemaForInsert:
      properties:
        project_id:
          type: string
          title: Project Id
        rows:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Rows
      type: object
      required:
        - project_id
        - rows
      title: TableSchemaForInsert
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