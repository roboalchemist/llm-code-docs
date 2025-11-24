# Source: https://dev.writer.com/api-reference/kg-api/update-graph.md

# Update graph

> Update the name and description of a Knowledge Graph.

## OpenAPI

````yaml put /v1/graphs/{graph_id}
paths:
  path: /v1/graphs/{graph_id}
  method: put
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
              urls:
                allOf:
                  - type: array
                    description: >-
                      An array of web connector URLs to update for this
                      Knowledge Graph. You can only connect URLs to Knowledge
                      Graphs with the type `web`. To clear the list of URLs, set
                      this field to an empty array.
                    items:
                      $ref: '#/components/schemas/update_graph_web_url'
            required: true
            title: update_graph_request
            refIdentifier: '#/components/schemas/update_graph_request'
        examples:
          example:
            value:
              name: <string>
              description: <string>
              urls:
                - url: <string>
                  exclude_urls:
                    - <string>
                  type: single_page
    codeSamples:
      - lang: cURL
        source: >-
          curl --location --request PUT
          https://api.writer.com/v1/graphs/{graph_id} \
           --header "Authorization: Bearer <token>" \
           --header "Content-Type: application/json" \
          --data-raw '{"name":"string", "description":"string",
          "urls":[{"url":"https://example.com/docs", "type":"sub_pages",
          "exclude_urls":["https://example.com/docs/private"]}]}'
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const graph = await client.graphs.update('182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e', 
              { name: 'name', description: 'description' }
            );

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
          graph = client.graphs.update(
              graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
              name="name",
              description="description",
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
              created_at: '2024-07-10T15:03:48.785843Z'
              name: Updated graph name
              description: Updated graph description
              urls:
                - url: https://example.com/docs
                  status:
                    status: success
                    error_type: null
                  type: sub_pages
        description: ''
  deprecated: false
  type: path
components:
  schemas:
    update_graph_web_url:
      title: update_graph_web_url
      required:
        - url
        - type
      type: object
      properties:
        url:
          type: string
          description: The URL to be processed by the web connector.
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