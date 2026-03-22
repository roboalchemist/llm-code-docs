# Source: https://docs.wandb.ai/weave/reference/service-api/files/files-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Files Stats



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /files/query_stats
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /files/query_stats:
    post:
      tags:
        - Files
      summary: Files Stats
      operationId: files_stats_files_query_stats_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FilesStatsReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FilesStatsRes'
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
    FilesStatsReq:
      properties:
        project_id:
          type: string
          title: Project Id
      additionalProperties: false
      type: object
      required:
        - project_id
      title: FilesStatsReq
    FilesStatsRes:
      properties:
        total_size_bytes:
          type: integer
          title: Total Size Bytes
      type: object
      required:
        - total_size_bytes
      title: FilesStatsRes
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