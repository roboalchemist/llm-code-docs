# Source: https://dev.writer.com/api-reference/file-api/files-retry.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retry failed files

> Retry processing of files that previously failed to process. This will re-attempt the processing of the specified files.



## OpenAPI

````yaml post /v1/files/retry
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/files/retry:
    post:
      tags:
        - File API
      summary: Retry failed files
      description: >-
        Retry processing of files that previously failed to process. This will
        re-attempt the processing of the specified files.
      operationId: gatewayRetryFailedFiles
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/retry_files_request'
        required: true
      responses:
        '200':
          description: The retry request is being processed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/retry_files_response'
              example:
                success: true
      security:
        - bearerAuth: []
components:
  schemas:
    retry_files_request:
      title: retry_files_request
      required:
        - file_ids
      type: object
      properties:
        file_ids:
          type: array
          items:
            type: string
            format: uuid
          description: The unique identifier of the files to retry.
    retry_files_response:
      title: retry_files_response
      type: object
      properties:
        success:
          type: boolean
          description: Indicates whether the retry operation was successful.
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