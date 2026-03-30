# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-types/update-block-type.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Block Type

> Update a block type.



## OpenAPI

````yaml patch /block_types/{id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_types/{id}:
    patch:
      tags:
        - Block types
      summary: Update Block Type
      description: Update a block type.
      operationId: update_block_type_block_types__id__patch
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The block type ID
            title: Id
          description: The block type ID
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
              $ref: '#/components/schemas/BlockTypeUpdate'
      responses:
        '204':
          description: Successful Response
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    BlockTypeUpdate:
      properties:
        logo_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Logo Url
        documentation_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Documentation Url
        description:
          anyOf:
            - type: string
            - type: 'null'
          title: Description
        code_example:
          anyOf:
            - type: string
            - type: 'null'
          title: Code Example
      additionalProperties: false
      type: object
      title: BlockTypeUpdate
      description: Data used by the Prefect REST API to update a block type.
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