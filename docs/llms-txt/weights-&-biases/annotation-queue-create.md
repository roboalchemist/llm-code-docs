# Source: https://docs.wandb.ai/weave/reference/service-api/annotation-queues/annotation-queue-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotation Queue Create

> Create a new annotation queue.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /annotation_queues
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /annotation_queues:
    post:
      tags:
        - Annotation Queues
      summary: Annotation Queue Create
      description: Create a new annotation queue.
      operationId: annotation_queue_create_annotation_queues_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnnotationQueueCreateReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotationQueueCreateRes'
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
    AnnotationQueueCreateReq:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        name:
          type: string
          title: Name
          examples:
            - Error Review Queue
        description:
          type: string
          title: Description
          default: ''
          examples:
            - Review calls with exceptions
        scorer_refs:
          items:
            type: string
          type: array
          title: Scorer Refs
          examples:
            - - weave:///entity/project/scorer/error_severity:abc123
              - weave:///entity/project/scorer/resolution_quality:def456
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
      additionalProperties: false
      type: object
      required:
        - project_id
        - name
        - scorer_refs
      title: AnnotationQueueCreateReq
      description: Request to create a new annotation queue.
    AnnotationQueueCreateRes:
      properties:
        id:
          type: string
          title: Id
      type: object
      required:
        - id
      title: AnnotationQueueCreateRes
      description: Response from creating an annotation queue.
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