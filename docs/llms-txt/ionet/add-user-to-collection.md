# Source: https://io.net/docs/reference/rag/collections/add-user-to-collection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add user to collection

> This endpoint grants a user access to a specific collection.

The authenticated user must have admin permissions for the collection to add new users.


## OpenAPI

````yaml openapi/rag-collections/add-user-to-collection.json post /api/r2r/v3/collections/{id}/users/{user_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/collections/{id}/users/{user_id}:
    post:
      summary: Add user to collection
      description: This endpoint grants a user access to a specific collection.
      operationId: add-user-to-collection
      parameters:
        - name: id
          in: path
          description: The unique identifier of the collection
          schema:
            type: string
          required: true
        - name: user_id
          in: path
          description: The unique identifier of the user to add
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