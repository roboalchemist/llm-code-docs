# Source: https://docs.wandb.ai/weave/reference/service-api/objects/objs-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Objs Query



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /objs/query
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /objs/query:
    post:
      tags:
        - Objects
      summary: Objs Query
      operationId: objs_query_objs_query_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ObjQueryReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ObjQueryRes'
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
    ObjQueryReq:
      properties:
        project_id:
          type: string
          title: Project Id
          description: The ID of the project to query
          examples:
            - user/project
        filter:
          anyOf:
            - $ref: '#/components/schemas/ObjectVersionFilter'
            - type: 'null'
          description: Filter criteria for the query. See `ObjectVersionFilter`
          examples:
            - latest_only: true
              object_ids:
                - my_favorite_model
        limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Limit
          description: Maximum number of results to return
          examples:
            - 100
        offset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Offset
          description: Number of results to skip before returning
          examples:
            - 0
        sort_by:
          anyOf:
            - items:
                $ref: '#/components/schemas/SortBy'
              type: array
            - type: 'null'
          title: Sort By
          description: >-
            Sorting criteria for the query results. Currently only supports
            'object_id' and 'created_at'.
          examples:
            - - direction: desc
                field: created_at
        metadata_only:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Metadata Only
          description: >-
            If true, the `val` column is not read from the database and is
            empty.All other fields are returned.
          default: false
        include_storage_size:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Include Storage Size
          description: If true, the `size_bytes` column is returned.
          default: false
      additionalProperties: false
      type: object
      required:
        - project_id
      title: ObjQueryReq
    ObjQueryRes:
      properties:
        objs:
          items:
            $ref: '#/components/schemas/ObjSchema'
          type: array
          title: Objs
      type: object
      required:
        - objs
      title: ObjQueryRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ObjectVersionFilter:
      properties:
        base_object_classes:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Base Object Classes
          description: Filter objects by their base classes
          examples:
            - - Model
            - - Dataset
        exclude_base_object_classes:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Exclude Base Object Classes
          description: Exclude objects by their base classes
          examples:
            - - Model
            - - Dataset
        leaf_object_classes:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Leaf Object Classes
          description: Filter objects by their leaf classes
          examples:
            - - Model
            - - Dataset
            - - LLMStructuredCompletionModel
        object_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Object Ids
          description: Filter objects by their IDs
          examples:
            - my_favorite_model
            - my_favorite_dataset
        is_op:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Op
          description: >-
            Filter objects based on whether they are weave.ops or not. `True`
            will only return ops, `False` will return non-ops, and `None` will
            return all objects
          examples:
            - true
            - false
            - null
        latest_only:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Latest Only
          description: >-
            If True, return only the latest version of each object. `False` and
            `None` will return all versions
          examples:
            - true
            - false
      additionalProperties: false
      type: object
      title: ObjectVersionFilter
    SortBy:
      properties:
        field:
          type: string
          title: Field
        direction:
          type: string
          enum:
            - asc
            - desc
          title: Direction
      additionalProperties: false
      type: object
      required:
        - field
        - direction
      title: SortBy
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