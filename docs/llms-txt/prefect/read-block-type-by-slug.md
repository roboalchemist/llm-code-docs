# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-types/read-block-type-by-slug.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Read Block Type By Slug

> Get a block type by name.



## OpenAPI

````yaml get /block_types/slug/{slug}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_types/slug/{slug}:
    get:
      tags:
        - Block types
      summary: Read Block Type By Slug
      description: Get a block type by name.
      operationId: read_block_type_by_slug_block_types_slug__slug__get
      parameters:
        - name: slug
          in: path
          required: true
          schema:
            type: string
            description: The block type name
            title: Slug
          description: The block type name
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
                $ref: '#/components/schemas/BlockType'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
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