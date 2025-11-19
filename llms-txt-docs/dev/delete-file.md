# Source: https://dev.writer.com/api-reference/file-api/delete-file.md

# Delete file

> Permanently delete a file from the system. This action cannot be undone.

## OpenAPI

````yaml delete /v1/files/{file_id}
paths:
  path: /v1/files/{file_id}
  method: delete
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
          curl --location --request DELETE
          https://api.writer.com/v1/files/{file_id} \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const file = await client.files.delete('file_id');

            console.log(file.id);
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
          file = client.files.delete(
              "file_id",
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
                    description: A unique identifier of the deleted file.
              deleted:
                allOf:
                  - type: boolean
                    description: Indicates whether the file was successfully deleted.
            title: delete_file_response
            refIdentifier: '#/components/schemas/delete_file_response'
            requiredProperties:
              - id
              - deleted
        examples:
          example:
            value:
              id: 7c36a365-392f-43ba-840d-8f3103b42572
              deleted: true
        description: ''
  deprecated: false
  type: path
components:
  schemas: {}

````