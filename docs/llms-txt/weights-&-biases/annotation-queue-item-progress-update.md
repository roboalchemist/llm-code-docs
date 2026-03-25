# Source: https://docs.wandb.ai/weave/reference/service-api/annotation-queues/annotation-queue-item-progress-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotation Queue Item Progress Update

> Update the annotation state of a queue item for the current annotator.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /annotation_queues/{queue_id}/items/{item_id}/progress
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /annotation_queues/{queue_id}/items/{item_id}/progress:
    post:
      tags:
        - Annotation Queues
      summary: Annotation Queue Item Progress Update
      description: Update the annotation state of a queue item for the current annotator.
      operationId: >-
        annotation_queue_item_progress_update_annotation_queues__queue_id__items__item_id__progress_post
      parameters:
        - name: queue_id
          in: path
          required: true
          schema:
            type: string
            title: Queue Id
        - name: item_id
          in: path
          required: true
          schema:
            type: string
            title: Item Id
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnnotationQueueItemProgressUpdateBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotatorQueueItemsProgressUpdateRes'
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
    AnnotationQueueItemProgressUpdateBody:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        annotation_state:
          type: string
          title: Annotation State
          description: 'New state: ''in_progress'', ''completed'', or ''skipped'''
          examples:
            - in_progress
            - completed
            - skipped
      additionalProperties: false
      type: object
      required:
        - project_id
        - annotation_state
      title: AnnotationQueueItemProgressUpdateBody
      description: >-
        Request body for updating annotation progress (queue_id and item_id come
        from path).


        Note: wb_user_id is not included in the body - it's set server-side from
        the authenticated session.
    AnnotatorQueueItemsProgressUpdateRes:
      properties:
        item:
          $ref: '#/components/schemas/AnnotationQueueItemSchema'
      type: object
      required:
        - item
      title: AnnotatorQueueItemsProgressUpdateRes
      description: Response from updating annotation state.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AnnotationQueueItemSchema:
      properties:
        id:
          type: string
          title: Id
        project_id:
          type: string
          title: Project Id
        queue_id:
          type: string
          title: Queue Id
        call_id:
          type: string
          title: Call Id
        call_started_at:
          type: string
          format: date-time
          title: Call Started At
        call_ended_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Call Ended At
        call_op_name:
          type: string
          title: Call Op Name
        call_trace_id:
          type: string
          title: Call Trace Id
        display_fields:
          items:
            type: string
          type: array
          title: Display Fields
        added_by:
          anyOf:
            - type: string
            - type: 'null'
          title: Added By
        annotation_state:
          type: string
          enum:
            - unstarted
            - in_progress
            - completed
            - skipped
          title: Annotation State
        annotator_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Annotator User Id
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
        position_in_queue:
          anyOf:
            - type: integer
            - type: 'null'
          title: Position In Queue
      type: object
      required:
        - id
        - project_id
        - queue_id
        - call_id
        - call_started_at
        - call_op_name
        - call_trace_id
        - display_fields
        - annotation_state
        - created_at
        - created_by
        - updated_at
      title: AnnotationQueueItemSchema
      description: Schema for annotation queue item responses.
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