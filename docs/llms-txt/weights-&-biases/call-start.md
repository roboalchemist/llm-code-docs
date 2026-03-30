# Source: https://docs.wandb.ai/weave/reference/service-api/calls/call-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Start



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /call/start
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /call/start:
    post:
      tags:
        - Calls
      summary: Call Start
      operationId: call_start_call_start_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallStartReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallStartRes'
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
    CallStartReq:
      properties:
        start:
          $ref: '#/components/schemas/StartedCallSchemaForInsert'
      additionalProperties: false
      type: object
      required:
        - start
      title: CallStartReq
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
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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