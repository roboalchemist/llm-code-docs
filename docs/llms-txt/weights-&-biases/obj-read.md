# Source: https://docs.wandb.ai/weave/reference/service-api/objects/obj-read.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Obj Read



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /obj/read
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /obj/read:
    post:
      tags:
        - Objects
      summary: Obj Read
      operationId: obj_read_obj_read_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObjReadReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ObjReadRes'
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
    ObjReadReq:
      properties:
        project_id:
          type: string
          title: Project Id
        object_id:
          type: string
          title: Object Id
        digest:
          type: string
          title: Digest
        metadata_only:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Metadata Only
          description: >-
            If true, the `val` column is not read from the database and is
            empty.All other fields are returned.
          default: false
      additionalProperties: false
      type: object
      required:
        - project_id
        - object_id
        - digest
      title: ObjReadReq
    ObjReadRes:
      properties:
        obj:
          $ref: '#/components/schemas/ObjSchema'
      type: object
      required:
        - obj
      title: ObjReadRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ObjSchema:
      properties:
        project_id:
          type: string
          title: Project Id
        object_id:
          type: string
          title: Object Id
        created_at:
          type: string
          format: date-time
          title: Created At
        deleted_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Deleted At
        digest:
          type: string
          title: Digest
        version_index:
          type: integer
          title: Version Index
        is_latest:
          type: integer
          title: Is Latest
        kind:
          type: string
          title: Kind
        base_object_class:
          anyOf:
            - type: string
            - type: 'null'
          title: Base Object Class
        leaf_object_class:
          anyOf:
            - type: string
            - type: 'null'
          title: Leaf Object Class
        val:
          title: Val
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
        size_bytes:
          anyOf:
            - type: integer
            - type: 'null'
          title: Size Bytes
      type: object
      required:
        - project_id
        - object_id
        - created_at
        - digest
        - version_index
        - is_latest
        - kind
        - base_object_class
        - val
      title: ObjSchema
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