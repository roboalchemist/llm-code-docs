# Source: https://docs.wandb.ai/weave/reference/service-api/tables/table-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Query



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /table/query
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /table/query:
    post:
      tags:
        - Tables
      summary: Table Query
      operationId: table_query_table_query_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TableQueryReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableQueryRes'
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
    TableQueryReq:
      properties:
        project_id:
          type: string
          title: Project Id
          description: The ID of the project
          examples:
            - my_entity/my_project
        digest:
          type: string
          title: Digest
          description: The digest of the table to query
          examples:
            - aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims
        filter:
          anyOf:
            - $ref: '#/components/schemas/TableRowFilter'
            - type: 'null'
          description: >-
            Optional filter to apply to the query. See `TableRowFilter` for more
            details.
          examples:
            - row_digests:
                - >-
                  aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims
                - >-
                  aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims
        limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Limit
          description: Maximum number of rows to return
          examples:
            - 100
        offset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Offset
          description: Number of rows to skip before starting to return rows
          examples:
            - 10
        sort_by:
          anyOf:
            - items:
                $ref: '#/components/schemas/SortBy'
              type: array
            - type: 'null'
          title: Sort By
          description: >-
            List of fields to sort by. Fields can be dot-separated to access
            dictionary values. No sorting uses the default table order
            (insertion order).
          examples:
            - - field: col_a.prop_b
                order: desc
      additionalProperties: false
      type: object
      required:
        - project_id
        - digest
      title: TableQueryReq
    TableQueryRes:
      properties:
        rows:
          items:
            $ref: '#/components/schemas/TableRowSchema'
          type: array
          title: Rows
      type: object
      required:
        - rows
      title: TableQueryRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    TableRowFilter:
      properties:
        row_digests:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Row Digests
          description: List of row digests to filter by
          examples:
            - - aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims
              - aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims
      additionalProperties: false
      type: object
      title: TableRowFilter
    SortBy:
      properties:
        field:
          type: string
          title: Field
        direction:
          type: string
          enum:
            - asc
            - desc
          title: Direction
      additionalProperties: false
      type: object
      required:
        - field
        - direction
      title: SortBy
    TableRowSchema:
      properties:
        digest:
          type: string
          title: Digest
        val:
          title: Val
        original_index:
          anyOf:
            - type: integer
            - type: 'null'
          title: Original Index
      type: object
      required:
        - digest
        - val
      title: TableRowSchema
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