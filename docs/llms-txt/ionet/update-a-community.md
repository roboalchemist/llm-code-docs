# Source: https://io.net/docs/reference/rag/graphs/communities/update-a-community.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update community

> Updates an existing community in the graph.



## OpenAPI

````yaml openapi/rag-graphs-communities/update-a-community.json post /api/r2r/v3/graphs/{collection_id}/communities/{community_id}
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
    post:
      summary: Update community
      description: Updates an existing community in the graph.
      operationId: update-a-community
      parameters:
        - name: collection_id
          in: path
          description: ID of the collection
          schema:
            type: string
          required: true
        - name: community_id
          in: path
          description: ID of the community to update
          schema:
            type: string
          required: true
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: New name for the community
                summary:
                  type: string
                  description: Additional metadata
                findings:
                  type: string
                rating:
                  type: number
                  description: '>=1 <=10'
                  format: double
                rating_explanation:
                  type: string
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      name: name
                      summary: summary
                      level: 1
                      findings:
                        - findings
                      id: 1
                      community_id: community_id
                      collection_id: collection_id
                      rating: 1.1
                      rating_explanation: rating_explanation
                      description_embedding:
                        - 1.1
                      attributes:
                        key: value
                      created_at: '2024-01-15T09:30:00Z'
                      updated_at: '2024-01-15T09:30:00Z'
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      name:
                        type: string
                        example: name
                      summary:
                        type: string
                        example: summary
                      level:
                        type: integer
                        example: 1
                        default: 0
                      findings:
                        type: array
                        items:
                          type: string
                          example: findings
                      id:
                        type: integer
                        example: 1
                        default: 0
                      community_id:
                        type: string
                        example: community_id
                      collection_id:
                        type: string
                        example: collection_id
                      rating:
                        type: number
                        example: 1.1
                        default: 0
                      rating_explanation:
                        type: string
                        example: rating_explanation
                      description_embedding:
                        type: array
                        items:
                          type: number
                          example: 1.1
                          default: 0
                      attributes:
                        type: object
                        properties:
                          key:
                            type: string
                            example: value
                      created_at:
                        type: string
                        example: '2024-01-15T09:30:00Z'
                      updated_at:
                        type: string
                        example: '2024-01-15T09:30:00Z'
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