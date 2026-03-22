# Source: https://docs.wandb.ai/weave/reference/service-api/annotation-queues/annotation-queue-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotation Queue Read

> Read a specific annotation queue.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json get /annotation_queues/{queue_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /annotation_queues/{queue_id}:
    get:
      tags:
        - Annotation Queues
      summary: Annotation Queue Read
      description: Read a specific annotation queue.
      operationId: annotation_queue_read_annotation_queues__queue_id__get
      parameters:
        - name: queue_id
          in: path
          required: true
          schema:
            type: string
            title: Queue Id
        - name: project_id
          in: query
          required: true
          schema:
            type: string
            title: Project Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotationQueueReadRes'
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
    AnnotationQueueReadRes:
      properties:
        queue:
          $ref: '#/components/schemas/AnnotationQueueSchema'
      type: object
      required:
        - queue
      title: AnnotationQueueReadRes
      description: Response from reading an annotation queue.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AnnotationQueueSchema:
      properties:
        id:
          type: string
          title: Id
        project_id:
          type: string
          title: Project Id
        name:
          type: string
          title: Name
        description:
          type: string
          title: Description
        scorer_refs:
          items:
            type: string
          type: array
          title: Scorer Refs
        created_at:
          type: string
          format: date-time
          title: Created At
        created_by:
          type: string
          title: Created By
        updated_at:
          type: string
          format: date-time
          title: Updated At
        deleted_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Deleted At
      type: object
      required:
        - id
        - project_id
        - name
        - description
        - scorer_refs
        - created_at
        - created_by
        - updated_at
      title: AnnotationQueueSchema
      description: Schema for annotation queue responses.
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