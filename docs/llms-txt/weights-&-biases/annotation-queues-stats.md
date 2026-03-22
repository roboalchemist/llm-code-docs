# Source: https://docs.wandb.ai/weave/reference/service-api/annotation-queues/annotation-queues-stats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotation Queues Stats

> Get stats for multiple annotation queues.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /annotation_queues/stats
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /annotation_queues/stats:
    post:
      tags:
        - Annotation Queues
      summary: Annotation Queues Stats
      description: Get stats for multiple annotation queues.
      operationId: annotation_queues_stats_annotation_queues_stats_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnnotationQueuesStatsReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotationQueuesStatsRes'
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
    AnnotationQueuesStatsReq:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        queue_ids:
          items:
            type: string
          type: array
          title: Queue Ids
          description: List of queue IDs to get stats for
          examples:
            - - 550e8400-e29b-41d4-a716-446655440000
              - 550e8400-e29b-41d4-a716-446655440001
      additionalProperties: false
      type: object
      required:
        - project_id
        - queue_ids
      title: AnnotationQueuesStatsReq
      description: Request to get stats for multiple annotation queues.
    AnnotationQueuesStatsRes:
      properties:
        stats:
          items:
            $ref: '#/components/schemas/AnnotationQueueStatsSchema'
          type: array
          title: Stats
      type: object
      required:
        - stats
      title: AnnotationQueuesStatsRes
      description: Response with stats for multiple annotation queues.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AnnotationQueueStatsSchema:
      properties:
        queue_id:
          type: string
          title: Queue Id
          description: The queue ID
          examples:
            - 550e8400-e29b-41d4-a716-446655440000
        total_items:
          type: integer
          title: Total Items
          description: Total number of items in the queue
        completed_items:
          type: integer
          title: Completed Items
          description: Number of items completed or skipped by at least one annotator
      type: object
      required:
        - queue_id
        - total_items
        - completed_items
      title: AnnotationQueueStatsSchema
      description: Statistics for a single annotation queue.
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