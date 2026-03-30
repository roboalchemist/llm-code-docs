# Source: https://io.net/docs/reference/rag/collections/create-a-new-collection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new collection

> Create a new collection and automatically add the creating user to it.

This endpoint allows authenticated users to create a new collection with a specified name and optional description. The user creating the collection is automatically added as a member.


## OpenAPI

````yaml openapi/rag-collections/create-a-new-collection.json post /api/r2r/v3/collections
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/collections:
    post:
      summary: Create a new collection
      description: Create a new collection and automatically add the creating user to it.
      operationId: create-a-new-collection
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - name
              properties:
                name:
                  type: string
                  description: Collection name
                description:
                  type: string
                  description: An optional description of the collection
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      id: id
                      name: name
                      graph_cluster_status: graph_cluster_status
                      graph_sync_status: graph_sync_status
                      created_at: '2024-01-15T09:30:00Z'
                      updated_at: '2024-01-15T09:30:00Z'
                      user_count: 1
                      document_count: 1
                      owner_id: owner_id
                      description: description
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      id:
                        type: string
                        example: id
                      name:
                        type: string
                        example: name
                      graph_cluster_status:
                        type: string
                        example: graph_cluster_status
                      graph_sync_status:
                        type: string
                        example: graph_sync_status
                      created_at:
                        type: string
                        example: '2024-01-15T09:30:00Z'
                      updated_at:
                        type: string
                        example: '2024-01-15T09:30:00Z'
                      user_count:
                        type: integer
                        example: 1
                        default: 0
                      document_count:
                        type: integer
                        example: 1
                        default: 0
                      owner_id:
                        type: string
                        example: owner_id
                      description:
                        type: string
                        example: description
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '422':
          description: '422'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````