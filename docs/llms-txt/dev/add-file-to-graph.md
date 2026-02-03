# Source: https://dev.writer.com/api-reference/kg-api/add-file-to-graph.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add file to graph

> Add a file to a Knowledge Graph.



## OpenAPI

````yaml post /v1/graphs/{graph_id}/file
openapi: 3.0.3
info:
  title: API
  version: '1.0'
servers:
  - url: https://api.writer.com
security:
  - bearerAuth: []
paths:
  /v1/graphs/{graph_id}/file:
    post:
      tags:
        - KG API
      summary: Add file to graph
      description: Add a file to a Knowledge Graph.
      operationId: addFileToGraph
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
              $ref: '#/components/schemas/graph_file_request'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/file_response'
              example:
                id: 7c36a365-392f-43ba-840d-8f3103b42572
                created_at: '2024-07-10T15:16:10.684826Z'
                name: example.pdf
                graph_id:
                  - 50daa3d0-e7d9-44a4-be42-b53e2379ebf7
      security:
        - bearerAuth: []
components:
  schemas:
    graph_file_request:
      title: graph_file_request
      required:
        - file_id
      type: object
      properties:
        file_id:
          type: string
          description: The unique identifier of the file.
    file_response:
      title: file_response
      required:
        - id
        - created_at
        - name
        - graph_ids
        - status
      type: object
      properties:
        id:
          type: string
          description: A unique identifier of the file.
        created_at:
          type: string
          format: date-time
          description: The timestamp when the file was uploaded.
        name:
          type: string
          description: The name of the file.
        graph_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            A list of Knowledge Graph IDs that the file is associated with.


            If you provided a `graphId` during upload, the file is associated
            with that Knowledge Graph. However, the `graph_ids` field in the
            upload response is an empty list. The association will be visible in
            the `graph_ids` list when you retrieve the file using the file
            retrieval endpoint.
        status:
          type: string
          description: The processing status of the file.
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