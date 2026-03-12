# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-documents/read-block-documents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Block Documents

> Query for block documents.



## OpenAPI

````yaml post /block_documents/filter
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_documents/filter:
    post:
      tags:
        - Block documents
      summary: Read Block Documents
      description: Query for block documents.
      operationId: read_block_documents_block_documents_filter_post
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
                #/components/schemas/Body_read_block_documents_block_documents_filter_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/BlockDocument'
                title: Response Read Block Documents Block Documents Filter Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_read_block_documents_block_documents_filter_post:
      properties:
        block_documents:
          anyOf:
            - $ref: '#/components/schemas/BlockDocumentFilter'
            - type: 'null'
        block_types:
          anyOf:
            - $ref: '#/components/schemas/BlockTypeFilter'
            - type: 'null'
        block_schemas:
          anyOf:
            - $ref: '#/components/schemas/BlockSchemaFilter'
            - type: 'null'
        include_secrets:
          type: boolean
          title: Include Secrets
          description: Whether to include sensitive values in the block document.
          default: false
        sort:
          anyOf:
            - $ref: '#/components/schemas/BlockDocumentSort'
            - type: 'null'
          default: NAME_ASC
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
      title: Body_read_block_documents_block_documents_filter_post
    BlockDocument:
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
          anyOf:
            - type: string
              pattern: ^[^/%&><]+$
            - type: 'null'
          title: Name
          description: >-
            The block document's name. Not required for anonymous block
            documents.
        data:
          additionalProperties: true
          type: object
          title: Data
          description: The block document's data
        block_schema_id:
          type: string
          format: uuid
          title: Block Schema Id
          description: A block schema ID
        block_schema:
          anyOf:
            - $ref: '#/components/schemas/BlockSchema'
            - type: 'null'
          description: The associated block schema
        block_type_id:
          type: string
          format: uuid
          title: Block Type Id
          description: A block type ID
        block_type_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Block Type Name
          description: The associated block type's name
        block_type:
          anyOf:
            - $ref: '#/components/schemas/BlockType'
            - type: 'null'
          description: The associated block type
        block_document_references:
          additionalProperties:
            additionalProperties: true
            type: object
          type: object
          title: Block Document References
          description: Record of the block document's references
        is_anonymous:
          type: boolean
          title: Is Anonymous
          description: >-
            Whether the block is anonymous (anonymous blocks are usually created
            by Prefect automatically)
          default: false
      type: object
      required:
        - block_schema_id
        - block_type_id
        - id
        - created
        - updated
      title: BlockDocument
      description: An ORM representation of a block document.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    BlockDocumentFilter:
      properties:
        operator:
          $ref: '#/components/schemas/Operator'
          description: Operator for combining filter criteria. Defaults to 'and_'.
          default: and_
        id:
          anyOf:
            - $ref: '#/components/schemas/BlockDocumentFilterId'
            - type: 'null'
          description: Filter criteria for `BlockDocument.id`
        is_anonymous:
          anyOf:
            - $ref: '#/components/schemas/BlockDocumentFilterIsAnonymous'
            - type: 'null'
          description: >-
            Filter criteria for `BlockDocument.is_anonymous`. Defaults to
            excluding anonymous blocks.
          default:
            eq_: false
        block_type_id:
          anyOf:
            - $ref: '#/components/schemas/BlockDocumentFilterBlockTypeId'
            - type: 'null'
          description: Filter criteria for `BlockDocument.block_type_id`
        name:
          anyOf:
            - $ref: '#/components/schemas/BlockDocumentFilterName'
            - type: 'null'
          description: Filter criteria for `BlockDocument.name`
      additionalProperties: false
      type: object
      title: BlockDocumentFilter
      description: >-
        Filter BlockDocuments. Only BlockDocuments matching all criteria will be
        returned
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
    BlockDocumentSort:
      type: string
      enum:
        - NAME_DESC
        - NAME_ASC
        - BLOCK_TYPE_AND_NAME_ASC
      title: BlockDocumentSort
      description: Defines block document sorting options.
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
    BlockDocumentFilterId:
      properties:
        any_:
          anyOf:
            - items:
                type: string
                format: uuid
              type: array
            - type: 'null'
          title: Any
          description: A list of block ids to include
      additionalProperties: false
      type: object
      title: BlockDocumentFilterId
      description: Filter by `BlockDocument.id`.
    BlockDocumentFilterIsAnonymous:
      properties:
        eq_:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Eq
          description: Filter block documents for only those that are or are not anonymous.
      additionalProperties: false
      type: object
      title: BlockDocumentFilterIsAnonymous
      description: Filter by `BlockDocument.is_anonymous`.
    BlockDocumentFilterBlockTypeId:
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
      title: BlockDocumentFilterBlockTypeId
      description: Filter by `BlockDocument.block_type_id`.
    BlockDocumentFilterName:
      properties:
        any_:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Any
          description: A list of block names to include
        like_:
          anyOf:
            - type: string
            - type: 'null'
          title: Like
          description: >-
            A string to match block names against. This can include SQL wildcard
            characters like `%` and `_`.
          examples:
            - my-block%
      additionalProperties: false
      type: object
      title: BlockDocumentFilterName
      description: Filter by `BlockDocument.name`.
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