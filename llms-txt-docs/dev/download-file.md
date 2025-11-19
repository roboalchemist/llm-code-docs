# Source: https://dev.writer.com/api-reference/file-api/download-file.md

# Download file

> Download the binary content of a file. The response will contain the file data in the appropriate MIME type.

## OpenAPI

````yaml get /v1/files/{file_id}/download
paths:
  path: /v1/files/{file_id}/download
  method: get
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
      path:
        file_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the file.
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request GET
          https://api.writer.com/v1/files/{file_id}/download \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const response = await client.files.download('file_id');

            console.log(response);

            const content = await response.blob();
            console.log(content);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          response = client.files.download(
              "file_id",
          )
          print(response)
          content = response.read()
          print(content)
  response:
    '200':
      application/octet-stream:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          fileDownloadExample:
            summary: Example binary file download
            value: File contents
        description: File download successful
  deprecated: false
  type: path
components:
  schemas: {}

````