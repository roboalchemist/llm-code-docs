# Source: https://docs.pinata.cloud/api-reference/endpoint/remove-file-from-group.md

# Remove File From Group

> `org:groups:write`


## OpenAPI

````yaml delete /groups/{network}/{id}/ids/{file_id}
paths:
  path: /groups/{network}/{id}/ids/{file_id}
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
              description: Target either the public or private IPFS network
        id:
          schema:
            - type: string
              required: true
              description: The ID of the target group
        file_id:
          schema:
            - type: string
              required: true
              description: The ID of the tart file to remove from the group
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
        examples:
          example:
            value:
              data: null
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````