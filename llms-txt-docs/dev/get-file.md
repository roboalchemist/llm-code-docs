# Source: https://dev.writer.com/api-reference/file-api/get-file.md

# Retrieve file

> Retrieve detailed information about a specific file, including its metadata, status, and associated graphs.

## OpenAPI

````yaml get /v1/files/{file_id}
paths:
  path: /v1/files/{file_id}
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
          https://api.writer.com/v1/files/{file_id} \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const file = await client.files.retrieve('file_id');

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
          file = client.files.retrieve(
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
              created_at: '2024-07-10T13:34:28.301201Z'
              name: example.pdf
              graph_ids:
                - 704ffd94-de04-4de2-9f8b-f9fc04831edd
              status: completed
        description: ''
  deprecated: false
  type: path
components:
  schemas: {}

````