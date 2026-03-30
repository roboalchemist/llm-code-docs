# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-documents/create-block-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Block Document

> Create a new block document.

For more information, see https://docs.prefect.io/v3/concepts/blocks.



## OpenAPI

````yaml post /block_documents/
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_documents/:
    post:
      tags:
        - Block documents
      summary: Create Block Document
      description: |-
        Create a new block document.

        For more information, see https://docs.prefect.io/v3/concepts/blocks.
      operationId: create_block_document_block_documents__post
      parameters:
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BlockDocumentCreate'
      responses:
        '201':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BlockDocument'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    BlockDocumentCreate:
      properties:
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
        block_type_id:
          type: string
          format: uuid
          title: Block Type Id
          description: A block type ID
        is_anonymous:
          type: boolean
          title: Is Anonymous
          description: >-
            Whether the block is anonymous (anonymous blocks are usually created
            by Prefect automatically)
          default: false
      additionalProperties: false
      type: object
      required:
        - block_schema_id
        - block_type_id
      title: BlockDocumentCreate
      description: Data used by the Prefect REST API to create a block document.
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

````

Built with [Mintlify](https://mintlify.com).