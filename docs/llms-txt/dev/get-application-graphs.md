# Source: https://dev.writer.com/api-reference/application-api/get-application-graphs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieve graphs

> Retrieve Knowledge Graphs associated with a no-code agent that has chat capabilities.

<Info>No-code applications are now called [no-code agents](/no-code/introduction). The [Applications API](api-reference/application-api/applications), which you can use to programmatically interact with no-code agents, still uses the term `application` to minimize breaking changes.</Info>


## OpenAPI

````yaml get /v1/applications/{application_id}/graphs
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
    get:
      tags:
        - template
      summary: Retrieve graphs
      description: >-
        Retrieve Knowledge Graphs associated with a no-code agent that has chat
        capabilities.
      parameters:
        - name: application_id
          in: path
          description: The ID of the no-code agent for which to retrieve Knowledge Graphs.
          required: true
          schema:
            type: string
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