# Source: https://docs.wandb.ai/weave/reference/service-api/calls/call-start-batch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Start Batch



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /call/upsert_batch
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /call/upsert_batch:
    post:
      tags:
        - Calls
      summary: Call Start Batch
      operationId: call_start_batch_call_upsert_batch_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallCreateBatchReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallCreateBatchRes'
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
    CallCreateBatchReq:
      properties:
        batch:
          items:
            anyOf:
              - $ref: '#/components/schemas/CallBatchStartMode'
              - $ref: '#/components/schemas/CallBatchEndMode'
          type: array
          title: Batch
      type: object
      required:
        - batch
      title: CallCreateBatchReq
    CallCreateBatchRes:
      properties:
        res:
          items:
            anyOf:
              - $ref: '#/components/schemas/CallStartRes'
              - $ref: '#/components/schemas/CallEndRes'
          type: array
          title: Res
      type: object
      required:
        - res
      title: CallCreateBatchRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    CallBatchStartMode:
      properties:
        mode:
          type: string
          title: Mode
          default: start
        req:
          $ref: '#/components/schemas/CallStartReq'
      type: object
      required:
        - req
      title: CallBatchStartMode
    CallBatchEndMode:
      properties:
        mode:
          type: string
          title: Mode
          default: end
        req:
          $ref: '#/components/schemas/CallEndReq'
      type: object
      required:
        - req
      title: CallBatchEndMode
    CallStartRes:
      properties:
        id:
          type: string
          title: Id
        trace_id:
          type: string
          title: Trace Id
      type: object
      required:
        - id
        - trace_id
      title: CallStartRes
    CallEndRes:
      properties: {}
      type: object
      title: CallEndRes
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
    CallStartReq:
      properties:
        start:
          $ref: '#/components/schemas/StartedCallSchemaForInsert'
      additionalProperties: false
      type: object
      required:
        - start
      title: CallStartReq
    CallEndReq:
      properties:
        end:
          $ref: '#/components/schemas/EndedCallSchemaForInsert'
      additionalProperties: false
      type: object
      required:
        - end
      title: CallEndReq
    StartedCallSchemaForInsert:
      properties:
        project_id:
          type: string
          title: Project Id
        id:
          anyOf:
            - type: string
            - type: 'null'
          title: Id
        op_name:
          type: string
          title: Op Name
        display_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Display Name
        trace_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Trace Id
        parent_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Parent Id
        thread_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Thread Id
        turn_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Turn Id
        started_at:
          type: string
          format: date-time
          title: Started At
        attributes:
          additionalProperties: true
          type: object
          title: Attributes
        inputs:
          additionalProperties: true
          type: object
          title: Inputs
        otel_dump:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Otel Dump
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
        wb_run_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb Run Id
        wb_run_step:
          anyOf:
            - type: integer
            - type: 'null'
          title: Wb Run Step
      type: object
      required:
        - project_id
        - op_name
        - started_at
        - attributes
        - inputs
      title: StartedCallSchemaForInsert
    EndedCallSchemaForInsert:
      properties:
        project_id:
          type: string
          title: Project Id
        id:
          type: string
          title: Id
        ended_at:
          type: string
          format: date-time
          title: Ended At
        exception:
          anyOf:
            - type: string
            - type: 'null'
          title: Exception
        output:
          anyOf:
            - {}
            - type: 'null'
          title: Output
        summary:
          $ref: '#/components/schemas/SummaryInsertMap'
        wb_run_step_end:
          anyOf:
            - type: integer
            - type: 'null'
          title: Wb Run Step End
      type: object
      required:
        - project_id
        - id
        - ended_at
        - summary
      title: EndedCallSchemaForInsert
    SummaryInsertMap:
      properties:
        usage:
          additionalProperties:
            $ref: '#/components/schemas/LLMUsageSchema'
          type: object
          title: Usage
        status_counts:
          additionalProperties:
            type: integer
          propertyNames:
            $ref: '#/components/schemas/TraceStatus'
          type: object
          title: Status Counts
      additionalProperties: true
      type: object
      title: SummaryInsertMap
    LLMUsageSchema:
      properties:
        prompt_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Prompt Tokens
        input_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Input Tokens
        completion_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completion Tokens
        output_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Output Tokens
        requests:
          anyOf:
            - type: integer
            - type: 'null'
          title: Requests
        total_tokens:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Tokens
      additionalProperties: true
      type: object
      title: LLMUsageSchema
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````