# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/variables/count-variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Count Variables



## OpenAPI

````yaml post /variables/count
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /variables/count:
    post:
      tags:
        - Variables
      summary: Count Variables
      operationId: count_variables_variables_count_post
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
              $ref: '#/components/schemas/Body_count_variables_variables_count_post'
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: integer
                title: Response Count Variables Variables Count Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_count_variables_variables_count_post:
      properties:
        variables:
          anyOf:
            - $ref: '#/components/schemas/VariableFilter'
            - type: 'null'
      type: object
      title: Body_count_variables_variables_count_post
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    VariableFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/VariableFilterId'
            - type: 'null'
          description: Filter criteria for `Variable.id`
        name:
          anyOf:
            - $ref: '#/components/schemas/VariableFilterName'
            - type: 'null'
          description: Filter criteria for `Variable.name`
        tags:
          anyOf:
            - $ref: '#/components/schemas/VariableFilterTags'
            - type: 'null'
          description: Filter criteria for `Variable.tags`
      additionalProperties: false
      type: object
      title: VariableFilter
      description: Filter variables. Only variables matching all criteria will be returned
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
    VariableFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of variable ids to include
      additionalProperties: false
      type: object
      title: VariableFilterId
      description: Filter by `Variable.id`.
    VariableFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of variables names to include
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A string to match variable names against. This can include SQL
            wildcard characters like `%` and `_`.
          examples:
            - my_variable_%
      additionalProperties: false
      type: object
      title: VariableFilterName
      description: Filter by `Variable.name`.
    VariableFilterTags:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        all_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: All
          description: >-
            A list of tags. Variables will be returned only if their tags are a
            superset of the list
          examples:
            - - tag-1
              - tag-2
        is_null_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Null
          description: If true, only include Variables without tags
      additionalProperties: false
      type: object
      title: VariableFilterTags
      description: Filter by `Variable.tags`.

````

Built with [Mintlify](https://mintlify.com).