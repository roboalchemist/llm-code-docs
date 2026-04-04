# Source: https://io.net/docs/reference/rag/collections/get-collection-by-name.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get collection by name

> Retrieve a collection by its (owner_id, name) combination.

The authenticated user can only fetch collections they own, or, if superuser, from anyone.


## OpenAPI

````yaml openapi/rag-collections/get-collection-by-name.json get /api/r2r/v3/collections/name/{collection_name}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/collections/name/{collection_name}:
    get:
      summary: Get collection by name
      description: Retrieve a collection by its (owner_id, name) combination.
      operationId: get-collection-by-name
      parameters:
        - name: collection_name
          in: path
          description: The name of the collection
          schema:
            type: string
          required: true
        - name: owner_id
          in: query
          description: >-
            (Superuser only) Specify the owner_id to retrieve a collection by
            name
          schema:
            type: string
            default: 'format: "uuid"'
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