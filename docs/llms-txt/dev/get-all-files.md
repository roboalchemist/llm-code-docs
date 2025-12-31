# Source: https://dev.writer.com/api-reference/file-api/get-all-files.md

# List files

> Retrieve a paginated list of files with optional filtering by status, graph association, and file type.

## OpenAPI

````yaml get /v1/files
paths:
  path: /v1/files
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
      path: {}
      query:
        before:
          schema:
            - type: string
              required: false
              description: >-
                The ID of the first object in the previous page. This parameter
                instructs the API to return the previous page of results.
        after:
          schema:
            - type: string
              required: false
              description: >-
                The ID of the last object in the previous page. This parameter
                instructs the API to return the next page of results.
        limit:
          schema:
            - type: integer
              required: false
              description: >-
                Specifies the maximum number of objects returned in a page. The
                default value is 50. The minimum value is 1, and the maximum
                value is 100.
              default: 50
        order:
          schema:
            - type: enum<string>
              enum:
                - asc
                - desc
              required: false
              description: >-
                Specifies the order of the results. Valid values are asc for
                ascending and desc for descending.
              default: desc
        graph_id:
          schema:
            - type: string
              required: false
              description: The unique identifier of the graph to which the files belong.
              format: uuid
        status:
          schema:
            - type: enum<string>
              enum:
                - in_progress
                - completed
                - failed
              required: false
              description: >-
                Specifies the status of the files to retrieve. Valid values are
                in_progress, completed or failed.
        file_types:
          schema:
            - type: string
              required: false
              description: >-
                The extensions of the files to retrieve. Separate multiple
                extensions with a comma. For example: `pdf,jpg,docx`.
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: |-
          curl --location --request GET https://api.writer.com/v1/files \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            // Automatically fetches more pages as needed.
            for await (const file of client.files.list()) {
              console.log(file.id);
            }
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
          page = client.files.list()
          page = page.data[0]
          print(page.id)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/file_response'
              has_more:
                allOf:
                  - type: boolean
                    description: >-
                      Indicates if there are more files available beyond the
                      current page.
              first_id:
                allOf:
                  - type: string
                    description: The ID of the first file in the current response.
              last_id:
                allOf:
                  - type: string
                    description: The ID of the last file in the current response.
            title: files_response
            refIdentifier: '#/components/schemas/files_response'
            requiredProperties:
              - data
              - has_more
        examples:
          example:
            value:
              data:
                - id: 7c36a365-392f-43ba-840d-8f3103b42572
                  name: example.pdf
                  created_at: '2024-07-10T12:00:00Z'
                  graph_ids:
                    - 31a8b75a-9a90-432f-8861-942229125333
                  status: in_progress
                - id: 4bbe6207-737e-486f-a287-c5e95536984a
                  name: image.jpg
                  created_at: '2024-07-09T15:30:00Z'
                  graph_ids:
                    - 31a8b75a-9a90-432f-8861-942229125333
                  status: completed
                - id: efc86bb4-30a4-40c9-a52a-ecee0d7e071f
                  name: document.txt
                  created_at: '2024-07-08T16:00:00Z'
                  graph_ids:
                    - 31a8b75a-9a90-432f-8861-942229125333
                  status: failed
              has_more: false
              first_id: 7c36a365-392f-43ba-840d-8f3103b42572
              last_id: efc86bb4-30a4-40c9-a52a-ecee0d7e071f
        description: ''
  deprecated: false
  type: path
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
          description: A list of Knowledge Graph IDs that the file is associated with.
        status:
          type: string
          description: The processing status of the file.

````