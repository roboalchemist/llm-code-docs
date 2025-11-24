# Source: https://dev.writer.com/api-reference/kg-api/add-file-to-graph.md

# Add file to graph

> Add a file to a Knowledge Graph.

## OpenAPI

````yaml post /v1/graphs/{graph_id}/file
paths:
  path: /v1/graphs/{graph_id}/file
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
      path:
        graph_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the Knowledge Graph.
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              file_id:
                allOf:
                  - type: string
                    description: The unique identifier of the file.
            required: true
            title: graph_file_request
            refIdentifier: '#/components/schemas/graph_file_request'
            requiredProperties:
              - file_id
        examples:
          example:
            value:
              file_id: <string>
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request POST
          https://api.writer.com/v1/graphs/{graph_id}/file \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"file_id":"string"}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const file = await client.graphs.addFileToGraph('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', {
              file_id: 'file_id',
            });

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
          file = client.graphs.add_file_to_graph(
              graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              file_id="file_id",
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
              created_at: '2024-07-10T15:16:10.684826Z'
              name: example.pdf
              graph_id:
                - 50daa3d0-e7d9-44a4-be42-b53e2379ebf7
        description: ''
  deprecated: false
  type: path
components:
  schemas: {}

````