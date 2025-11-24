# Source: https://dev.writer.com/api-reference/file-api/upload-files.md

# Upload file

> Upload a new file to the system. Supports various file formats including PDF, DOC, DOCX, PPT, PPTX, JPG, PNG, EML, HTML, SRT, CSV, XLS, and XLSX.

## OpenAPI

````yaml post /v1/files
paths:
  path: /v1/files
  method: post
  servers:
    - url: https://api.writer.com
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
          cookie: {}
    parameters:
      path: {}
      query: {}
      header:
        Content-Disposition:
          schema:
            - type: string
              required: true
              description: >-
                The disposition type of the file, typically used to indicate the
                form-data name. Use `attachment` with the filename parameter to
                specify the name of the file, for example: `attachment;
                filename=example.pdf`.
        Content-Type:
          schema:
            - type: string
              required: true
              description: >-
                The [MIME
                type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)
                of the file being uploaded. Supports `txt`, `doc`, `docx`,
                `ppt`, `pptx`, `jpg`, `png`, `eml`, `html`, `pdf`, `srt`, `csv`,
                `xls`, `xlsx`, `mp3`, and `mp4` file extensions.
        Content-Length:
          schema:
            - type: integer
              required: true
              description: The size of the file in bytes.
      cookie: {}
    body:
      text/plain:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/msword:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/vnd.openxmlformats-officedocument.wordprocessingml.document:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/vnd.ms-powerpoint:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/vnd.openxmlformats-officedocument.presentationml.presentation:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      image/jpeg:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      image/png:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      message/rfc822:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      text/html:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/pdf:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/x-subrip:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      text/csv:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/vnd.ms-excel:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
      application/vnd.openxmlformats-officedocument.spreadsheetml.sheet:
        schemaArray:
          - type: file
            contentEncoding: binary
            required: true
        examples:
          example: {}
    codeSamples:
      - lang: cURL
        source: |-
          curl --location --request POST https://api.writer.com/v1/files \
           --header "Authorization: Bearer <token>"
           --header "Accept: */*" \
           --header "Content-Disposition: attachment; filename=descriptions.pdf" \
           --header "Content-Length: size_in_bytes" \
           --header "Content-Type: application/pdf" \
           --data-binary "@descriptions.pdf"
      - lang: JavaScript
        source: |-
          import fs from 'fs';
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const file = await client.files.upload({
              content: fs.createReadStream('path/to/file/descriptions.pdf'),
              'Content-Disposition': 'attachment; filename=descriptions.pdf',
              'Content-Type': 'application/pdf',
            });

            console.log(file.id);
          }

          main();
      - lang: Python
        source: |-
          import os
          from pathlib import Path
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          file = client.files.upload(
              content=Path('/path/to/file/descriptions.pdf'),
              content_disposition="attachment; filename=descriptions.pdf",
              content_type="application/pdf"
          )
          print(file.id)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    description: A unique identifier of the file.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the file was uploaded.
              name:
                allOf:
                  - type: string
                    description: The name of the file.
              graph_ids:
                allOf:
                  - type: array
                    items:
                      type: string
                      format: uuid
                    description: >-
                      A list of Knowledge Graph IDs that the file is associated
                      with.
              status:
                allOf:
                  - type: string
                    description: The processing status of the file.
            title: file_response
            refIdentifier: '#/components/schemas/file_response'
            requiredProperties:
              - id
              - created_at
              - name
              - graph_ids
              - status
        examples:
          example:
            value:
              id: 7c36a365-392f-43ba-840d-8f3103b42572
              name: example.pdf
              created_at: '2024-07-10T14:30:00Z'
              graph_id: []
              status: in_progress
        description: ''
  deprecated: false
  type: path
components:
  schemas: {}

````