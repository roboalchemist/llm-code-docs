# Source: https://dev.writer.com/api-reference/file-api/delete-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete file

> Permanently delete a file from the system. This action cannot be undone.



## OpenAPI

````yaml delete /v1/files/{file_id}
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/files/{file_id}:
    delete:
      tags:
        - File API
      summary: Delete file
      description: Permanently delete a file from the system. This action cannot be undone.
      operationId: gatewayDeleteFile
      parameters:
        - name: file_id
          in: path
          required: true
          schema:
            type: string
          description: The unique identifier of the file.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/delete_file_response'
              example:
                id: 7c36a365-392f-43ba-840d-8f3103b42572
                deleted: true
      security:
        - bearerAuth: []
components:
  schemas:
    delete_file_response:
      title: delete_file_response
      required:
        - id
        - deleted
      type: object
      properties:
        id:
          type: string
          description: A unique identifier of the deleted file.
        deleted:
          type: boolean
          description: Indicates whether the file was successfully deleted.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````