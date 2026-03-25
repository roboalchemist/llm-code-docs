# Source: https://docs.wandb.ai/weave/reference/service-api/feedback/feedback-replace.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Feedback Replace



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /feedback/replace
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /feedback/replace:
    post:
      tags:
        - Feedback
      summary: Feedback Replace
      operationId: feedback_replace_feedback_replace_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FeedbackReplaceReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FeedbackReplaceRes'
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
    FeedbackReplaceReq:
      properties:
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
          description: >-
            If provided by the client, this ID will be used for the feedback row
            instead of a server-generated one.
          examples:
            - 018f1f2a-9c2b-7d3e-b5a1-8c9d2e4f6a7b
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        weave_ref:
          type: string
          title: Weave Ref
          examples:
            - weave:///entity/project/object/name:digest
        creator:
          anyOf:
            - type: string
            - type: 'null'
          title: Creator
          examples:
            - Jane Smith
        feedback_type:
          type: string
          title: Feedback Type
          examples:
            - custom
        payload:
          additionalProperties: true
          type: object
          title: Payload
          examples:
            - key: value
        annotation_ref:
          anyOf:
            - type: string
            - type: 'null'
          title: Annotation Ref
          examples:
            - weave:///entity/project/object/name:digest
        runnable_ref:
          anyOf:
            - type: string
            - type: 'null'
          title: Runnable Ref
          examples:
            - weave:///entity/project/op/name:digest
        call_ref:
          anyOf:
            - type: string
            - type: 'null'
          title: Call Ref
          examples:
            - weave:///entity/project/call/call_id
        trigger_ref:
          anyOf:
            - type: string
            - type: 'null'
          title: Trigger Ref
          examples:
            - weave:///entity/project/object/name:digest
        queue_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Id
          description: >-
            The annotation queue ID this feedback was created from. References
            annotation_queues.id. NULL when feedback is created outside of
            queues.
          examples:
            - 018f1f2a-9c2b-7d3e-b5a1-8c9d2e4f6a7b
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
        feedback_id:
          type: string
          title: Feedback Id
      additionalProperties: false
      type: object
      required:
        - project_id
        - weave_ref
        - feedback_type
        - payload
        - feedback_id
      title: FeedbackReplaceReq
    FeedbackReplaceRes:
      properties:
        id:
          type: string
          title: Id
        created_at:
          type: string
          format: date-time
          title: Created At
        wb_user_id:
          type: string
          title: Wb User Id
        payload:
          additionalProperties: true
          type: object
          title: Payload
      type: object
      required:
        - id
        - created_at
        - wb_user_id
        - payload
      title: FeedbackReplaceRes
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