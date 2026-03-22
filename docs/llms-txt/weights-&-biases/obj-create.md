# Source: https://docs.wandb.ai/weave/reference/service-api/objects/obj-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Obj Create



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /obj/create
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /obj/create:
    post:
      tags:
        - Objects
      summary: Obj Create
      operationId: obj_create_obj_create_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObjCreateReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ObjCreateRes'
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
    ObjCreateReq:
      properties:
        obj:
          $ref: '#/components/schemas/ObjSchemaForInsert'
      additionalProperties: false
      type: object
      required:
        - obj
      title: ObjCreateReq
    ObjCreateRes:
      properties:
        digest:
          type: string
          title: Digest
        object_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Object Id
      type: object
      required:
        - digest
      title: ObjCreateRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ObjSchemaForInsert:
      properties:
        project_id:
          type: string
          title: Project Id
        object_id:
          type: string
          title: Object Id
        val:
          title: Val
        builtin_object_class:
          anyOf:
            - type: string
            - type: 'null'
          title: Builtin Object Class
        set_base_object_class:
          anyOf:
            - type: string
            - type: 'null'
          title: Set Base Object Class
          deprecated: true
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
      type: object
      required:
        - project_id
        - object_id
        - val
      title: ObjSchemaForInsert
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