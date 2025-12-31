# Source: https://docs.pinata.cloud/api-reference/endpoint/delete-file-by-id.md

# Delete File by ID

> `org:files:write`


## OpenAPI

````yaml delete /files/{network}/{id}
paths:
  path: /files/{network}/{id}
  method: delete
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
              description: Target a file on either the public or private IPFS network
        id:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '500':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value:
              data: null
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````