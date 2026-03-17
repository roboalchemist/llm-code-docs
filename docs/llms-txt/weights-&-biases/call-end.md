# Source: https://docs.wandb.ai/weave/reference/service-api/calls/call-end.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Call End



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /call/end
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /call/end:
    post:
      tags:
        - Calls
      summary: Call End
      operationId: call_end_call_end_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallEndReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallEndRes'
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
    CallEndReq:
      properties:
        end:
          $ref: '#/components/schemas/EndedCallSchemaForInsert'
      additionalProperties: false
      type: object
      required:
        - end
      title: CallEndReq
    CallEndRes:
      properties: {}
      type: object
      title: CallEndRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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