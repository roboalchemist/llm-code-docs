# Source: https://dev.writer.com/api-reference/application-api/put-application-graphs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Associate graphs

> Updates the list of Knowledge Graphs associated with a no-code chat agent.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml put /v1/applications/{application_id}/graphs
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/applications/{application_id}/graphs:
    put:
      tags:
        - template
      summary: Associate graphs
      description: >-
        Updates the list of Knowledge Graphs associated with a no-code chat
        agent.
      parameters:
        - name: application_id
          in: path
          description: >-
            The ID of the no-code agent to update.


            Only no-code agents with chat capabilities can have associated
            Knowledge Graphs. No-code agents with text generation and research
            capabilities do not support Knowledge Graphs.
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/application_graph_ids_request'
        required: true
      responses:
        '200':
          description: Successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/application_graphs_response'
      security:
        - bearerAuth: []
components:
  schemas:
    application_graph_ids_request:
      title: application_graph_ids_request
      required:
        - graph_ids
      type: object
      properties:
        graph_ids:
          type: array
          description: >-
            A list of Knowledge Graph IDs to associate with the application.
            Note that this will replace the existing list of Knowledge Graphs
            associated with the application, not add to it.
          items:
            type: string
            format: uuid
    application_graphs_response:
      title: application_graphs_response
      required:
        - graph_ids
      type: object
      properties:
        graph_ids:
          type: array
          description: A list of Knowledge Graphs associated with the application.
          items:
            type: string
            format: uuid
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