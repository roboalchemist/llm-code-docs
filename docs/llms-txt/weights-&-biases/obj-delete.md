# Source: https://docs.wandb.ai/weave/reference/service-api/objects/obj-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Obj Delete



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /obj/delete
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /obj/delete:
    post:
      tags:
        - Objects
      summary: Obj Delete
      operationId: obj_delete_obj_delete_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObjDeleteReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ObjDeleteRes'
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
    ObjDeleteReq:
      properties:
        project_id:
          type: string
          title: Project Id
        object_id:
          type: string
          title: Object Id
        digests:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Digests
          description: >-
            List of digests to delete. If not provided, all digests for the
            object will be deleted.
      additionalProperties: false
      type: object
      required:
        - project_id
        - object_id
      title: ObjDeleteReq
    ObjDeleteRes:
      properties:
        num_deleted:
          type: integer
          title: Num Deleted
      type: object
      required:
        - num_deleted
      title: ObjDeleteRes
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