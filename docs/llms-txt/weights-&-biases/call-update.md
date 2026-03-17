# Source: https://docs.wandb.ai/weave/reference/service-api/calls/call-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Update



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /call/update
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /call/update:
    post:
      tags:
        - Calls
      summary: Call Update
      operationId: call_update_call_update_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallUpdateReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallUpdateRes'
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
    CallUpdateReq:
      properties:
        project_id:
          type: string
          title: Project Id
        call_id:
          type: string
          title: Call Id
        display_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Display Name
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
        - call_id
      title: CallUpdateReq
    CallUpdateRes:
      properties: {}
      type: object
      title: CallUpdateRes
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