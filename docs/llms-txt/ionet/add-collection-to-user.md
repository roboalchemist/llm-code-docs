# Source: https://io.net/docs/reference/rag/users/add-collection-to-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add user to collection

> Grants a user access to an existing collection.



## OpenAPI

````yaml openapi/rag-users/add-collection-to-user.json post /api/r2r/v3/users/{id}/collections/{collection_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/users/{id}/collections/{collection_id}:
    post:
      summary: Add user to collection
      description: Grants a user access to an existing collection.
      operationId: add-collection-to-user
      parameters:
        - name: id
          in: path
          description: User ID
          schema:
            type: string
          required: true
        - name: collection_id
          in: path
          description: ID of the collection to share
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