# Source: https://docs.pinata.cloud/api-reference/endpoint/create-group.md

# Create Group

> `org:groups:write`


## OpenAPI

````yaml post /groups/{network}
paths:
  path: /groups/{network}
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: The name of the group you want to create
              is_public:
                allOf:
                  - type: boolean
                    description: Flag if group is public or not
            requiredProperties:
              - name
            example:
              name: Test Group 3
        examples:
          example:
            value:
              name: Test Group 3
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
                public: false
                created_at: '2024-08-28T14:49:31.246596Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````