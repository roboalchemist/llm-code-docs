# Source: https://docs.unstructured.io/api-reference/sources/delete-source-connector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete source connector

> Delete a specific source connector identified by its ID.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json delete /api/v1/sources/{source_id}
openapi: 3.1.0
info:
  title: Platform API
  version: 3.1.0
servers:
  - url: https://platform.unstructuredapp.io/
    description: Unstructured Platform API
    x-speakeasy-server-id: platform-api
security: []
paths:
  /api/v1/sources/{source_id}:
    delete:
      tags:
        - sources
      summary: Delete source connector
      description: Delete a specific source connector identified by its ID.
      operationId: delete_source
      parameters:
        - name: source_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Source Id
        - name: unstructured-api-key
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Unstructured-Api-Key
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
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
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````