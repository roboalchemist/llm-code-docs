# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-types/read-block-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Block Types

> Gets all block types. Optionally limit return with limit and offset.



## OpenAPI

````yaml post /block_types/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_types/filter:
    post:
      tags:
        - Block types
      summary: Read Block Types
      description: Gets all block types. Optionally limit return with limit and offset.
      operationId: read_block_types_block_types_filter_post
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
              $ref: >-
                #/components/schemas/Body_read_block_types_block_types_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/BlockType'
                title: Response Read Block Types Block Types Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_block_types_block_types_filter_post:
      properties:
        block_types:
          anyOf:
            - $ref: '#/components/schemas/BlockTypeFilter'
            - type: 'null'
        block_schemas:
          anyOf:
            - $ref: '#/components/schemas/BlockSchemaFilter'
            - type: 'null'
        offset:
          type: integer
          minimum: 0
          title: Offset
          default: 0
        limit:
          type: integer
          title: Limit
          description: Defaults to PREFECT_API_DEFAULT_LIMIT if not provided.
      type: object
      title: Body_read_block_types_block_types_filter_post
    BlockType:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        created:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Created
        updated:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Updated
        name:
          type: string
          pattern: ^[^/%&><]+$
          title: Name
          description: A block type's name
        slug:
          type: string
          title: Slug
          description: A block type's slug
        logo_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Logo Url
          description: Web URL for the block type's logo
        documentation_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Documentation Url
          description: Web URL for the block type's documentation
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
          description: A short blurb about the corresponding block's intended use
        code_example:
          anyOf:
            - type: string
            - type: 'null'
          title: Code Example
          description: A code snippet demonstrating use of the corresponding block
        is_protected:
          type: boolean
          title: Is Protected
          description: Protected block types cannot be modified via API.
          default: false
      type: object
      required:
        - name
        - slug
        - id
        - created
        - updated
      title: BlockType
      description: An ORM representation of a block type
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    BlockTypeFilter:
      properties:
        name:
          anyOf:
            - $ref: '#/components/schemas/BlockTypeFilterName'
            - type: 'null'
          description: Filter criteria for `BlockType.name`
        slug:
          anyOf:
            - $ref: '#/components/schemas/BlockTypeFilterSlug'
            - type: 'null'
          description: Filter criteria for `BlockType.slug`
      additionalProperties: false
      type: object
      title: BlockTypeFilter
      description: Filter BlockTypes
    BlockSchemaFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        block_type_id:
          anyOf:
            - $ref: '#/components/schemas/BlockSchemaFilterBlockTypeId'
            - type: 'null'
          description: Filter criteria for `BlockSchema.block_type_id`
        block_capabilities:
          anyOf:
            - $ref: '#/components/schemas/BlockSchemaFilterCapabilities'
            - type: 'null'
          description: Filter criteria for `BlockSchema.capabilities`
        id:
          anyOf:
            - $ref: '#/components/schemas/BlockSchemaFilterId'
            - type: 'null'
          description: Filter criteria for `BlockSchema.id`
        version:
          anyOf:
            - $ref: '#/components/schemas/BlockSchemaFilterVersion'
            - type: 'null'
          description: Filter criteria for `BlockSchema.version`
      additionalProperties: false
      type: object
      title: BlockSchemaFilter
      description: Filter BlockSchemas
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
    BlockTypeFilterName:
      properties:
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A case-insensitive partial match. For example,  passing 'marvin'
            will match 'marvin', 'sad-Marvin', and 'marvin-robot'.
          examples:
            - marvin
      additionalProperties: false
      type: object
      title: BlockTypeFilterName
      description: Filter by `BlockType.name`
    BlockTypeFilterSlug:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of slugs to match
      additionalProperties: false
      type: object
      title: BlockTypeFilterSlug
      description: Filter by `BlockType.slug`
    Operator:
      type: string
      enum:
        - and_
        - or_
      title: Operator
      description: Operators for combining filter criteria.
    BlockSchemaFilterBlockTypeId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of block type ids to include
      additionalProperties: false
      type: object
      title: BlockSchemaFilterBlockTypeId
      description: Filter by `BlockSchema.block_type_id`.
    BlockSchemaFilterCapabilities:
      properties:
        all_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: All
          description: >-
            A list of block capabilities. Block entities will be returned only
            if an associated block schema has a superset of the defined
            capabilities.
          examples:
            - - write-storage
              - read-storage
      additionalProperties: false
      type: object
      title: BlockSchemaFilterCapabilities
      description: Filter by `BlockSchema.capabilities`
    BlockSchemaFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of IDs to include
      additionalProperties: false
      type: object
      title: BlockSchemaFilterId
      description: Filter by BlockSchema.id
    BlockSchemaFilterVersion:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of block schema versions.
          examples:
            - - 2.0.0
              - 2.1.0
      additionalProperties: false
      type: object
      title: BlockSchemaFilterVersion
      description: Filter by `BlockSchema.capabilities`

````

Built with [Mintlify](https://mintlify.com).