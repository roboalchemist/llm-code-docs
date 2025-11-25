# Source: https://docs.pinata.cloud/api-reference/endpoint/update-group.md

# Update Group

> `org:groups:write`


## OpenAPI

````yaml put /groups/{network}/{id}
paths:
  path: /groups/{network}/{id}
  method: put
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
              description: The ID of the target group
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
                    description: Updated name for target group
              is_public:
                allOf:
                  - type: boolean
                    description: Toggle if group is public or not
            example:
              name: Updated Name
              is_public: true
        examples:
          example:
            value:
              name: Updated Name
              is_public: true
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
                id: 01919ac8-a6f5-7e8e-a8a2-6cfe00122b90
                name: Updated Name
                is_public: true
                created_at: '2024-08-28T20:58:46.96779Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````