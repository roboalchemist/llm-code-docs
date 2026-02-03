# Source: https://dev.writer.com/api-reference/kg-api/update-graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update graph

> Update the name and description of a Knowledge Graph.



## OpenAPI

````yaml put /v1/graphs/{graph_id}
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
    put:
      tags:
        - KG API
      summary: Update graph
      description: Update the name and description of a Knowledge Graph.
      operationId: updateGraph
      parameters:
        - name: graph_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
          description: The unique identifier of the Knowledge Graph.
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/update_graph_request'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/graph_response'
              example:
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
      security:
        - bearerAuth: []
components:
  schemas:
    update_graph_request:
      title: update_graph_request
      type: object
      properties:
        name:
          type: string
          description: >-
            The name of the Knowledge Graph (max 255 characters). Omitting this
            field leaves the name unchanged.
        description:
          type: string
          description: >-
            A description of the Knowledge Graph (max 255 characters). Omitting
            this field leaves the description unchanged.
        urls:
          type: array
          description: >-
            An array of web connector URLs to update for this Knowledge Graph.
            You can only connect URLs to Knowledge Graphs with the type `web`.
            To clear the list of URLs, set this field to an empty array.
          items:
            $ref: '#/components/schemas/update_graph_web_url'
    graph_response:
      title: graph_response
      required:
        - id
        - created_at
        - name
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: A unique identifier of the Knowledge Graph.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the Knowledge Graph was created.
        name:
          type: string
          description: The name of the Knowledge Graph (max 255 characters).
        description:
          type: string
          description: A description of the Knowledge Graph (max 255 characters).
        urls:
          type: array
          description: An array of web connector URLs associated with this Knowledge Graph.
          items:
            $ref: '#/components/schemas/web_connector_url'
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
    web_connector_url_type:
      title: web_connector_url_type
      description: The type of web connector processing for a URL.
      type: string
      enum:
        - single_page
        - sub_pages
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