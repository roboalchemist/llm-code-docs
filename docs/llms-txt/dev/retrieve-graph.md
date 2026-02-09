# Source: https://dev.writer.com/api-reference/kg-api/retrieve-graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve graph

> Retrieve a Knowledge Graph.



## OpenAPI

````yaml get /v1/graphs/{graph_id}
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/graphs/{graph_id}:
    get:
      tags:
        - KG API
      summary: Retrieve graph
      description: Retrieve a Knowledge Graph.
      operationId: findGraphWithFileStatus
      parameters:
        - name: graph_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
          description: The unique identifier of the Knowledge Graph.
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/graph'
              example:
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
      security:
        - bearerAuth: []
components:
  schemas:
    graph:
      title: graph
      required:
        - id
        - created_at
        - name
        - file_status
        - type
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: The unique identifier of the Knowledge Graph.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the Knowledge Graph was created.
        name:
          type: string
          description: The name of the Knowledge Graph.
        description:
          type: string
          description: A description of the Knowledge Graph.
        file_status:
          $ref: '#/components/schemas/graph_file_status'
          description: The processing status of files in the Knowledge Graph.
        type:
          $ref: '#/components/schemas/graph_type'
          description: >-
            The type of Knowledge Graph.


            - `manual`: files are uploaded via UI or API

            - `connector`: files are uploaded via a data connector such as
            Google Drive or Confluence

            - `web`: URLs are connected to the Knowledge Graph
        urls:
          type: array
          description: An array of web connector URLs associated with this Knowledge Graph.
          items:
            $ref: '#/components/schemas/web_connector_url'
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
    web_connector_url_status:
      title: web_connector_url_status
      description: The status of web connector URL processing.
      type: string
      enum:
        - validating
        - success
        - error
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: >-
        Bearer authentication header of the form `Bearer <token>`, where
        `<token>` is your [Writer API
        key](https://dev.writer.com/api-reference/api-keys).

````