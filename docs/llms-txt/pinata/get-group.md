# Source: https://docs.pinata.cloud/api-reference/endpoint/get-group.md

# Get Group

> `org:groups:read`


## OpenAPI

````yaml get /groups/{network}/{id}
paths:
  path: /groups/{network}/{id}
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
      path:
        network:
          schema:
            - type: enum<string>
              enum:
                - public
                - private
              required: true
              description: Target either the public or private IPFS network
        id:
          schema:
            - type: string
              required: true
      query: {}
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
                      id:
                        type: string
                      name:
                        type: string
                      is_public:
                        type: boolean
                      created_at:
                        type: string
        examples:
          example:
            value:
              data:
                id: 01919976-955f-7d06-bd59-72e80743fb95
                name: Test Private Group
                is_public: false
                created_at: '2024-08-28T14:49:31.246596Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````