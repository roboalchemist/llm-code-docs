# Source: https://docs.wandb.ai/weave/reference/service-api/annotation-queues/annotation-queue-items-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotation Queue Items Query

> Query items in an annotation queue with pagination and sorting.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /annotation_queues/{queue_id}/items/query
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /annotation_queues/{queue_id}/items/query:
    post:
      tags:
        - Annotation Queues
      summary: Annotation Queue Items Query
      description: Query items in an annotation queue with pagination and sorting.
      operationId: >-
        annotation_queue_items_query_annotation_queues__queue_id__items_query_post
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
              $ref: '#/components/schemas/AnnotationQueueItemsQueryBody'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotationQueueItemsQueryRes'
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
    AnnotationQueueItemsQueryBody:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        filter:
          anyOf:
            - $ref: '#/components/schemas/AnnotationQueueItemsFilter'
            - type: 'null'
          description: Filter queue items by call metadata and annotation state
        sort_by:
          anyOf:
            - items:
                $ref: '#/components/schemas/SortBy'
              type: array
            - type: 'null'
          title: Sort By
          description: Sort by multiple fields (e.g., created_at, updated_at)
        limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Limit
          examples:
            - 50
        offset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Offset
          examples:
            - 0
        include_position:
          type: boolean
          title: Include Position
          description: Include position_in_queue field (1-based index in full queue)
          default: false
      additionalProperties: false
      type: object
      required:
        - project_id
      title: AnnotationQueueItemsQueryBody
      description: >-
        Request body for querying items in an annotation queue (queue_id comes
        from path).
    AnnotationQueueItemsQueryRes:
      properties:
        items:
          items:
            $ref: '#/components/schemas/AnnotationQueueItemSchema'
          type: array
          title: Items
      type: object
      required:
        - items
      title: AnnotationQueueItemsQueryRes
      description: Response from querying annotation queue items.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    AnnotationQueueItemsFilter:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
          description: Filter by exact queue item ID
        call_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Call Id
          description: Filter by exact call ID
        call_op_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Call Op Name
          description: Filter by exact operation name
        call_trace_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Call Trace Id
          description: Filter by exact trace ID
        added_by:
          anyOf:
            - type: string
            - type: 'null'
          title: Added By
          description: Filter by W&B user ID who added the call
        annotation_states:
          anyOf:
            - items:
                type: string
                enum:
                  - unstarted
                  - in_progress
                  - completed
                  - skipped
              type: array
            - type: 'null'
          title: Annotation States
          description: >-
            Filter by annotation states (unstarted, in_progress, completed,
            skipped)
          examples:
            - - unstarted
              - in_progress
      type: object
      title: AnnotationQueueItemsFilter
      description: >-
        Simple filter for annotation queue items.


        Supports equality filtering on call metadata fields and IN filtering on
        annotation state.
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