# Source: https://dev.writer.com/api-reference/kg-api/delete-graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete graph

> Delete a Knowledge Graph.



## OpenAPI

````yaml delete /v1/graphs/{graph_id}
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
    delete:
      tags:
        - KG API
      summary: Delete graph
      description: Delete a Knowledge Graph.
      operationId: deleteGraph
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
                $ref: '#/components/schemas/delete_graph_response'
              example:
                id: e7392337-1c4e-4bc9-aaf5-b719bf1e938a
                deleted: true
      security:
        - bearerAuth: []
components:
  schemas:
    delete_graph_response:
      title: delete_graph_response
      required:
        - id
        - deleted
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: A unique identifier of the deleted Knowledge Graph.
        deleted:
          type: boolean
          description: Indicates whether the Knowledge Graph was successfully deleted.
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