# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-schemas/delete-block-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Block Schema

> Delete a block schema by id.



## OpenAPI

````yaml delete /block_schemas/{id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_schemas/{id}:
    delete:
      tags:
        - Block schemas
      summary: Delete Block Schema
      description: Delete a block schema by id.
      operationId: delete_block_schema_block_schemas__id__delete
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The block schema id
            title: Id
          description: The block schema id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
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