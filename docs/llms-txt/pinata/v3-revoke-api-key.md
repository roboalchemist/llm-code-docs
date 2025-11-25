# Source: https://docs.pinata.cloud/api-reference/endpoint/v3-revoke-api-key.md

# Revoke API Key

> `org:write`


## OpenAPI

````yaml delete /api_keys/{key}
paths:
  path: /api_keys/{key}
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
        key:
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
            properties: {}
        examples:
          example:
            value: Revoked
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````