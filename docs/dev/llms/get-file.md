# Source: https://dev.writer.com/api-reference/file-api/get-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve file

> Retrieve detailed information about a specific file, including its metadata, status, and associated graphs.



## OpenAPI

````yaml get /v1/files/{file_id}
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
    get:
      tags:
        - File API
      summary: Retrieve file
      description: >-
        Retrieve detailed information about a specific file, including its
        metadata, status, and associated graphs.
      operationId: gatewayGetFile
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
                $ref: '#/components/schemas/file_response'
              example:
                id: 7c36a365-392f-43ba-840d-8f3103b42572
                created_at: '2024-07-10T13:34:28.301201Z'
                name: example.pdf
                graph_ids:
                  - 704ffd94-de04-4de2-9f8b-f9fc04831edd
                status: completed
      security:
        - bearerAuth: []
components:
  schemas:
    file_response:
      title: file_response
      required:
        - id
        - created_at
        - name
        - graph_ids
        - status
      type: object
      properties:
        id:
          type: string
          description: A unique identifier of the file.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the file was uploaded.
        name:
          type: string
          description: The name of the file.
        graph_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            A list of Knowledge Graph IDs that the file is associated with.


            If you provided a `graphId` during upload, the file is associated
            with that Knowledge Graph. However, the `graph_ids` field in the
            upload response is an empty list. The association will be visible in
            the `graph_ids` list when you retrieve the file using the file
            retrieval endpoint.
        status:
          type: string
          description: The processing status of the file.
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