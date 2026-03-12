# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-schemas/read-block-schemas.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Block Schemas

> Read all block schemas, optionally filtered by type



## OpenAPI

````yaml post /block_schemas/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_schemas/filter:
    post:
      tags:
        - Block schemas
      summary: Read Block Schemas
      description: Read all block schemas, optionally filtered by type
      operationId: read_block_schemas_block_schemas_filter_post
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
                #/components/schemas/Body_read_block_schemas_block_schemas_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/BlockSchema'
                title: Response Read Block Schemas Block Schemas Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_block_schemas_block_schemas_filter_post:
      properties:
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
      title: Body_read_block_schemas_block_schemas_filter_post
    BlockSchema:
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
        checksum:
          type: string
          title: Checksum
          description: The block schema's unique checksum
        fields:
          additionalProperties: true
          type: object
          title: Fields
          description: The block schema's field schema
        block_type_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Block Type Id
          description: A block type ID
        block_type:
          anyOf:
            - $ref: '#/components/schemas/BlockType'
            - type: 'null'
          description: The associated block type
        capabilities:
          items:
            type: string
          type: array
          title: Capabilities
          description: A list of Block capabilities
        version:
          type: string
          title: Version
          description: Human readable identifier for the block schema
          default: non-versioned
      type: object
      required:
        - checksum
        - block_type_id
        - id
        - created
        - updated
      title: BlockSchema
      description: An ORM representation of a block schema.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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