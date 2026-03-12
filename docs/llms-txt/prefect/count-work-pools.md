# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/work-pools/count-work-pools.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Count Work Pools

> Count work pools



## OpenAPI

````yaml post /work_pools/count
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /work_pools/count:
    post:
      tags:
        - Work Pools
      summary: Count Work Pools
      description: Count work pools
      operationId: count_work_pools_work_pools_count_post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Body_count_work_pools_work_pools_count_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: integer
                title: Response Count Work Pools Work Pools Count Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_count_work_pools_work_pools_count_post:
      properties:
        work_pools:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilter'
            - type: 'null'
      type: object
      title: Body_count_work_pools_work_pools_count_post
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    WorkPoolFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterId'
            - type: 'null'
          description: Filter criteria for `WorkPool.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterName'
            - type: 'null'
          description: Filter criteria for `WorkPool.name`
        type:
          anyOf:
            - $ref: '#/components/schemas/WorkPoolFilterType'
            - type: 'null'
          description: Filter criteria for `WorkPool.type`
      additionalProperties: false
      type: object
      title: WorkPoolFilter
      description: >-
        Filter work pools. Only work pools matching all criteria will be
        returned
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
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
    Operator:
      type: string
      enum:
        - and_
        - or_
      title: Operator
      description: Operators for combining filter criteria.
    WorkPoolFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool ids to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterId
      description: Filter by `WorkPool.id`.
    WorkPoolFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool names to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterName
      description: Filter by `WorkPool.name`.
    WorkPoolFilterType:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of work pool types to include
      additionalProperties: false
      type: object
      title: WorkPoolFilterType
      description: Filter by `WorkPool.type`.

````

Built with [Mintlify](https://mintlify.com).