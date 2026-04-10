# Source: https://dev.writer.com/api-reference/file-api/download-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Download file

> Download the binary content of a file. The response will contain the file data in the appropriate MIME type.



## OpenAPI

````yaml get /v1/files/{file_id}/download
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/files/{file_id}/download:
    get:
      tags:
        - File API
      summary: Download file
      description: >-
        Download the binary content of a file. The response will contain the
        file data in the appropriate MIME type.
      operationId: gatewayDownloadFile
      parameters:
        - name: file_id
          in: path
          required: true
          schema:
            type: string
          description: The unique identifier of the file.
      responses:
        '200':
          description: File download successful
          headers:
            Content-Type:
              description: The MIME type of the file being downloaded
              required: true
              schema:
                type: object
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
              examples:
                fileDownloadExample:
                  summary: Example binary file download
                  value: File contents
      security:
        - bearerAuth: []
components:
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