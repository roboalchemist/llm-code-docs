# Source: https://docs.wandb.ai/weave/reference/service-api/tables/table-query-stats-batch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Query Stats Batch



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /table/query_stats_batch
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /table/query_stats_batch:
    post:
      tags:
        - Tables
      summary: Table Query Stats Batch
      operationId: table_query_stats_batch_table_query_stats_batch_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TableQueryStatsBatchReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableQueryStatsBatchRes'
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
    TableQueryStatsBatchReq:
      properties:
        project_id:
          type: string
          title: Project Id
          description: The ID of the project
          examples:
            - my_entity/my_project
        digests:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Digests
          description: The digests of the tables to query
          default: []
          examples:
            - aonareimsvtl13apimtalpa4435rpmgnaemrpgmarltarstaorsnte134avrims
            - smirva431etnsroatsratlrampgrmeangmpr5344aplatmipa31ltvsmiераnoa
        include_storage_size:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Include Storage Size
          description: If true, the `storage_size_bytes` column is returned.
          default: false
      additionalProperties: false
      type: object
      required:
        - project_id
      title: TableQueryStatsBatchReq
    TableQueryStatsBatchRes:
      properties:
        tables:
          items:
            $ref: '#/components/schemas/TableStatsRow'
          type: array
          title: Tables
      type: object
      required:
        - tables
      title: TableQueryStatsBatchRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    TableStatsRow:
      properties:
        count:
          type: integer
          title: Count
        digest:
          type: string
          title: Digest
        storage_size_bytes:
          anyOf:
            - type: integer
            - type: 'null'
          title: Storage Size Bytes
      type: object
      required:
        - count
        - digest
      title: TableStatsRow
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