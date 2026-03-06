# Source: https://io.net/docs/reference/rag/collections/list-collections.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List collections

> Returns a paginated list of collections the authenticated user has access to.

Results can be filtered by providing specific collection IDs. Regular users will only see collections they own or have access to. Superusers can see all collections. The collections are returned in order of last modification, with most recent first.


## OpenAPI

````yaml openapi/rag-collections/list-collections.json get /api/r2r/v3/collections
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
    get:
      summary: List collections
      description: >-
        Returns a paginated list of collections the authenticated user has
        access to.
      operationId: list-collections
      parameters:
        - name: ids
          in: query
          description: >-
            A list of collection IDs to retrieve. If not provided, all
            collections will be returned.
          schema:
            type: string
        - name: offset
          in: query
          description: Specifies the number of objects to skip. Defaults to 0. м
          schema:
            type: integer
            format: int32
            default: 0
        - name: limit
          in: query
          description: >-
            Specifies a limit on the number of objects to return, ranging
            between 1 and 100. Defaults to 100. >=1 <=1000
          schema:
            type: integer
            format: int32
            default: 100
        - name: owner_only
          in: query
          description: >-
            If true, only returns collections owned by the user, not all
            accessible collections.
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      - id: id
                        name: name
                        graph_cluster_status: graph_cluster_status
                        graph_sync_status: graph_sync_status
                        created_at: '2024-01-15T09:30:00Z'
                        updated_at: '2024-01-15T09:30:00Z'
                        user_count: 1
                        document_count: 1
                        owner_id: owner_id
                        description: description
                    total_entries: 1
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
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
                  total_entries:
                    type: integer
                    example: 1
                    default: 0
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