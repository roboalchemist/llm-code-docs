# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-schemas/read-block-schema-by-checksum.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Block Schema By Checksum



## OpenAPI

````yaml get /block_schemas/checksum/{checksum}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_schemas/checksum/{checksum}:
    get:
      tags:
        - Block schemas
      summary: Read Block Schema By Checksum
      operationId: read_block_schema_by_checksum_block_schemas_checksum__checksum__get
      parameters:
        - name: checksum
          in: path
          required: true
          schema:
            type: string
            description: The block schema checksum
            title: Checksum
          description: The block schema checksum
        - name: version
          in: query
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            description: >-
              Version of block schema. If not provided the most recently created
              block schema with the matching checksum will be returned.
            title: Version
          description: >-
            Version of block schema. If not provided the most recently created
            block schema with the matching checksum will be returned.
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BlockSchema'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
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