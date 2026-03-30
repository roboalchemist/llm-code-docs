# Source: https://docs.wandb.ai/weave/reference/service-api/calls/call-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Read



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /call/read
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /call/read:
    post:
      tags:
        - Calls
      summary: Call Read
      operationId: call_read_call_read_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallReadReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallReadRes'
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
    CallReadReq:
      properties:
        project_id:
          type: string
          title: Project Id
        id:
          type: string
          title: Id
        include_costs:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Include Costs
          default: false
        include_storage_size:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Include Storage Size
          default: false
        include_total_storage_size:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Include Total Storage Size
          default: false
      additionalProperties: false
      type: object
      required:
        - project_id
        - id
      title: CallReadReq
    CallReadRes:
      properties:
        call:
          anyOf:
            - $ref: '#/components/schemas/CallSchema'
            - type: 'null'
      type: object
      required:
        - call
      title: CallReadRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    CallSchema:
      properties:
        id:
          type: string
          title: Id
        project_id:
          type: string
          title: Project Id
        op_name:
          type: string
          title: Op Name
        display_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Display Name
        trace_id:
          type: string
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
        ended_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
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
          additionalProperties: true
          type: object
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
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
        wb_run_step_end:
          anyOf:
            - type: integer
            - type: 'null'
          title: Wb Run Step End
        deleted_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Deleted At
        storage_size_bytes:
          anyOf:
            - type: integer
            - type: 'null'
          title: Storage Size Bytes
        total_storage_size_bytes:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Storage Size Bytes
      type: object
      required:
        - id
        - project_id
        - op_name
        - trace_id
        - started_at
        - attributes
        - inputs
      title: CallSchema
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