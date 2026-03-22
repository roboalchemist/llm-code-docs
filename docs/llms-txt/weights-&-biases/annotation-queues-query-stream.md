# Source: https://docs.wandb.ai/weave/reference/service-api/annotation-queues/annotation-queues-query-stream.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotation Queues Query Stream

> Query annotation queues for a project (streaming NDJSON response).



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /annotation_queues/query
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /annotation_queues/query:
    post:
      tags:
        - Annotation Queues
      summary: Annotation Queues Query Stream
      description: Query annotation queues for a project (streaming NDJSON response).
      operationId: annotation_queues_query_stream_annotation_queues_query_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnnotationQueuesQueryReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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
    AnnotationQueuesQueryReq:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
          description: Filter by queue name (case-insensitive partial match)
          examples:
            - Error
        sort_by:
          anyOf:
            - items:
                $ref: '#/components/schemas/SortBy'
              type: array
            - type: 'null'
          title: Sort By
          description: Sort by multiple fields (e.g., created_at, updated_at, name)
        limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Limit
          examples:
            - 10
        offset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Offset
          examples:
            - 0
      additionalProperties: false
      type: object
      required:
        - project_id
      title: AnnotationQueuesQueryReq
      description: Request to query annotation queues for a project.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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