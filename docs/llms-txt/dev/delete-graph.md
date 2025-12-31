# Source: https://dev.writer.com/api-reference/kg-api/delete-graph.md

# Delete graph

> Delete a Knowledge Graph.

## OpenAPI

````yaml delete /v1/graphs/{graph_id}
paths:
  path: /v1/graphs/{graph_id}
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
        graph_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the Knowledge Graph.
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request DELETE
          https://api.writer.com/v1/graphs/{graph_id} \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const graph = await client.graphs.delete('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

            console.log(graph.id);
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
          graph = client.graphs.delete(
              "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
          )
          print(graph.id)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
                    description: A unique identifier of the deleted Knowledge Graph.
              deleted:
                allOf:
                  - type: boolean
                    description: >-
                      Indicates whether the Knowledge Graph was successfully
                      deleted.
            title: delete_graph_response
            refIdentifier: '#/components/schemas/delete_graph_response'
            requiredProperties:
              - id
              - deleted
        examples:
          example:
            value:
              id: e7392337-1c4e-4bc9-aaf5-b719bf1e938a
              deleted: true
        description: ''
  deprecated: false
  type: path
components:
  schemas: {}

````