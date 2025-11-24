# Source: https://dev.writer.com/api-reference/kg-api/retrieve-graph.md

# Retrieve graph

> Retrieve a Knowledge Graph.

## OpenAPI

````yaml get /v1/graphs/{graph_id}
paths:
  path: /v1/graphs/{graph_id}
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
          curl --location --request GET
          https://api.writer.com/v1/graphs/{graph_id} \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const graph = await client.graphs.retrieve('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e');

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
          graph = client.graphs.retrieve(
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
                    description: The unique identifier of the Knowledge Graph.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the Knowledge Graph was created.
              name:
                allOf:
                  - type: string
                    description: The name of the Knowledge Graph.
              description:
                allOf:
                  - type: string
                    description: A description of the Knowledge Graph.
              file_status:
                allOf:
                  - $ref: '#/components/schemas/graph_file_status'
                    description: The processing status of files in the Knowledge Graph.
              type:
                allOf:
                  - $ref: '#/components/schemas/graph_type'
                    description: >-
                      The type of Knowledge Graph.


                      - `manual`: files are uploaded via UI or API

                      - `connector`: files are uploaded via a data connector
                      such as Google Drive or Confluence

                      - `web`: URLs are connected to the Knowledge Graph
              urls:
                allOf:
                  - type: array
                    description: >-
                      An array of web connector URLs associated with this
                      Knowledge Graph.
                    items:
                      $ref: '#/components/schemas/web_connector_url'
            title: graph
            refIdentifier: '#/components/schemas/graph'
            requiredProperties:
              - id
              - created_at
              - name
              - file_status
              - type
        examples:
          example:
            value:
              id: 50daa3d0-e7d9-44a4-be42-b53e2379ebf7
              created_at: '2024-07-10T15:03:48.785843Z'
              name: Example Knowledge Graph
              description: Example description
              file_status:
                in_progress: 0
                completed: 0
                failed: 0
                total: 0
              type: web
              urls:
                - url: https://example.com/docs
                  status:
                    status: success
                    error_type: null
                  type: sub_pages
                - url: https://docs.example.com
                  status:
                    status: error
                    error_type: invalid_url
                  type: single_page
        description: ''
  deprecated: false
  type: path
components:
  schemas:
    graph_type:
      title: graph_type
      description: >-
        The type of Knowledge Graph:


        - `manual`: files are uploaded via UI or API

        - `connector`: files are uploaded via a data connector such as Google
        Drive or Confluence

        - `web`: URLs are connected to the Knowledge Graph
      type: string
      enum:
        - manual
        - connector
        - web
    graph_file_status:
      title: graph_file_status
      required:
        - in_progress
        - completed
        - failed
        - total
      type: object
      properties:
        in_progress:
          type: integer
          format: int64
          description: The number of files currently being processed.
        completed:
          type: integer
          format: int64
          description: The number of files that have been successfully processed.
        failed:
          type: integer
          format: int64
          description: The number of files that failed to process.
        total:
          type: integer
          format: int64
          description: The total number of files associated with the Knowledge Graph.
    web_connector_url:
      title: web_connector_url
      required:
        - url
        - status
        - type
      type: object
      properties:
        url:
          type: string
          description: The URL to be processed by the web connector.
        status:
          $ref: '#/components/schemas/web_connector_url_state'
          description: The current status of the URL processing.
        exclude_urls:
          type: array
          description: >-
            An array of URLs to exclude from processing within this web
            connector.
          items:
            type: string
        type:
          $ref: '#/components/schemas/web_connector_url_type'
          description: The type of web connector processing for this URL.
    web_connector_url_state:
      title: web_connector_url_state
      description: The state of a web connector URL processing.
      required:
        - status
      type: object
      properties:
        status:
          $ref: '#/components/schemas/web_connector_url_status'
          description: The current status of the URL processing.
        error_type:
          $ref: '#/components/schemas/web_connector_url_error_type'
          description: The type of error that occurred during processing, if any.
    web_connector_url_type:
      title: web_connector_url_type
      description: The type of web connector processing for a URL.
      type: string
      enum:
        - single_page
        - sub_pages
    web_connector_url_error_type:
      title: web_connector_url_error_type
      description: The type of error that can occur during web connector URL processing.
      type: string
      enum:
        - invalid_url
        - not_searchable
        - not_found
        - paywall_or_login_page
        - unexpected_error
    web_connector_url_status:
      title: web_connector_url_status
      description: The status of web connector URL processing.
      type: string
      enum:
        - validating
        - success
        - error

````