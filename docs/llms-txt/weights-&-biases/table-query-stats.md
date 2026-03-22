# Source: https://docs.wandb.ai/weave/reference/service-api/tables/table-query-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Table Query Stats



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /table/query_stats
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /table/query_stats:
    post:
      tags:
        - Tables
      summary: Table Query Stats
      operationId: table_query_stats_table_query_stats_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TableQueryStatsReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TableQueryStatsRes'
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
    TableQueryStatsReq:
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
      additionalProperties: false
      type: object
      required:
        - project_id
        - digest
      title: TableQueryStatsReq
    TableQueryStatsRes:
      properties:
        count:
          type: integer
          title: Count
      type: object
      required:
        - count
      title: TableQueryStatsRes
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