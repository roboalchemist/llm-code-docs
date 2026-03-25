# Source: https://docs.wandb.ai/weave/reference/service-api/calls/calls-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Calls Delete



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /calls/delete
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /calls/delete:
    post:
      tags:
        - Calls
      summary: Calls Delete
      operationId: calls_delete_calls_delete_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CallsDeleteReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CallsDeleteRes'
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
    CallsDeleteReq:
      properties:
        project_id:
          type: string
          title: Project Id
        call_ids:
          items:
            type: string
          type: array
          title: Call Ids
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
        - call_ids
      title: CallsDeleteReq
    CallsDeleteRes:
      properties:
        num_deleted:
          type: integer
          title: Num Deleted
          description: The number of calls deleted
      type: object
      required:
        - num_deleted
      title: CallsDeleteRes
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