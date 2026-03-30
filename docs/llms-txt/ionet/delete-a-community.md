# Source: https://io.net/docs/reference/rag/graphs/communities/delete-a-community.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Community: Delete

> Permanently removes a specific community (cluster) from the graph.



## OpenAPI

````yaml openapi/rag-graphs-communities/delete-a-community.json delete /api/r2r/v3/graphs/{collection_id}/communities/{community_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/graphs/{collection_id}/communities/{community_id}:
    delete:
      summary: 'Community: Delete'
      description: Permanently removes a specific community (cluster) from the graph.
      operationId: delete-a-community
      parameters:
        - name: collection_id
          in: path
          description: ID of the collection
          schema:
            type: string
          required: true
        - name: community_id
          in: path
          description: ID of the community to delete
          schema:
            type: string
          required: true
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      success: true
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      success:
                        type: boolean
                        example: true
                        default: true
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