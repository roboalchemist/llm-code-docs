# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/block-documents/update-block-document-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Block Document Data



## OpenAPI

````yaml patch /block_documents/{id}
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /block_documents/{id}:
    patch:
      tags:
        - Block documents
      summary: Update Block Document Data
      operationId: update_block_document_data_block_documents__id__patch
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The block document id
            title: Id
          description: The block document id
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
              $ref: '#/components/schemas/BlockDocumentUpdate'
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
    BlockDocumentUpdate:
      properties:
        block_schema_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Block Schema Id
          description: A block schema ID
        data:
          additionalProperties: true
          type: object
          title: Data
          description: The block document's data
        merge_existing_data:
          type: boolean
          title: Merge Existing Data
          default: true
      additionalProperties: false
      type: object
      title: BlockDocumentUpdate
      description: Data used by the Prefect REST API to update a block document.
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