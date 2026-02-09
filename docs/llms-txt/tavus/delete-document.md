# Source: https://docs.tavus.io/api-reference/documents/delete-document.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Document

> Delete a specific document

Delete a document and its associated data using its unique identifier.


## OpenAPI

````yaml delete /v2/documents/{document_id}
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/documents/{document_id}:
    delete:
      tags:
        - Documents
      summary: Delete Document
      description: |
        Delete a document and its associated data using its unique identifier.
      operationId: deleteDocument
      parameters:
        - in: path
          name: document_id
          required: true
          schema:
            type: string
          description: The unique identifier of the document to delete
      responses:
        '204':
          description: NO CONTENT - Document deleted successfully
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message
                    example: Invalid access token
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message
                    example: Document not found
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````