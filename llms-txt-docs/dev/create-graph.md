# Source: https://dev.writer.com/api-reference/kg-api/create-graph.md

# Create graph

> Create a new Knowledge Graph.

## OpenAPI

````yaml post /v1/graphs
paths:
  path: /v1/graphs
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
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: >-
                      The name of the Knowledge Graph (max 255 characters).
                      Omitting this field leaves the name unchanged.
              description:
                allOf:
                  - type: string
                    description: >-
                      A description of the Knowledge Graph (max 255 characters).
                      Omitting this field leaves the description unchanged.
            required: true
            title: graph_request
            refIdentifier: '#/components/schemas/graph_request'
        examples:
          example:
            value:
              name: <string>
              description: <string>
    codeSamples:
      - lang: cURL
        source: |-
          curl --location --request POST https://api.writer.com/v1/graphs \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"name":"string"}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const graph = await client.graphs.create({ name: 'name' });

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
          graph = client.graphs.create(
              name="name",
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
                    description: A unique identifier of the Knowledge Graph.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the Knowledge Graph was created.
              name:
                allOf:
                  - type: string
                    description: The name of the Knowledge Graph (max 255 characters).
              description:
                allOf:
                  - type: string
                    description: A description of the Knowledge Graph (max 255 characters).
              urls:
                allOf:
                  - type: array
                    description: >-
                      An array of web connector URLs associated with this
                      Knowledge Graph.
                    items:
                      $ref: '#/components/schemas/web_connector_url'
            title: graph_response
            refIdentifier: '#/components/schemas/graph_response'
            requiredProperties:
              - id
              - created_at
              - name
        examples:
          example:
            value:
              id: 50daa3d0-e7d9-44a4-be42-b53e2379ebf7
              created_at: '2024-07-10T13:34:28.301201Z'
              name: Example Knowledge Graph
              description: Example description
              urls: null
        description: ''
  deprecated: false
  type: path
components:
  schemas:
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