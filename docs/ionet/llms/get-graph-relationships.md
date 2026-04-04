# Source: https://io.net/docs/reference/rag/graphs/relationships/get-graph-relationships.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Relationships

> Lists all relationships in the graph with pagination support.



## OpenAPI

````yaml openapi/rag-graphs-relationships/get-graph-relationships.json get /api/r2r/v3/graphs/{collection_id}/relationships
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/graphs/{collection_id}/relationships:
    get:
      summary: Get Relationships
      description: Lists all relationships in the graph with pagination support.
      operationId: get-graph-relationships
      parameters:
        - name: collection_id
          in: path
          description: Collection ID
          schema:
            type: string
          required: true
        - name: offset
          in: query
          description: Specifies the number of objects to skip. Defaults to 0. >=0
          schema:
            type: string
            default: '0'
        - name: limit
          in: query
          description: >-
            Specifies a limit on the number of objects to return, ranging
            between 1 and 100. Defaults to 100. >=1 <=1000
          schema:
            type: string
            default: '100'
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      - subject: subject
                        predicate: predicate
                        object: object
                        id: id
                        description: description
                        subject_id: subject_id
                        object_id: object_id
                        weight: 1.1
                        chunk_ids:
                          - chunk_ids
                        parent_id: parent_id
                        description_embedding:
                          - 1.1
                        metadata:
                          key: value
                    total_entries: 1
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        subject:
                          type: string
                          example: subject
                        predicate:
                          type: string
                          example: predicate
                        object:
                          type: string
                          example: object
                        id:
                          type: string
                          example: id
                        description:
                          type: string
                          example: description
                        subject_id:
                          type: string
                          example: subject_id
                        object_id:
                          type: string
                          example: object_id
                        weight:
                          type: number
                          example: 1.1
                          default: 0
                        chunk_ids:
                          type: array
                          items:
                            type: string
                            example: chunk_ids
                        parent_id:
                          type: string
                          example: parent_id
                        description_embedding:
                          type: array
                          items:
                            type: number
                            example: 1.1
                            default: 0
                        metadata:
                          type: object
                          properties:
                            key:
                              type: string
                              example: value
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