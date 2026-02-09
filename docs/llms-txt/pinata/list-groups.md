# Source: https://docs.pinata.cloud/api-reference/endpoint/list-groups.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinata.cloud/llms.txt
> Use this file to discover all available pages before exploring further.

# List Groups

> `org:groups:read`




## OpenAPI

````yaml get /groups/{network}
openapi: 3.0.0
info:
  title: Pinata V3 API
  version: 1.0.0
servers:
  - url: https://api.pinata.cloud/v3
security:
  - bearerAuth: []
paths:
  /groups/{network}:
    get:
      tags:
        - Groups
      summary: List Groups
      description: |
        `org:groups:read`
      operationId: listGroups
      parameters:
        - name: name
          in: query
          schema:
            type: string
          description: Filter groups by name
        - name: isPublic
          in: query
          schema:
            type: boolean
          description: Filters groups by is_public set to true or false
          example: 'true'
        - name: limit
          in: query
          schema:
            type: integer
          description: Limit the number of results
          example: '10'
        - name: pageToken
          in: query
          schema:
            type: string
          description: Paginate using the nextPageToken
      responses:
        '200':
          description: OK
          headers:
            Date:
              schema:
                type: string
                example: Wed, 28 Aug 2024 14:50:07 GMT
            Content-Type:
              schema:
                type: string
                example: application/json; charset=utf-8
            Content-Length:
              schema:
                type: integer
                example: '266'
            Connection:
              schema:
                type: string
                example: keep-alive
            X-Request-Id:
              schema:
                type: string
                example: 256ce2733baf16700d77f582c8ae95c8
            Strict-Transport-Security:
              schema:
                type: string
                example: max-age=15724800; includeSubDomains
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      groups:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                            name:
                              type: string
                            is_public:
                              type: boolean
                            created_at:
                              type: string
                      next_page_token:
                        type: string
              example:
                data:
                  groups:
                    - id: 01919976-955f-7d06-bd59-72e80743fb95
                      name: Test Private Group
                      is_public: false
                      created_at: '2024-08-28T14:49:31.246596Z'
                  next_page_token: MDE5MTk5NzYtOTU1Zi03ZDA2LWJkNTktNzJlODA3NDNmYjk1
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

````