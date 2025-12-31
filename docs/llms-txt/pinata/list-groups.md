# Source: https://docs.pinata.cloud/api-reference/endpoint/list-groups.md

# List Groups

> `org:groups:read`


## OpenAPI

````yaml get /groups/{network}
paths:
  path: /groups/{network}
  method: get
  servers:
    - url: https://api.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query:
        name:
          schema:
            - type: string
              description: Filter groups by name
        isPublic:
          schema:
            - type: boolean
              description: Filters groups by is_public set to true or false
        limit:
          schema:
            - type: integer
              description: Limit the number of results
        pageToken:
          schema:
            - type: string
              description: Paginate using the nextPageToken
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
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
        examples:
          example:
            value:
              data:
                groups:
                  - id: 01919976-955f-7d06-bd59-72e80743fb95
                    name: Test Private Group
                    is_public: false
                    created_at: '2024-08-28T14:49:31.246596Z'
                next_page_token: MDE5MTk5NzYtOTU1Zi03ZDA2LWJkNTktNzJlODA3NDNmYjk1
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````