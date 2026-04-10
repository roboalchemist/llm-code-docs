# Source: https://dev.writer.com/api-reference/file-api/upload-files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload file

> Upload a new file to the system. Supports various file formats including PDF, DOC, DOCX, PPT, PPTX, JPG, PNG, EML, HTML, SRT, CSV, XLS, and XLSX.



## OpenAPI

````yaml post /v1/files
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/files:
    post:
      tags:
        - File API
      summary: Upload file
      description: >-
        Upload a new file to the system. Supports various file formats including
        PDF, DOC, DOCX, PPT, PPTX, JPG, PNG, EML, HTML, SRT, CSV, XLS, and XLSX.
      operationId: gatewayUploadFile
      parameters:
        - name: Content-Disposition
          in: header
          required: true
          schema:
            type: string
          description: >-
            The disposition type of the file, typically used to indicate the
            form-data name. Use `attachment` with the filename parameter to
            specify the name of the file, for example: `attachment;
            filename=example.pdf`.
        - name: Content-Type
          in: header
          required: true
          schema:
            type: string
          description: >-
            The [MIME
            type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)
            of the file being uploaded. Supports `txt`, `doc`, `docx`, `ppt`,
            `pptx`, `jpg`, `png`, `eml`, `html`, `pdf`, `srt`, `csv`, `xls`,
            `xlsx`, `mp3`, and `mp4` file extensions.
        - name: Content-Length
          in: header
          required: true
          schema:
            type: integer
            format: int64
          description: The size of the file in bytes.
        - name: graphId
          in: query
          required: false
          schema:
            type: string
            format: uuid
          description: >-
            The unique identifier of the Knowledge Graph to associate the
            uploaded file with.


            Note: The response from the upload endpoint does not include the
            `graphId` field, but the association will be visible when you
            retrieve the file using the file retrieval endpoint.
      requestBody:
        content:
          text/plain:
            schema:
              type: string
              format: binary
          application/msword:
            schema:
              type: string
              format: binary
          application/vnd.openxmlformats-officedocument.wordprocessingml.document:
            schema:
              type: string
              format: binary
          application/vnd.ms-powerpoint:
            schema:
              type: string
              format: binary
          application/vnd.openxmlformats-officedocument.presentationml.presentation:
            schema:
              type: string
              format: binary
          image/jpeg:
            schema:
              type: string
              format: binary
          image/png:
            schema:
              type: string
              format: binary
          message/rfc822:
            schema:
              type: string
              format: binary
          text/html:
            schema:
              type: string
              format: binary
          application/pdf:
            schema:
              type: string
              format: binary
          application/x-subrip:
            schema:
              type: string
              format: binary
          text/csv:
            schema:
              type: string
              format: binary
          application/vnd.ms-excel:
            schema:
              type: string
              format: binary
          application/vnd.openxmlformats-officedocument.spreadsheetml.sheet:
            schema:
              type: string
              format: binary
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/file_response'
              example:
                id: 7c36a365-392f-43ba-840d-8f3103b42572
                name: example.pdf
                created_at: '2024-07-10T14:30:00Z'
                graph_id: []
                status: in_progress
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