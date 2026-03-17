# Source: https://docs.wandb.ai/weave/reference/service-api/annotation-queues/annotation-queue-add-calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotation Queue Add Calls

> Add calls to an annotation queue.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /annotation_queues/{queue_id}/items
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /annotation_queues/{queue_id}/items:
    post:
      tags:
        - Annotation Queues
      summary: Annotation Queue Add Calls
      description: Add calls to an annotation queue.
      operationId: annotation_queue_add_calls_annotation_queues__queue_id__items_post
      parameters:
        - name: queue_id
          in: path
          required: true
          schema:
            type: string
            title: Queue Id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnnotationQueueAddCallsBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotationQueueAddCallsRes'
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
    AnnotationQueueAddCallsBody:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        call_ids:
          items:
            type: string
          type: array
          title: Call Ids
          examples:
            - - call-1
              - call-2
              - call-3
        display_fields:
          items:
            type: string
          type: array
          title: Display Fields
          description: JSON paths to display to annotators
          examples:
            - - input.prompt
              - output.text
      additionalProperties: false
      type: object
      required:
        - project_id
        - call_ids
        - display_fields
      title: AnnotationQueueAddCallsBody
      description: >-
        Request body for adding calls to an annotation queue (queue_id comes
        from path).
    AnnotationQueueAddCallsRes:
      properties:
        added_count:
          type: integer
          title: Added Count
        duplicates:
          type: integer
          title: Duplicates
      type: object
      required:
        - added_count
        - duplicates
      title: AnnotationQueueAddCallsRes
      description: Response from adding calls to a queue.
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