# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-documents/count-block-documents.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Count Block Documents

> Count block documents.



## OpenAPI

````yaml post /block_documents/count
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_documents/count:
    post:
      tags:
        - Block documents
      summary: Count Block Documents
      description: Count block documents.
      operationId: count_block_documents_block_documents_count_post
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
                #/components/schemas/Body_count_block_documents_block_documents_count_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: integer
                title: Response Count Block Documents Block Documents Count Post
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_count_block_documents_block_documents_count_post:
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
      type: object
      title: Body_count_block_documents_block_documents_count_post
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